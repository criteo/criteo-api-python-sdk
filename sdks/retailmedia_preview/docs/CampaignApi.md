# criteo_api_retailmedia_preview.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_campaigns_by_balance_id**](CampaignApi.md#append_campaigns_by_balance_id) | **POST** /preview/retail-media/balances/{balance-id}/campaigns/append | 
[**append_product_button_by_line_item_id**](CampaignApi.md#append_product_button_by_line_item_id) | **POST** /preview/retail-media/line-items/{line-item-id}/product-buttons/create | 
[**append_promoted_products**](CampaignApi.md#append_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/append | 
[**compute_display_min_bid_by_retailer_id**](CampaignApi.md#compute_display_min_bid_by_retailer_id) | **POST** /preview/retail-media/retailers/{retailerId}/compute-display-min-bid | 
[**create_auction_line_item**](CampaignApi.md#create_auction_line_item) | **POST** /preview/retail-media/campaigns/{campaignId}/auction-line-items | 
[**create_creative**](CampaignApi.md#create_creative) | **POST** /preview/retail-media/accounts/{account-id}/creatives | 
[**create_preferred_line_item_by_campaign_id**](CampaignApi.md#create_preferred_line_item_by_campaign_id) | **POST** /preview/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**delete_product_button_by_line_item_and_product_button_id**](CampaignApi.md#delete_product_button_by_line_item_and_product_button_id) | **DELETE** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**delete_promoted_products**](CampaignApi.md#delete_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/delete | 
[**fetch_promoted_products**](CampaignApi.md#fetch_promoted_products) | **GET** /preview/retail-media/line-items/{line-item-id}/products | 
[**get_api_external_v1_retailer_brands_by_retailer_id**](CampaignApi.md#get_api_external_v1_retailer_brands_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailerId}/brands | 
[**get_api_external_v1_retailer_by_retailer_id_sellersseller**](CampaignApi.md#get_api_external_v1_retailer_by_retailer_id_sellersseller) | **GET** /preview/retail-media/retailers/{retailerId}/sellers/{seller} | 
[**get_api_external_v1_retailer_cpc_rates_by_retailer_id**](CampaignApi.md#get_api_external_v1_retailer_cpc_rates_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/cpc-rates | 
[**get_api_external_v1_retailer_placements_by_retailer_id**](CampaignApi.md#get_api_external_v1_retailer_placements_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/placements | 
[**get_auction_line_item**](CampaignApi.md#get_auction_line_item) | **GET** /preview/retail-media/auction-line-items/{lineItemId} | 
[**get_auction_line_items_by_campaign**](CampaignApi.md#get_auction_line_items_by_campaign) | **GET** /preview/retail-media/campaigns/{campaignId}/auction-line-items | 
[**get_capout_history**](CampaignApi.md#get_capout_history) | **POST** /preview/retail-media/accounts/{account-id}/line-items/cap-out-history | 
[**get_catalog_status**](CampaignApi.md#get_catalog_status) | **GET** /preview/retail-media/catalogs/{catalogId}/status | 
[**get_creative**](CampaignApi.md#get_creative) | **GET** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**get_preferred_line_items_by_campaign_id**](CampaignApi.md#get_preferred_line_items_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaign-id}/preferred-line-items | 
[**get_preferred_line_items_by_line_item_id**](CampaignApi.md#get_preferred_line_items_by_line_item_id) | **GET** /preview/retail-media/preferred-line-items/{line-item-id} | 
[**get_product_button_by_line_item_and_product_button_id**](CampaignApi.md#get_product_button_by_line_item_and_product_button_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**get_product_buttons_by_line_item_id**](CampaignApi.md#get_product_buttons_by_line_item_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons | 
[**pause_promoted_products**](CampaignApi.md#pause_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/pause | 
[**post_api_external_v1_catalogs_sku_retrieval**](CampaignApi.md#post_api_external_v1_catalogs_sku_retrieval) | **POST** /preview/retail-media/catalogs/sku-retrieval | 
[**post_api_external_v1_catalogs_sku_search**](CampaignApi.md#post_api_external_v1_catalogs_sku_search) | **POST** /preview/retail-media/catalogs/sku-search | 
[**search_account_creatives**](CampaignApi.md#search_account_creatives) | **POST** /preview/retail-media/accounts/{account-id}/creatives/search | 
[**search_account_retailers**](CampaignApi.md#search_account_retailers) | **POST** /preview/retail-media/accounts/{accountId}/retailers/search | 
[**search_brands**](CampaignApi.md#search_brands) | **POST** /preview/retail-media/brands/search | 
[**unpause_promoted_products**](CampaignApi.md#unpause_promoted_products) | **POST** /preview/retail-media/line-items/{line-item-id}/products/unpause | 
[**update_auction_line_item**](CampaignApi.md#update_auction_line_item) | **PUT** /preview/retail-media/auction-line-items/{lineItemId} | 
[**update_creative**](CampaignApi.md#update_creative) | **PUT** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**update_preferred_line_item_by_line_item_id**](CampaignApi.md#update_preferred_line_item_by_line_item_id) | **PUT** /preview/retail-media/preferred-line-items/{line-item-id} | 
[**update_product_button_by_line_item_and_product_button_id**](CampaignApi.md#update_product_button_by_line_item_and_product_button_id) | **PUT** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 


# **append_campaigns_by_balance_id**
> EntityResourceCollectionOutcomeOfBalanceCampaignV1 append_campaigns_by_balance_id(balance_id, entity_resource_collection_input_of_balance_campaign_v1)



appends one or more campaigns to the specified balance

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_collection_input_of_balance_campaign_v1 import EntityResourceCollectionInputOfBalanceCampaignV1
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_of_balance_campaign_v1 import EntityResourceCollectionOutcomeOfBalanceCampaignV1
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
    balance_id = "balance-id_example" # str | The balance to add campaigns from
    entity_resource_collection_input_of_balance_campaign_v1 = EntityResourceCollectionInputOfBalanceCampaignV1(
        data=[
            EntityResourceOfBalanceCampaignV1(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # EntityResourceCollectionInputOfBalanceCampaignV1 | The campaigns to append

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.append_campaigns_by_balance_id(balance_id, entity_resource_collection_input_of_balance_campaign_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to add campaigns from |
 **entity_resource_collection_input_of_balance_campaign_v1** | [**EntityResourceCollectionInputOfBalanceCampaignV1**](EntityResourceCollectionInputOfBalanceCampaignV1.md)| The campaigns to append |

### Return type

[**EntityResourceCollectionOutcomeOfBalanceCampaignV1**](EntityResourceCollectionOutcomeOfBalanceCampaignV1.md)

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

# **append_product_button_by_line_item_id**
> ProductButtonResponseListResponse append_product_button_by_line_item_id(line_item_id)



Add Specific Product Buttons

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_request_list_request import ProductButtonRequestListRequest
from criteo_api_retailmedia_preview.model.product_button_response_list_response import ProductButtonResponseListResponse
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
    line_item_id = "line-item-id_example" # str | LineItemId for productButton retrieval
    product_button_request_list_request = ProductButtonRequestListRequest(
        data=[
            ResourceOfProductButtonRequest(
                attributes=ProductButtonRequest(
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
    ) # ProductButtonRequestListRequest | List of Product Buttons to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.append_product_button_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_product_button_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.append_product_button_by_line_item_id(line_item_id, product_button_request_list_request=product_button_request_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->append_product_button_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for productButton retrieval |
 **product_button_request_list_request** | [**ProductButtonRequestListRequest**](ProductButtonRequestListRequest.md)| List of Product Buttons to append | [optional]

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductButtons added |  -  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_display_min_bid_by_retailer_id**
> ValueResourceCollectionOutcomeDisplayAuctionMinBidResult compute_display_min_bid_by_retailer_id(retailer_id)



Computes the min bid for relevant page types based on the provided information

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_collection_outcome_display_auction_min_bid_result import ValueResourceCollectionOutcomeDisplayAuctionMinBidResult
from criteo_api_retailmedia_preview.model.value_resource_input_display_auction_min_bid_request import ValueResourceInputDisplayAuctionMinBidRequest
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
    retailer_id = 1 # int | The retailer id
    value_resource_input_display_auction_min_bid_request = ValueResourceInputDisplayAuctionMinBidRequest(
        data=ValueResourceDisplayAuctionMinBidRequest(
            attributes=DisplayAuctionMinBidRequest(
                creative_ids=[
                    "creative_ids_example",
                ],
                product_ids=[
                    "product_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputDisplayAuctionMinBidRequest | The details for what creatives and product ids to use to compute the min bids (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.compute_display_min_bid_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->compute_display_min_bid_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.compute_display_min_bid_by_retailer_id(retailer_id, value_resource_input_display_auction_min_bid_request=value_resource_input_display_auction_min_bid_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->compute_display_min_bid_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id |
 **value_resource_input_display_auction_min_bid_request** | [**ValueResourceInputDisplayAuctionMinBidRequest**](ValueResourceInputDisplayAuctionMinBidRequest.md)| The details for what creatives and product ids to use to compute the min bids | [optional]

### Return type

[**ValueResourceCollectionOutcomeDisplayAuctionMinBidResult**](ValueResourceCollectionOutcomeDisplayAuctionMinBidResult.md)

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

# **create_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem create_auction_line_item(campaign_id, value_resource_input_of_sponsored_products_line_item_create_request_model)



Creates new auction line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from criteo_api_retailmedia_preview.model.value_resource_input_of_sponsored_products_line_item_create_request_model import ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel
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
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **create_creative**
> Creative2Response create_creative(account_id, creative_create_model2)



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
    ) # CreativeCreateModel2 | The creative to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_creative(account_id, creative_create_model2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->create_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to create a creative for |
 **creative_create_model2** | [**CreativeCreateModel2**](CreativeCreateModel2.md)| The creative to create |

### Return type

[**Creative2Response**](Creative2Response.md)

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
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **delete_product_button_by_line_item_and_product_button_id**
> ProductButtonResponseListResponse delete_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)



Delete Specific Product Button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_response_list_response import ProductButtonResponseListResponse
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
    line_item_id = "line-item-id_example" # str | LineItemId for productButton delete
    product_button_id = "product-button-id_example" # str | productButtonId used for delete

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_product_button_by_line_item_and_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for productButton delete |
 **product_button_id** | **str**| productButtonId used for delete |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductButton deleted |  -  |

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
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products removed from the line item |  -  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_external_v1_retailer_brands_by_retailer_id**
> BrandPreviewListResponse get_api_external_v1_retailer_brands_by_retailer_id(retailer_id)



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
    brand_type = "uc" # str | Filter to narrow down brands [all|uc|retailer]. Defaults to uc (optional) if omitted the server will use the default value of "uc"
    sku_stock_type_filter = "first-and-third-party" # str | Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party (optional) if omitted the server will use the default value of "first-and-third-party"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_external_v1_retailer_brands_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_retailer_brands_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_external_v1_retailer_brands_by_retailer_id(retailer_id, brand_type=brand_type, sku_stock_type_filter=sku_stock_type_filter)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_retailer_brands_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which brands should be fetched. |
 **brand_type** | **str**| Filter to narrow down brands [all|uc|retailer]. Defaults to uc | [optional] if omitted the server will use the default value of "uc"
 **sku_stock_type_filter** | **str**| Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party | [optional] if omitted the server will use the default value of "first-and-third-party"

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

# **get_api_external_v1_retailer_by_retailer_id_sellersseller**
> SellerPreviewResponse get_api_external_v1_retailer_by_retailer_id_sellersseller(retailer_id, seller)



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
        api_response = api_instance.get_api_external_v1_retailer_by_retailer_id_sellersseller(retailer_id, seller)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_retailer_by_retailer_id_sellersseller: %s\n" % e)
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

# **get_api_external_v1_retailer_cpc_rates_by_retailer_id**
> CpcRateCardPreviewResponse get_api_external_v1_retailer_cpc_rates_by_retailer_id(retailer_id)



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
        api_response = api_instance.get_api_external_v1_retailer_cpc_rates_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_retailer_cpc_rates_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_external_v1_retailer_cpc_rates_by_retailer_id(retailer_id, fields=fields)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_retailer_cpc_rates_by_retailer_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_external_v1_retailer_placements_by_retailer_id**
> PlacementPreviewListResponse get_api_external_v1_retailer_placements_by_retailer_id(retailer_id)



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
        api_response = api_instance.get_api_external_v1_retailer_placements_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_external_v1_retailer_placements_by_retailer_id: %s\n" % e)
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
**200** | placements records |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem get_auction_line_item(line_item_id)



Gets a sponsored product line item by its id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
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
    line_item_id = 1 # int | The id of the line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_auction_line_item(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_of_sponsored_products_line_item_and_metadata import EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_auction_line_items_by_campaign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_auction_line_items_by_campaign(campaign_id, limit=limit, limit_to_ids=limit_to_ids, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **get_capout_history**
> ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse get_capout_history(account_id, value_resource_input_line_item_budget_cap_out_history_request)



Get the cap out history for line items

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_line_item_budget_cap_out_history_response import ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse
from criteo_api_retailmedia_preview.model.value_resource_input_line_item_budget_cap_out_history_request import ValueResourceInputLineItemBudgetCapOutHistoryRequest
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
    account_id = "account-id_example" # str | account id that own the lineitem
    value_resource_input_line_item_budget_cap_out_history_request = ValueResourceInputLineItemBudgetCapOutHistoryRequest(
        data=ValueResourceLineItemBudgetCapOutHistoryRequest(
            attributes=LineItemBudgetCapOutHistoryRequest(
                budget_types=[
                    "total",
                ],
                line_item_ids=[
                    "line_item_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputLineItemBudgetCapOutHistoryRequest | lineitem budgetcapout history  object

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_capout_history(account_id, value_resource_input_line_item_budget_cap_out_history_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_capout_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id that own the lineitem |
 **value_resource_input_line_item_budget_cap_out_history_request** | [**ValueResourceInputLineItemBudgetCapOutHistoryRequest**](ValueResourceInputLineItemBudgetCapOutHistoryRequest.md)| lineitem budgetcapout history  object |

### Return type

[**ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse**](ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse.md)

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

# **get_catalog_status**
> EntityResourceOutcomeOfCatalogStatusV2 get_catalog_status(catalog_id)



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
        api_response = api_instance.get_catalog_status(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_catalog_status: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creative**
> Creative2Response get_creative(account_id, creative_id)



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
        api_response = api_instance.get_creative(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **get_preferred_line_items_by_campaign_id**
> PreferredLineItemV2PagedListResponse get_preferred_line_items_by_campaign_id(campaign_id)



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
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_preferred_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_preferred_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_preferred_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
        api_response = api_instance.get_preferred_line_items_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **get_product_button_by_line_item_and_product_button_id**
> ProductButtonResponseListResponse get_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)



Get Specific Product Button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_response_list_response import ProductButtonResponseListResponse
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
    line_item_id = "line-item-id_example" # str | LineItemId for productButton retrieval
    product_button_id = "product-button-id_example" # str | productButtonId used for retrieval

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_product_button_by_line_item_and_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for productButton retrieval |
 **product_button_id** | **str**| productButtonId used for retrieval |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductButton found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_buttons_by_line_item_id**
> ProductButtonResponseListResponse get_product_buttons_by_line_item_id(line_item_id)



Get LineItem Product Buttons

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_response_list_response import ProductButtonResponseListResponse
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
    line_item_id = "line-item-id_example" # str | LineItemId for productButton retrieval

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_product_buttons_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_product_buttons_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for productButton retrieval |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductButtons found |  -  |

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
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Promoted products paused |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_external_v1_catalogs_sku_retrieval**
> SkuDataPreviewListResponse post_api_external_v1_catalogs_sku_retrieval(request_body)



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
    request_body = [
        "request_body_example",
    ] # [str] | The list of SKU keys to retrieve sku information
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_external_v1_catalogs_sku_retrieval(request_body)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v1_catalogs_sku_retrieval: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_external_v1_catalogs_sku_retrieval(request_body, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v1_catalogs_sku_retrieval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**| The list of SKU keys to retrieve sku information |
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100

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

# **post_api_external_v1_catalogs_sku_search**
> SkuDataPreviewListResponse post_api_external_v1_catalogs_sku_search(sku_search_request_preview_request)



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
    sku_search_request_preview_request = SkuSearchRequestPreviewRequest(
        data=ResourceOfSkuSearchRequestPreview(
            attributes=SkuSearchRequestPreview(
                brand_ids=[
                    "brand_ids_example",
                ],
                brand_type="uC",
                id="id_example",
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
    ) # SkuSearchRequestPreviewRequest | 
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_external_v1_catalogs_sku_search(sku_search_request_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v1_catalogs_sku_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_external_v1_catalogs_sku_search(sku_search_request_preview_request, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_external_v1_catalogs_sku_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku_search_request_preview_request** | [**SkuSearchRequestPreviewRequest**](SkuSearchRequestPreviewRequest.md)|  |
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100

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

# **search_account_creatives**
> EntityResourceCollectionOutcomeCreativeSearchResponse search_account_creatives(account_id, entity_resource_input_creative_search_request)



Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_input_creative_search_request import EntityResourceInputCreativeSearchRequest
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_creative_search_response import EntityResourceCollectionOutcomeCreativeSearchResponse
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
    entity_resource_input_creative_search_request = EntityResourceInputCreativeSearchRequest(
        data=EntityResourceCreativeSearchRequest(
            attributes=CreativeSearchRequest(
                brand_ids=[
                    "brand_ids_example",
                ],
                creative_ids=[
                    "creative_ids_example",
                ],
                creative_name="creative_name_example",
                creative_types=[
                    "CommerceDisplay",
                ],
                page_types=[
                    "Unknown",
                ],
                retailer_ids=[
                    "retailer_ids_example",
                ],
                template_ids=[
                    "template_ids_example",
                ],
            ),
            id="id_example",
            type="type_example",
        ),
    ) # EntityResourceInputCreativeSearchRequest | search request filter
    limit = 50 # int | limit to paginated result (optional) if omitted the server will use the default value of 50
    offset = 0 # int | offset to paginated result (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_account_creatives(account_id, entity_resource_input_creative_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_account_creatives: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_account_creatives(account_id, entity_resource_input_creative_search_request, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_account_creatives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to retrieve creatives for |
 **entity_resource_input_creative_search_request** | [**EntityResourceInputCreativeSearchRequest**](EntityResourceInputCreativeSearchRequest.md)| search request filter |
 **limit** | **int**| limit to paginated result | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| offset to paginated result | [optional] if omitted the server will use the default value of 0

### Return type

[**EntityResourceCollectionOutcomeCreativeSearchResponse**](EntityResourceCollectionOutcomeCreativeSearchResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.value_resource_input_of_retailer_search_request import ValueResourceInputOfRetailerSearchRequest
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_of_retailer_result_and_metadata import EntityResourceCollectionOutcomeOfRetailerResultAndMetadata
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_account_retailers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_account_retailers(account_id, value_resource_input_of_retailer_search_request, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
        api_response = api_instance.search_brands(limit=limit, offset=offset, value_resource_input_brand_id_search_request=value_resource_input_brand_id_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from criteo_api_retailmedia_preview.model.value_resource_input_of_sponsored_products_line_item_update_request_model import ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel
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
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **update_creative**
> Creative2Response update_creative(account_id, creative_id, creative_update_model2)



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
    ) # CreativeUpdateModel2 | The creative to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_creative(account_id, creative_id, creative_update_model2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->update_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id containing the creative |
 **creative_id** | **str**| Creative to update |
 **creative_update_model2** | [**CreativeUpdateModel2**](CreativeUpdateModel2.md)| The creative to create |

### Return type

[**Creative2Response**](Creative2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Creative updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response update_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)



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
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **update_product_button_by_line_item_and_product_button_id**
> ProductButtonResponseListResponse update_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id, product_button_request_request)



Update Specific Product Button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_request_request import ProductButtonRequestRequest
from criteo_api_retailmedia_preview.model.product_button_response_list_response import ProductButtonResponseListResponse
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
    line_item_id = "line-item-id_example" # str | LineItemId for productButton update
    product_button_id = "product-button-id_example" # str | productButtonId used for update
    product_button_request_request = ProductButtonRequestRequest(
        data=ResourceOfProductButtonRequest(
            attributes=ProductButtonRequest(
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
    ) # ProductButtonRequestRequest | Specific Product button update info

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id, product_button_request_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->update_product_button_by_line_item_and_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| LineItemId for productButton update |
 **product_button_id** | **str**| productButtonId used for update |
 **product_button_request_request** | [**ProductButtonRequestRequest**](ProductButtonRequestRequest.md)| Specific Product button update info |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductButton updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

