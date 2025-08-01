# criteo_api_retailmedia_v2025_01.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_keywords**](CampaignApi.md#add_remove_keywords) | **POST** /2025-01/retail-media/line-items/{id}/keywords/add-remove | 
[**append_promoted_products**](CampaignApi.md#append_promoted_products) | **POST** /2025-01/retail-media/line-items/{line-item-id}/products/append | 
[**create_asset**](CampaignApi.md#create_asset) | **POST** /2025-01/retail-media/assets | 
[**delete_promoted_products**](CampaignApi.md#delete_promoted_products) | **POST** /2025-01/retail-media/line-items/{line-item-id}/products/delete | 
[**fetch_keywords**](CampaignApi.md#fetch_keywords) | **GET** /2025-01/retail-media/line-items/{id}/keywords | 
[**fetch_promoted_products**](CampaignApi.md#fetch_promoted_products) | **GET** /2025-01/retail-media/line-items/{line-item-id}/products | 
[**get_api202110_external_account_creatives_by_account_id**](CampaignApi.md#get_api202110_external_account_creatives_by_account_id) | **GET** /2025-01/retail-media/accounts/{account-id}/creatives | 
[**get_api202110_external_auction_line_item_targeting_keywords_by_line_item_id**](CampaignApi.md#get_api202110_external_auction_line_item_targeting_keywords_by_line_item_id) | **GET** /2025-01/retail-media/auction-line-items/{line-item-id}/targeting/keywords | 
[**get_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id**](CampaignApi.md#get_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id) | **GET** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | 
[**get_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id**](CampaignApi.md#get_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id) | **GET** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | 
[**get_api202110_external_preferred_line_item_targeting_stores_by_line_item_id**](CampaignApi.md#get_api202110_external_preferred_line_item_targeting_stores_by_line_item_id) | **GET** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | 
[**get_api202110_external_retailer_pages_by_retailer_id**](CampaignApi.md#get_api202110_external_retailer_pages_by_retailer_id) | **GET** /2025-01/retail-media/retailers/{retailerId}/pages | 
[**get_api202204_external_categorie_by_category_id**](CampaignApi.md#get_api202204_external_categorie_by_category_id) | **GET** /2025-01/retail-media/categories/{categoryId} | 
[**get_api202204_external_categories**](CampaignApi.md#get_api202204_external_categories) | **GET** /2025-01/retail-media/categories | 
[**get_api202207_external_retailer_by_retailer_id_templatestemplate_id**](CampaignApi.md#get_api202207_external_retailer_by_retailer_id_templatestemplate_id) | **GET** /2025-01/retail-media/retailers/{retailer-id}/templates/{template-id} | 
[**get_api202207_external_retailer_templates_by_retailer_id**](CampaignApi.md#get_api202207_external_retailer_templates_by_retailer_id) | **GET** /2025-01/retail-media/retailers/{retailer-id}/templates | 
[**get_api202301_external_account_campaigns_by_account_id**](CampaignApi.md#get_api202301_external_account_campaigns_by_account_id) | **GET** /2025-01/retail-media/accounts/{account-id}/campaigns | 
[**get_api202301_external_campaign_by_campaign_id**](CampaignApi.md#get_api202301_external_campaign_by_campaign_id) | **GET** /2025-01/retail-media/campaigns/{campaignId} | 
[**get_api_v1_external_account_brands_by_account_id**](CampaignApi.md#get_api_v1_external_account_brands_by_account_id) | **GET** /2025-01/retail-media/accounts/{accountId}/brands | 
[**get_api_v1_external_account_retailers_by_account_id**](CampaignApi.md#get_api_v1_external_account_retailers_by_account_id) | **GET** /2025-01/retail-media/accounts/{accountId}/retailers | 
[**get_api_v1_external_catalog_output_by_catalog_id**](CampaignApi.md#get_api_v1_external_catalog_output_by_catalog_id) | **GET** /2025-01/retail-media/catalogs/{catalogId}/output | 
[**get_api_v1_external_catalog_status_by_catalog_id**](CampaignApi.md#get_api_v1_external_catalog_status_by_catalog_id) | **GET** /2025-01/retail-media/catalogs/{catalogId}/status | 
[**get_api_v2_external_account_by_account_id_creativescreative_id**](CampaignApi.md#get_api_v2_external_account_by_account_id_creativescreative_id) | **GET** /2025-01/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**get_api_v2_external_account_line_items_by_account_id**](CampaignApi.md#get_api_v2_external_account_line_items_by_account_id) | **GET** /2025-01/retail-media/accounts/{account-id}/line-items | 
[**get_api_v2_external_auction_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_auction_line_item_by_line_item_id) | **GET** /2025-01/retail-media/auction-line-items/{line-item-id} | 
[**get_api_v2_external_campaign_auction_line_items_by_campaign_id**](CampaignApi.md#get_api_v2_external_campaign_auction_line_items_by_campaign_id) | **GET** /2025-01/retail-media/campaigns/{campaign-id}/auction-line-items | 
[**get_api_v2_external_campaign_preferred_line_items_by_campaign_id**](CampaignApi.md#get_api_v2_external_campaign_preferred_line_items_by_campaign_id) | **GET** /2025-01/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**get_api_v2_external_line_item_bid_multipliers_by_line_item_id**](CampaignApi.md#get_api_v2_external_line_item_bid_multipliers_by_line_item_id) | **GET** /2025-01/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**get_api_v2_external_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_line_item_by_line_item_id) | **GET** /2025-01/retail-media/line-items/{line-item-id} | 
[**get_api_v2_external_preferred_line_item_by_line_item_id**](CampaignApi.md#get_api_v2_external_preferred_line_item_by_line_item_id) | **GET** /2025-01/retail-media/preferred-line-items/{line-item-id} | 
[**get_campaign_budget_overrides**](CampaignApi.md#get_campaign_budget_overrides) | **GET** /2025-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | 
[**get_line_item_budget_overrides**](CampaignApi.md#get_line_item_budget_overrides) | **GET** /2025-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | 
[**get_recommended_keywords**](CampaignApi.md#get_recommended_keywords) | **GET** /2025-01/retail-media/line-items/{externalLineItemId}/keywords/recommended | 
[**pause_promoted_products**](CampaignApi.md#pause_promoted_products) | **POST** /2025-01/retail-media/line-items/{line-item-id}/products/pause | 
[**post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id**](CampaignApi.md#post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id) | **POST** /2025-01/retail-media/auction-line-items/{line-item-id}/targeting/keywords/append | 
[**post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id**](CampaignApi.md#post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id) | **POST** /2025-01/retail-media/auction-line-items/{line-item-id}/targeting/keywords/delete | 
[**post_api202110_external_balance_campaigns_append_by_balance_id**](CampaignApi.md#post_api202110_external_balance_campaigns_append_by_balance_id) | **POST** /2025-01/retail-media/balances/{balance-id}/campaigns/append | 
[**post_api202110_external_balance_campaigns_delete_by_balance_id**](CampaignApi.md#post_api202110_external_balance_campaigns_delete_by_balance_id) | **POST** /2025-01/retail-media/balances/{balance-id}/campaigns/delete | 
[**post_api202110_external_campaign_preferred_line_items_by_campaign_id**](CampaignApi.md#post_api202110_external_campaign_preferred_line_items_by_campaign_id) | **POST** /2025-01/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id**](CampaignApi.md#post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id) | **POST** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append | 
[**post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id**](CampaignApi.md#post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id) | **POST** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete | 
[**post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id**](CampaignApi.md#post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id) | **POST** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append | 
[**post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id**](CampaignApi.md#post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id) | **POST** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete | 
[**post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id**](CampaignApi.md#post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id) | **POST** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append | 
[**post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id**](CampaignApi.md#post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id) | **POST** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete | 
[**post_api202210_external_account_creatives_by_account_id**](CampaignApi.md#post_api202210_external_account_creatives_by_account_id) | **POST** /2025-01/retail-media/accounts/{account-id}/creatives | 
[**post_api202301_external_account_campaigns_by_account_id**](CampaignApi.md#post_api202301_external_account_campaigns_by_account_id) | **POST** /2025-01/retail-media/accounts/{account-id}/campaigns | 
[**post_api_v1_external_account_catalogs_by_account_id**](CampaignApi.md#post_api_v1_external_account_catalogs_by_account_id) | **POST** /2025-01/retail-media/accounts/{accountId}/catalogs | 
[**post_api_v1_external_account_catalogs_sellers_by_account_id**](CampaignApi.md#post_api_v1_external_account_catalogs_sellers_by_account_id) | **POST** /2025-01/retail-media/accounts/{accountId}/catalogs/sellers | 
[**post_api_v2_external_account_creatives_search_by_account_id**](CampaignApi.md#post_api_v2_external_account_creatives_search_by_account_id) | **POST** /2025-01/retail-media/accounts/{account-id}/creatives/search | 
[**post_api_v2_external_campaign_auction_line_items_by_campaign_id**](CampaignApi.md#post_api_v2_external_campaign_auction_line_items_by_campaign_id) | **POST** /2025-01/retail-media/campaigns/{campaign-id}/auction-line-items | 
[**put_api202110_external_preferred_line_item_by_line_item_id**](CampaignApi.md#put_api202110_external_preferred_line_item_by_line_item_id) | **PUT** /2025-01/retail-media/preferred-line-items/{line-item-id} | 
[**put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id**](CampaignApi.md#put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id) | **PUT** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | 
[**put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id**](CampaignApi.md#put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id) | **PUT** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | 
[**put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id**](CampaignApi.md#put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id) | **PUT** /2025-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | 
[**put_api202210_external_account_by_account_id_creativescreative_id**](CampaignApi.md#put_api202210_external_account_by_account_id_creativescreative_id) | **PUT** /2025-01/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**put_api202301_external_campaign_by_campaign_id**](CampaignApi.md#put_api202301_external_campaign_by_campaign_id) | **PUT** /2025-01/retail-media/campaigns/{campaignId} | 
[**put_api_v2_external_auction_line_item_by_line_item_id**](CampaignApi.md#put_api_v2_external_auction_line_item_by_line_item_id) | **PUT** /2025-01/retail-media/auction-line-items/{line-item-id} | 
[**put_api_v2_external_line_item_bid_multipliers_by_line_item_id**](CampaignApi.md#put_api_v2_external_line_item_bid_multipliers_by_line_item_id) | **PUT** /2025-01/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**set_keyword_bids**](CampaignApi.md#set_keyword_bids) | **POST** /2025-01/retail-media/line-items/{id}/keywords/set-bid | 
[**unpause_promoted_products**](CampaignApi.md#unpause_promoted_products) | **POST** /2025-01/retail-media/line-items/{line-item-id}/products/unpause | 
[**update_campaign_budget_overrides**](CampaignApi.md#update_campaign_budget_overrides) | **PUT** /2025-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | 
[**update_line_item_budget_overrides**](CampaignApi.md#update_line_item_budget_overrides) | **PUT** /2025-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | 


# **add_remove_keywords**
> ResourceOutcome add_remove_keywords(id)



Add or Remove keywords from the line item in bulk

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.add_remove_keywords_model_request import AddRemoveKeywordsModelRequest
from criteo_api_retailmedia_v2025_01.model.resource_outcome import ResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->add_remove_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_remove_keywords(id, add_remove_keywords_model_request=add_remove_keywords_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from criteo_api_retailmedia_v2025_01.model.product_resource_outcome import ProductResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->append_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **create_asset**
> AssetResponse create_asset(asset_file)



Creates an asset

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.asset_response import AssetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    asset_file = open('/path/to/file', 'rb') # file_type | The asset binary content

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_asset(asset_file)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->create_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_file** | **file_type**| The asset binary content |

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_promoted_products**
> delete_promoted_products(line_item_id)



Remove a collection of promoted products from a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from criteo_api_retailmedia_v2025_01.model.product_resource_outcome import ProductResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.keywords_model_response import KeywordsModelResponse
from criteo_api_retailmedia_v2025_01.model.resource_outcome import ResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | ID of the line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_keywords(id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.promoted_product_resource_collection_outcome import PromotedProductResourceCollectionOutcome
from criteo_api_retailmedia_v2025_01.model.product_resource_outcome import ProductResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->fetch_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_promoted_products(line_item_id, fields=fields, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **get_api202110_external_account_creatives_by_account_id**
> Creative202110ListResponse get_api202110_external_account_creatives_by_account_id(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.creative202110_list_response import Creative202110ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_account_creatives_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_account_creatives_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to retrieve creatives for |

### Return type

[**Creative202110ListResponse**](Creative202110ListResponse.md)

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

# **get_api202110_external_auction_line_item_targeting_keywords_by_line_item_id**
> KeywordTarget202110Response get_api202110_external_auction_line_item_targeting_keywords_by_line_item_id(line_item_id)



This endpoint gets the keyword target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.keyword_target202110_response import KeywordTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_auction_line_item_targeting_keywords_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_auction_line_item_targeting_keywords_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |

### Return type

[**KeywordTarget202110Response**](KeywordTarget202110Response.md)

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

# **get_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id**
> AddToBasketTarget202110Response get_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id(line_item_id)



This endpoint gets the add to basket target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

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

# **get_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id**
> AudienceTarget202110Response get_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id(line_item_id)



This endpoint gets the audience target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

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

# **get_api202110_external_preferred_line_item_targeting_stores_by_line_item_id**
> StoreTarget202110Response get_api202110_external_preferred_line_item_targeting_stores_by_line_item_id(line_item_id)



This endpoint gets the store target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_preferred_line_item_targeting_stores_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_preferred_line_item_targeting_stores_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

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

# **get_api202110_external_retailer_pages_by_retailer_id**
> ExternalRetailerPages202110 get_api202110_external_retailer_pages_by_retailer_id(retailer_id)



Get the page types available for the given retailer

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.external_retailer_pages202110 import ExternalRetailerPages202110
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | The retailers to fetch pages for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_retailer_pages_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_retailer_pages_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailers to fetch pages for |

### Return type

[**ExternalRetailerPages202110**](ExternalRetailerPages202110.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pages fetched successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202204_external_categorie_by_category_id**
> Category202204 get_api202204_external_categorie_by_category_id(category_id)



Endpoint to search for a specific category by categoryId.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.category202204 import Category202204
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    category_id = 1 # int | ID of the desired category

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202204_external_categorie_by_category_id(category_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202204_external_categorie_by_category_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of the desired category |

### Return type

[**Category202204**](Category202204.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieval completed and category is returned. |  -  |
**400** | No IDs were passed in. |  -  |
**500** | A non-request input based error occurred in the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202204_external_categories**
> Category202204ListResponse get_api202204_external_categories()



Endpoint to search categories by text and retailer.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.category202204_list_response import Category202204ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    retailer_id = 1 # int | The retailer id for which Categories fetched (optional)
    text_substring = "textSubstring_example" # str | Query string to search across Categories (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api202204_external_categories(page_index=page_index, page_size=page_size, retailer_id=retailer_id, text_substring=text_substring)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202204_external_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
 **retailer_id** | **int**| The retailer id for which Categories fetched | [optional]
 **text_substring** | **str**| Query string to search across Categories | [optional]

### Return type

[**Category202204ListResponse**](Category202204ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202207_external_retailer_by_retailer_id_templatestemplate_id**
> TemplateResponse get_api202207_external_retailer_by_retailer_id_templatestemplate_id(retailer_id, template_id)



Gets the template for the specified retailer id and template id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.template_response import TemplateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | Retailer Id
    template_id = 1 # int | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202207_external_retailer_by_retailer_id_templatestemplate_id(retailer_id, template_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202207_external_retailer_by_retailer_id_templatestemplate_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| Retailer Id |
 **template_id** | **int**| Template Id |

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template found for the retailer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202207_external_retailer_templates_by_retailer_id**
> TemplateListResponse get_api202207_external_retailer_templates_by_retailer_id(retailer_id)



Get retailer creative templates

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.template_list_response import TemplateListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | External retailer id to retrieve creative templates for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202207_external_retailer_templates_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202207_external_retailer_templates_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| External retailer id to retrieve creative templates for |

### Return type

[**TemplateListResponse**](TemplateListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Templates found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202301_external_account_campaigns_by_account_id**
> JsonApiPageResponseOfCampaignV202301 get_api202301_external_account_campaigns_by_account_id(account_id)



Get all the editable and creatable campaign attributes including all types of budgets for each campaigns in relation to the account id, limited by the campaign ids.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_page_response_of_campaign_v202301 import JsonApiPageResponseOfCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The account to request the campaign for.
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202301_external_account_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202301_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api202301_external_account_campaigns_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202301_external_account_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the campaign for. |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

### Return type

[**JsonApiPageResponseOfCampaignV202301**](JsonApiPageResponseOfCampaignV202301.md)

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

# **get_api202301_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaignV202301 get_api202301_external_campaign_by_campaign_id(campaign_id)



Get all the editable and creatable campaign attributes including all types of budgets given the campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | Campaign Id of the campaign detail

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202301_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202301_external_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign Id of the campaign detail |

### Return type

[**JsonApiSingleResponseOfCampaignV202301**](JsonApiSingleResponseOfCampaignV202301.md)

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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_brands_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_brands_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_retailers_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_retailers_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **get_api_v1_external_catalog_output_by_catalog_id**
> file_type get_api_v1_external_catalog_output_by_catalog_id(catalog_id)



Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream of v2021_07 CatalogProduct json objects.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_catalog_output_by_catalog_id(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_catalog_output_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

**file_type**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-json-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog download initiated. |  -  |
**204** | Catalog has expired. |  -  |
**400** | The indicated catalog is not available for retrieval, wait for a success status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_catalog_status_by_catalog_id**
> JsonApiSingleResponseOfCatalogStatus get_api_v1_external_catalog_status_by_catalog_id(catalog_id)



Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_catalog_status_by_catalog_id(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_catalog_status_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_account_by_account_id_creativescreative_id**
> Creative2Response get_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Get the specified creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.creative2_response import Creative2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_id = "creative-id_example" # str | Creative to get

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **get_api_v2_external_account_line_items_by_account_id**
> CommonLineItemPagedListResponse get_api_v2_external_account_line_items_by_account_id(account_id)



Gets page of line item objects for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.common_line_item_paged_list_response import CommonLineItemPagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The given account id
    limit_to_campaign_id = [
        "limitToCampaignId_example",
    ] # [str] | The campaign ids that you would like to limit your result set to (optional)
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    limit_to_type = "Unknown" # str, none_type | The campaign types that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_account_line_items_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_account_line_items_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_account_line_items_by_account_id(account_id, limit_to_campaign_id=limit_to_campaign_id, limit_to_id=limit_to_id, limit_to_type=limit_to_type, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_account_line_items_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_campaign_id** | **[str]**| The campaign ids that you would like to limit your result set to | [optional]
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **limit_to_type** | **str, none_type**| The campaign types that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**CommonLineItemPagedListResponse**](CommonLineItemPagedListResponse.md)

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

# **get_api_v2_external_auction_line_item_by_line_item_id**
> AuctionLineItemResponse get_api_v2_external_auction_line_item_by_line_item_id(line_item_id)



Gets the auction line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.auction_line_item_response import AuctionLineItemResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_auction_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_auction_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**AuctionLineItemResponse**](AuctionLineItemResponse.md)

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

# **get_api_v2_external_campaign_auction_line_items_by_campaign_id**
> AuctionLineItemPagedListResponse get_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)



Gets page of auction line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.auction_line_item_paged_list_response import AuctionLineItemPagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_campaign_auction_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **get_api_v2_external_campaign_preferred_line_items_by_campaign_id**
> PreferredLineItemV2PagedListResponse get_api_v2_external_campaign_preferred_line_items_by_campaign_id(campaign_id)



Gets page of preferred line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.preferred_line_item_v2_paged_list_response import PreferredLineItemV2PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_campaign_preferred_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_campaign_preferred_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_line_item_bid_multipliers_v2 import JsonApiSingleResponseOfLineItemBidMultipliersV2
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | External LineItemId for bid multiplier retrieval

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **get_api_v2_external_line_item_by_line_item_id**
> CommonLineItemResponse get_api_v2_external_line_item_by_line_item_id(line_item_id)



Gets the line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.common_line_item_response import CommonLineItemResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v2_external_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**CommonLineItemResponse**](CommonLineItemResponse.md)

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

# **get_api_v2_external_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response get_api_v2_external_preferred_line_item_by_line_item_id(line_item_id)



Gets the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_preferred_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **get_campaign_budget_overrides**
> ValueResourceOutcomeOfCampaignBudgetOverrides get_campaign_budget_overrides(campaign_id)



Get current campaign budget overrides by given campaign id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.value_resource_outcome_of_campaign_budget_overrides import ValueResourceOutcomeOfCampaignBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | Campaign id.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign_budget_overrides(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign_budget_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Campaign id. |

### Return type

[**ValueResourceOutcomeOfCampaignBudgetOverrides**](ValueResourceOutcomeOfCampaignBudgetOverrides.md)

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

# **get_line_item_budget_overrides**
> ValueResourceOutcomeOfLineItemBudgetOverrides get_line_item_budget_overrides(line_item_id)



Gets a collection of monthly and daily budget overrides for the provided line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.value_resource_outcome_of_line_item_budget_overrides import ValueResourceOutcomeOfLineItemBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item id to get budget overrides for.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_line_item_budget_overrides(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_line_item_budget_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item id to get budget overrides for. |

### Return type

[**ValueResourceOutcomeOfLineItemBudgetOverrides**](ValueResourceOutcomeOfLineItemBudgetOverrides.md)

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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.value_resource_outcome_of_recommended_keywords_result import ValueResourceOutcomeOfRecommendedKeywordsResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    external_line_item_id = "externalLineItemId_example" # str | The line item identifier

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_recommended_keywords(external_line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->get_recommended_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_line_item_id** | **str**| The line item identifier |

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

# **pause_promoted_products**
> pause_promoted_products(line_item_id)



Pause a collection of promoted products associated with a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from criteo_api_retailmedia_v2025_01.model.product_resource_outcome import ProductResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->pause_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.pause_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id**
> KeywordTarget202110Response post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id(line_item_id)



This endpoint appends one or more keywords to targeting on the specified line item.  The resulting state of the keyword target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.keyword_target202110_response import KeywordTarget202110Response
from criteo_api_retailmedia_v2025_01.model.keyword_target202110_request import KeywordTarget202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    keyword_target202110_request = KeywordTarget202110Request(
        data=ValueTypeResourceOfKeywordTarget202110(
            attributes=ExternalKeywordTarget202110(
                keywords={
                    "unknown": "unknown",
                },
            ),
            type="type_example",
        ),
    ) # KeywordTarget202110Request |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id(line_item_id, keyword_target202110_request=keyword_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_auction_line_item_targeting_keywords_append_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **keyword_target202110_request** | [**KeywordTarget202110Request**](KeywordTarget202110Request.md)|  | [optional]

### Return type

[**KeywordTarget202110Response**](KeywordTarget202110Response.md)

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

# **post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id**
> KeywordTarget202110Response post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id(line_item_id)



This endpoint removes one or more keywords from targeting on the specified line item.  The resulting state of the keyword target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.keyword_target202110_response import KeywordTarget202110Response
from criteo_api_retailmedia_v2025_01.model.keyword_target202110_request import KeywordTarget202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    keyword_target202110_request = KeywordTarget202110Request(
        data=ValueTypeResourceOfKeywordTarget202110(
            attributes=ExternalKeywordTarget202110(
                keywords={
                    "unknown": "unknown",
                },
            ),
            type="type_example",
        ),
    ) # KeywordTarget202110Request |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id(line_item_id, keyword_target202110_request=keyword_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_auction_line_item_targeting_keywords_delete_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **keyword_target202110_request** | [**KeywordTarget202110Request**](KeywordTarget202110Request.md)|  | [optional]

### Return type

[**KeywordTarget202110Response**](KeywordTarget202110Response.md)

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

# **post_api202110_external_balance_campaigns_append_by_balance_id**
> BalanceCampaign202110PagedListResponse post_api202110_external_balance_campaigns_append_by_balance_id(balance_id)



appends one or more campaigns to the specified balance

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from criteo_api_retailmedia_v2025_01.model.balance_campaign202110_list_request import BalanceCampaign202110ListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balance-id_example" # str | The balance to add campaigns from
    balance_campaign202110_list_request = BalanceCampaign202110ListRequest(
        data=[
            ResourceOfBalanceCampaign202110(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # BalanceCampaign202110ListRequest | The campaigns to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_balance_campaigns_append_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_balance_campaigns_append_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_balance_campaigns_append_by_balance_id(balance_id, balance_campaign202110_list_request=balance_campaign202110_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_balance_campaigns_append_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to add campaigns from |
 **balance_campaign202110_list_request** | [**BalanceCampaign202110ListRequest**](BalanceCampaign202110ListRequest.md)| The campaigns to append | [optional]

### Return type

[**BalanceCampaign202110PagedListResponse**](BalanceCampaign202110PagedListResponse.md)

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

# **post_api202110_external_balance_campaigns_delete_by_balance_id**
> BalanceCampaign202110PagedListResponse post_api202110_external_balance_campaigns_delete_by_balance_id(balance_id)



Removes one or more campaigns on the specified balance

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from criteo_api_retailmedia_v2025_01.model.balance_campaign202110_list_request import BalanceCampaign202110ListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balance-id_example" # str | The balance to remove campaigns from
    balance_campaign202110_list_request = BalanceCampaign202110ListRequest(
        data=[
            ResourceOfBalanceCampaign202110(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # BalanceCampaign202110ListRequest | The campaigns to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_balance_campaigns_delete_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_balance_campaigns_delete_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_balance_campaigns_delete_by_balance_id(balance_id, balance_campaign202110_list_request=balance_campaign202110_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_balance_campaigns_delete_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to remove campaigns from |
 **balance_campaign202110_list_request** | [**BalanceCampaign202110ListRequest**](BalanceCampaign202110ListRequest.md)| The campaigns to append | [optional]

### Return type

[**BalanceCampaign202110PagedListResponse**](BalanceCampaign202110PagedListResponse.md)

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

# **post_api202110_external_campaign_preferred_line_items_by_campaign_id**
> PreferredLineItemV2Response post_api202110_external_campaign_preferred_line_items_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)



Creates a new preferred line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from criteo_api_retailmedia_v2025_01.model.preferred_line_item_create_model_v2_request import PreferredLineItemCreateModelV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id**
> AddToBasketTarget202110Response post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id(line_item_id)



This endpoint appends one or more add to basket ids to targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from criteo_api_retailmedia_v2025_01.model.add_to_basket_ids_update_model202110_request import AddToBasketIdsUpdateModel202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    add_to_basket_ids_update_model202110_request = AddToBasketIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAddToBasketIdsUpdateModel202110(
            attributes=ExternalAddToBasketIdsUpdateModel202110(
                category_ids=[
                    "category_ids_example",
                ],
                product_ids=[
                    "product_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AddToBasketIdsUpdateModel202110Request | Ids to append to the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id(line_item_id, add_to_basket_ids_update_model202110_request=add_to_basket_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_add_to_basket_append_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **add_to_basket_ids_update_model202110_request** | [**AddToBasketIdsUpdateModel202110Request**](AddToBasketIdsUpdateModel202110Request.md)| Ids to append to the target | [optional]

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

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

# **post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id**
> AddToBasketTarget202110Response post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id(line_item_id)



This endpoint removes one or more add to basket ids from targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from criteo_api_retailmedia_v2025_01.model.add_to_basket_ids_update_model202110_request import AddToBasketIdsUpdateModel202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    add_to_basket_ids_update_model202110_request = AddToBasketIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAddToBasketIdsUpdateModel202110(
            attributes=ExternalAddToBasketIdsUpdateModel202110(
                category_ids=[
                    "category_ids_example",
                ],
                product_ids=[
                    "product_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AddToBasketIdsUpdateModel202110Request | Ids to remove from the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id(line_item_id, add_to_basket_ids_update_model202110_request=add_to_basket_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_add_to_basket_delete_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **add_to_basket_ids_update_model202110_request** | [**AddToBasketIdsUpdateModel202110Request**](AddToBasketIdsUpdateModel202110Request.md)| Ids to remove from the target | [optional]

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

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

# **post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id**
> AudienceTarget202110Response post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id(line_item_id)



This endpoint appends one or more audiences ids to targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.audience_ids_update_model202110_request import AudienceIdsUpdateModel202110Request
from criteo_api_retailmedia_v2025_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    audience_ids_update_model202110_request = AudienceIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAudienceIdsUpdateModel202110(
            attributes=ExternalAudienceIdsUpdateModel202110(
                audience_ids=[
                    "audience_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AudienceIdsUpdateModel202110Request | Audience ids to append to the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id(line_item_id, audience_ids_update_model202110_request=audience_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_audiences_append_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **audience_ids_update_model202110_request** | [**AudienceIdsUpdateModel202110Request**](AudienceIdsUpdateModel202110Request.md)| Audience ids to append to the target | [optional]

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

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

# **post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id**
> AudienceTarget202110Response post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id(line_item_id)



This endpoint removes one or more audiences ids from targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.audience_ids_update_model202110_request import AudienceIdsUpdateModel202110Request
from criteo_api_retailmedia_v2025_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    audience_ids_update_model202110_request = AudienceIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAudienceIdsUpdateModel202110(
            attributes=ExternalAudienceIdsUpdateModel202110(
                audience_ids=[
                    "audience_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AudienceIdsUpdateModel202110Request | Audience ids to remove from the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id(line_item_id, audience_ids_update_model202110_request=audience_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_audiences_delete_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **audience_ids_update_model202110_request** | [**AudienceIdsUpdateModel202110Request**](AudienceIdsUpdateModel202110Request.md)| Audience ids to remove from the target | [optional]

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

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

# **post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id**
> StoreTarget202110Response post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id(line_item_id)



This endpoint appends one or more store ids to targeting on the specified line item.  The resulting state of the store target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.store_ids_update_model202110_request import StoreIdsUpdateModel202110Request
from criteo_api_retailmedia_v2025_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    store_ids_update_model202110_request = StoreIdsUpdateModel202110Request(
        data=ValueTypeResourceOfStoreIdsUpdateModel202110(
            attributes=ExternalStoreIdsUpdateModel202110(
                store_ids=[
                    "store_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # StoreIdsUpdateModel202110Request | Store ids to append to the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id(line_item_id, store_ids_update_model202110_request=store_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_stores_append_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **store_ids_update_model202110_request** | [**StoreIdsUpdateModel202110Request**](StoreIdsUpdateModel202110Request.md)| Store ids to append to the target | [optional]

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

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

# **post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id**
> StoreTarget202110Response post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id(line_item_id)



This endpoint removes one or more store ids from targeting on the specified line item.  The resulting state of the store target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.store_ids_update_model202110_request import StoreIdsUpdateModel202110Request
from criteo_api_retailmedia_v2025_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    store_ids_update_model202110_request = StoreIdsUpdateModel202110Request(
        data=ValueTypeResourceOfStoreIdsUpdateModel202110(
            attributes=ExternalStoreIdsUpdateModel202110(
                store_ids=[
                    "store_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # StoreIdsUpdateModel202110Request | Store ids to remove from the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id(line_item_id, store_ids_update_model202110_request=store_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202110_external_preferred_line_item_targeting_stores_delete_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **store_ids_update_model202110_request** | [**StoreIdsUpdateModel202110Request**](StoreIdsUpdateModel202110Request.md)| Store ids to remove from the target | [optional]

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

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

# **post_api202210_external_account_creatives_by_account_id**
> Creative202210Response post_api202210_external_account_creatives_by_account_id(account_id)



Create a creative for an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_v2025_01.model.creative_create_model202207 import CreativeCreateModel202207
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to create a creative for
    creative_create_model202207 = CreativeCreateModel202207(
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
    ) # CreativeCreateModel202207 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202210_external_account_creatives_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_account_creatives_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202210_external_account_creatives_by_account_id(account_id, creative_create_model202207=creative_create_model202207)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_account_creatives_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to create a creative for |
 **creative_create_model202207** | [**CreativeCreateModel202207**](CreativeCreateModel202207.md)| The creative to create | [optional]

### Return type

[**Creative202210Response**](Creative202210Response.md)

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

# **post_api202301_external_account_campaigns_by_account_id**
> JsonApiSingleResponseOfCampaignV202301 post_api202301_external_account_campaigns_by_account_id(account_id)



Create a campaign and assign budgets for the given account id with creatable campaign attributes given in request body constrained by business validation. The validation error includes details and source of errors. Pacing can be adjusted and affected by the status of the campaign and the days left on the campaign if auto daily pacing is enabled.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from criteo_api_retailmedia_v2025_01.model.post_campaign_v202301 import PostCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The account to request the campaign for.
    post_campaign_v202301 = PostCampaignV202301(
        data=JsonApiBodyWithoutIdOfCampaignAttributesV202301AndCampaignV202301(
            attributes=CampaignAttributesV202301(
                budget=3.14,
                click_attribution_scope="unknown",
                click_attribution_window="30D",
                company_name="company_name_example",
                daily_pacing=3.14,
                drawable_balance_ids=[
                    "drawable_balance_ids_example",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                is_auto_daily_pacing=True,
                monthly_pacing=3.14,
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                type="auction",
                view_attribution_scope="unknown",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # PostCampaignV202301 | Creatable campaign attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202301_external_account_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202301_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202301_external_account_campaigns_by_account_id(account_id, post_campaign_v202301=post_campaign_v202301)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api202301_external_account_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the campaign for. |
 **post_campaign_v202301** | [**PostCampaignV202301**](PostCampaignV202301.md)| Creatable campaign attributes | [optional]

### Return type

[**JsonApiSingleResponseOfCampaignV202301**](JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_catalogs_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v1_external_account_catalogs_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_v2025_01.model.json_api_request_of_catalog_request import JsonApiRequestOfCatalogRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to request the catalog for.
    json_api_request_of_catalog_request = JsonApiRequestOfCatalogRequest(
        data=JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequest(
            attributes=ExternalCatalogRequest(
                brand_id_filter=[
                    "brand_id_filter_example",
                ],
                format="json-newline",
            ),
            type="type_example",
        ),
    ) # JsonApiRequestOfCatalogRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_by_account_id(account_id, json_api_request_of_catalog_request=json_api_request_of_catalog_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_catalogs_sellers_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v1_external_account_catalogs_sellers_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_v2025_01.model.json_api_request_of_seller_catalog_request import JsonApiRequestOfSellerCatalogRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to request the catalog for.
    json_api_request_of_seller_catalog_request = JsonApiRequestOfSellerCatalogRequest(
        data=JsonApiBodyWithoutIdOfSellerCatalogRequestAndSellerCatalogRequest(
            attributes=SellerCatalogRequest(
                sellers=[
                    SellerIdentifier(
                        retailer_id="retailer_id_example",
                        seller_id="seller_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # JsonApiRequestOfSellerCatalogRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_sellers_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_sellers_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_sellers_by_account_id(account_id, json_api_request_of_seller_catalog_request=json_api_request_of_seller_catalog_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **post_api_v2_external_account_creatives_search_by_account_id**
> Creative2ListResponse post_api_v2_external_account_creatives_search_by_account_id(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.creative2_list_response import Creative2ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_account_creatives_search_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v2_external_account_creatives_search_by_account_id(account_id, creative_ids=creative_ids)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **post_api_v2_external_campaign_auction_line_items_by_campaign_id**
> AuctionLineItemResponse post_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)



Creates new auction line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.auction_line_item_create_model_request import AuctionLineItemCreateModelRequest
from criteo_api_retailmedia_v2025_01.model.auction_line_item_response import AuctionLineItemResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | The given campaign id
    auction_line_item_create_model_request = AuctionLineItemCreateModelRequest(
        data=InputResourceOfAuctionLineItemCreateModel(
            attributes=ExternalAuctionLineItemCreateModel(
                bid_strategy="conversion",
                budget=3.14,
                daily_pacing=3.14,
                end_date=dateutil_parser('1970-01-01').date(),
                is_auto_daily_pacing=False,
                max_bid=3.14,
                monthly_pacing=3.14,
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                target_bid=3.14,
                target_retailer_id="target_retailer_id_example",
            ),
            type="type_example",
        ),
    ) # AuctionLineItemCreateModelRequest | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v2_external_campaign_auction_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v2_external_campaign_auction_line_items_by_campaign_id(campaign_id, auction_line_item_create_model_request=auction_line_item_create_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **put_api202110_external_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response put_api202110_external_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)



Updates the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from criteo_api_retailmedia_v2025_01.model.preferred_line_item_update_model_v2_request import PreferredLineItemUpdateModelV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id**
> AddToBasketTarget202110Response put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id(line_item_id)



This endpoint sets the scope of the add to basket target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from criteo_api_retailmedia_v2025_01.model.add_to_basket_target202110_request import AddToBasketTarget202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    add_to_basket_target202110_request = AddToBasketTarget202110Request(
        data=ValueTypeResourceOfAddToBasketTarget202110(
            attributes=ExternalAddToBasketTarget202110(
                category_ids=[
                    "category_ids_example",
                ],
                product_ids=[
                    "product_ids_example",
                ],
                scope="unknown",
            ),
            type="type_example",
        ),
    ) # AddToBasketTarget202110Request | The add to basket target to set the scope for (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id(line_item_id, add_to_basket_target202110_request=add_to_basket_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_targeting_add_to_basket_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **add_to_basket_target202110_request** | [**AddToBasketTarget202110Request**](AddToBasketTarget202110Request.md)| The add to basket target to set the scope for | [optional]

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

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

# **put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id**
> AudienceTarget202110Response put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id(line_item_id)



This endpoint sets the scope of the audience target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.audience_target202110_response import AudienceTarget202110Response
from criteo_api_retailmedia_v2025_01.model.audience_target202110_request import AudienceTarget202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    audience_target202110_request = AudienceTarget202110Request(
        data=ValueTypeResourceOfAudienceTarget202110(
            attributes=ExternalAudienceTarget202110(
                audience_ids=[
                    "audience_ids_example",
                ],
                scope="unknown",
            ),
            type="type_example",
        ),
    ) # AudienceTarget202110Request | The audience target to set the scope for (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id(line_item_id, audience_target202110_request=audience_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_targeting_audiences_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **audience_target202110_request** | [**AudienceTarget202110Request**](AudienceTarget202110Request.md)| The audience target to set the scope for | [optional]

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

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

# **put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id**
> StoreTarget202110Response put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id(line_item_id)



This endpoint sets the scope of the store target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.store_target202110_request import StoreTarget202110Request
from criteo_api_retailmedia_v2025_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    store_target202110_request = StoreTarget202110Request(
        data=ValueTypeResourceOfStoreTarget202110(
            attributes=ExternalStoreTarget202110(
                scope="unknown",
                store_ids=[
                    "store_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # StoreTarget202110Request | The store target to set the scope for (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id(line_item_id, store_target202110_request=store_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202110_external_preferred_line_item_targeting_stores_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **store_target202110_request** | [**StoreTarget202110Request**](StoreTarget202110Request.md)| The store target to set the scope for | [optional]

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

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

# **put_api202210_external_account_by_account_id_creativescreative_id**
> Creative202210Response put_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Update a creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_v2025_01.model.creative_update_model202207 import CreativeUpdateModel202207
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id containing the creative
    creative_id = "creative-id_example" # str | Creative to update
    creative_update_model202207 = CreativeUpdateModel202207(
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
    ) # CreativeUpdateModel202207 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_account_by_account_id_creativescreative_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id, creative_update_model202207=creative_update_model202207)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_account_by_account_id_creativescreative_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id containing the creative |
 **creative_id** | **str**| Creative to update |
 **creative_update_model202207** | [**CreativeUpdateModel202207**](CreativeUpdateModel202207.md)| The creative to create | [optional]

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creative updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api202301_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaignV202301 put_api202301_external_campaign_by_campaign_id(campaign_id)



Edit a campaign for the given campaign id with a given editable attributes. This will return updated creatable and editable attributes of the campaign as the result of the operation. Pacing can be adjusted and affected by the status of the campaign and the days left on the campaign if auto daily pacing is enabled.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.put_campaign_v202301 import PutCampaignV202301
from criteo_api_retailmedia_v2025_01.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | Campaign Id of the updating campaign
    put_campaign_v202301 = PutCampaignV202301(
        data=JsonApiBodyWithExternalIdOfEditableCampaignAttributesV202301AndCampaignV202301(
            attributes=EditableCampaignAttributesV202301(
                budget=3.14,
                click_attribution_scope="unknown",
                click_attribution_window="7D",
                company_name="company_name_example",
                daily_pacing=3.14,
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                is_auto_daily_pacing=True,
                monthly_pacing=3.14,
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                view_attribution_scope="unknown",
                view_attribution_window="none",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # PutCampaignV202301 | Editable campaign attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202301_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202301_external_campaign_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202301_external_campaign_by_campaign_id(campaign_id, put_campaign_v202301=put_campaign_v202301)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api202301_external_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign Id of the updating campaign |
 **put_campaign_v202301** | [**PutCampaignV202301**](PutCampaignV202301.md)| Editable campaign attributes | [optional]

### Return type

[**JsonApiSingleResponseOfCampaignV202301**](JsonApiSingleResponseOfCampaignV202301.md)

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

# **put_api_v2_external_auction_line_item_by_line_item_id**
> AuctionLineItemResponse put_api_v2_external_auction_line_item_by_line_item_id(line_item_id)



Updates the auction line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.auction_line_item_update_model_request import AuctionLineItemUpdateModelRequest
from criteo_api_retailmedia_v2025_01.model.auction_line_item_response import AuctionLineItemResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id
    auction_line_item_update_model_request = AuctionLineItemUpdateModelRequest(
        data=ResourceOfAuctionLineItemUpdateModel(
            attributes=ExternalAuctionLineItemUpdateModel(
                bid_strategy="conversion",
                budget=3.14,
                daily_pacing=3.14,
                end_date=dateutil_parser('1970-01-01').date(),
                is_auto_daily_pacing=True,
                max_bid=3.14,
                monthly_pacing=3.14,
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                status="unknown",
                target_bid=3.14,
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AuctionLineItemUpdateModelRequest | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v2_external_auction_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_auction_line_item_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v2_external_auction_line_item_by_line_item_id(line_item_id, auction_line_item_update_model_request=auction_line_item_update_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **put_api_v2_external_line_item_bid_multipliers_by_line_item_id**
> LineItemBidMultipliersV2Response put_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)



Updates the bid multipliers for a given line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.line_item_bid_multipliers_v2_response import LineItemBidMultipliersV2Response
from criteo_api_retailmedia_v2025_01.model.line_item_bid_multipliers_v2_request import LineItemBidMultipliersV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | External LineItemId for bid multiplier retrieval
    line_item_bid_multipliers_v2_request = LineItemBidMultipliersV2Request(
        data=ResourceOfLineItemBidMultipliersV2(
            attributes=ExternalLineItemBidMultipliersV2(
                category=3.14,
                category_menu=3.14,
                checkout=3.14,
                confirmation=3.14,
                deals=3.14,
                favorites=3.14,
                home=3.14,
                id="id_example",
                merchandising=3.14,
                product_detail=3.14,
                search=3.14,
                search_bar=3.14,
            ),
            id="id_example",
            type="type_example",
        ),
    ) # LineItemBidMultipliersV2Request | New Bid Multipliers to be set (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v2_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v2_external_line_item_bid_multipliers_by_line_item_id(line_item_id, line_item_bid_multipliers_v2_request=line_item_bid_multipliers_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.set_bids_model_request import SetBidsModelRequest
from criteo_api_retailmedia_v2025_01.model.resource_outcome import ResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->set_keyword_bids: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_keyword_bids(id, set_bids_model_request=set_bids_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from criteo_api_retailmedia_v2025_01.model.product_resource_outcome import ProductResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->unpause_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.unpause_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
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

# **update_campaign_budget_overrides**
> ValueResourceOutcomeOfCampaignBudgetOverrides update_campaign_budget_overrides(campaign_id)



Update campaign budget overrides by given campaign id and new campaign budget overrides settings.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.value_resource_outcome_of_campaign_budget_overrides import ValueResourceOutcomeOfCampaignBudgetOverrides
from criteo_api_retailmedia_v2025_01.model.value_resource_input_of_campaign_budget_overrides import ValueResourceInputOfCampaignBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | Campaign id.
    value_resource_input_of_campaign_budget_overrides = ValueResourceInputOfCampaignBudgetOverrides(
        data=ValueResourceOfCampaignBudgetOverrides(
            attributes=CampaignBudgetOverrides(
                daily_budget_overrides=[
                    CampaignDailyBudgetOverride(
                        duration="duration_example",
                        max_daily_spend=3.14,
                        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        status="Expired",
                    ),
                ],
                monthly_budget_overrides=[
                    CampaignMonthlyBudgetOverride(
                        duration="duration_example",
                        max_monthly_spend=3.14,
                        start_month=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        status="Expired",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfCampaignBudgetOverrides | New campaign budget overrides settings value resource input. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_campaign_budget_overrides(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->update_campaign_budget_overrides: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_campaign_budget_overrides(campaign_id, value_resource_input_of_campaign_budget_overrides=value_resource_input_of_campaign_budget_overrides)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->update_campaign_budget_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Campaign id. |
 **value_resource_input_of_campaign_budget_overrides** | [**ValueResourceInputOfCampaignBudgetOverrides**](ValueResourceInputOfCampaignBudgetOverrides.md)| New campaign budget overrides settings value resource input. | [optional]

### Return type

[**ValueResourceOutcomeOfCampaignBudgetOverrides**](ValueResourceOutcomeOfCampaignBudgetOverrides.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_line_item_budget_overrides**
> ValueResourceOutcomeOfLineItemBudgetOverrides update_line_item_budget_overrides(line_item_id)



Update line item budget overrides by given line item id and new line item budget overrides settings.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_01
from criteo_api_retailmedia_v2025_01.api import campaign_api
from criteo_api_retailmedia_v2025_01.model.value_resource_input_of_line_item_budget_overrides import ValueResourceInputOfLineItemBudgetOverrides
from criteo_api_retailmedia_v2025_01.model.value_resource_outcome_of_line_item_budget_overrides import ValueResourceOutcomeOfLineItemBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | Line item id.
    value_resource_input_of_line_item_budget_overrides = ValueResourceInputOfLineItemBudgetOverrides(
        data=ValueResourceOfLineItemBudgetOverrides(
            attributes=LineItemBudgetOverrides(
                daily_line_item_budget_overrides=[
                    DailyLineItemBudgetOverride(
                        duration="duration_example",
                        max_daily_spend=3.14,
                        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        status="Expired",
                    ),
                ],
                monthly_line_item_budget_overrides=[
                    MonthlyLineItemBudegetOverride(
                        duration="duration_example",
                        max_monthly_spend=3.14,
                        start_month=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        status="Expired",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfLineItemBudgetOverrides | New line item budget overrides settings value resource input. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_line_item_budget_overrides(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->update_line_item_budget_overrides: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_line_item_budget_overrides(line_item_id, value_resource_input_of_line_item_budget_overrides=value_resource_input_of_line_item_budget_overrides)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_01.ApiException as e:
        print("Exception when calling CampaignApi->update_line_item_budget_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Line item id. |
 **value_resource_input_of_line_item_budget_overrides** | [**ValueResourceInputOfLineItemBudgetOverrides**](ValueResourceInputOfLineItemBudgetOverrides.md)| New line item budget overrides settings value resource input. | [optional]

### Return type

[**ValueResourceOutcomeOfLineItemBudgetOverrides**](ValueResourceOutcomeOfLineItemBudgetOverrides.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

