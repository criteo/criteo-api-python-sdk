# criteo_api_marketingsolutions_preview.AdvertiserApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_portfolio_get**](AdvertiserApi.md#api_portfolio_get) | **GET** /preview/advertisers/me | 
[**create_advertiser**](AdvertiserApi.md#create_advertiser) | **POST** /preview/advertisers | 
[**get_dataset_list**](AdvertiserApi.md#get_dataset_list) | **GET** /preview/advertisers/{advertiser-id}/datasets | 
[**list_industries**](AdvertiserApi.md#list_industries) | **GET** /preview/industries | 


# **api_portfolio_get**
> GetPortfolioResponse api_portfolio_get()



Fetch the portfolio of Advertisers for this account

### Example

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

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
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

# **create_advertiser**
> AdvertiserCreationResponse create_advertiser(advertiser_creation_request)



Create a new advertiser based on provided parameters. This could take up to 30 seconds.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import advertiser_api
from criteo_api_marketingsolutions_preview.model.advertiser_creation_response import AdvertiserCreationResponse
from criteo_api_marketingsolutions_preview.model.advertiser_creation_request import AdvertiserCreationRequest
from criteo_api_marketingsolutions_preview.model.unauthorized_response_v2 import UnauthorizedResponseV2
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)
    advertiser_creation_request = AdvertiserCreationRequest(
        type="campaign",
        data=AdvertiserCreationInput(
            account_name="account_name_example",
            website_url="website_url_example",
            country_iso_code="country_iso_code_example",
            currency_iso_code="currency_iso_code_example",
            industry_id="industry_id_example",
        ),
    ) # AdvertiserCreationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_advertiser(advertiser_creation_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->create_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_creation_request** | [**AdvertiserCreationRequest**](AdvertiserCreationRequest.md)|  |

### Return type

[**AdvertiserCreationResponse**](AdvertiserCreationResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_list**
> AdvertiserDatasetListResponse get_dataset_list(advertiser_id)



Retrieves corresponding Datasets for a given Advertiser. Only those Datasets are included for which the given Advertiser is marked a primary.

### Example

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

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The id of the Advertiser for which Datasets are being retrieved.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dataset_list(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AdvertiserApi->get_dataset_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The id of the Advertiser for which Datasets are being retrieved. |

### Return type

[**AdvertiserDatasetListResponse**](AdvertiserDatasetListResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_industries**
> ListAvailableIndustriesResponse list_industries()



Returns the list of available industries for new advertisers.

### Example

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

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
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

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

