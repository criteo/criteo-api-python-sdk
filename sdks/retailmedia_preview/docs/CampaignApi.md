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
[**fetch_proposal**](CampaignApi.md#fetch_proposal) | **GET** /preview/retail-media/preferred-deal-line-items/{id}/proposal | 
[**get_api202210_external_line_item_product_buttons_by_line_item_id**](CampaignApi.md#get_api202210_external_line_item_product_buttons_by_line_item_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons | 
[**get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**get_api_v1_external_account_brands_by_account_id**](CampaignApi.md#get_api_v1_external_account_brands_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/brands | 
[**get_api_v1_external_account_retailers_by_account_id**](CampaignApi.md#get_api_v1_external_account_retailers_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/retailers | 
[**get_api_v1_external_retailer_brands_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_brands_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailerId}/brands | 
[**get_api_v1_external_retailer_by_retailer_id_seller_by_seller**](CampaignApi.md#get_api_v1_external_retailer_by_retailer_id_seller_by_seller) | **GET** /preview/retail-media/retailers/{retailerId}/sellers/{seller} | 
[**get_api_v1_external_retailer_category_cpc_rates_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_category_cpc_rates_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/cpc-rates | 
[**get_api_v1_external_retailer_placements_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_placements_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/placements | 
[**get_api_v2_external_account_by_account_id_creativescreative_id**](CampaignApi.md#get_api_v2_external_account_by_account_id_creativescreative_id) | **GET** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**get_api_v2_external_campaign_preferred_line_items_by_campaign_id**](CampaignApi.md#get_api_v2_external_campaign_preferred_line_items_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**get_api_v2_external_line_item_bid_multipliers_by_line_item_id**](CampaignApi.md#get_api_v2_external_line_item_bid_multipliers_by_line_item_id) | **GET** /preview/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**get_api_v2_external_preferred_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_preferred_line_item_by_line_item_id) | **GET** /preview/retail-media/preferred-line-items/{line-item-id} | 
[**get_insertion_order_history_change_data_capture_v2**](CampaignApi.md#get_insertion_order_history_change_data_capture_v2) | **GET** /preview/retail-media/insertion-order-history/{insertionOrderId}/change-data-capture | 
[**get_recommended_keywords**](CampaignApi.md#get_recommended_keywords) | **GET** /preview/retail-media/line-items/{externalLineItemId}/keywords/recommended | 
[**get_sku_by_product_id**](CampaignApi.md#get_sku_by_product_id) | **POST** /preview/retail-media/catalogs/sku/search/accounts/{accountId}/retailers/{retailerId}/by-id | 
[**pause_promoted_products**](CampaignApi.md#pause_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/pause | 
[**post_api202110_external_campaign_preferred_line_items_by_campaign_id**](CampaignApi.md#post_api202110_external_campaign_preferred_line_items_by_campaign_id) | **POST** /preview/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**post_api202210_external_line_item_product_buttons_create_by_line_item_id**](CampaignApi.md#post_api202210_external_line_item_product_buttons_create_by_line_item_id) | **POST** /preview/retail-media/line-items/{line-item-id}/product-buttons/create | 
[**post_api_v1_external_account_catalogs_sellers_by_account_id**](CampaignApi.md#post_api_v1_external_account_catalogs_sellers_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/catalogs/sellers | 
[**post_api_v1_external_catalogs_sku_retrieval**](CampaignApi.md#post_api_v1_external_catalogs_sku_retrieval) | **POST** /preview/retail-media/catalogs/sku-retrieval | 
[**post_api_v1_external_catalogs_sku_search**](CampaignApi.md#post_api_v1_external_catalogs_sku_search) | **POST** /preview/retail-media/catalogs/sku-search | 
[**post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id**](CampaignApi.md#post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id) | **POST** /preview/retail-media/catalogs/sku-search/accounts/{account-id}/retailers/{retailer-id} | 
[**post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id**](CampaignApi.md#post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id) | **POST** /preview/retail-media/catalogs/sku/search/retailers/{retailer-id} | 
[**post_api_v2_external_account_creatives_by_account_id**](CampaignApi.md#post_api_v2_external_account_creatives_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/creatives | 
[**post_api_v2_external_account_creatives_search_by_account_id**](CampaignApi.md#post_api_v2_external_account_creatives_search_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/creatives/search | 
[**put_api202110_external_preferred_line_item_by_line_item_id**](CampaignApi.md#put_api202110_external_preferred_line_item_by_line_item_id) | **PUT** /preview/retail-media/preferred-line-items/{line-item-id} | 
[**put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **PUT** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**put_api_v2_external_account_by_account_id_creativescreative_id**](CampaignApi.md#put_api_v2_external_account_by_account_id_creativescreative_id) | **PUT** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**put_api_v2_external_line_item_bid_multipliers_by_line_item_id**](CampaignApi.md#put_api_v2_external_line_item_bid_multipliers_by_line_item_id) | **PUT** /preview/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**set_keyword_bids**](CampaignApi.md#set_keyword_bids) | **POST** /preview/retail-media/line-items/{id}/keywords/set-bid | 
[**submit_proposal**](CampaignApi.md#submit_proposal) | **POST** /preview/retail-media/preferred-deal-line-items/{id}/proposal/submit | 
[**unpause_promoted_products**](CampaignApi.md#unpause_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/unpause | 


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
            id="id_example",
            type="type_example",
            attributes=AddRemoveKeywordsModel(
                keywords=[
                    AddRemoveKeywordModel(
                        phrase="phrase_example",
                        match_type=MatchTypeModel("PositiveExactMatch"),
                        is_deleted=True,
                    ),
                ],
            ),
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
> append_promoted_products(line_item_id)



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
                id="id_example",
                type="type_example",
                attributes=PromotedProduct(
                    id="id_example",
                    bid_override=3.14,
                    status=LineItemProductStatus("Unknown"),
                ),
            ),
        ],
    ) # PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.append_promoted_products(line_item_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.append_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_promoted_products: %s\n" % e)
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
                id="id_example",
                type="type_example",
                attributes=PromotedProduct(
                    id="id_example",
                    bid_override=3.14,
                    status=LineItemProductStatus("Unknown"),
                ),
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
    offset = 1 # int | Offset of the first item to fetch. Defaults to zero. (optional)
    limit = 1 # int | Maximum page size to fetch. Defaults to 500. (optional)
    fields = "fields_example" # str | A comma separated list of attribute names from the response model to compute and return.              Valid values are `status` and `bidOverride` in any order. Defaults to `status`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_promoted_products(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_promoted_products(line_item_id, offset=offset, limit=limit, fields=fields)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_promoted_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| ID of the line item. |
 **offset** | **int**| Offset of the first item to fetch. Defaults to zero. | [optional]
 **limit** | **int**| Maximum page size to fetch. Defaults to 500. | [optional]
 **fields** | **str**| A comma separated list of attribute names from the response model to compute and return.              Valid values are &#x60;status&#x60; and &#x60;bidOverride&#x60; in any order. Defaults to &#x60;status&#x60;. | [optional]

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

# **fetch_proposal**
> ProposalStatusModelResponse fetch_proposal(id)



Includes the state of the proposal, the status of the booking and approval, as well as any comments explaining why it might have been rejected.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.proposal_status_model_response import ProposalStatusModelResponse
from criteo_api_retailmedia_preview.model.resource_outcome import ResourceOutcome
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
        api_response = api_instance.fetch_proposal(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_proposal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the line item |

### Return type

[**ProposalStatusModelResponse**](ProposalStatusModelResponse.md)

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
**403** | Forbidden |  -  |

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

# **get_api_v1_external_account_brands_by_account_id**
> JsonApiPageResponseOfBrand get_api_v1_external_account_brands_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):
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
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

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
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

### Return type

[**JsonApiPageResponseOfBrand**](JsonApiPageResponseOfBrand.md)

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

# **get_api_v1_external_account_retailers_by_account_id**
> JsonApiPageResponseOfRetailer get_api_v1_external_account_retailers_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):
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
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

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
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

### Return type

[**JsonApiPageResponseOfRetailer**](JsonApiPageResponseOfRetailer.md)

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
    sku_stock_type_filter = "first-party" # str | Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party (optional)
    brand_type = "all" # str |  Filter to narrow down brands [all|uc|retailer]. Defaults to uc (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id, sku_stock_type_filter=sku_stock_type_filter, brand_type=brand_type)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which brands should be fetched. |
 **sku_stock_type_filter** | **str**| Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party | [optional]
 **brand_type** | **str**|  Filter to narrow down brands [all|uc|retailer]. Defaults to uc | [optional]

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
> CreativeV2Response get_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Get the specified creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative_v2_response import CreativeV2Response
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

[**CreativeV2Response**](CreativeV2Response.md)

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

# **get_api_v2_external_line_item_bid_multipliers_by_line_item_id**
> JsonApiSingleResponseOfLineItemBidMultipliersV2 get_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)



Fetch all bid multipliers for a given line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item_bid_multipliers_v2 import JsonApiSingleResponseOfLineItemBidMultipliersV2
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
    line_item_id = "line-item-id_example" # str | External LineItemId for bid multiplier retrieval

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| External LineItemId for bid multiplier retrieval |

### Return type

[**JsonApiSingleResponseOfLineItemBidMultipliersV2**](JsonApiSingleResponseOfLineItemBidMultipliersV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BidMultipliers Found |  -  |

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

# **get_insertion_order_history_change_data_capture_v2**
> PageOfInsertionOrderHistoryChangeDataCaptureV2 get_insertion_order_history_change_data_capture_v2(insertion_order_id)



Gets the balance's historical data change capture.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.page_of_insertion_order_history_change_data_capture_v2 import PageOfInsertionOrderHistoryChangeDataCaptureV2
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
    insertion_order_id = "insertionOrderId_example" # str | External insertion order id.
    offset = 0 # int | The (zero-based) starting offset in the collection. (optional) if omitted the server will use the default value of 0
    limit = 25 # int | The number of elements to be returned. (optional) if omitted the server will use the default value of 25
    limit_to_change_types = "limitToChangeTypes_example" # str | Comma separated change types string that will be queried. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_insertion_order_history_change_data_capture_v2(insertion_order_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_insertion_order_history_change_data_capture_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_insertion_order_history_change_data_capture_v2(insertion_order_id, offset=offset, limit=limit, limit_to_change_types=limit_to_change_types)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_insertion_order_history_change_data_capture_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insertion_order_id** | **str**| External insertion order id. |
 **offset** | **int**| The (zero-based) starting offset in the collection. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The number of elements to be returned. | [optional] if omitted the server will use the default value of 25
 **limit_to_change_types** | **str**| Comma separated change types string that will be queried. | [optional]

### Return type

[**PageOfInsertionOrderHistoryChangeDataCaptureV2**](PageOfInsertionOrderHistoryChangeDataCaptureV2.md)

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

# **get_recommended_keywords**
> ValueResourceOutcomeOfRecommendedKeywordsResult get_recommended_keywords(external_line_item_id)



Retrieves a collection of recommended keywords for a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_of_recommended_keywords_result import ValueResourceOutcomeOfRecommendedKeywordsResult
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
    external_line_item_id = "externalLineItemId_example" # str | The external line item identifier

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_recommended_keywords(external_line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_recommended_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_line_item_id** | **str**| The external line item identifier |

### Return type

[**ValueResourceOutcomeOfRecommendedKeywordsResult**](ValueResourceOutcomeOfRecommendedKeywordsResult.md)

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

# **get_sku_by_product_id**
> ResourceCollectionOutcomeOfSkuSearchResult get_sku_by_product_id(account_id, retailer_id)



Gets a list of SKUs based on a privided list of Product Ids

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.resource_collection_outcome_of_sku_search_result import ResourceCollectionOutcomeOfSkuSearchResult
from criteo_api_retailmedia_preview.model.sku_search_request import SkuSearchRequest
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
    account_id = "4" # str | account id
    retailer_id = 1 # int | retailer id
    offset = 0 # int | skip a number of matches before retrning results, used with limit (optional) if omitted the server will use the default value of 0
    limit = 100 # int | max number of results to return (optional) if omitted the server will use the default value of 100
    sku_search_request = SkuSearchRequest(
        data=SkuSearchRequestBody(
            product_id_type="SkuKey",
            query_ids=[
                "query_ids_example",
            ],
        ),
    ) # SkuSearchRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sku_by_product_id(account_id, retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_sku_by_product_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sku_by_product_id(account_id, retailer_id, offset=offset, limit=limit, sku_search_request=sku_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_sku_by_product_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id |
 **retailer_id** | **int**| retailer id |
 **offset** | **int**| skip a number of matches before retrning results, used with limit | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| max number of results to return | [optional] if omitted the server will use the default value of 100
 **sku_search_request** | [**SkuSearchRequest**](SkuSearchRequest.md)|  | [optional]

### Return type

[**ResourceCollectionOutcomeOfSkuSearchResult**](ResourceCollectionOutcomeOfSkuSearchResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


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
                id="id_example",
                type="type_example",
                attributes=PromotedProduct(
                    id="id_example",
                    bid_override=3.14,
                    status=LineItemProductStatus("Unknown"),
                ),
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
            type="type_example",
            attributes=ExternalPreferredLineItemCreateModelV2(
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                pacing="unknown",
                capping=ExternalLineItemCappingV2(
                    type="unknown",
                    count=1,
                ),
                page=ExternalLineItemPageV2(
                    page_type="unknown",
                    categories=[
                        ExternalLineItemPageCategoryV2(
                            category_id="category_id_example",
                            include_children=True,
                        ),
                    ],
                    search_keywords=[
                        "search_keywords_example",
                    ],
                ),
                target_retailer_id="target_retailer_id_example",
                budget=3.14,
                creative_id="creative_id_example",
            ),
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
                    name="name_example",
                    background_image="background_image_example",
                    is_mandatory=1,
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

# **post_api_v1_external_account_catalogs_sellers_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v1_external_account_catalogs_sellers_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_preview.model.json_api_request_of_seller_catalog_request import JsonApiRequestOfSellerCatalogRequest
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
    json_api_request_of_seller_catalog_request = JsonApiRequestOfSellerCatalogRequest(
        data=JsonApiBodyWithoutIdOfSellerCatalogRequestAndSellerCatalogRequest(
            type="type_example",
            attributes=SellerCatalogRequest(
                sellers=[
                    SellerIdentifier(
                        retailer_id="retailer_id_example",
                        seller_id="seller_id_example",
                    ),
                ],
            ),
        ),
    ) # JsonApiRequestOfSellerCatalogRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_sellers_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_sellers_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_sellers_by_account_id(account_id, json_api_request_of_seller_catalog_request=json_api_request_of_seller_catalog_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_sellers_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **json_api_request_of_seller_catalog_request** | [**JsonApiRequestOfSellerCatalogRequest**](JsonApiRequestOfSellerCatalogRequest.md)|  | [optional]

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

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
                product_id_type="skuKey",
                product_ids=[
                    "product_ids_example",
                ],
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
    offset = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    sku_search_request_slim_preview_request = SkuSearchRequestSlimPreviewRequest(
        data=ResourceOfSkuSearchRequestSlimPreview(
            attributes=SkuSearchRequestSlimPreview(
                search_string="search_string_example",
                limit_results_to_skus_with_brand_ids=[
                    "limit_results_to_skus_with_brand_ids_example",
                ],
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
        api_response = api_instance.post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id(account_id, retailer_id, offset=offset, limit=limit, sku_search_request_slim_preview_request=sku_search_request_slim_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search_account_id_and_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account for which skus should be searched for. |
 **retailer_id** | **str**| The client id/retailer id for which skus should be searched for. |
 **offset** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
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
    x_origin_account = "X-Origin-Account_example" # str | The account id of the initiator of the call. (optional)
    offset = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The maximum number of results to return with each call. Must be greater than zero and less than 1500. 10,000 records deep is the max limit. (optional) if omitted the server will use the default value of 100
    sku_search_request_slim_v2_preview_request = SkuSearchRequestSlimV2PreviewRequest(
        data=ResourceOfSkuSearchRequestSlimV2Preview(
            attributes=SkuSearchRequestSlimV2Preview(
                search_string="search_string_example",
                brand_id=[
                    "brand_id_example",
                ],
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
        api_response = api_instance.post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id(retailer_id, x_origin_account=x_origin_account, offset=offset, limit=limit, sku_search_request_slim_v2_preview_request=sku_search_request_slim_v2_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search_retailer_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The client id/retailer id for which skus should be searched for. |
 **x_origin_account** | **str**| The account id of the initiator of the call. | [optional]
 **offset** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to return with each call. Must be greater than zero and less than 1500. 10,000 records deep is the max limit. | [optional] if omitted the server will use the default value of 100
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
> CreativeV2Response post_api_v2_external_account_creatives_by_account_id(account_id)



Create a creative for an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.external_creative_create_model_v2 import ExternalCreativeCreateModelV2
from criteo_api_retailmedia_preview.model.creative_v2_response import CreativeV2Response
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
    external_creative_create_model_v2 = ExternalCreativeCreateModelV2(
        name="name_example",
        brand_id=1,
        retailer_id=1,
        template_id=1,
        template_variable_values=[
            ExternalTemplateVariableValue(
                id="id_example",
                text_variable_value=ExternalTextVariableValue(
                    text="text_example",
                ),
                choice_variable_value=ExternalChoiceVariableValue(
                    chosen_options=[
                        "chosen_options_example",
                    ],
                ),
                color_variable_value=ExternalColorVariableValue(
                    color="#2EC",
                ),
                files_variable_value=ExternalFilesVariableValue(
                    asset_ids=[
                        "asset_ids_example",
                    ],
                ),
                hyperlink_variable_value=ExternalHyperlinkVariableValue(
                    url="url_example",
                ),
                video_variable_value=ExternalVideoVariableValue(
                    url="url_example",
                    width=1,
                    height=1,
                    duration="duration_example",
                ),
            ),
        ],
    ) # ExternalCreativeCreateModelV2 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_by_account_id(account_id, external_creative_create_model_v2=external_creative_create_model_v2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to create a creative for |
 **external_creative_create_model_v2** | [**ExternalCreativeCreateModelV2**](ExternalCreativeCreateModelV2.md)| The creative to create | [optional]

### Return type

[**CreativeV2Response**](CreativeV2Response.md)

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
> CreativeV2ListResponse post_api_v2_external_account_creatives_search_by_account_id(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative_v2_list_response import CreativeV2ListResponse
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

[**CreativeV2ListResponse**](CreativeV2ListResponse.md)

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
            id="id_example",
            type="type_example",
            attributes=ExternalPreferredLineItemUpdateModelV2(
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                pacing="accelerated",
                capping=ExternalLineItemCappingV2(
                    type="unknown",
                    count=1,
                ),
                page=ExternalLineItemPageV2(
                    page_type="unknown",
                    categories=[
                        ExternalLineItemPageCategoryV2(
                            category_id="category_id_example",
                            include_children=True,
                        ),
                    ],
                    search_keywords=[
                        "search_keywords_example",
                    ],
                ),
                budget=3.14,
                creative_id="creative_id_example",
            ),
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
                name="name_example",
                background_image="background_image_example",
                is_mandatory=1,
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
> CreativeV2Response put_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Update a creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.external_creative_update_model_v2 import ExternalCreativeUpdateModelV2
from criteo_api_retailmedia_preview.model.creative_v2_response import CreativeV2Response
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
    external_creative_update_model_v2 = ExternalCreativeUpdateModelV2(
        name="name_example",
        brand_id=1,
        retailer_id=1,
        template_id=1,
        template_variable_values=[
            ExternalTemplateVariableValue(
                id="id_example",
                text_variable_value=ExternalTextVariableValue(
                    text="text_example",
                ),
                choice_variable_value=ExternalChoiceVariableValue(
                    chosen_options=[
                        "chosen_options_example",
                    ],
                ),
                color_variable_value=ExternalColorVariableValue(
                    color="#2EC",
                ),
                files_variable_value=ExternalFilesVariableValue(
                    asset_ids=[
                        "asset_ids_example",
                    ],
                ),
                hyperlink_variable_value=ExternalHyperlinkVariableValue(
                    url="url_example",
                ),
                video_variable_value=ExternalVideoVariableValue(
                    url="url_example",
                    width=1,
                    height=1,
                    duration="duration_example",
                ),
            ),
        ],
    ) # ExternalCreativeUpdateModelV2 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_account_by_account_id_creativescreative_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id, external_creative_update_model_v2=external_creative_update_model_v2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_account_by_account_id_creativescreative_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id containing the creative |
 **creative_id** | **str**| Creative to update |
 **external_creative_update_model_v2** | [**ExternalCreativeUpdateModelV2**](ExternalCreativeUpdateModelV2.md)| The creative to create | [optional]

### Return type

[**CreativeV2Response**](CreativeV2Response.md)

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

# **put_api_v2_external_line_item_bid_multipliers_by_line_item_id**
> LineItemBidMultipliersV2Response put_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)



Updates the bid multipliers for a given line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers_v2_response import LineItemBidMultipliersV2Response
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers_v2_request import LineItemBidMultipliersV2Request
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
    line_item_id = "line-item-id_example" # str | External LineItemId for bid multiplier retrieval
    line_item_bid_multipliers_v2_request = LineItemBidMultipliersV2Request(
        data=ResourceOfLineItemBidMultipliersV2(
            attributes=ExternalLineItemBidMultipliersV2(
                search=3.14,
                home=3.14,
                category=3.14,
                product_detail=3.14,
                confirmation=3.14,
                merchandising=3.14,
                deals=3.14,
                checkout=3.14,
                favorites=3.14,
                search_bar=3.14,
                category_menu=3.14,
            ),
            id="id_example",
            type="type_example",
        ),
    ) # LineItemBidMultipliersV2Request | New Bid Multipliers to be set (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id, line_item_bid_multipliers_v2_request=line_item_bid_multipliers_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| External LineItemId for bid multiplier retrieval |
 **line_item_bid_multipliers_v2_request** | [**LineItemBidMultipliersV2Request**](LineItemBidMultipliersV2Request.md)| New Bid Multipliers to be set | [optional]

### Return type

[**LineItemBidMultipliersV2Response**](LineItemBidMultipliersV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BidMultipliers Updated |  -  |

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
            id="id_example",
            type="type_example",
            attributes=SetBidsModel(
                keywords=[
                    SetBidModel(
                        phrase="phrase_example",
                        bid=3.14,
                    ),
                ],
            ),
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

# **submit_proposal**
> ProposalStatusModelResponse submit_proposal(id)



Only the components of the Line Item that are in a valid state will be reviewed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.proposal_status_model_response import ProposalStatusModelResponse
from criteo_api_retailmedia_preview.model.resource_outcome import ResourceOutcome
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
        api_response = api_instance.submit_proposal(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->submit_proposal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the line item |

### Return type

[**ProposalStatusModelResponse**](ProposalStatusModelResponse.md)

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
**403** | Forbidden |  -  |

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
                id="id_example",
                type="type_example",
                attributes=PromotedProduct(
                    id="id_example",
                    bid_override=3.14,
                    status=LineItemProductStatus("Unknown"),
                ),
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

