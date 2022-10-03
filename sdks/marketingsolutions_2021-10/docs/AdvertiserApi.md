# criteo_api_marketingsolutions_v2021_10.AdvertiserApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_portfolio_get**](AdvertiserApi.md#api_portfolio_get) | **GET** /2021-10/advertisers/me | 


# **api_portfolio_get**
> GetPortfolioResponse api_portfolio_get()



Fetch the portfolio of Advertisers for this account

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_v2021_10
from criteo_api_marketingsolutions_v2021_10.api import advertiser_api
from criteo_api_marketingsolutions_v2021_10.model.get_portfolio_response import GetPortfolioResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2021_10.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2021_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_portfolio_get()
        pprint(api_response)
    except criteo_api_marketingsolutions_v2021_10.ApiException as e:
        print("Exception when calling AdvertiserApi->api_portfolio_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPortfolioResponse**](GetPortfolioResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

