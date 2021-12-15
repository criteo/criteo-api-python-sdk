# criteo_api_retailmedia_v2020_10.OAuthApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](OAuthApi.md#create_token) | **POST** /oauth2/token | 


# **create_token**
> JwtModel create_token()



Creates a token when the supplied client credentials are valid

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2020_10
from criteo_api_retailmedia_v2020_10.api import o_auth_api
from criteo_api_retailmedia_v2020_10.model.o_auth2_error import OAuth2Error
from criteo_api_retailmedia_v2020_10.model.jwt_model import JwtModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = o_auth_api.OAuthApi(api_client)
    client_id = "client_id_example" # str | API Client-Id or Username (optional)
    client_secret = "client_secret_example" # str | API Client secret or password (optional)
    grant_type = "client_credentials" # str | Other grant types are not available (optional) if omitted the server will use the default value of "client_credentials"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_token(client_id=client_id, client_secret=client_secret, grant_type=grant_type)
        pprint(api_response)
    except criteo_api_retailmedia_v2020_10.ApiException as e:
        print("Exception when calling OAuthApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Client-Id or Username | [optional]
 **client_secret** | **str**| API Client secret or password | [optional]
 **grant_type** | **str**| Other grant types are not available | [optional] if omitted the server will use the default value of "client_credentials"

### Return type

[**JwtModel**](JwtModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

