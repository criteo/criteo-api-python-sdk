from criteo_api_retailmedia_v2022_10.configuration import Configuration
from criteo_api_retailmedia_v2022_10.criteo_api_client import CriteoApiClient

class ApiClientBuilder :

    @staticmethod
    def WithClientCredentials(clientId, clientSecret):
        configuration = Configuration(username=clientId, password=clientSecret)

        return CriteoApiClient(configuration)

    @staticmethod
    def WithNoAuthorization():

        return CriteoApiClient()
