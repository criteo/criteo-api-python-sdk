# criteo_api_retailmedia_preview.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v1_external_balance_campaigns_by_balance_id**](CampaignApi.md#delete_api_v1_external_balance_campaigns_by_balance_id) | **DELETE** /preview/retail-media/balances/{balanceId}/campaigns | 
[**delete_api_v1_external_line_item_products_by_line_item_id**](CampaignApi.md#delete_api_v1_external_line_item_products_by_line_item_id) | **DELETE** /preview/retail-media/line-items/{lineItemId}/products | 
[**get_api_v0_external_catalog_output_by_catalog_id**](CampaignApi.md#get_api_v0_external_catalog_output_by_catalog_id) | **GET** /preview/retail-media/catalogs/{catalogId}/output | 
[**get_api_v0_external_catalog_status_by_catalog_id**](CampaignApi.md#get_api_v0_external_catalog_status_by_catalog_id) | **GET** /preview/retail-media/catalogs/{catalogId}/status | 
[**get_api_v1_external_account_balances_by_account_id**](CampaignApi.md#get_api_v1_external_account_balances_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/balances | 
[**get_api_v1_external_account_brands_by_account_id**](CampaignApi.md#get_api_v1_external_account_brands_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/brands | 
[**get_api_v1_external_account_campaigns_by_account_id**](CampaignApi.md#get_api_v1_external_account_campaigns_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/campaigns | 
[**get_api_v1_external_account_retailers_by_account_id**](CampaignApi.md#get_api_v1_external_account_retailers_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/retailers | 
[**get_api_v1_external_accounts**](CampaignApi.md#get_api_v1_external_accounts) | **GET** /preview/retail-media/accounts | 
[**get_api_v1_external_balance_campaigns_by_balance_id**](CampaignApi.md#get_api_v1_external_balance_campaigns_by_balance_id) | **GET** /preview/retail-media/balances/{balanceId}/campaigns | 
[**get_api_v1_external_campaign_by_campaign_id**](CampaignApi.md#get_api_v1_external_campaign_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaignId} | 
[**get_api_v1_external_campaign_line_items_by_campaign_id**](CampaignApi.md#get_api_v1_external_campaign_line_items_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaignId}/line-items | 
[**get_api_v1_external_line_item_by_line_item_id**](CampaignApi.md#get_api_v1_external_line_item_by_line_item_id) | **GET** /preview/retail-media/line-items/{lineItemId} | 
[**get_api_v1_external_line_item_products_by_line_item_id**](CampaignApi.md#get_api_v1_external_line_item_products_by_line_item_id) | **GET** /preview/retail-media/line-items/{lineItemId}/products | 
[**get_api_v1_external_retailer_brands_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_brands_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailerId}/brands | 
[**get_api_v1_external_retailer_by_retailer_id_seller_by_seller**](CampaignApi.md#get_api_v1_external_retailer_by_retailer_id_seller_by_seller) | **GET** /preview/retail-media/retailers/{retailerId}/sellers/{seller} | 
[**post_api_v0_external_account_catalogs_by_account_id**](CampaignApi.md#post_api_v0_external_account_catalogs_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/catalogs | 
[**post_api_v1_external_account_campaigns_by_account_id**](CampaignApi.md#post_api_v1_external_account_campaigns_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/campaigns | 
[**post_api_v1_external_campaign_line_items_by_campaign_id**](CampaignApi.md#post_api_v1_external_campaign_line_items_by_campaign_id) | **POST** /preview/retail-media/campaigns/{campaignId}/line-items | 
[**post_api_v1_external_catalogs_sku_retrieval**](CampaignApi.md#post_api_v1_external_catalogs_sku_retrieval) | **POST** /preview/retail-media/catalogs/sku-retrieval | 
[**post_api_v1_external_catalogs_sku_search**](CampaignApi.md#post_api_v1_external_catalogs_sku_search) | **POST** /preview/retail-media/catalogs/sku-search | 
[**put_api_v1_external_balance_campaigns_by_balance_id**](CampaignApi.md#put_api_v1_external_balance_campaigns_by_balance_id) | **PUT** /preview/retail-media/balances/{balanceId}/campaigns | 
[**put_api_v1_external_campaign_by_campaign_id**](CampaignApi.md#put_api_v1_external_campaign_by_campaign_id) | **PUT** /preview/retail-media/campaigns/{campaignId} | 
[**put_api_v1_external_line_item_by_line_item_id**](CampaignApi.md#put_api_v1_external_line_item_by_line_item_id) | **PUT** /preview/retail-media/line-items/{lineItemId} | 
[**put_api_v1_external_line_item_products_by_line_item_id**](CampaignApi.md#put_api_v1_external_line_item_products_by_line_item_id) | **PUT** /preview/retail-media/line-items/{lineItemId}/products | 


# **delete_api_v1_external_balance_campaigns_by_balance_id**
> PageOfBalanceCampaign delete_api_v1_external_balance_campaigns_by_balance_id(balance_id)



Removes one or more campaigns on the specified balance

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.page_of_balance_campaign import PageOfBalanceCampaign
from criteo_api_retailmedia_preview.model.json_api_data_request_of_delete_balance_campaign import JsonApiDataRequestOfDeleteBalanceCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balanceId_example" # str | The balance to remove campaigns from
    json_api_data_request_of_delete_balance_campaign = JsonApiDataRequestOfDeleteBalanceCampaign(
        data=[
            ExternalDeleteBalanceCampaign(
                type="type_example",
                id="id_example",
                attributes={},
            ),
        ],
    ) # JsonApiDataRequestOfDeleteBalanceCampaign | The campaigns to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_api_v1_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_api_v1_external_balance_campaigns_by_balance_id(balance_id, json_api_data_request_of_delete_balance_campaign=json_api_data_request_of_delete_balance_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to remove campaigns from |
 **json_api_data_request_of_delete_balance_campaign** | [**JsonApiDataRequestOfDeleteBalanceCampaign**](JsonApiDataRequestOfDeleteBalanceCampaign.md)| The campaigns to append | [optional]

### Return type

[**PageOfBalanceCampaign**](PageOfBalanceCampaign.md)

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

# **delete_api_v1_external_line_item_products_by_line_item_id**
> JsonApiPageResponseOfStringAndPromotedProduct delete_api_v1_external_line_item_products_by_line_item_id(line_item_id)



This endpoint removes one or more products from promotion on the specified line item.  The resulting state of the line item is returned.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_data_request_with_id_of_string_and_promoted_product import JsonApiDataRequestWithIdOfStringAndPromotedProduct
from criteo_api_retailmedia_preview.model.json_api_page_response_of_string_and_promoted_product import JsonApiPageResponseOfStringAndPromotedProduct
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item to interact with
    json_api_data_request_with_id_of_string_and_promoted_product = JsonApiDataRequestWithIdOfStringAndPromotedProduct(
        data=[
            JsonApiBodyWithIdOfStringAndPromotedProductAndPromotedProduct(
                id="id_example",
                type="type_example",
                attributes=ExternalPromotedProduct(
                    bid_override=3.14,
                ),
            ),
        ],
    ) # JsonApiDataRequestWithIdOfStringAndPromotedProduct |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_api_v1_external_line_item_products_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_api_v1_external_line_item_products_by_line_item_id(line_item_id, json_api_data_request_with_id_of_string_and_promoted_product=json_api_data_request_with_id_of_string_and_promoted_product)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **json_api_data_request_with_id_of_string_and_promoted_product** | [**JsonApiDataRequestWithIdOfStringAndPromotedProduct**](JsonApiDataRequestWithIdOfStringAndPromotedProduct.md)|  | [optional]

### Return type

[**JsonApiPageResponseOfStringAndPromotedProduct**](JsonApiPageResponseOfStringAndPromotedProduct.md)

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

# **get_api_v0_external_catalog_output_by_catalog_id**
> get_api_v0_external_catalog_output_by_catalog_id(catalog_id)



Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream of CatalogProduct json objects.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_api_v0_external_catalog_output_by_catalog_id(catalog_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v0_external_catalog_output_by_catalog_id: %s\n" % e)
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

# **get_api_v0_external_catalog_status_by_catalog_id**
> JsonApiSingleResponseOfCatalogStatus get_api_v0_external_catalog_status_by_catalog_id(catalog_id)



Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v0_external_catalog_status_by_catalog_id(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v0_external_catalog_status_by_catalog_id: %s\n" % e)
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

# **get_api_v1_external_account_balances_by_account_id**
> JsonApiPageResponseOfBalance get_api_v1_external_account_balances_by_account_id(account_id)



Gets page of balance objects for the given account id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_balance import JsonApiPageResponseOfBalance
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to get balances for
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_balances_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_balances_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_balances_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_balances_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to get balances for |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfBalance**](JsonApiPageResponseOfBalance.md)

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

# **get_api_v1_external_account_brands_by_account_id**
> JsonApiPageResponseOfBrand get_api_v1_external_account_brands_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_brands_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_brands_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_campaign import JsonApiPageResponseOfCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_campaigns_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_retailers_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_retailers_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **get_api_v1_external_balance_campaigns_by_balance_id**
> PageOfBalanceCampaign get_api_v1_external_balance_campaigns_by_balance_id(balance_id)



Gets page of campaigns for the given balanceId

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.page_of_balance_campaign import PageOfBalanceCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balanceId_example" # str | The balance to get campaigns from
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_balance_campaigns_by_balance_id(balance_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to get campaigns from |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**PageOfBalanceCampaign**](PageOfBalanceCampaign.md)

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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **get_api_v1_external_campaign_line_items_by_campaign_id**
> JsonApiPageResponseOfLineItem get_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)



Gets page of line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_line_item import JsonApiPageResponseOfLineItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_campaign_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfLineItem**](JsonApiPageResponseOfLineItem.md)

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

# **get_api_v1_external_line_item_by_line_item_id**
> JsonApiSingleResponseOfLineItem get_api_v1_external_line_item_by_line_item_id(line_item_id)



Gets the line item for the given line item id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item import JsonApiSingleResponseOfLineItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**JsonApiSingleResponseOfLineItem**](JsonApiSingleResponseOfLineItem.md)

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

# **get_api_v1_external_line_item_products_by_line_item_id**
> JsonApiPageResponseOfStringAndPromotedProduct get_api_v1_external_line_item_products_by_line_item_id(line_item_id)



This endpoint gets the promoted products on the specified line item.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_string_and_promoted_product import JsonApiPageResponseOfStringAndPromotedProduct
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item to interact with
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_line_item_products_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_line_item_products_by_line_item_id(line_item_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfStringAndPromotedProduct**](JsonApiPageResponseOfStringAndPromotedProduct.md)

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

# **get_api_v1_external_retailer_brands_by_retailer_id**
> BrandPreviewListResponse get_api_v1_external_retailer_brands_by_retailer_id(retailer_id)



Gets the brands for the given retailer

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.brand_preview_list_response import BrandPreviewListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | The retailer id for which brands should be fetched.
    sku_stock_type_filter = "first-party" # str | Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id, sku_stock_type_filter=sku_stock_type_filter)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which brands should be fetched. |
 **sku_stock_type_filter** | **str**| Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party | [optional]

### Return type

[**BrandPreviewListResponse**](BrandPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Brands found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_by_retailer_id_seller_by_seller**
> SellerPreviewResponse get_api_v1_external_retailer_by_retailer_id_seller_by_seller(retailer_id, seller)



Endpoint to get market place seller id and name

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.seller_preview_response import SellerPreviewResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | The retailer id for which seller should be fetched.
    seller = "seller_example" # str | The seller id or seller name which should be validated.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_by_retailer_id_seller_by_seller(retailer_id, seller)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_by_retailer_id_seller_by_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which seller should be fetched. |
 **seller** | **str**| The seller id or seller name which should be validated. |

### Return type

[**SellerPreviewResponse**](SellerPreviewResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Seller found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v0_external_account_catalogs_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v0_external_account_catalogs_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_request_of_catalog_request_preview import JsonApiRequestOfCatalogRequestPreview
from criteo_api_retailmedia_preview.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to request the catalog for.
    json_api_request_of_catalog_request_preview = JsonApiRequestOfCatalogRequestPreview(
        data=JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequestPreview(
            type="type_example",
            attributes=ExternalCatalogRequestPreview(
                format="json-newline",
            ),
        ),
    ) # JsonApiRequestOfCatalogRequestPreview |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v0_external_account_catalogs_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v0_external_account_catalogs_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v0_external_account_catalogs_by_account_id(account_id, json_api_request_of_catalog_request_preview=json_api_request_of_catalog_request_preview)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v0_external_account_catalogs_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **json_api_request_of_catalog_request_preview** | [**JsonApiRequestOfCatalogRequestPreview**](JsonApiRequestOfCatalogRequestPreview.md)|  | [optional]

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

# **post_api_v1_external_account_campaigns_by_account_id**
> JsonApiSingleResponseOfCampaign post_api_v1_external_account_campaigns_by_account_id(account_id)



Creates a new campaign with the specified settings

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from criteo_api_retailmedia_preview.model.external_post_campaign import ExternalPostCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_campaigns_by_account_id(account_id, external_post_campaign=external_post_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **post_api_v1_external_campaign_line_items_by_campaign_id**
> JsonApiSingleResponseOfLineItem post_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)



Creates a new line item with the specified settings

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item import JsonApiSingleResponseOfLineItem
from criteo_api_retailmedia_preview.model.external_post_line_item import ExternalPostLineItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    external_post_line_item = ExternalPostLineItem(
        data=JsonApiBodyWithoutIdOfLineItemAttributesAndLineItem(
            type="type_example",
            attributes=ExternalLineItemAttributes(
                target_retailer_id="target_retailer_id_example",
                status="unknown",
                target_bid=3.14,
                is_auto_daily_pacing=False,
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                max_bid=3.14,
                budget=3.14,
                monthly_pacing=3.14,
                daily_pacing=3.14,
                bid_strategy="conversion",
            ),
        ),
    ) # ExternalPostLineItem | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_campaign_line_items_by_campaign_id(campaign_id, external_post_line_item=external_post_line_item)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **external_post_line_item** | [**ExternalPostLineItem**](ExternalPostLineItem.md)| The line item settings to create a line item with | [optional]

### Return type

[**JsonApiSingleResponseOfLineItem**](JsonApiSingleResponseOfLineItem.md)

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

# **post_api_v1_external_catalogs_sku_retrieval**
> SkuDataPreviewListResponse post_api_v1_external_catalogs_sku_retrieval()



Endpoint to search skus by text, retailer and sellers/brands.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.sku_data_preview_list_response import SkuDataPreviewListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    request_body = [
        "request_body_example",
    ] # [str] | The list of SKU keys to retrieve sku information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_retrieval(page_index=page_index, page_size=page_size, request_body=request_body)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_retrieval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
 **request_body** | **[str]**| The list of SKU keys to retrieve sku information | [optional]

### Return type

[**SkuDataPreviewListResponse**](SkuDataPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_catalogs_sku_search**
> SkuDataPreviewListResponse post_api_v1_external_catalogs_sku_search()



Endpoint to search skus by text, retailer and sellers/brands.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.sku_data_preview_list_response import SkuDataPreviewListResponse
from criteo_api_retailmedia_preview.model.sku_search_request_preview_request import SkuSearchRequestPreviewRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    sku_search_request_preview_request = SkuSearchRequestPreviewRequest(
        data=ResourceOfSkuSearchRequestPreview(
            id="id_example",
            type="type_example",
            attributes=SkuSearchRequestPreview(
                query_string="query_string_example",
                retailer_id="retailer_id_example",
                sellers=[
                    "sellers_example",
                ],
                brand_ids=[
                    "brand_ids_example",
                ],
                sku_type="brand",
            ),
        ),
    ) # SkuSearchRequestPreviewRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_search(page_index=page_index, page_size=page_size, sku_search_request_preview_request=sku_search_request_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
 **sku_search_request_preview_request** | [**SkuSearchRequestPreviewRequest**](SkuSearchRequestPreviewRequest.md)|  | [optional]

### Return type

[**SkuDataPreviewListResponse**](SkuDataPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_external_balance_campaigns_by_balance_id**
> PageOfBalanceCampaign put_api_v1_external_balance_campaigns_by_balance_id(balance_id)



appends one or more campaigns to the specified balance

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_data_request_of_put_balance_campaign import JsonApiDataRequestOfPutBalanceCampaign
from criteo_api_retailmedia_preview.model.page_of_balance_campaign import PageOfBalanceCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balanceId_example" # str | The balance to add campaigns from
    json_api_data_request_of_put_balance_campaign = JsonApiDataRequestOfPutBalanceCampaign(
        data=[
            ExternalPutBalanceCampaign(
                type="type_example",
                id="id_example",
                attributes={},
            ),
        ],
    ) # JsonApiDataRequestOfPutBalanceCampaign | The campaigns to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_balance_campaigns_by_balance_id(balance_id, json_api_data_request_of_put_balance_campaign=json_api_data_request_of_put_balance_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to add campaigns from |
 **json_api_data_request_of_put_balance_campaign** | [**JsonApiDataRequestOfPutBalanceCampaign**](JsonApiDataRequestOfPutBalanceCampaign.md)| The campaigns to append | [optional]

### Return type

[**PageOfBalanceCampaign**](PageOfBalanceCampaign.md)

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

# **put_api_v1_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaign put_api_v1_external_campaign_by_campaign_id(campaign_id)



Updates the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from criteo_api_retailmedia_preview.model.external_put_campaign import ExternalPutCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_campaign_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_campaign_by_campaign_id(campaign_id, external_put_campaign=external_put_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **put_api_v1_external_line_item_by_line_item_id**
> JsonApiSingleResponseOfLineItem put_api_v1_external_line_item_by_line_item_id(line_item_id)



Updates the line item for the given line item id

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.external_put_line_item import ExternalPutLineItem
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item import JsonApiSingleResponseOfLineItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The given line item id
    external_put_line_item = ExternalPutLineItem(
        data=JsonApiBodyWithExternalIdOfEditableLineItemAttributesAndLineItem(
            id="id_example",
            type="type_example",
            attributes=ExternalEditableLineItemAttributes(
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                target_bid=3.14,
                max_bid=3.14,
                budget=3.14,
                monthly_pacing=3.14,
                daily_pacing=3.14,
                is_auto_daily_pacing=True,
                bid_strategy="conversion",
                status="unknown",
            ),
        ),
    ) # ExternalPutLineItem | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_line_item_by_line_item_id(line_item_id, external_put_line_item=external_put_line_item)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |
 **external_put_line_item** | [**ExternalPutLineItem**](ExternalPutLineItem.md)| The line item settings to create a line item with | [optional]

### Return type

[**JsonApiSingleResponseOfLineItem**](JsonApiSingleResponseOfLineItem.md)

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

# **put_api_v1_external_line_item_products_by_line_item_id**
> JsonApiPageResponseOfStringAndPromotedProduct put_api_v1_external_line_item_products_by_line_item_id(line_item_id)



This endpoint appends one or more products to promote on the specified line item.  The resulting state of the line item is returned.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_data_request_with_id_of_string_and_promoted_product import JsonApiDataRequestWithIdOfStringAndPromotedProduct
from criteo_api_retailmedia_preview.model.json_api_page_response_of_string_and_promoted_product import JsonApiPageResponseOfStringAndPromotedProduct
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item to interact with
    json_api_data_request_with_id_of_string_and_promoted_product = JsonApiDataRequestWithIdOfStringAndPromotedProduct(
        data=[
            JsonApiBodyWithIdOfStringAndPromotedProductAndPromotedProduct(
                id="id_example",
                type="type_example",
                attributes=ExternalPromotedProduct(
                    bid_override=3.14,
                ),
            ),
        ],
    ) # JsonApiDataRequestWithIdOfStringAndPromotedProduct | the products to append to this line item (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_line_item_products_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_line_item_products_by_line_item_id(line_item_id, json_api_data_request_with_id_of_string_and_promoted_product=json_api_data_request_with_id_of_string_and_promoted_product)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **json_api_data_request_with_id_of_string_and_promoted_product** | [**JsonApiDataRequestWithIdOfStringAndPromotedProduct**](JsonApiDataRequestWithIdOfStringAndPromotedProduct.md)| the products to append to this line item | [optional]

### Return type

[**JsonApiPageResponseOfStringAndPromotedProduct**](JsonApiPageResponseOfStringAndPromotedProduct.md)

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

