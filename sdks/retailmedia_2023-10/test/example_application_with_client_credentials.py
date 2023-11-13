from criteo_api_retailmedia_v2023_10.api.gateway_api import GatewayApi
from criteo_api_retailmedia_v2023_10 import ApiClientBuilder

class ExampleApplication:

    def call_then_application_endpoint(self, clientId, clientSecret):
        # Create a client using your choosen OAuth flow, Client Credentials in this case. The client will handle the token generation/renewal for you
        client = ApiClientBuilder.WithClientCredentials(clientId=clientId, clientSecret=clientSecret)

        # The Gateway API regroups common technical endpoints that exists for all versions
        # You can find the other endpoints in the other *Api
        # You can reuse the same client with several Apis, but be careful, as they will then use the same token and credentials
        api = GatewayApi(client)

        # Perform the call to the application introspection endpoint
        response = api.get_current_application()

        # Most of Criteo's API response follow the same structure:
        # The response consists of a Data, Errors and Warnings fields
        # The Data fields contains an Id (if applicable), a Type, and an Attributes field that contains the business object
        myApplication = response.data.attributes
        print(f'Hello, I\'m using Criteo API and I\'m connected as {myApplication.name}')