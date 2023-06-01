from criteo_api_marketingsolutions_preview.api_client import ApiClient
from criteo_api_marketingsolutions_preview.criteo_rest import CriteoRESTClientObject

class CriteoApiClient(ApiClient):
    def __init__(self, configuration=None, header_name=None, header_value=None,
             cookie=None, pool_threads=1, additional_parameters= {}):
        super().__init__(configuration=configuration,header_name=header_name, header_value=header_value, cookie=cookie, pool_threads=pool_threads)
        self.rest_client = CriteoRESTClientObject(self.configuration, additional_parameters)

    def get_refresh_token(self):
        return self.rest_client.get_refresh_token()