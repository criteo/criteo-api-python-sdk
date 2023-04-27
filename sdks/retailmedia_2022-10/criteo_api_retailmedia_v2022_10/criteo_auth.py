import json
from datetime import datetime, timedelta
from criteo_api_retailmedia_v2022_10.exceptions import ApiException
from criteo_api_retailmedia_v2022_10.api_client import ApiClient

class Token(object):

    def __init__(self, token_string , expiration_date = None):
        self.expiration_date = expiration_date 
        self.token_string = token_string

    def has_expired(self):
        if not self.expiration_date:
            return False
        return self.expiration_date > datetime.utcnow()

class BasicAuth(object):

    def __init__(self, token_string):
        self.token = Token(token_string)

    def get_token(self, client : ApiClient, headers) -> str:
        return self.token

class RetryingOAuth(object):

    def __init__(self, grant_type, client_id, client_secret):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def get_token(self, client : ApiClient, headers) -> str:    
        if self.token and not self.token.has_expired():
            self.token = None

        if self.token is None:
            self.refresh_token(client, headers)

        return self.token   

    def refresh_token(self, client : ApiClient, headers, parameters_dict= {}):
        oauth_url = client.host + '/oauth2/token'
        new_headers = {'Accept': 'application/json',
                       'Content-Type': 'application/x-www-form-urlencoded',
                       'User-Agent': headers['User-Agent']}
        params = dict(parameters_dict, **{
            'client_id':  self.client_id,
            'client_secret': self.client_secret,
            'grant_type' : self.grant_type 
            })
        try:
            response = client.request('POST', oauth_url,
                                    headers=new_headers,
                                    query_params=[],
                                    post_params=list(params.items()),
                                    _preload_content=True,
                                    _request_timeout=None,
                                    body=None,
                                    no_auth=True)
            data = json.loads(response.data)
            self.token = Token('Bearer '+ (data['access_token'] or ''),
               RetryingOAuth.compute_expiration_date(data['expires_in']))

            return self.token
        except ApiException as e:
            raise self._enrich_exception_message(e, oauth_url)

    def _enrich_exception_message(self, e, url):
        try:
            data = json.loads(e.body or {})
        except ValueError:
            data = {}
        data['token_error'] = "Cannot refresh token by calling '" + url + "'"
        e.body = json.dumps(data).encode()
        return e            

    @staticmethod
    def compute_expiration_date(expires_in):
        return datetime.utcnow() + timedelta(seconds=int(expires_in) + 15)

class RetryingClientCredentials(RetryingOAuth):
    
    def __init__(self, client_id, client_secret):
        super().__init__('client_credentials', client_id, client_secret)

class RetryingAuthorizationCode(RetryingOAuth):
   
    def __init__(self, client_id, client_secret, code, redirect_uri):
        super().__init__('authorization_code', client_id, client_secret)
        self.authorization_code = code
        self.redirect_uri = redirect_uri

    def refresh_token(self, client : ApiClient, headers, parameters_dict= {}):  
        params = dict(parameters_dict, **{
            'authorization_code' : self.authorization_code,
            'redirect_uri' : self.redirect_uri
        })
        return super().refresh_token(client, headers, params)
