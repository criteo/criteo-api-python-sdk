# criteo_api_retailmedia_preview.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_keywords**](CampaignApi.md#add_remove_keywords) | **POST** /preview/retail-media/line-items/{id}/keywords/add-remove | 
[**append_promoted_products**](CampaignApi.md#append_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/append | 
[**delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **DELETE** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**delete_promoted_products**](CampaignApi.md#delete_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/delete | 
[**fetch_keywords**](CampaignApi.md#fetch_keywords) | **GET** /preview/retail-media/line-items/{id}/keywords | 
[**fetch_promoted_products**](CampaignApi.md#fetch_promoted_products) | **GET** /preview/retail-media/line-items/{line-item-id}/products | 
[**get_api202210_external_line_item_product_buttons_by_line_item_id**](CampaignApi.md#get_api202210_external_line_item_product_buttons_by_line_item_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons | 
[**get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**get_api_external_v2_catalog_status_by_catalog_id**](CampaignApi.md#get_api_external_v2_catalog_status_by_catalog_id) | **GET** /preview/retail-media/catalogs/{catalogId}/status | 
[**get_api_v1_external_retailer_brands_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_brands_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailerId}/brands | 
[**get_api_v1_external_retailer_by_retailer_id_seller_by_seller**](CampaignApi.md#get_api_v1_external_retailer_by_retailer_id_seller_by_seller) | **GET** /preview/retail-media/retailers/{retailerId}/sellers/{seller} | 
[**get_api_v1_external_retailer_category_cpc_rates_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_category_cpc_rates_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/cpc-rates | 
[**get_api_v1_external_retailer_placements_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_placements_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/placements | 
[**get_api_v2_external_account_by_account_id_creativescreative_id**](CampaignApi.md#get_api_v2_external_account_by_account_id_creativescreative_id) | **GET** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**get_api_v2_external_campaign_preferred_line_items_by_campaign_id**](CampaignApi.md#get_api_v2_external_campaign_preferred_line_items_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**get_api_v2_external_preferred_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_preferred_line_item_by_line_item_id) | **GET** /preview/retail-media/preferred-line-items/{line-item-id} | 
[**get_cpc_min_bids_by_sku_ids_v1**](CampaignApi.md#get_cpc_min_bids_by_sku_ids_v1) | **POST** /preview/retail-media/retailers/{retailerId}/cpc-min-bids | 
[**in_review_report_v1**](CampaignApi.md#in_review_report_v1) | **GET** /preview/retail-media/accounts/{account-id}/keywords/in-review-report | 
[**pause_promoted_products**](CampaignApi.md#pause_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/pause | 
[**post_api202110_external_campaign_preferred_line_items_by_campaign_id**](CampaignApi.md#post_api202110_external_campaign_preferred_line_items_by_campaign_id) | **POST** /preview/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**post_api202210_external_line_item_product_buttons_create_by_line_item_id**](CampaignApi.md#post_api202210_external_line_item_product_buttons_create_by_line_item_id) | **POST** /preview/retail-media/line-items/{line-item-id}/product-buttons/create | 
[**post_api_external_v2_account_brand_catalog_export_by_account_id**](CampaignApi.md#post_api_external_v2_account_brand_catalog_export_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/brand-catalog-export | 
[**post_api_external_v2_account_seller_catalog_export_by_account_id**](CampaignApi.md#post_api_external_v2_account_seller_catalog_export_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/seller-catalog-export | 
[**post_api_v1_external_catalogs_sku_retrieval**](CampaignApi.md#post_api_v1_external_catalogs_sku_retrieval) | **POST** /preview/retail-media/catalogs/sku-retrieval | 
[**post_api_v1_external_catalogs_sku_search**](CampaignApi.md#post_api_v1_external_catalogs_sku_search) | **POST** /preview/retail-media/catalogs/sku-search | 
[**post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id**](CampaignApi.md#post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id) | **POST** /preview/retail-media/catalogs/sku-search/accounts/{account-id}/retailers/{retailer-id} | 
[**post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id**](CampaignApi.md#post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id) | **POST** /preview/retail-media/catalogs/sku/search/retailers/{retailer-id} | 
[**post_api_v2_external_account_creatives_by_account_id**](CampaignApi.md#post_api_v2_external_account_creatives_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/creatives | 
[**post_api_v2_external_account_creatives_search_by_account_id**](CampaignApi.md#post_api_v2_external_account_creatives_search_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/creatives/search | 
[**put_api202110_external_preferred_line_item_by_line_item_id**](CampaignApi.md#put_api202110_external_preferred_line_item_by_line_item_id) | **PUT** /preview/retail-media/preferred-line-items/{line-item-id} | 
[**put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **PUT** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**put_api_v2_external_account_by_account_id_creativescreative_id**](CampaignApi.md#put_api_v2_external_account_by_account_id_creativescreative_id) | **PUT** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**search_brands_by_name_async_v1**](CampaignApi.md#search_brands_by_name_async_v1) | **POST** /preview/retail-media/brands/search | 
[**set_keyword_bids**](CampaignApi.md#set_keyword_bids) | **POST** /preview/retail-media/line-items/{id}/keywords/set-bid | 
[**unpause_promoted_products**](CampaignApi.md#unpause_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/unpause | 
[**update_keyword_reviews_v1**](CampaignApi.md#update_keyword_reviews_v1) | **POST** /preview/retail-media/line-items/{line-item-id}/keywords/review | 


# **add_remove_keywords**
> ResourceOutcome add_remove_keywords(id)



Add or Remove keywords from the line item in bulk

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.resource_outcome import ResourceOutcome
from criteo_api_retailmedia_preview.model.add_remove_keywords_model_request import AddRemoveKeywordsModelRequest
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | ID of the line item
    add_remove_keywords_model_request = AddRemoveKeywordsModelRequest(
        data=AddRemoveKeywordsModelResource(
            attributes=AddRemoveKeywordsModel(
                keywords=[
                    AddRemoveKeywordModel(
                        is_deleted=True,
                        match_type=MatchTypeModel("PositiveExactMatch"),
                        phrase="phrase_example",
                    ),
                ],
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AddRemoveKeywordsModelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_remove_keywords(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->add_remove_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_remove_keywords(id, add_remove_keywords_model_request=add_remove_keywords_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->add_remove_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the line item |
 **add_remove_keywords_model_request** | [**AddRemoveKeywordsModelRequest**](AddRemoveKeywordsModelRequest.md)|  | [optional]

### Return type

[**ResourceOutcome**](ResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_promoted_products**
> ProductResourceOutcome append_promoted_products(line_item_id)



Append a collection of promoted products to a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_resource_outcome import ProductResourceOutcome
from criteo_api_retailmedia_preview.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | ID of the line item
    promoted_product_resource_collection_input = PromotedProductResourceCollectionInput(
        data=[
            PromotedProductResource(
                attributes=PromotedProduct(
                    bid_override=3.14,
                    id="id_example",
                    status=LineItemProductStatus("unknown"),
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.append_promoted_products(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_promoted_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| ID of the line item |
 **promoted_product_resource_collection_input** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional]

### Return type

[**ProductResourceOutcome**](ProductResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Promoted products appended to the line item with warnings |  -  |
**204** | Promoted products appended to the line item |  -  |
**400** | Invalid request body |  -  |
**403** | Invalid external line item ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**
> delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)



Delete a product button

### Example

* OAuth Authentication (oauth):
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_id = "product-button-id_example" # str | Sequential id of the product button

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_id** | **str**| Sequential id of the product button |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_promoted_products**
> delete_promoted_products(line_item_id)



Remove a collection of promoted products from a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_resource_outcome import ProductResourceOutcome
from criteo_api_retailmedia_preview.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | ID of the line item
    promoted_product_resource_collection_input = PromotedProductResourceCollectionInput(
        data=[
            PromotedProductResource(
                attributes=PromotedProduct(
                    bid_override=3.14,
                    id="id_example",
                    status=LineItemProductStatus("unknown"),
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_promoted_products(line_item_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_promoted_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| ID of the line item |
 **promoted_product_resource_collection_input** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products removed from the line item |  -  |
**400** | Invalid request body |  -  |
**403** | Invalid external line item ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_keywords**
> KeywordsModelResponse fetch_keywords(id)



Fetch keywords associated with the specified line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.resource_outcome import ResourceOutcome
from criteo_api_retailmedia_preview.model.keywords_model_response import KeywordsModelResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | ID of the line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_keywords(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the line item |

### Return type

[**KeywordsModelResponse**](KeywordsModelResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_promoted_products**
> PromotedProductResourceCollectionOutcome fetch_promoted_products(line_item_id)



Retrieve a page of promoted products for a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.promoted_product_resource_collection_outcome import PromotedProductResourceCollectionOutcome
from criteo_api_retailmedia_preview.model.product_resource_outcome import ProductResourceOutcome
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | ID of the line item.
    fields = "fields_example" # str | A comma separated list of attribute names from the response model to compute and return.              Valid values are `status` and `bidOverride` in any order. Defaults to `status`. (optional)
    limit = 1 # int | Maximum page size to fetch. Defaults to 500. (optional)
    offset = 1 # int | Offset of the first item to fetch. Defaults to zero. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_promoted_products(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_promoted_products(line_item_id, fields=fields, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_promoted_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| ID of the line item. |
 **fields** | **str**| A comma separated list of attribute names from the response model to compute and return.              Valid values are &#x60;status&#x60; and &#x60;bidOverride&#x60; in any order. Defaults to &#x60;status&#x60;. | [optional]
 **limit** | **int**| Maximum page size to fetch. Defaults to 500. | [optional]
 **offset** | **int**| Offset of the first item to fetch. Defaults to zero. | [optional]

### Return type

[**PromotedProductResourceCollectionOutcome**](PromotedProductResourceCollectionOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Promoted products associated with the line item |  -  |
**403** | Invalid external line item ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202210_external_line_item_product_buttons_by_line_item_id**
> ProductButtonListResponse get_api202210_external_line_item_product_buttons_by_line_item_id(line_item_id)



Get all the product buttons associated with a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202210_external_line_item_product_buttons_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api202210_external_line_item_product_buttons_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |

### Return type

[**ProductButtonListResponse**](ProductButtonListResponse.md)

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

# **get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**
> ProductButtonListResponse get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)



Get a single product button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_id = "product-button-id_example" # str | Sequential id of the product button

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_id** | **str**| Sequential id of the product button |

### Return type

[**ProductButtonListResponse**](ProductButtonListResponse.md)

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

# **get_api_external_v2_catalog_status_by_catalog_id**
> EntityResourceOutcomeOfCatalogStatusV2 get_api_external_v2_catalog_status_by_catalog_id(catalog_id)



Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_catalog_status_v2 import EntityResourceOutcomeOfCatalogStatusV2
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
        api_response = api_instance.get_api_external_v2_catalog_status_by_catalog_id(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v2_catalog_status_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request found. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_brands_by_retailer_id**
> BrandPreviewListResponse get_api_v1_external_retailer_brands_by_retailer_id(retailer_id)



Gets the brands for the given retailer

### Example

* OAuth Authentication (oauth):
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
    brand_type = "all" # str |  Filter to narrow down brands [all|uc|retailer]. Defaults to uc (optional)
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
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id, brand_type=brand_type, sku_stock_type_filter=sku_stock_type_filter)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which brands should be fetched. |
 **brand_type** | **str**|  Filter to narrow down brands [all|uc|retailer]. Defaults to uc | [optional]
 **sku_stock_type_filter** | **str**| Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party | [optional]

### Return type

[**BrandPreviewListResponse**](BrandPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

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

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Seller found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_category_cpc_rates_by_retailer_id**
> CpcRateCardPreviewResponse get_api_v1_external_retailer_category_cpc_rates_by_retailer_id(retailer_id)



Gets the minimum cpc bid for the retailer, and optionally the categories under the retailer

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.cpc_rate_card_preview_response import CpcRateCardPreviewResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer id
    fields = [
        "fields_example",
    ] # [str] | The fields in the response that is to be included (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_category_cpc_rates_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_category_cpc_rates_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_retailer_category_cpc_rates_by_retailer_id(retailer_id, fields=fields)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_category_cpc_rates_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer id |
 **fields** | **[str]**| The fields in the response that is to be included | [optional]

### Return type

[**CpcRateCardPreviewResponse**](CpcRateCardPreviewResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bids found |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_placements_by_retailer_id**
> PlacementPreviewListResponse get_api_v1_external_retailer_placements_by_retailer_id(retailer_id)



Gets all placement information for the given retailer

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.placement_preview_list_response import PlacementPreviewListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer id for which placements should be fetched.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_placements_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_placements_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer id for which placements should be fetched. |

### Return type

[**PlacementPreviewListResponse**](PlacementPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | placements records. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_account_by_account_id_creativescreative_id**
> Creative2Response get_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Get the specified creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative2_response import Creative2Response
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_id = "creative-id_example" # str | Creative to get

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_account_by_account_id_creativescreative_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to retrieve creatives for |
 **creative_id** | **str**| Creative to get |

### Return type

[**Creative2Response**](Creative2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_campaign_preferred_line_items_by_campaign_id**
> PreferredLineItemV2PagedListResponse get_api_v2_external_campaign_preferred_line_items_by_campaign_id(campaign_id)



Gets page of preferred line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.preferred_line_item_v2_paged_list_response import PreferredLineItemV2PagedListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
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
        api_response = api_instance.get_api_v2_external_campaign_preferred_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_campaign_preferred_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_campaign_preferred_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_campaign_preferred_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**PreferredLineItemV2PagedListResponse**](PreferredLineItemV2PagedListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response get_api_v2_external_preferred_line_item_by_line_item_id(line_item_id)



Gets the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.preferred_line_item_v2_response import PreferredLineItemV2Response
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_preferred_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_preferred_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**PreferredLineItemV2Response**](PreferredLineItemV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cpc_min_bids_by_sku_ids_v1**
> ValueResourceOutcomeCpcMinBidsResponse get_cpc_min_bids_by_sku_ids_v1(retailer_id)



Get overall and individual minimum bid amount for given retailer id and sku id list.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_input_cpc_min_bids_request import ValueResourceInputCpcMinBidsRequest
from criteo_api_retailmedia_preview.model.value_resource_outcome_cpc_min_bids_response import ValueResourceOutcomeCpcMinBidsResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | Retailer Id.
    value_resource_input_cpc_min_bids_request = ValueResourceInputCpcMinBidsRequest(
        data=ValueResourceCpcMinBidsRequest(
            attributes=CpcMinBidsRequest(
                sku_ids=[
                    "sku_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputCpcMinBidsRequest | Cpc minimum bid amount request object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cpc_min_bids_by_sku_ids_v1(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_cpc_min_bids_by_sku_ids_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cpc_min_bids_by_sku_ids_v1(retailer_id, value_resource_input_cpc_min_bids_request=value_resource_input_cpc_min_bids_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_cpc_min_bids_by_sku_ids_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| Retailer Id. |
 **value_resource_input_cpc_min_bids_request** | [**ValueResourceInputCpcMinBidsRequest**](ValueResourceInputCpcMinBidsRequest.md)| Cpc minimum bid amount request object. | [optional]

### Return type

[**ValueResourceOutcomeCpcMinBidsResponse**](ValueResourceOutcomeCpcMinBidsResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **in_review_report_v1**
> EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata in_review_report_v1(account_id)



Generate a list of reports for line items which contain one or more actionable keyword reviews

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_line_item_keyword_review_report_and_metadata import EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = 1 # int | The account to generate a report for
    limit = 25 # int | Number of items per page (optional) if omitted the server will use the default value of 25
    offset = 0 # int | Offset for pagination (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.in_review_report_v1(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->in_review_report_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.in_review_report_v1(account_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->in_review_report_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account to generate a report for |
 **limit** | **int**| Number of items per page | [optional] if omitted the server will use the default value of 25
 **offset** | **int**| Offset for pagination | [optional] if omitted the server will use the default value of 0

### Return type

[**EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata**](EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_promoted_products**
> pause_promoted_products(line_item_id)



Pause a collection of promoted products associated with a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_resource_outcome import ProductResourceOutcome
from criteo_api_retailmedia_preview.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | ID of the line item
    promoted_product_resource_collection_input = PromotedProductResourceCollectionInput(
        data=[
            PromotedProductResource(
                attributes=PromotedProduct(
                    bid_override=3.14,
                    id="id_example",
                    status=LineItemProductStatus("unknown"),
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.pause_promoted_products(line_item_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->pause_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.pause_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->pause_promoted_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| ID of the line item |
 **promoted_product_resource_collection_input** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products paused |  -  |
**400** | Invalid request body |  -  |
**403** | Invalid external line item ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api202110_external_campaign_preferred_line_items_by_campaign_id**
> PreferredLineItemV2Response post_api202110_external_campaign_preferred_line_items_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)



Creates a new preferred line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.preferred_line_item_create_model_v2_request import PreferredLineItemCreateModelV2Request
from criteo_api_retailmedia_preview.model.preferred_line_item_v2_response import PreferredLineItemV2Response
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | The given campaign id
    preferred_line_item_create_model_v2_request = PreferredLineItemCreateModelV2Request(
        data=InputResourceOfPreferredLineItemCreateModelV2(
            attributes=ExternalPreferredLineItemCreateModelV2(
                budget=3.14,
                capping=ExternalLineItemCappingV2(
                    count=1,
                    type="unknown",
                ),
                creative_id="creative_id_example",
                end_date=dateutil_parser('1970-01-01').date(),
                name="name_example",
                pacing="unknown",
                page=ExternalLineItemPageV2(
                    categories=[
                        ExternalLineItemPageCategoryV2(
                            category_id="category_id_example",
                            include_children=True,
                        ),
                    ],
                    page_type="unknown",
                    search_keywords=[
                        "search_keywords_example",
                    ],
                ),
                start_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                target_retailer_id="target_retailer_id_example",
            ),
            type="type_example",
        ),
    ) # PreferredLineItemCreateModelV2Request | The line item settings to create a line item with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_campaign_preferred_line_items_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_campaign_preferred_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **preferred_line_item_create_model_v2_request** | [**PreferredLineItemCreateModelV2Request**](PreferredLineItemCreateModelV2Request.md)| The line item settings to create a line item with |

### Return type

[**PreferredLineItemV2Response**](PreferredLineItemV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api202210_external_line_item_product_buttons_create_by_line_item_id**
> ProductButtonListResponse post_api202210_external_line_item_product_buttons_create_by_line_item_id(line_item_id)



Append new product buttons to a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
from criteo_api_retailmedia_preview.model.product_button_list_request import ProductButtonListRequest
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_list_request = ProductButtonListRequest(
        data=[
            ResourceOfProductButtonRequest(
                attributes=ExternalProductButtonRequest(
                    background_image="background_image_example",
                    is_mandatory=1,
                    name="name_example",
                    skus=[
                        "skus_example",
                    ],
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # ProductButtonListRequest | List of product buttons to append to the specified line item (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202210_external_line_item_product_buttons_create_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_line_item_product_buttons_create_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202210_external_line_item_product_buttons_create_by_line_item_id(line_item_id, product_button_list_request=product_button_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_line_item_product_buttons_create_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_list_request** | [**ProductButtonListRequest**](ProductButtonListRequest.md)| List of product buttons to append to the specified line item | [optional]

### Return type

[**ProductButtonListResponse**](ProductButtonListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_external_v2_account_brand_catalog_export_by_account_id**
> EntityResourceOutcomeOfCatalogStatusV2 post_api_external_v2_account_brand_catalog_export_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_catalog_status_v2 import EntityResourceOutcomeOfCatalogStatusV2
from criteo_api_retailmedia_preview.model.value_resource_input_of_brand_catalog_request_v2 import ValueResourceInputOfBrandCatalogRequestV2
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
    value_resource_input_of_brand_catalog_request_v2 = ValueResourceInputOfBrandCatalogRequestV2(
        data=ValueResourceOfBrandCatalogRequestV2(
            attributes=BrandCatalogRequestV2(
                brand_id_filter=[
                    "brand_id_filter_example",
                ],
                include_fields=[
                    "Unknown",
                ],
                modified_after=dateutil_parser('1970-01-01T00:00:00.00Z'),
                retailer_id_filter=[
                    1,
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfBrandCatalogRequestV2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_external_v2_account_brand_catalog_export_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v2_account_brand_catalog_export_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_external_v2_account_brand_catalog_export_by_account_id(account_id, value_resource_input_of_brand_catalog_request_v2=value_resource_input_of_brand_catalog_request_v2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v2_account_brand_catalog_export_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **value_resource_input_of_brand_catalog_request_v2** | [**ValueResourceInputOfBrandCatalogRequestV2**](ValueResourceInputOfBrandCatalogRequestV2.md)|  | [optional]

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request successfully created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_external_v2_account_seller_catalog_export_by_account_id**
> EntityResourceOutcomeOfCatalogStatusV2 post_api_external_v2_account_seller_catalog_export_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_input_of_seller_catalog_request_v2 import ValueResourceInputOfSellerCatalogRequestV2
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_catalog_status_v2 import EntityResourceOutcomeOfCatalogStatusV2
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
    value_resource_input_of_seller_catalog_request_v2 = ValueResourceInputOfSellerCatalogRequestV2(
        data=ValueResourceOfSellerCatalogRequestV2(
            attributes=SellerCatalogRequestV2(
                include_fields=[
                    "Unknown",
                ],
                modified_after=dateutil_parser('1970-01-01T00:00:00.00Z'),
                sellers=[
                    SellerIdentifierV2(
                        retailer_id="retailer_id_example",
                        seller_id="seller_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfSellerCatalogRequestV2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_external_v2_account_seller_catalog_export_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v2_account_seller_catalog_export_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_external_v2_account_seller_catalog_export_by_account_id(account_id, value_resource_input_of_seller_catalog_request_v2=value_resource_input_of_seller_catalog_request_v2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v2_account_seller_catalog_export_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **value_resource_input_of_seller_catalog_request_v2** | [**ValueResourceInputOfSellerCatalogRequestV2**](ValueResourceInputOfSellerCatalogRequestV2.md)|  | [optional]

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request successfully created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_catalogs_sku_retrieval**
> SkuDataPreviewListResponse post_api_v1_external_catalogs_sku_retrieval()



Endpoint to search skus by text, retailer and sellers/brands.

### Example

* OAuth Authentication (oauth):
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

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

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
            attributes=SkuSearchRequestPreview(
                brand_ids=[
                    "brand_ids_example",
                ],
                product_ids=[
                    "product_ids_example",
                ],
                product_id_type="skuKey",
                query_string="query_string_example",
                retailer_id="retailer_id_example",
                sellers=[
                    "sellers_example",
                ],
                sku_type="brand",
            ),
            id="id_example",
            type="type_example",
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

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id**
> SkuSlimDataPreviewListResponse post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id(account_id, retailer_id)



Endpoint to search skus by text, account and retailer with an option to filter by brands id's.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.sku_search_request_slim_preview_request import SkuSearchRequestSlimPreviewRequest
from criteo_api_retailmedia_preview.model.sku_slim_data_preview_list_response import SkuSlimDataPreviewListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The account for which skus should be searched for.
    retailer_id = "retailer-id_example" # str | The client id/retailer id for which skus should be searched for.
    limit = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    sku_search_request_slim_preview_request = SkuSearchRequestSlimPreviewRequest(
        data=ResourceOfSkuSearchRequestSlimPreview(
            attributes=SkuSearchRequestSlimPreview(
                limit_results_to_skus_with_brand_ids=[
                    "limit_results_to_skus_with_brand_ids_example",
                ],
                search_string="search_string_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # SkuSearchRequestSlimPreviewRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id(account_id, retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id(account_id, retailer_id, limit=limit, offset=offset, sku_search_request_slim_preview_request=sku_search_request_slim_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account for which skus should be searched for. |
 **retailer_id** | **str**| The client id/retailer id for which skus should be searched for. |
 **limit** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **sku_search_request_slim_preview_request** | [**SkuSearchRequestSlimPreviewRequest**](SkuSearchRequestSlimPreviewRequest.md)|  | [optional]

### Return type

[**SkuSlimDataPreviewListResponse**](SkuSlimDataPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id**
> SkuSlimDataV2ListResponse post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id(retailer_id)



Endpoint to search skus by text for a retailer with an option to filter by brands id's.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.sku_slim_data_v2_list_response import SkuSlimDataV2ListResponse
from criteo_api_retailmedia_preview.model.sku_search_request_slim_v2_preview_request import SkuSearchRequestSlimV2PreviewRequest
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailer-id_example" # str | The client id/retailer id for which skus should be searched for.
    limit = 100 # int | The maximum number of results to return with each call. Must be greater than zero and less than 1500. 10,000 records deep is the max limit. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    x_origin_account = "X-Origin-Account_example" # str | The account id of the initiator of the call. (optional)
    sku_search_request_slim_v2_preview_request = SkuSearchRequestSlimV2PreviewRequest(
        data=ResourceOfSkuSearchRequestSlimV2Preview(
            attributes=SkuSearchRequestSlimV2Preview(
                brand_id=[
                    "brand_id_example",
                ],
                search_string="search_string_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # SkuSearchRequestSlimV2PreviewRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id(retailer_id, limit=limit, offset=offset, x_origin_account=x_origin_account, sku_search_request_slim_v2_preview_request=sku_search_request_slim_v2_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The client id/retailer id for which skus should be searched for. |
 **limit** | **int**| The maximum number of results to return with each call. Must be greater than zero and less than 1500. 10,000 records deep is the max limit. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **x_origin_account** | **str**| The account id of the initiator of the call. | [optional]
 **sku_search_request_slim_v2_preview_request** | [**SkuSearchRequestSlimV2PreviewRequest**](SkuSearchRequestSlimV2PreviewRequest.md)|  | [optional]

### Return type

[**SkuSlimDataV2ListResponse**](SkuSlimDataV2ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v2_external_account_creatives_by_account_id**
> Creative2Response post_api_v2_external_account_creatives_by_account_id(account_id)



Create a creative for an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative2_response import Creative2Response
from criteo_api_retailmedia_preview.model.creative_create_model2 import CreativeCreateModel2
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to create a creative for
    creative_create_model2 = CreativeCreateModel2(
        brand_id=1,
        name="name_example",
        retailer_id=1,
        template_id=1,
        template_variable_values=[
            TemplateVariableValue(
                choice_variable_value=ChoiceVariableValue(
                    chosen_options=[
                        "chosen_options_example",
                    ],
                ),
                color_variable_value=ColorVariableValue(
                    color="#2EC",
                ),
                files_variable_value=FilesVariableValue(
                    asset_ids=[
                        "asset_ids_example",
                    ],
                ),
                hyperlink_variable_value=HyperlinkVariableValue(
                    url="url_example",
                ),
                id="id_example",
                text_variable_value=TextVariableValue(
                    text="text_example",
                ),
                video_variable_value=VideoVariableValue(
                    duration="duration_example",
                    height=1,
                    url="url_example",
                    width=1,
                ),
            ),
        ],
    ) # CreativeCreateModel2 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_by_account_id(account_id, creative_create_model2=creative_create_model2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to create a creative for |
 **creative_create_model2** | [**CreativeCreateModel2**](CreativeCreateModel2.md)| The creative to create | [optional]

### Return type

[**Creative2Response**](Creative2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creatives created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v2_external_account_creatives_search_by_account_id**
> Creative2ListResponse post_api_v2_external_account_creatives_search_by_account_id(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative2_list_response import Creative2ListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_ids = [
        "creative-ids_example",
    ] # [str] | Creatives to filter by (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_search_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_search_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_search_by_account_id(account_id, creative_ids=creative_ids)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_search_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to retrieve creatives for |
 **creative_ids** | **[str]**| Creatives to filter by | [optional]

### Return type

[**Creative2ListResponse**](Creative2ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api202110_external_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response put_api202110_external_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)



Updates the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from criteo_api_retailmedia_preview.model.preferred_line_item_update_model_v2_request import PreferredLineItemUpdateModelV2Request
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id
    preferred_line_item_update_model_v2_request = PreferredLineItemUpdateModelV2Request(
        data=ResourceOfPreferredLineItemUpdateModelV2(
            attributes=ExternalPreferredLineItemUpdateModelV2(
                budget=3.14,
                capping=ExternalLineItemCappingV2(
                    count=1,
                    type="unknown",
                ),
                creative_id="creative_id_example",
                end_date=dateutil_parser('1970-01-01').date(),
                name="name_example",
                pacing="accelerated",
                page=ExternalLineItemPageV2(
                    categories=[
                        ExternalLineItemPageCategoryV2(
                            category_id="category_id_example",
                            include_children=True,
                        ),
                    ],
                    page_type="unknown",
                    search_keywords=[
                        "search_keywords_example",
                    ],
                ),
                start_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # PreferredLineItemUpdateModelV2Request | The line item settings to create a line item with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |
 **preferred_line_item_update_model_v2_request** | [**PreferredLineItemUpdateModelV2Request**](PreferredLineItemUpdateModelV2Request.md)| The line item settings to create a line item with |

### Return type

[**PreferredLineItemV2Response**](PreferredLineItemV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**
> ProductButtonListResponse put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)



Update a product button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_request import ProductButtonRequest
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_id = "product-button-id_example" # str | Sequential id of the product button
    product_button_request = ProductButtonRequest(
        data=ResourceOfProductButtonRequest(
            attributes=ExternalProductButtonRequest(
                background_image="background_image_example",
                is_mandatory=1,
                name="name_example",
                skus=[
                    "skus_example",
                ],
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ProductButtonRequest | Details of the updated product button (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id, product_button_request=product_button_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_id** | **str**| Sequential id of the product button |
 **product_button_request** | [**ProductButtonRequest**](ProductButtonRequest.md)| Details of the updated product button | [optional]

### Return type

[**ProductButtonListResponse**](ProductButtonListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v2_external_account_by_account_id_creativescreative_id**
> Creative2Response put_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Update a creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative2_response import Creative2Response
from criteo_api_retailmedia_preview.model.creative_update_model2 import CreativeUpdateModel2
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id containing the creative
    creative_id = "creative-id_example" # str | Creative to update
    creative_update_model2 = CreativeUpdateModel2(
        brand_id=1,
        name="name_example",
        retailer_id=1,
        template_id=1,
        template_variable_values=[
            TemplateVariableValue(
                choice_variable_value=ChoiceVariableValue(
                    chosen_options=[
                        "chosen_options_example",
                    ],
                ),
                color_variable_value=ColorVariableValue(
                    color="#2EC",
                ),
                files_variable_value=FilesVariableValue(
                    asset_ids=[
                        "asset_ids_example",
                    ],
                ),
                hyperlink_variable_value=HyperlinkVariableValue(
                    url="url_example",
                ),
                id="id_example",
                text_variable_value=TextVariableValue(
                    text="text_example",
                ),
                video_variable_value=VideoVariableValue(
                    duration="duration_example",
                    height=1,
                    url="url_example",
                    width=1,
                ),
            ),
        ],
    ) # CreativeUpdateModel2 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_account_by_account_id_creativescreative_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id, creative_update_model2=creative_update_model2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_account_by_account_id_creativescreative_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id containing the creative |
 **creative_id** | **str**| Creative to update |
 **creative_update_model2** | [**CreativeUpdateModel2**](CreativeUpdateModel2.md)| The creative to create | [optional]

### Return type

[**Creative2Response**](Creative2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Creative updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_brands_by_name_async_v1**
> EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata search_brands_by_name_async_v1()



Search for brands given a retailer ID and search term.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_input_brand_id_search_request import ValueResourceInputBrandIdSearchRequest
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_brand_id_search_result_paging_offset_limit_metadata import EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    limit = 25 # int | the number of brands to return (optional) if omitted the server will use the default value of 25
    offset = 0 # int | offset of paginated results (optional) if omitted the server will use the default value of 0
    value_resource_input_brand_id_search_request = ValueResourceInputBrandIdSearchRequest(
        data=ValueResourceBrandIdSearchRequest(
            attributes=BrandIdSearchRequest(
                brand_type="uc",
                name="name_example",
                retailer_ids=[
                    1,
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputBrandIdSearchRequest | BrandIdSearchRequest which contains the request parameters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_brands_by_name_async_v1(limit=limit, offset=offset, value_resource_input_brand_id_search_request=value_resource_input_brand_id_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_brands_by_name_async_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| the number of brands to return | [optional] if omitted the server will use the default value of 25
 **offset** | **int**| offset of paginated results | [optional] if omitted the server will use the default value of 0
 **value_resource_input_brand_id_search_request** | [**ValueResourceInputBrandIdSearchRequest**](ValueResourceInputBrandIdSearchRequest.md)| BrandIdSearchRequest which contains the request parameters | [optional]

### Return type

[**EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata**](EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_keyword_bids**
> ResourceOutcome set_keyword_bids(id)



Set bid overrides for associated keywords to the given line item in bulk

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.resource_outcome import ResourceOutcome
from criteo_api_retailmedia_preview.model.set_bids_model_request import SetBidsModelRequest
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | ID of the line item
    set_bids_model_request = SetBidsModelRequest(
        data=SetBidsModelResource(
            attributes=SetBidsModel(
                keywords=[
                    SetBidModel(
                        bid=3.14,
                        phrase="phrase_example",
                    ),
                ],
            ),
            id="id_example",
            type="type_example",
        ),
    ) # SetBidsModelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_keyword_bids(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_keyword_bids: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_keyword_bids(id, set_bids_model_request=set_bids_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_keyword_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the line item |
 **set_bids_model_request** | [**SetBidsModelRequest**](SetBidsModelRequest.md)|  | [optional]

### Return type

[**ResourceOutcome**](ResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpause_promoted_products**
> unpause_promoted_products(line_item_id)



Un-pause a collection of promoted products associated with a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_resource_outcome import ProductResourceOutcome
from criteo_api_retailmedia_preview.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | ID of the line item
    promoted_product_resource_collection_input = PromotedProductResourceCollectionInput(
        data=[
            PromotedProductResource(
                attributes=PromotedProduct(
                    bid_override=3.14,
                    id="id_example",
                    status=LineItemProductStatus("unknown"),
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.unpause_promoted_products(line_item_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->unpause_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.unpause_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->unpause_promoted_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| ID of the line item |
 **promoted_product_resource_collection_input** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products un-paused |  -  |
**400** | Invalid request body |  -  |
**403** | Invalid external line item ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_keyword_reviews_v1**
> ValueResourceOutcomeRetailMediaKeywordsReviewResult update_keyword_reviews_v1(line_item_id)



Update the status of keyword reviews under a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_input_retail_media_keywords_review import ValueResourceInputRetailMediaKeywordsReview
from criteo_api_retailmedia_preview.model.value_resource_outcome_retail_media_keywords_review_result import ValueResourceOutcomeRetailMediaKeywordsReviewResult
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = 1 # int | The line item to update keyword review statuses for
    value_resource_input_retail_media_keywords_review = ValueResourceInputRetailMediaKeywordsReview(
        data=ValueResourceRetailMediaKeywordsReview(
            attributes=RetailMediaKeywordsReview(
                keywords=[
                    ReviewSetState(
                        phrase="phrase_example",
                        review_state="Unknown",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputRetailMediaKeywordsReview | Request object containing a list of Phrase-ReviewState pairs to update (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_keyword_reviews_v1(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->update_keyword_reviews_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_keyword_reviews_v1(line_item_id, value_resource_input_retail_media_keywords_review=value_resource_input_retail_media_keywords_review)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->update_keyword_reviews_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **int**| The line item to update keyword review statuses for |
 **value_resource_input_retail_media_keywords_review** | [**ValueResourceInputRetailMediaKeywordsReview**](ValueResourceInputRetailMediaKeywordsReview.md)| Request object containing a list of Phrase-ReviewState pairs to update | [optional]

### Return type

[**ValueResourceOutcomeRetailMediaKeywordsReviewResult**](ValueResourceOutcomeRetailMediaKeywordsReviewResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

