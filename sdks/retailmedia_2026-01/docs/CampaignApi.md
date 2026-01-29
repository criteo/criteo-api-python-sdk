# criteo_api_retailmedia_v2026_01.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_keywords**](CampaignApi.md#add_remove_keywords) | **POST** /2026-01/retail-media/line-items/{id}/keywords/add-remove | 
[**append_add_to_basket_targets_by_line_item_id**](CampaignApi.md#append_add_to_basket_targets_by_line_item_id) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append | 
[**append_audience_targets_by_line_item_id**](CampaignApi.md#append_audience_targets_by_line_item_id) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append | 
[**append_campaigns_by_balance_id**](CampaignApi.md#append_campaigns_by_balance_id) | **POST** /2026-01/retail-media/balances/{balance-id}/campaigns/append | 
[**append_promoted_products**](CampaignApi.md#append_promoted_products) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/append | 
[**append_store_targets_by_line_item_id**](CampaignApi.md#append_store_targets_by_line_item_id) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append | 
[**create_asset**](CampaignApi.md#create_asset) | **POST** /2026-01/retail-media/assets | 
[**create_auction_line_item**](CampaignApi.md#create_auction_line_item) | **POST** /2026-01/retail-media/campaigns/{campaignId}/auction-line-items | 
[**create_brand_catalog_export**](CampaignApi.md#create_brand_catalog_export) | **POST** /2026-01/retail-media/accounts/{accountId}/brand-catalog-export | 
[**create_campaigns_by_account_id**](CampaignApi.md#create_campaigns_by_account_id) | **POST** /2026-01/retail-media/accounts/{account-id}/campaigns | 
[**create_creative**](CampaignApi.md#create_creative) | **POST** /2026-01/retail-media/accounts/{account-id}/creatives | 
[**create_preferred_line_item_by_campaign_id**](CampaignApi.md#create_preferred_line_item_by_campaign_id) | **POST** /2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**create_seller_catalog_export**](CampaignApi.md#create_seller_catalog_export) | **POST** /2026-01/retail-media/accounts/{accountId}/seller-catalog-export | 
[**delete_add_to_basket_targets_by_line_item_id**](CampaignApi.md#delete_add_to_basket_targets_by_line_item_id) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete | 
[**delete_audience_targets_by_line_item_id**](CampaignApi.md#delete_audience_targets_by_line_item_id) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete | 
[**delete_campaigns_by_balance_id**](CampaignApi.md#delete_campaigns_by_balance_id) | **POST** /2026-01/retail-media/balances/{balance-id}/campaigns/delete | 
[**delete_promoted_products**](CampaignApi.md#delete_promoted_products) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/delete | 
[**delete_store_target_by_line_item_id**](CampaignApi.md#delete_store_target_by_line_item_id) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete | 
[**fetch_keywords**](CampaignApi.md#fetch_keywords) | **GET** /2026-01/retail-media/line-items/{id}/keywords | 
[**fetch_promoted_products**](CampaignApi.md#fetch_promoted_products) | **GET** /2026-01/retail-media/line-items/{line-item-id}/products | 
[**get_account_creatives**](CampaignApi.md#get_account_creatives) | **GET** /2026-01/retail-media/accounts/{account-id}/creatives | 
[**get_add_to_basket_targets_by_line_item_id**](CampaignApi.md#get_add_to_basket_targets_by_line_item_id) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | 
[**get_api202110_external_retailer_pages_by_retailer_id**](CampaignApi.md#get_api202110_external_retailer_pages_by_retailer_id) | **GET** /2026-01/retail-media/retailers/{retailerId}/pages | 
[**get_api_external_v1_categories**](CampaignApi.md#get_api_external_v1_categories) | **GET** /2026-01/retail-media/categories | 
[**get_auction_line_item**](CampaignApi.md#get_auction_line_item) | **GET** /2026-01/retail-media/auction-line-items/{lineItemId} | 
[**get_auction_line_items_by_campaign**](CampaignApi.md#get_auction_line_items_by_campaign) | **GET** /2026-01/retail-media/campaigns/{campaignId}/auction-line-items | 
[**get_audience_targets_by_line_item_id**](CampaignApi.md#get_audience_targets_by_line_item_id) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | 
[**get_bid_multipliers_by_line_item_id**](CampaignApi.md#get_bid_multipliers_by_line_item_id) | **GET** /2026-01/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**get_brands_by_account_id**](CampaignApi.md#get_brands_by_account_id) | **GET** /2026-01/retail-media/accounts/{accountId}/brands | 
[**get_campaign_budget_overrides**](CampaignApi.md#get_campaign_budget_overrides) | **GET** /2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | 
[**get_campaign_by_campaign_id**](CampaignApi.md#get_campaign_by_campaign_id) | **GET** /2026-01/retail-media/campaigns/{campaignId} | 
[**get_campaigns_by_account_id**](CampaignApi.md#get_campaigns_by_account_id) | **GET** /2026-01/retail-media/accounts/{account-id}/campaigns | 
[**get_catalog_output**](CampaignApi.md#get_catalog_output) | **GET** /2026-01/retail-media/catalogs/{catalogId}/output | 
[**get_catalog_status**](CampaignApi.md#get_catalog_status) | **GET** /2026-01/retail-media/catalogs/{catalogId}/status | 
[**get_category**](CampaignApi.md#get_category) | **GET** /2026-01/retail-media/categories/{categoryId} | 
[**get_cpc_min_bids_by_sku_ids_v1**](CampaignApi.md#get_cpc_min_bids_by_sku_ids_v1) | **POST** /2026-01/retail-media/retailers/{retailerId}/cpc-min-bids | 
[**get_creative**](CampaignApi.md#get_creative) | **GET** /2026-01/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**get_creative_template**](CampaignApi.md#get_creative_template) | **GET** /2026-01/retail-media/retailers/{retailer-id}/templates/{template-id} | 
[**get_keyword_in_review_report**](CampaignApi.md#get_keyword_in_review_report) | **GET** /2026-01/retail-media/accounts/{account-id}/keywords/in-review-report | 
[**get_line_item_budget_overrides**](CampaignApi.md#get_line_item_budget_overrides) | **GET** /2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | 
[**get_line_items_by_account_id**](CampaignApi.md#get_line_items_by_account_id) | **GET** /2026-01/retail-media/accounts/{account-id}/line-items | 
[**get_line_items_by_campaign_id**](CampaignApi.md#get_line_items_by_campaign_id) | **GET** /2026-01/retail-media/line-items/{line-item-id} | 
[**get_preferred_line_items_by_campaign_id**](CampaignApi.md#get_preferred_line_items_by_campaign_id) | **GET** /2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**get_preferred_line_items_by_line_item_id**](CampaignApi.md#get_preferred_line_items_by_line_item_id) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id} | 
[**get_recommended_categories**](CampaignApi.md#get_recommended_categories) | **POST** /2026-01/retail-media/retailers/{retailerId}/recommend-categories | 
[**get_recommended_keywords**](CampaignApi.md#get_recommended_keywords) | **GET** /2026-01/retail-media/line-items/{externalLineItemId}/keywords/recommended | 
[**get_retailer_creative_templates**](CampaignApi.md#get_retailer_creative_templates) | **GET** /2026-01/retail-media/retailers/{retailer-id}/templates | 
[**get_store_targets_by_line_item_id**](CampaignApi.md#get_store_targets_by_line_item_id) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | 
[**pause_promoted_products**](CampaignApi.md#pause_promoted_products) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/pause | 
[**post_api_external_v1_account_catalogs_sellers_by_account_id**](CampaignApi.md#post_api_external_v1_account_catalogs_sellers_by_account_id) | **POST** /2026-01/retail-media/accounts/{accountId}/catalogs/sellers | 
[**post_api_v1_external_account_catalogs_by_account_id**](CampaignApi.md#post_api_v1_external_account_catalogs_by_account_id) | **POST** /2026-01/retail-media/accounts/{accountId}/catalogs | 
[**put_add_to_basket_target_by_line_item_id**](CampaignApi.md#put_add_to_basket_target_by_line_item_id) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | 
[**put_audience_targets_by_line_item_id**](CampaignApi.md#put_audience_targets_by_line_item_id) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | 
[**put_store_target_by_line_item_id**](CampaignApi.md#put_store_target_by_line_item_id) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | 
[**recommended_keywords**](CampaignApi.md#recommended_keywords) | **POST** /2026-01/retail-media/retailers/{retailerId}/recommend-keywords | 
[**search_account_creatives**](CampaignApi.md#search_account_creatives) | **POST** /2026-01/retail-media/accounts/{account-id}/creatives/search | 
[**search_account_retailers**](CampaignApi.md#search_account_retailers) | **POST** /2026-01/retail-media/accounts/{accountId}/retailers/search | 
[**search_brands**](CampaignApi.md#search_brands) | **POST** /2026-01/retail-media/brands/search | 
[**search_category**](CampaignApi.md#search_category) | **POST** /2026-01/retail-media/retailers/{retailerId}/categories/search | 
[**set_keyword_bids**](CampaignApi.md#set_keyword_bids) | **POST** /2026-01/retail-media/line-items/{id}/keywords/set-bid | 
[**unpause_promoted_products**](CampaignApi.md#unpause_promoted_products) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/unpause | 
[**update_auction_line_item**](CampaignApi.md#update_auction_line_item) | **PUT** /2026-01/retail-media/auction-line-items/{lineItemId} | 
[**update_bid_multipliers_by_line_item_id**](CampaignApi.md#update_bid_multipliers_by_line_item_id) | **PUT** /2026-01/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**update_campaign_budget_overrides**](CampaignApi.md#update_campaign_budget_overrides) | **PUT** /2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | 
[**update_campaign_by_campaign_id**](CampaignApi.md#update_campaign_by_campaign_id) | **PUT** /2026-01/retail-media/campaigns/{campaignId} | 
[**update_creative**](CampaignApi.md#update_creative) | **PUT** /2026-01/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**update_keyword_reviews**](CampaignApi.md#update_keyword_reviews) | **POST** /2026-01/retail-media/line-items/{line-item-id}/keywords/review | 
[**update_line_item_budget_overrides**](CampaignApi.md#update_line_item_budget_overrides) | **PUT** /2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | 
[**update_preferred_line_item_by_line_item_id**](CampaignApi.md#update_preferred_line_item_by_line_item_id) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id} | 


# **add_remove_keywords**
> ResourceOutcome add_remove_keywords(id)



Add or Remove keywords from the line item in bulk

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.add_remove_keywords_model_request import AddRemoveKeywordsModelRequest
from criteo_api_retailmedia_v2026_01.model.resource_outcome import ResourceOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->add_remove_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_remove_keywords(id, add_remove_keywords_model_request=add_remove_keywords_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_add_to_basket_targets_by_line_item_id**
> AddToBasketTarget202110Response append_add_to_basket_targets_by_line_item_id(line_item_id)



This endpoint appends one or more add to basket ids to targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.add_to_basket_ids_update_model202110_request import AddToBasketIdsUpdateModel202110Request
from criteo_api_retailmedia_v2026_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    add_to_basket_ids_update_model202110_request = AddToBasketIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAddToBasketIdsUpdateModel202110(
            attributes=AddToBasketIdsUpdateModel202110(
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
        api_response = api_instance.append_add_to_basket_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_add_to_basket_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_add_to_basket_targets_by_line_item_id(line_item_id, add_to_basket_ids_update_model202110_request=add_to_basket_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_add_to_basket_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_audience_targets_by_line_item_id**
> AudienceTarget202110Response append_audience_targets_by_line_item_id(line_item_id)



This endpoint appends one or more audiences ids to targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.audience_ids_update_model202110_request import AudienceIdsUpdateModel202110Request
from criteo_api_retailmedia_v2026_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    audience_ids_update_model202110_request = AudienceIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAudienceIdsUpdateModel202110(
            attributes=AudienceIdsUpdateModel202110(
                audience_ids=[
                    "audience_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AudienceIdsUpdateModel202110Request | Audience ids to append to the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.append_audience_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_audience_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_audience_targets_by_line_item_id(line_item_id, audience_ids_update_model202110_request=audience_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_audience_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_campaigns_by_balance_id**
> BalanceCampaign202110PagedListResponse append_campaigns_by_balance_id(balance_id)



appends one or more campaigns to the specified balance

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.balance_campaign202110_list_request import BalanceCampaign202110ListRequest
from criteo_api_retailmedia_v2026_01.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
        api_response = api_instance.append_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_campaigns_by_balance_id(balance_id, balance_campaign202110_list_request=balance_campaign202110_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_campaigns_by_balance_id: %s\n" % e)
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

# **append_promoted_products**
> ProductResourceOutcome append_promoted_products(line_item_id)



Append a collection of promoted products to a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.product_resource_outcome import ProductResourceOutcome
from criteo_api_retailmedia_v2026_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_store_targets_by_line_item_id**
> StoreTarget202110Response append_store_targets_by_line_item_id(line_item_id)



This endpoint appends one or more store ids to targeting on the specified line item.  The resulting state of the store target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.store_ids_update_model202110_request import StoreIdsUpdateModel202110Request
from criteo_api_retailmedia_v2026_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    store_ids_update_model202110_request = StoreIdsUpdateModel202110Request(
        data=ValueTypeResourceOfStoreIdsUpdateModel202110(
            attributes=StoreIdsUpdateModel202110(
                store_ids=[
                    "store_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # StoreIdsUpdateModel202110Request | Store ids to append to the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.append_store_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_store_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_store_targets_by_line_item_id(line_item_id, store_ids_update_model202110_request=store_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->append_store_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset**
> AssetResponse create_asset(asset_file)



Creates an asset

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.asset_response import AssetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    asset_file = open('/path/to/file', 'rb') # file_type | The asset binary content

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_asset(asset_file)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem create_auction_line_item(campaign_id, value_resource_input_of_sponsored_products_line_item_create_request_model)



Creates new auction line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_sponsored_products_line_item_create_request_model import ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    value_resource_input_of_sponsored_products_line_item_create_request_model = ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel(
        data=ValueResourceOfSponsoredProductsLineItemCreateRequestModel(
            attributes=SponsoredProductsLineItemCreateRequestModel(
                bid_strategy="manual",
                budget=3.14,
                daily_pacing=3.14,
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flight_schedule=FlightSchedule(
                    legs=[
                        FlightLeg(
                            day_of_week="sunday",
                            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                    ],
                ),
                is_auto_daily_pacing=False,
                keyword_strategy="conquesting",
                max_bid=3.14,
                monthly_pacing=3.14,
                name="name_example",
                optimization_strategy="conversion",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                target_bid=3.14,
                target_retailer_id="target_retailer_id_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel | The line item settings to create a line item with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_auction_line_item(campaign_id, value_resource_input_of_sponsored_products_line_item_create_request_model)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->create_auction_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **value_resource_input_of_sponsored_products_line_item_create_request_model** | [**ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel**](ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel.md)| The line item settings to create a line item with |

### Return type

[**EntityResourceOutcomeOfSponsoredProductsLineItem**](EntityResourceOutcomeOfSponsoredProductsLineItem.md)

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

# **create_brand_catalog_export**
> EntityResourceOutcomeOfCatalogStatusV2 create_brand_catalog_export(account_id, value_resource_input_of_brand_catalog_request_v2)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_outcome_of_catalog_status_v2 import EntityResourceOutcomeOfCatalogStatusV2
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_brand_catalog_request_v2 import ValueResourceInputOfBrandCatalogRequestV2
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    ) # ValueResourceInputOfBrandCatalogRequestV2 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_brand_catalog_export(account_id, value_resource_input_of_brand_catalog_request_v2)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->create_brand_catalog_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **value_resource_input_of_brand_catalog_request_v2** | [**ValueResourceInputOfBrandCatalogRequestV2**](ValueResourceInputOfBrandCatalogRequestV2.md)|  |

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

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

# **create_campaigns_by_account_id**
> JsonApiSingleResponseOfCampaignV202301 create_campaigns_by_account_id(account_id, post_campaign_v202301)



Creates a new campaign with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from criteo_api_retailmedia_v2026_01.model.post_campaign_v202301 import PostCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The given account id
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
    ) # PostCampaignV202301 | The campaign settings to create a campaign with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_campaigns_by_account_id(account_id, post_campaign_v202301)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->create_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **post_campaign_v202301** | [**PostCampaignV202301**](PostCampaignV202301.md)| The campaign settings to create a campaign with |

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

# **create_creative**
> Creative202210Response create_creative(account_id, creative_create_model202207)



Create a creative for an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_v2026_01.model.creative_create_model202207 import CreativeCreateModel202207
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to create a creative for
    creative_create_model202207 = CreativeCreateModel202207(
        brand_id=1,
        id="id_example",
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
    ) # CreativeCreateModel202207 | The creative to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_creative(account_id, creative_create_model202207)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->create_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to create a creative for |
 **creative_create_model202207** | [**CreativeCreateModel202207**](CreativeCreateModel202207.md)| The creative to create |

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creatives created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_preferred_line_item_by_campaign_id**
> PreferredLineItemV2Response create_preferred_line_item_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)



Creates a new preferred line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from criteo_api_retailmedia_v2026_01.model.preferred_line_item_create_model_v2_request import PreferredLineItemCreateModelV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | The given campaign id
    preferred_line_item_create_model_v2_request = PreferredLineItemCreateModelV2Request(
        data=InputResourceOfPreferredLineItemCreateModelV2(
            attributes=PreferredLineItemCreateModelV2(
                budget=3.14,
                capping=LineItemCappingV2(
                    count=1,
                    type="unknown",
                ),
                creative_id="creative_id_example",
                end_date=dateutil_parser('1970-01-01').date(),
                name="name_example",
                pacing="unknown",
                page=LineItemPageV2(
                    categories=[
                        LineItemPageCategoryV2(
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
        api_response = api_instance.create_preferred_line_item_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->create_preferred_line_item_by_campaign_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_seller_catalog_export**
> EntityResourceOutcomeOfCatalogStatusV2 create_seller_catalog_export(account_id, value_resource_input_of_seller_catalog_request_v2)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_outcome_of_catalog_status_v2 import EntityResourceOutcomeOfCatalogStatusV2
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_seller_catalog_request_v2 import ValueResourceInputOfSellerCatalogRequestV2
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    ) # ValueResourceInputOfSellerCatalogRequestV2 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_seller_catalog_export(account_id, value_resource_input_of_seller_catalog_request_v2)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->create_seller_catalog_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **value_resource_input_of_seller_catalog_request_v2** | [**ValueResourceInputOfSellerCatalogRequestV2**](ValueResourceInputOfSellerCatalogRequestV2.md)|  |

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

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

# **delete_add_to_basket_targets_by_line_item_id**
> AddToBasketTarget202110Response delete_add_to_basket_targets_by_line_item_id(line_item_id)



This endpoint removes one or more add to basket ids from targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.add_to_basket_ids_update_model202110_request import AddToBasketIdsUpdateModel202110Request
from criteo_api_retailmedia_v2026_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    add_to_basket_ids_update_model202110_request = AddToBasketIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAddToBasketIdsUpdateModel202110(
            attributes=AddToBasketIdsUpdateModel202110(
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
        api_response = api_instance.delete_add_to_basket_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_add_to_basket_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_add_to_basket_targets_by_line_item_id(line_item_id, add_to_basket_ids_update_model202110_request=add_to_basket_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_add_to_basket_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audience_targets_by_line_item_id**
> AudienceTarget202110Response delete_audience_targets_by_line_item_id(line_item_id)



This endpoint removes one or more audiences ids from targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.audience_ids_update_model202110_request import AudienceIdsUpdateModel202110Request
from criteo_api_retailmedia_v2026_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    audience_ids_update_model202110_request = AudienceIdsUpdateModel202110Request(
        data=ValueTypeResourceOfAudienceIdsUpdateModel202110(
            attributes=AudienceIdsUpdateModel202110(
                audience_ids=[
                    "audience_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AudienceIdsUpdateModel202110Request | Audience ids to remove from the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_audience_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_audience_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_audience_targets_by_line_item_id(line_item_id, audience_ids_update_model202110_request=audience_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_audience_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaigns_by_balance_id**
> BalanceCampaign202110PagedListResponse delete_campaigns_by_balance_id(balance_id)



Removes one or more campaigns on the specified balance

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.balance_campaign202110_list_request import BalanceCampaign202110ListRequest
from criteo_api_retailmedia_v2026_01.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
        api_response = api_instance.delete_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_campaigns_by_balance_id(balance_id, balance_campaign202110_list_request=balance_campaign202110_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_campaigns_by_balance_id: %s\n" % e)
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

# **delete_promoted_products**
> delete_promoted_products(line_item_id)



Remove a collection of promoted products from a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products removed from the line item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store_target_by_line_item_id**
> StoreTarget202110Response delete_store_target_by_line_item_id(line_item_id)



This endpoint removes one or more store ids from targeting on the specified line item.  The resulting state of the store target is returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.store_ids_update_model202110_request import StoreIdsUpdateModel202110Request
from criteo_api_retailmedia_v2026_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    store_ids_update_model202110_request = StoreIdsUpdateModel202110Request(
        data=ValueTypeResourceOfStoreIdsUpdateModel202110(
            attributes=StoreIdsUpdateModel202110(
                store_ids=[
                    "store_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # StoreIdsUpdateModel202110Request | Store ids to remove from the target (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_store_target_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_store_target_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_store_target_by_line_item_id(line_item_id, store_ids_update_model202110_request=store_ids_update_model202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->delete_store_target_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_keywords**
> KeywordsModelResponse fetch_keywords(id)



Fetch keywords associated with the specified line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.keywords_model_response import KeywordsModelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | ID of the line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_keywords(id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_promoted_products**
> PromotedProductResourceCollectionOutcome fetch_promoted_products(line_item_id)



Retrieve a page of promoted products for a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.promoted_product_resource_collection_outcome import PromotedProductResourceCollectionOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->fetch_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_promoted_products(line_item_id, fields=fields, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_creatives**
> Creative202110ListResponse get_account_creatives(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.creative202110_list_response import Creative202110ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_account_creatives(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_account_creatives: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_add_to_basket_targets_by_line_item_id**
> AddToBasketTarget202110Response get_add_to_basket_targets_by_line_item_id(line_item_id)



This endpoint gets the add to basket target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_add_to_basket_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_add_to_basket_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202110_external_retailer_pages_by_retailer_id**
> RetailerPages202110 get_api202110_external_retailer_pages_by_retailer_id(retailer_id)



Get the page types available for the given retailer

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.retailer_pages202110 import RetailerPages202110
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | The retailers to fetch pages for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_retailer_pages_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api202110_external_retailer_pages_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailers to fetch pages for |

### Return type

[**RetailerPages202110**](RetailerPages202110.md)

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

# **get_api_external_v1_categories**
> Category202204ListResponse get_api_external_v1_categories()



Endpoint to search categories by text and retailer.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.category202204_list_response import Category202204ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    retailer_id = 1 # int | The retailer id for which Categories fetched (optional)
    text_substring = "textSubstring_example" # str | Query string to search across Categories (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_external_v1_categories(page_index=page_index, page_size=page_size, retailer_id=retailer_id, text_substring=text_substring)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_categories: %s\n" % e)
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

# **get_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem get_auction_line_item(line_item_id)



Gets a sponsored product line item by its id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = 1 # int | The id of the line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_auction_line_item(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_auction_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **int**| The id of the line item |

### Return type

[**EntityResourceOutcomeOfSponsoredProductsLineItem**](EntityResourceOutcomeOfSponsoredProductsLineItem.md)

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

# **get_auction_line_items_by_campaign**
> EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata get_auction_line_items_by_campaign(campaign_id)



Gets a page of sponsored product line items by campaign id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_collection_outcome_of_sponsored_products_line_item_and_metadata import EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The id of the campaign
    limit = 25 # int | The number of elements to be returned on a page. (optional) if omitted the server will use the default value of 25
    limit_to_ids = [
        "limitToIds_example",
    ] # [str] | The ids to limit the auction line item results to (optional)
    offset = 0 # int | The (zero-based) starting offset into the collection. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_auction_line_items_by_campaign(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_auction_line_items_by_campaign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_auction_line_items_by_campaign(campaign_id, limit=limit, limit_to_ids=limit_to_ids, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_auction_line_items_by_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The id of the campaign |
 **limit** | **int**| The number of elements to be returned on a page. | [optional] if omitted the server will use the default value of 25
 **limit_to_ids** | **[str]**| The ids to limit the auction line item results to | [optional]
 **offset** | **int**| The (zero-based) starting offset into the collection. | [optional] if omitted the server will use the default value of 0

### Return type

[**EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata**](EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata.md)

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

# **get_audience_targets_by_line_item_id**
> AudienceTarget202110Response get_audience_targets_by_line_item_id(line_item_id)



This endpoint gets the audience target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audience_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_audience_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bid_multipliers_by_line_item_id**
> JsonApiSingleResponseOfLineItemBidMultipliersV2 get_bid_multipliers_by_line_item_id(line_item_id)



Fetch all bid multipliers for a given line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_line_item_bid_multipliers_v2 import JsonApiSingleResponseOfLineItemBidMultipliersV2
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | LineItemId for bid multiplier retrieval

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_bid_multipliers_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for bid multiplier retrieval |

### Return type

[**JsonApiSingleResponseOfLineItemBidMultipliersV2**](JsonApiSingleResponseOfLineItemBidMultipliersV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BidMultipliers Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brands_by_account_id**
> JsonApiPageResponseOfBrand get_brands_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
        api_response = api_instance.get_brands_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_brands_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_brands_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_brands_by_account_id: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_budget_overrides**
> ValueResourceOutcomeOfCampaignBudgetOverrides get_campaign_budget_overrides(campaign_id)



Get current campaign budget overrides by given campaign id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_of_campaign_budget_overrides import ValueResourceOutcomeOfCampaignBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | Campaign id.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign_budget_overrides(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

# **get_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaignV202301 get_campaign_by_campaign_id(campaign_id)



Gets the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |

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

# **get_campaigns_by_account_id**
> JsonApiPageResponseOfCampaignV202301 get_campaigns_by_account_id(account_id)



Gets page of campaign objects for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_page_response_of_campaign_v202301 import JsonApiPageResponseOfCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_campaigns_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
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

# **get_catalog_output**
> file_type get_catalog_output(catalog_id)



Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream CatalogProduct json objects (first introduced in the 2021-07 version).

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_catalog_output(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_catalog_output: %s\n" % e)
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
 - **Accept**: application/x-json-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog download initiated. |  -  |
**204** | Catalog has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_status**
> JsonApiSingleResponseOfCatalogStatus get_catalog_status(catalog_id)



Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_catalog_status(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_catalog_status: %s\n" % e)
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

# **get_category**
> Category202204 get_category(category_id)



Endpoint to search for a specific category by categoryId.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.category202204 import Category202204
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    category_id = 1 # int | ID of the desired category

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_category(category_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_category: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cpc_min_bids_by_sku_ids_v1**
> ValueResourceOutcomeCpcMinBidsResponse get_cpc_min_bids_by_sku_ids_v1(retailer_id, value_resource_input_cpc_min_bids_request)



Get overall and individual minimum bid amount for given retailer id and sku id list.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_input_cpc_min_bids_request import ValueResourceInputCpcMinBidsRequest
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_cpc_min_bids_response import ValueResourceOutcomeCpcMinBidsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    ) # ValueResourceInputCpcMinBidsRequest | Cpc minimum bid amount request object.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cpc_min_bids_by_sku_ids_v1(retailer_id, value_resource_input_cpc_min_bids_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_cpc_min_bids_by_sku_ids_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| Retailer Id. |
 **value_resource_input_cpc_min_bids_request** | [**ValueResourceInputCpcMinBidsRequest**](ValueResourceInputCpcMinBidsRequest.md)| Cpc minimum bid amount request object. |

### Return type

[**ValueResourceOutcomeCpcMinBidsResponse**](ValueResourceOutcomeCpcMinBidsResponse.md)

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

# **get_creative**
> Creative2Response get_creative(account_id, creative_id)



Get the specified creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.creative2_response import Creative2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_id = "creative-id_example" # str | Creative to get

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_creative(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_creative: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creative_template**
> TemplateResponse get_creative_template(retailer_id, template_id)



Gets the template for the specified retailer id and template id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.template_response import TemplateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | Retailer Id
    template_id = 1 # int | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_creative_template(retailer_id, template_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_creative_template: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template found for the retailer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keyword_in_review_report**
> EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata get_keyword_in_review_report(account_id)



Generate a list of reports for line items which contain one or more actionable keyword reviews

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_collection_outcome_line_item_keyword_review_report_and_metadata import EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = 1 # int | The account to generate a report for
    limit = 25 # int | Number of items per page (optional) if omitted the server will use the default value of 25
    offset = 0 # int | Offset for pagination (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_keyword_in_review_report(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_keyword_in_review_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_keyword_in_review_report(account_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_keyword_in_review_report: %s\n" % e)
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
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_of_line_item_budget_overrides import ValueResourceOutcomeOfLineItemBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item id to get budget overrides for.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_line_item_budget_overrides(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

# **get_line_items_by_account_id**
> CommonLineItemPagedListResponse get_line_items_by_account_id(account_id)



Gets page of line item objects for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.common_line_item_paged_list_response import CommonLineItemPagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_line_items_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_line_items_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_line_items_by_account_id(account_id, limit_to_campaign_id=limit_to_campaign_id, limit_to_id=limit_to_id, limit_to_type=limit_to_type, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_line_items_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_campaign_id** | **[str]**| The campaign ids that you would like to limit your result set to | [optional]
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **limit_to_type** | **str, none_type**| The campaign types that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

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

# **get_line_items_by_campaign_id**
> CommonLineItemResponse get_line_items_by_campaign_id(line_item_id)



Gets the line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.common_line_item_response import CommonLineItemResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_line_items_by_campaign_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_line_items_by_campaign_id: %s\n" % e)
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

# **get_preferred_line_items_by_campaign_id**
> PreferredLineItemV2PagedListResponse get_preferred_line_items_by_campaign_id(campaign_id)



Gets page of preferred line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.preferred_line_item_v2_paged_list_response import PreferredLineItemV2PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | The given campaign id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_preferred_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_preferred_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_preferred_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_preferred_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preferred_line_items_by_line_item_id**
> PreferredLineItemV2Response get_preferred_line_items_by_line_item_id(line_item_id)



Gets the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_preferred_line_items_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_preferred_line_items_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_categories**
> EntityResourceCollectionOutcomeCategory202204 get_recommended_categories(retailer_id, value_resource_input_recommended_categories_request_v1)



Endpoint to get recommended categories by given retailer id and sku id list.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_input_recommended_categories_request_v1 import ValueResourceInputRecommendedCategoriesRequestV1
from criteo_api_retailmedia_v2026_01.model.entity_resource_collection_outcome_category202204 import EntityResourceCollectionOutcomeCategory202204
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | Retailer id.
    value_resource_input_recommended_categories_request_v1 = ValueResourceInputRecommendedCategoriesRequestV1(
        data=ValueResourceRecommendedCategoriesRequestV1(
            attributes=RecommendedCategoriesRequestV1(
                product_ids=[
                    "product_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputRecommendedCategoriesRequestV1 | Request of recommended categories.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_recommended_categories(retailer_id, value_resource_input_recommended_categories_request_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_recommended_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| Retailer id. |
 **value_resource_input_recommended_categories_request_v1** | [**ValueResourceInputRecommendedCategoriesRequestV1**](ValueResourceInputRecommendedCategoriesRequestV1.md)| Request of recommended categories. |

### Return type

[**EntityResourceCollectionOutcomeCategory202204**](EntityResourceCollectionOutcomeCategory202204.md)

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

# **get_recommended_keywords**
> ValueResourceOutcomeOfRecommendedKeywordsResult get_recommended_keywords(external_line_item_id)



Retrieves a collection of recommended keywords for a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_of_recommended_keywords_result import ValueResourceOutcomeOfRecommendedKeywordsResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    external_line_item_id = "externalLineItemId_example" # str | The line item identifier

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_recommended_keywords(external_line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

# **get_retailer_creative_templates**
> TemplateListResponse get_retailer_creative_templates(retailer_id)



Get retailer creative templates

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.template_list_response import TemplateListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | External retailer id to retrieve creative templates for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_retailer_creative_templates(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_retailer_creative_templates: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Templates found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_targets_by_line_item_id**
> StoreTarget202110Response get_store_targets_by_line_item_id(line_item_id)



This endpoint gets the store target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.store_target202110_response import StoreTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_store_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->get_store_targets_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_promoted_products**
> pause_promoted_products(line_item_id)



Pause a collection of promoted products associated with a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->pause_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.pause_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products paused |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_external_v1_account_catalogs_sellers_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_external_v1_account_catalogs_sellers_by_account_id(account_id, json_api_request_of_seller_catalog_request)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_request_of_seller_catalog_request import JsonApiRequestOfSellerCatalogRequest
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    ) # JsonApiRequestOfSellerCatalogRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_external_v1_account_catalogs_sellers_by_account_id(account_id, json_api_request_of_seller_catalog_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v1_account_catalogs_sellers_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **json_api_request_of_seller_catalog_request** | [**JsonApiRequestOfSellerCatalogRequest**](JsonApiRequestOfSellerCatalogRequest.md)|  |

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

# **post_api_v1_external_account_catalogs_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v1_external_account_catalogs_by_account_id(account_id, json_api_request_of_catalog_request)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.json_api_request_of_catalog_request import JsonApiRequestOfCatalogRequest
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    ) # JsonApiRequestOfCatalogRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_catalogs_by_account_id(account_id, json_api_request_of_catalog_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_catalogs_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **json_api_request_of_catalog_request** | [**JsonApiRequestOfCatalogRequest**](JsonApiRequestOfCatalogRequest.md)|  |

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

# **put_add_to_basket_target_by_line_item_id**
> AddToBasketTarget202110Response put_add_to_basket_target_by_line_item_id(line_item_id, add_to_basket_target202110_request)



This endpoint sets the scope of the add to basket target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.add_to_basket_target202110_request import AddToBasketTarget202110Request
from criteo_api_retailmedia_v2026_01.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    add_to_basket_target202110_request = AddToBasketTarget202110Request(
        data=ValueTypeResourceOfAddToBasketTarget202110(
            attributes=AddToBasketTarget202110(
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
    ) # AddToBasketTarget202110Request | The add to basket target to set the scope for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_add_to_basket_target_by_line_item_id(line_item_id, add_to_basket_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->put_add_to_basket_target_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **add_to_basket_target202110_request** | [**AddToBasketTarget202110Request**](AddToBasketTarget202110Request.md)| The add to basket target to set the scope for |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_audience_targets_by_line_item_id**
> AudienceTarget202110Response put_audience_targets_by_line_item_id(line_item_id, audience_target202110_request)



This endpoint sets the scope of the audience target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.audience_target202110_request import AudienceTarget202110Request
from criteo_api_retailmedia_v2026_01.model.audience_target202110_response import AudienceTarget202110Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    audience_target202110_request = AudienceTarget202110Request(
        data=ValueTypeResourceOfAudienceTarget202110(
            attributes=AudienceTarget202110(
                audience_ids=[
                    "audience_ids_example",
                ],
                scope="unknown",
            ),
            type="type_example",
        ),
    ) # AudienceTarget202110Request | The audience target to set the scope for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_audience_targets_by_line_item_id(line_item_id, audience_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->put_audience_targets_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **audience_target202110_request** | [**AudienceTarget202110Request**](AudienceTarget202110Request.md)| The audience target to set the scope for |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_store_target_by_line_item_id**
> StoreTarget202110Response put_store_target_by_line_item_id(line_item_id, store_target202110_request)



This endpoint sets the scope of the store target on the specified line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.store_target202110_response import StoreTarget202110Response
from criteo_api_retailmedia_v2026_01.model.store_target202110_request import StoreTarget202110Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item to interact with
    store_target202110_request = StoreTarget202110Request(
        data=ValueTypeResourceOfStoreTarget202110(
            attributes=StoreTarget202110(
                scope="unknown",
                store_ids=[
                    "store_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # StoreTarget202110Request | The store target to set the scope for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_store_target_by_line_item_id(line_item_id, store_target202110_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->put_store_target_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **store_target202110_request** | [**StoreTarget202110Request**](StoreTarget202110Request.md)| The store target to set the scope for |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommended_keywords**
> ValueResourceOutcomeRecommendedKeywordsResponseV1 recommended_keywords(retailer_id, value_resource_input_recommended_keywords_request_v1)



Recommend keywords by given retailer id and sku ids.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_recommended_keywords_response_v1 import ValueResourceOutcomeRecommendedKeywordsResponseV1
from criteo_api_retailmedia_v2026_01.model.value_resource_input_recommended_keywords_request_v1 import ValueResourceInputRecommendedKeywordsRequestV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailerId_example" # str | Retailer id.
    value_resource_input_recommended_keywords_request_v1 = ValueResourceInputRecommendedKeywordsRequestV1(
        data=ValueResourceRecommendedKeywordsRequestV1(
            attributes=RecommendedKeywordsRequestV1(
                product_ids=[
                    "product_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputRecommendedKeywordsRequestV1 | Request of recommended keywords.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.recommended_keywords(retailer_id, value_resource_input_recommended_keywords_request_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->recommended_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| Retailer id. |
 **value_resource_input_recommended_keywords_request_v1** | [**ValueResourceInputRecommendedKeywordsRequestV1**](ValueResourceInputRecommendedKeywordsRequestV1.md)| Request of recommended keywords. |

### Return type

[**ValueResourceOutcomeRecommendedKeywordsResponseV1**](ValueResourceOutcomeRecommendedKeywordsResponseV1.md)

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

# **search_account_creatives**
> Creative2ListResponse search_account_creatives(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.creative2_list_response import Creative2ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_ids = [
        "creative-ids_example",
    ] # [str] | Creatives to filter by (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_account_creatives(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_account_creatives: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_account_creatives(account_id, creative_ids=creative_ids)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_account_creatives: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_account_retailers**
> EntityResourceCollectionOutcomeOfRetailerResultAndMetadata search_account_retailers(account_id, value_resource_input_of_retailer_search_request)



Searches for retailers associated with the specified account based on provided search criteria

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_retailer_search_request import ValueResourceInputOfRetailerSearchRequest
from criteo_api_retailmedia_v2026_01.model.entity_resource_collection_outcome_of_retailer_result_and_metadata import EntityResourceCollectionOutcomeOfRetailerResultAndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The external account identifier
    value_resource_input_of_retailer_search_request = ValueResourceInputOfRetailerSearchRequest(
        data=ValueResourceOfRetailerSearchRequest(
            attributes=RetailerSearchRequest(
                retailer_id_filter=[
                    "retailer_id_filter_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailerSearchRequest | The search request containing filtering parameters
    limit = 5 # int | The maximum number of items to return. Must be between 1 and 10. Default is 5. (optional) if omitted the server will use the default value of 5
    offset = 0 # int | The number of items to skip before starting to collect the result set. Default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_account_retailers(account_id, value_resource_input_of_retailer_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_account_retailers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_account_retailers(account_id, value_resource_input_of_retailer_search_request, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_account_retailers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account identifier |
 **value_resource_input_of_retailer_search_request** | [**ValueResourceInputOfRetailerSearchRequest**](ValueResourceInputOfRetailerSearchRequest.md)| The search request containing filtering parameters |
 **limit** | **int**| The maximum number of items to return. Must be between 1 and 10. Default is 5. | [optional] if omitted the server will use the default value of 5
 **offset** | **int**| The number of items to skip before starting to collect the result set. Default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**EntityResourceCollectionOutcomeOfRetailerResultAndMetadata**](EntityResourceCollectionOutcomeOfRetailerResultAndMetadata.md)

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

# **search_brands**
> EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata search_brands()



Search for brands given a retailer ID and search term.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_collection_outcome_brand_id_search_result_paging_offset_limit_metadata import EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata
from criteo_api_retailmedia_v2026_01.model.value_resource_input_brand_id_search_request import ValueResourceInputBrandIdSearchRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
        api_response = api_instance.search_brands(limit=limit, offset=offset, value_resource_input_brand_id_search_request=value_resource_input_brand_id_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_brands: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_category**
> EntityResourceCollectionOutcomeCategory202204Metadata search_category(retailer_id)



Search a retailer categories by given text substring and category ids.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_collection_outcome_category202204_metadata import EntityResourceCollectionOutcomeCategory202204Metadata
from criteo_api_retailmedia_v2026_01.model.value_resource_input_categories_search_request_v1 import ValueResourceInputCategoriesSearchRequestV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | Retailer id.
    limit = 50 # int | Limit of the search result. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | Offset of the search result. (optional) if omitted the server will use the default value of 0
    value_resource_input_categories_search_request_v1 = ValueResourceInputCategoriesSearchRequestV1(
        data=ValueResourceCategoriesSearchRequestV1(
            attributes=CategoriesSearchRequestV1(
                category_ids=[
                    "category_ids_example",
                ],
                text_substring="text_substring_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputCategoriesSearchRequestV1 | Request of categories search. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_category(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_category(retailer_id, limit=limit, offset=offset, value_resource_input_categories_search_request_v1=value_resource_input_categories_search_request_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->search_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| Retailer id. |
 **limit** | **int**| Limit of the search result. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| Offset of the search result. | [optional] if omitted the server will use the default value of 0
 **value_resource_input_categories_search_request_v1** | [**ValueResourceInputCategoriesSearchRequestV1**](ValueResourceInputCategoriesSearchRequestV1.md)| Request of categories search. | [optional]

### Return type

[**EntityResourceCollectionOutcomeCategory202204Metadata**](EntityResourceCollectionOutcomeCategory202204Metadata.md)

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

# **set_keyword_bids**
> ResourceOutcome set_keyword_bids(id)



Set bid overrides for associated keywords to the given line item in bulk

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.resource_outcome import ResourceOutcome
from criteo_api_retailmedia_v2026_01.model.set_bids_model_request import SetBidsModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->set_keyword_bids: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_keyword_bids(id, set_bids_model_request=set_bids_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpause_promoted_products**
> unpause_promoted_products(line_item_id)



Un-pause a collection of promoted products associated with a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.promoted_product_resource_collection_input import PromotedProductResourceCollectionInput
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->unpause_promoted_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.unpause_promoted_products(line_item_id, promoted_product_resource_collection_input=promoted_product_resource_collection_input)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
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
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products un-paused |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem update_auction_line_item(line_item_id, value_resource_input_of_sponsored_products_line_item_update_request_model)



Updates a Sponsored Products Line Item given a line item id and a request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_sponsored_products_line_item_update_request_model import ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = 1 # int | The external line item ID of the sponsored products line item.
    value_resource_input_of_sponsored_products_line_item_update_request_model = ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel(
        data=ValueResourceOfSponsoredProductsLineItemUpdateRequestModel(
            attributes=SponsoredProductsLineItemUpdateRequestModel(
                bid_strategy="manual",
                budget=3.14,
                daily_pacing=3.14,
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flight_schedule=FlightSchedule(
                    legs=[
                        FlightLeg(
                            day_of_week="sunday",
                            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                    ],
                ),
                is_auto_daily_pacing=True,
                max_bid=3.14,
                monthly_pacing=3.14,
                name="name_example",
                optimization_strategy="conversion",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="active",
                target_bid=3.14,
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel | An update request containing all details of the requested update.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_auction_line_item(line_item_id, value_resource_input_of_sponsored_products_line_item_update_request_model)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_auction_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **int**| The external line item ID of the sponsored products line item. |
 **value_resource_input_of_sponsored_products_line_item_update_request_model** | [**ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel**](ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel.md)| An update request containing all details of the requested update. |

### Return type

[**EntityResourceOutcomeOfSponsoredProductsLineItem**](EntityResourceOutcomeOfSponsoredProductsLineItem.md)

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

# **update_bid_multipliers_by_line_item_id**
> LineItemBidMultipliersV2Response update_bid_multipliers_by_line_item_id(line_item_id, line_item_bid_multipliers_v2_request)



Updates the bid multipliers for a given line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.line_item_bid_multipliers_v2_response import LineItemBidMultipliersV2Response
from criteo_api_retailmedia_v2026_01.model.line_item_bid_multipliers_v2_request import LineItemBidMultipliersV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | LineItemId for bid multiplier retrieval
    line_item_bid_multipliers_v2_request = LineItemBidMultipliersV2Request(
        data=ResourceOfLineItemBidMultipliersV2(
            attributes=LineItemBidMultipliersV2(
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
    ) # LineItemBidMultipliersV2Request | New Bid Multipliers to be set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_bid_multipliers_by_line_item_id(line_item_id, line_item_bid_multipliers_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_bid_multipliers_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for bid multiplier retrieval |
 **line_item_bid_multipliers_v2_request** | [**LineItemBidMultipliersV2Request**](LineItemBidMultipliersV2Request.md)| New Bid Multipliers to be set |

### Return type

[**LineItemBidMultipliersV2Response**](LineItemBidMultipliersV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BidMultipliers Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_budget_overrides**
> ValueResourceOutcomeOfCampaignBudgetOverrides update_campaign_budget_overrides(campaign_id, value_resource_input_of_campaign_budget_overrides)



Update campaign budget overrides by given campaign id and new campaign budget overrides settings.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_campaign_budget_overrides import ValueResourceInputOfCampaignBudgetOverrides
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_of_campaign_budget_overrides import ValueResourceOutcomeOfCampaignBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
    ) # ValueResourceInputOfCampaignBudgetOverrides | New campaign budget overrides settings value resource input.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_campaign_budget_overrides(campaign_id, value_resource_input_of_campaign_budget_overrides)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_campaign_budget_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Campaign id. |
 **value_resource_input_of_campaign_budget_overrides** | [**ValueResourceInputOfCampaignBudgetOverrides**](ValueResourceInputOfCampaignBudgetOverrides.md)| New campaign budget overrides settings value resource input. |

### Return type

[**ValueResourceOutcomeOfCampaignBudgetOverrides**](ValueResourceOutcomeOfCampaignBudgetOverrides.md)

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

# **update_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaignV202301 update_campaign_by_campaign_id(campaign_id, put_campaign_v202301)



Updates the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.put_campaign_v202301 import PutCampaignV202301
from criteo_api_retailmedia_v2026_01.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
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
    ) # PutCampaignV202301 | The campaign settings to update that campaign with

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_campaign_by_campaign_id(campaign_id, put_campaign_v202301)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **put_campaign_v202301** | [**PutCampaignV202301**](PutCampaignV202301.md)| The campaign settings to update that campaign with |

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

# **update_creative**
> Creative202210Response update_creative(account_id, creative_id, creative_update_model202207)



Update a creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.creative_update_model202207 import CreativeUpdateModel202207
from criteo_api_retailmedia_v2026_01.model.creative202210_response import Creative202210Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id containing the creative
    creative_id = "creative-id_example" # str | Creative to update
    creative_update_model202207 = CreativeUpdateModel202207(
        brand_id=1,
        id="id_example",
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
    ) # CreativeUpdateModel202207 | The creative to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_creative(account_id, creative_id, creative_update_model202207)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id containing the creative |
 **creative_id** | **str**| Creative to update |
 **creative_update_model202207** | [**CreativeUpdateModel202207**](CreativeUpdateModel202207.md)| The creative to create |

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creative updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_keyword_reviews**
> ValueResourceOutcomeRetailMediaKeywordsReviewResult update_keyword_reviews(line_item_id)



Update the status of keyword reviews under a line item

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_input_retail_media_keywords_review import ValueResourceInputRetailMediaKeywordsReview
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_retail_media_keywords_review_result import ValueResourceOutcomeRetailMediaKeywordsReviewResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
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
        api_response = api_instance.update_keyword_reviews(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_keyword_reviews: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_keyword_reviews(line_item_id, value_resource_input_retail_media_keywords_review=value_resource_input_retail_media_keywords_review)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_keyword_reviews: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_line_item_budget_overrides**
> ValueResourceOutcomeOfLineItemBudgetOverrides update_line_item_budget_overrides(line_item_id, value_resource_input_of_line_item_budget_overrides)



Update line item budget overrides by given external line item id and new line item budget overrides settings.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.value_resource_input_of_line_item_budget_overrides import ValueResourceInputOfLineItemBudgetOverrides
from criteo_api_retailmedia_v2026_01.model.value_resource_outcome_of_line_item_budget_overrides import ValueResourceOutcomeOfLineItemBudgetOverrides
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | Line item external id.
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
    ) # ValueResourceInputOfLineItemBudgetOverrides | New line item budget overrides settings value resource input.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_line_item_budget_overrides(line_item_id, value_resource_input_of_line_item_budget_overrides)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_line_item_budget_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Line item external id. |
 **value_resource_input_of_line_item_budget_overrides** | [**ValueResourceInputOfLineItemBudgetOverrides**](ValueResourceInputOfLineItemBudgetOverrides.md)| New line item budget overrides settings value resource input. |

### Return type

[**ValueResourceOutcomeOfLineItemBudgetOverrides**](ValueResourceOutcomeOfLineItemBudgetOverrides.md)

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

# **update_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response update_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)



Updates the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2026_01
from criteo_api_retailmedia_v2026_01.api import campaign_api
from criteo_api_retailmedia_v2026_01.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from criteo_api_retailmedia_v2026_01.model.preferred_line_item_update_model_v2_request import PreferredLineItemUpdateModelV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The given line item id
    preferred_line_item_update_model_v2_request = PreferredLineItemUpdateModelV2Request(
        data=ResourceOfPreferredLineItemUpdateModelV2(
            attributes=PreferredLineItemUpdateModelV2(
                budget=3.14,
                capping=LineItemCappingV2(
                    count=1,
                    type="unknown",
                ),
                creative_id="creative_id_example",
                end_date=dateutil_parser('1970-01-01').date(),
                name="name_example",
                pacing="accelerated",
                page=LineItemPageV2(
                    categories=[
                        LineItemPageCategoryV2(
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
        api_response = api_instance.update_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2026_01.ApiException as e:
        print("Exception when calling CampaignApi->update_preferred_line_item_by_line_item_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

