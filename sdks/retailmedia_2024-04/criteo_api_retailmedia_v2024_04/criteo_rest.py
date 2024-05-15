from criteo_api_retailmedia_v2024_04.rest import RESTClientObject
from criteo_api_retailmedia_v2024_04.criteo_auth import *
from criteo_api_retailmedia_v2024_04 import flow_constants


class CriteoRESTClientObject(RESTClientObject):

    def __init__(self, configuration, additional_parameters = {}, pools_size=4, maxsize=None):
        super().__init__(configuration, pools_size, maxsize)

        self.host = configuration.host
        client_id = configuration.username
        client_secret = configuration.password

        grant_type = additional_parameters.get('flow', 'client_credentials')
        if grant_type == flow_constants.AUTHORIZATION_CODE_FLOW :
            self.authorization = RetryingAuthorizationCode(
                client_id,
                client_secret, 
                additional_parameters.get('authorization_code',''),
                additional_parameters.get('redirect_uri','')
            )
        elif grant_type == flow_constants.REFRESH_TOKEN_FLOW :
             self.authorization = RetryingRefreshToken(
                  client_id,
                  client_secret,
                  additional_parameters.get('refresh_token', '')
             )
        else:
            self.authorization = RetryingClientCredentials(
                client_id,
                client_secret
            )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
            return self.request(method, url, query_params, headers, body,post_params, _preload_content, _request_timeout, no_auth=False)

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None,  no_auth=False):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param no_auth: if True, token is not refreshed
                                 and authorization header is not set
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """

        headers = headers or {}
        if not no_auth:
            token = self.authorization.get_token(self, headers)
            headers['Authorization'] = token.token_string

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        return super().request(method, url, query_params, headers, body, post_params, _preload_content, _request_timeout)

    def get_refresh_token(self):
         return self.authorization.get_refresh_token()