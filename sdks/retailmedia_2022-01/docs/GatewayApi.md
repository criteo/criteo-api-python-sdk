# criteo_api_retailmedia_v2022_01.GatewayApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_application**](GatewayApi.md#get_current_application) | **GET** /me | 


# **get_current_application**
> ApplicationSummaryModelResponse get_current_application()



Get information about the currently logged application

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2022_01
from criteo_api_retailmedia_v2022_01.api import gateway_api
from criteo_api_retailmedia_v2022_01.model.application_summary_model_response import ApplicationSummaryModelResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_api.GatewayApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_current_application()
        pprint(api_response)
    except criteo_api_retailmedia_v2022_01.ApiException as e:
        print("Exception when calling GatewayApi->get_current_application: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationSummaryModelResponse**](ApplicationSummaryModelResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

