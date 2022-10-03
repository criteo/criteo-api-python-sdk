# criteo_api_retailmedia_v2021_07.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_external_account_brands_by_account_id**](CampaignApi.md#get_api_v1_external_account_brands_by_account_id) | **GET** /2021-07/retail-media/accounts/{accountId}/brands | 
[**get_api_v1_external_account_campaigns_by_account_id**](CampaignApi.md#get_api_v1_external_account_campaigns_by_account_id) | **GET** /2021-07/retail-media/accounts/{accountId}/campaigns | 
[**get_api_v1_external_account_retailers_by_account_id**](CampaignApi.md#get_api_v1_external_account_retailers_by_account_id) | **GET** /2021-07/retail-media/accounts/{accountId}/retailers | 
[**get_api_v1_external_accounts**](CampaignApi.md#get_api_v1_external_accounts) | **GET** /2021-07/retail-media/accounts | 
[**get_api_v1_external_campaign_by_campaign_id**](CampaignApi.md#get_api_v1_external_campaign_by_campaign_id) | **GET** /2021-07/retail-media/campaigns/{campaignId} | 
[**get_api_v1_external_catalog_output_by_catalog_id**](CampaignApi.md#get_api_v1_external_catalog_output_by_catalog_id) | **GET** /2021-07/retail-media/catalogs/{catalogId}/output | 
[**get_api_v1_external_catalog_status_by_catalog_id**](CampaignApi.md#get_api_v1_external_catalog_status_by_catalog_id) | **GET** /2021-07/retail-media/catalogs/{catalogId}/status | 
[**get_api_v2_external_account_line_items_by_account_id**](CampaignApi.md#get_api_v2_external_account_line_items_by_account_id) | **GET** /2021-07/retail-media/accounts/{account-id}/line-items | 
[**get_api_v2_external_auction_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_auction_line_item_by_line_item_id) | **GET** /2021-07/retail-media/auction-line-items/{line-item-id} | 
[**get_api_v2_external_campaign_auction_line_items_by_campaign_id**](CampaignApi.md#get_api_v2_external_campaign_auction_line_items_by_campaign_id) | **GET** /2021-07/retail-media/campaigns/{campaign-id}/auction-line-items | 
[**get_api_v2_external_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_line_item_by_line_item_id) | **GET** /2021-07/retail-media/line-items/{line-item-id} | 
[**post_api_v1_external_account_campaigns_by_account_id**](CampaignApi.md#post_api_v1_external_account_campaigns_by_account_id) | **POST** /2021-07/retail-media/accounts/{accountId}/campaigns | 
[**post_api_v1_external_account_catalogs_by_account_id**](CampaignApi.md#post_api_v1_external_account_catalogs_by_account_id) | **POST** /2021-07/retail-media/accounts/{accountId}/catalogs | 
[**post_api_v2_external_campaign_auction_line_items_by_campaign_id**](CampaignApi.md#post_api_v2_external_campaign_auction_line_items_by_campaign_id) | **POST** /2021-07/retail-media/campaigns/{campaign-id}/auction-line-items | 
[**put_api_v1_external_campaign_by_campaign_id**](CampaignApi.md#put_api_v1_external_campaign_by_campaign_id) | **PUT** /2021-07/retail-media/campaigns/{campaignId} | 
[**put_api_v2_external_auction_line_item_by_line_item_id**](CampaignApi.md#put_api_v2_external_auction_line_item_by_line_item_id) | **PUT** /2021-07/retail-media/auction-line-items/{line-item-id} | 


# **get_api_v1_external_account_brands_by_account_id**
> JsonApiPageResponseOfBrand get_api_v1_external_account_brands_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_brands_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_brands_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_brands_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_brands_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfBrand**](JsonApiPageResponseOfBrand.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_account_campaigns_by_account_id**
> JsonApiPageResponseOfCampaign get_api_v1_external_account_campaigns_by_account_id(account_id)



Gets page of campaign objects for the given account id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_page_response_of_campaign import JsonApiPageResponseOfCampaign
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_campaigns_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfCampaign**](JsonApiPageResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_account_retailers_by_account_id**
> JsonApiPageResponseOfRetailer get_api_v1_external_account_retailers_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_retailers_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_retailers_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_retailers_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_retailers_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfRetailer**](JsonApiPageResponseOfRetailer.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_accounts**
> JsonApiPageResponseOfAccount get_api_v1_external_accounts()



Gets page of account objects that the current user can access

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_accounts(limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfAccount**](JsonApiPageResponseOfAccount.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaign get_api_v1_external_campaign_by_campaign_id(campaign_id)



Gets the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |

### Return type

[**JsonApiSingleResponseOfCampaign**](JsonApiSingleResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_catalog_output_by_catalog_id**
> get_api_v1_external_catalog_output_by_catalog_id(catalog_id)



Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream of v2021_07 CatalogProduct json objects.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_api_v1_external_catalog_output_by_catalog_id(catalog_id)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_catalog_output_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-json-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog download initiated. |  -  |
**400** | The indicated catalog is not available for retrieval, wait for a success status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_catalog_status_by_catalog_id**
> JsonApiSingleResponseOfCatalogStatus get_api_v1_external_catalog_status_by_catalog_id(catalog_id)



Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_catalog_status_by_catalog_id(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_catalog_status_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_account_line_items_by_account_id**
> CommonLineItemPagedListResponse get_api_v2_external_account_line_items_by_account_id(account_id)



Gets page of line item objects for the given account id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.common_line_item_paged_list_response import CommonLineItemPagedListResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The given account id
    limit_to_campaign_id = [
        "limitToCampaignId_example",
    ] # [str] | The campaign ids that you would like to limit your result set to (optional)
    limit_to_type = "Unknown" # str | The campaign types that you would like to limit your result set to (optional)
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_account_line_items_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_account_line_items_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_account_line_items_by_account_id(account_id, limit_to_campaign_id=limit_to_campaign_id, limit_to_type=limit_to_type, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_account_line_items_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_campaign_id** | **[str]**| The campaign ids that you would like to limit your result set to | [optional]
 **limit_to_type** | **str**| The campaign types that you would like to limit your result set to | [optional]
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**CommonLineItemPagedListResponse**](CommonLineItemPagedListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_auction_line_item_by_line_item_id**
> AuctionLineItemResponse get_api_v2_external_auction_line_item_by_line_item_id(line_item_id)



Gets the auction line item for the given line item id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.auction_line_item_response import AuctionLineItemResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_auction_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_auction_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**AuctionLineItemResponse**](AuctionLineItemResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_campaign_auction_line_items_by_campaign_id**
> AuctionLineItemPagedListResponse get_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)



Gets page of auction line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.auction_line_item_paged_list_response import AuctionLineItemPagedListResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | The given campaign id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_campaign_auction_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_campaign_auction_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**AuctionLineItemPagedListResponse**](AuctionLineItemPagedListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_line_item_by_line_item_id**
> CommonLineItemResponse get_api_v2_external_line_item_by_line_item_id(line_item_id)



Gets the line item for the given line item id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.common_line_item_response import CommonLineItemResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**CommonLineItemResponse**](CommonLineItemResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_campaigns_by_account_id**
> JsonApiSingleResponseOfCampaign post_api_v1_external_account_campaigns_by_account_id(account_id)



Creates a new campaign with the specified settings

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.external_post_campaign import ExternalPostCampaign
from criteo_api_retailmedia_v2021_07.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    external_post_campaign = ExternalPostCampaign(
        data=JsonApiBodyWithoutIdOfCampaignAttributesAndCampaign(
            type="type_example",
            attributes=ExternalCampaignAttributes(
                type="auction",
                drawable_balance_ids=[
                    "drawable_balance_ids_example",
                ],
                click_attribution_window="30D",
                view_attribution_window="none",
                name="name_example",
                budget=3.14,
                click_attribution_scope="unknown",
                view_attribution_scope="unknown",
            ),
        ),
    ) # ExternalPostCampaign | The campaign settings to create a campaign with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_campaigns_by_account_id(account_id, external_post_campaign=external_post_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **external_post_campaign** | [**ExternalPostCampaign**](ExternalPostCampaign.md)| The campaign settings to create a campaign with | [optional]

### Return type

[**JsonApiSingleResponseOfCampaign**](JsonApiSingleResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_catalogs_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v1_external_account_catalogs_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_v2021_07.model.json_api_request_of_catalog_request import JsonApiRequestOfCatalogRequest
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to request the catalog for.
    json_api_request_of_catalog_request = JsonApiRequestOfCatalogRequest(
        data=JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequest(
            type="type_example",
            attributes=ExternalCatalogRequest(
                format="json-newline",
                brand_id_filter=[
                    "brand_id_filter_example",
                ],
            ),
        ),
    ) # JsonApiRequestOfCatalogRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_by_account_id(account_id, json_api_request_of_catalog_request=json_api_request_of_catalog_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **json_api_request_of_catalog_request** | [**JsonApiRequestOfCatalogRequest**](JsonApiRequestOfCatalogRequest.md)|  | [optional]

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v2_external_campaign_auction_line_items_by_campaign_id**
> AuctionLineItemResponse post_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)



Creates new auction line item with the specified settings

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.auction_line_item_response import AuctionLineItemResponse
from criteo_api_retailmedia_v2021_07.model.auction_line_item_create_model_request import AuctionLineItemCreateModelRequest
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | The given campaign id
    auction_line_item_create_model_request = AuctionLineItemCreateModelRequest(
        data=InputResourceOfAuctionLineItemCreateModel(
            type="type_example",
            attributes=ExternalAuctionLineItemCreateModel(
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                target_retailer_id="target_retailer_id_example",
                budget=3.14,
                target_bid=3.14,
                max_bid=3.14,
                monthly_pacing=3.14,
                daily_pacing=3.14,
                is_auto_daily_pacing=False,
                bid_strategy="conversion",
            ),
        ),
    ) # AuctionLineItemCreateModelRequest | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_campaign_auction_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id, auction_line_item_create_model_request=auction_line_item_create_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_campaign_auction_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **auction_line_item_create_model_request** | [**AuctionLineItemCreateModelRequest**](AuctionLineItemCreateModelRequest.md)| The line item settings to create a line item with | [optional]

### Return type

[**AuctionLineItemResponse**](AuctionLineItemResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaign put_api_v1_external_campaign_by_campaign_id(campaign_id)



Updates the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from criteo_api_retailmedia_v2021_07.model.external_put_campaign import ExternalPutCampaign
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    external_put_campaign = ExternalPutCampaign(
        data=JsonApiBodyWithExternalIdOfEditableCampaignAttributesAndCampaign(
            id="id_example",
            type="type_example",
            attributes=ExternalEditableCampaignAttributes(
                name="name_example",
                budget=3.14,
                click_attribution_window="7D",
                view_attribution_window="none",
                click_attribution_scope="unknown",
                view_attribution_scope="unknown",
            ),
        ),
    ) # ExternalPutCampaign | The campaign settings to update that campaign with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_campaign_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_campaign_by_campaign_id(campaign_id, external_put_campaign=external_put_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **external_put_campaign** | [**ExternalPutCampaign**](ExternalPutCampaign.md)| The campaign settings to update that campaign with | [optional]

### Return type

[**JsonApiSingleResponseOfCampaign**](JsonApiSingleResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v2_external_auction_line_item_by_line_item_id**
> AuctionLineItemResponse put_api_v2_external_auction_line_item_by_line_item_id(line_item_id)



Updates the auction line item for the given line item id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2021_07
from criteo_api_retailmedia_v2021_07.api import campaign_api
from criteo_api_retailmedia_v2021_07.model.auction_line_item_update_model_request import AuctionLineItemUpdateModelRequest
from criteo_api_retailmedia_v2021_07.model.auction_line_item_response import AuctionLineItemResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2021_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2021_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id
    auction_line_item_update_model_request = AuctionLineItemUpdateModelRequest(
        data=ResourceOfAuctionLineItemUpdateModel(
            id="id_example",
            type="type_example",
            attributes=ExternalAuctionLineItemUpdateModel(
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                budget=3.14,
                target_bid=3.14,
                max_bid=3.14,
                monthly_pacing=3.14,
                daily_pacing=3.14,
                is_auto_daily_pacing=True,
                bid_strategy="conversion",
            ),
        ),
    ) # AuctionLineItemUpdateModelRequest | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v2_external_auction_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_auction_line_item_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v2_external_auction_line_item_by_line_item_id(line_item_id, auction_line_item_update_model_request=auction_line_item_update_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2021_07.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_auction_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |
 **auction_line_item_update_model_request** | [**AuctionLineItemUpdateModelRequest**](AuctionLineItemUpdateModelRequest.md)| The line item settings to create a line item with | [optional]

### Return type

[**AuctionLineItemResponse**](AuctionLineItemResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

