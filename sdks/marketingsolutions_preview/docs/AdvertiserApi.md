# criteo_api_marketingsolutions_preview.AdvertiserApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_advertisers**](AdvertiserApi.md#list_advertisers) | **GET** /preview/advertisers/me | 
[**list_datasets_by_advertiser**](AdvertiserApi.md#list_datasets_by_advertiser) | **GET** /preview/advertisers/{advertiser-id}/datasets | 
[**list_industries**](AdvertiserApi.md#list_industries) | **GET** /preview/industries | 


# **list_advertisers**
> GetPortfolioResponse list_advertisers()



Fetch the portfolio of Advertisers for this account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
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
        api_response = api_instance.list_advertisers()
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->list_advertisers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPortfolioResponse**](GetPortfolioResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets_by_advertiser**
> AdvertiserDatasetListResponse list_datasets_by_advertiser(advertiser_id)



Retrieves corresponding Datasets for a given Advertiser. Only those Datasets are included for which the given Advertiser is marked a primary.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import advertiser_api
from criteo_api_marketingsolutions_preview.model.advertiser_dataset_list_response import AdvertiserDatasetListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The id of the Advertiser for which Datasets are being retrieved.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_datasets_by_advertiser(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->list_datasets_by_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The id of the Advertiser for which Datasets are being retrieved. |

### Return type

[**AdvertiserDatasetListResponse**](AdvertiserDatasetListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_industries**
> ListAvailableIndustriesResponse list_industries()



Returns the list of available industries for new advertisers.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import advertiser_api
from criteo_api_marketingsolutions_preview.model.list_available_industries_response import ListAvailableIndustriesResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
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
        api_response = api_instance.list_industries()
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->list_industries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAvailableIndustriesResponse**](ListAvailableIndustriesResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

