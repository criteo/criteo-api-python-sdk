# criteo_api_marketingsolutions_preview.AdvertiserApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_portfolio_get**](AdvertiserApi.md#api_portfolio_get) | **GET** /2021-04/advertisers/me | 
[**get_categories**](AdvertiserApi.md#get_categories) | **GET** /legacy/marketing/v1/advertisers/{advertiserId}/categories | Gets all advertiser&#39;s categories
[**get_category**](AdvertiserApi.md#get_category) | **GET** /legacy/marketing/v1/advertisers/{advertiserId}/categories/{categoryHashCode} | Gets a specific advertiser&#39;s category


# **api_portfolio_get**
> GetPortfolioResponse api_portfolio_get()



Use this call to fetch a list of all advertisers in your account.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import advertiser_api
from criteo_api_marketingsolutions_preview.model.get_portfolio_response import GetPortfolioResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_portfolio_get()
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->api_portfolio_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPortfolioResponse**](GetPortfolioResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> [CategoryMessage] get_categories(advertiser_id)

Gets all advertiser's categories

Get the list of all the categories linked to the requested advertiser.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import advertiser_api
from criteo_api_marketingsolutions_preview.model.category_message import CategoryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)
    advertiser_id = 1 # int | Mandatory. The id of the advertiser to return.
    enabled_only = True # bool | Optional. Returns only categories you can bid on. Defaults to false. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets all advertiser's categories
        api_response = api_instance.get_categories(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->get_categories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets all advertiser's categories
        api_response = api_instance.get_categories(advertiser_id, enabled_only=enabled_only)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->get_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. |
 **enabled_only** | **bool**| Optional. Returns only categories you can bid on. Defaults to false. | [optional]

### Return type

[**[CategoryMessage]**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | The requested advertiser is missing from current user’s portfolio. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> [CategoryMessage] get_category(advertiser_id, category_hash_code)

Gets a specific advertiser's category

Get a specific category linked to the requested advertiser.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import advertiser_api
from criteo_api_marketingsolutions_preview.model.category_message import CategoryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)
    advertiser_id = 1 # int | Mandatory. The id of the advertiser to return.
    category_hash_code = 1 # int | Mandatory. The id of the category to return.

    # example passing only required values which don't have defaults set
    try:
        # Gets a specific advertiser's category
        api_response = api_instance.get_category(advertiser_id, category_hash_code)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->get_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. |
 **category_hash_code** | **int**| Mandatory. The id of the category to return. |

### Return type

[**[CategoryMessage]**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | The requested advertiser is missing from current user’s portfolio. |  -  |
**404** | The requested category was not found for the advertiser. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

