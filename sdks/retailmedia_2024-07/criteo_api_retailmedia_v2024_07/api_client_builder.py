from criteo_api_retailmedia_v2024_07.configuration import Configuration
from criteo_api_retailmedia_v2024_07.criteo_api_client import CriteoApiClient
from criteo_api_retailmedia_v2024_07 import flow_constants

class ApiClientBuilder :

    @staticmethod
    def WithClientCredentials(clientId, clientSecret, host=None):
        configuration = Configuration(username=clientId, password=clientSecret, host=host)

        return CriteoApiClient(configuration)

    @staticmethod
    def WithNoAuthorization():

        return CriteoApiClient()

    @staticmethod
    def WithAuthorizationCode(clientId, clientSecret, authorization_code, redirect_uri, host=None):
        configuration = Configuration(username=clientId, password=clientSecret, host=host)
        additional_parameters =  {
            'flow' : flow_constants.AUTHORIZATION_CODE_FLOW,
            'authorization_code': authorization_code,
            'redirect_uri': redirect_uri
        }
        
        return CriteoApiClient(configuration = configuration, additional_parameters = additional_parameters)

    @staticmethod
    def WithRefreshToken(clientId, clientSecret, refreshToken, host=None):
        configuration = Configuration(username=clientId, password=clientSecret, host=host)
        additional_parameters = {
            'flow' : flow_constants.REFRESH_TOKEN_FLOW,
            'refresh_token': refreshToken
        }

        return CriteoApiClient(configuration = configuration, additional_parameters = additional_parameters)