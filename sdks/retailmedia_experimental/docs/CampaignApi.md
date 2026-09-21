# criteo_api_retailmedia_experimental.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_products**](CampaignApi.md#add_products) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/add | /experimental/retail-media/line-items/{line-item-id}/products/add
[**append_product_button_by_line_item_id**](CampaignApi.md#append_product_button_by_line_item_id) | **POST** /experimental/retail-media/line-items/{line-item-id}/product-buttons/create | /experimental/retail-media/line-items/{line-item-id}/product-buttons/create
[**create_auction_line_item**](CampaignApi.md#create_auction_line_item) | **POST** /experimental/retail-media/campaigns/{campaignId}/auction-line-items | /experimental/retail-media/campaigns/{campaignId}/auction-line-items
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /experimental/retail-media/accounts/{account-id}/campaigns | /experimental/retail-media/accounts/{account-id}/campaigns
[**create_creative**](CampaignApi.md#create_creative) | **POST** /experimental/retail-media/accounts/{account-id}/creatives | /experimental/retail-media/accounts/{account-id}/creatives
[**create_line_item**](CampaignApi.md#create_line_item) | **POST** /experimental/retail-media/line-items | /experimental/retail-media/line-items
[**create_preferred_line_item_by_campaign_id**](CampaignApi.md#create_preferred_line_item_by_campaign_id) | **POST** /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items | /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items
[**create_targets_by_line_item_id**](CampaignApi.md#create_targets_by_line_item_id) | **POST** /experimental/retail-media/line-items/{line-item-id}/targets/create | /experimental/retail-media/line-items/{line-item-id}/targets/create
[**delete_creatives**](CampaignApi.md#delete_creatives) | **POST** /experimental/retail-media/line-items/{line-item-id}/creatives/delete | /experimental/retail-media/line-items/{line-item-id}/creatives/delete
[**delete_product_button_by_line_item_and_product_button_id**](CampaignApi.md#delete_product_button_by_line_item_and_product_button_id) | **DELETE** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}
[**delete_products**](CampaignApi.md#delete_products) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/delete | /experimental/retail-media/line-items/{line-item-id}/products/delete
[**fetch_creatives**](CampaignApi.md#fetch_creatives) | **GET** /experimental/retail-media/line-items/{line-item-id}/creatives | /experimental/retail-media/line-items/{line-item-id}/creatives
[**get_bidding_strategy_by_line_item_id**](CampaignApi.md#get_bidding_strategy_by_line_item_id) | **GET** /experimental/retail-media/line-items/{line-item-id}/bidding-strategy | /experimental/retail-media/line-items/{line-item-id}/bidding-strategy
[**get_campaign**](CampaignApi.md#get_campaign) | **GET** /experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id} | /experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id}
[**get_capout_history**](CampaignApi.md#get_capout_history) | **POST** /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history | /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history
[**get_catalog_status**](CampaignApi.md#get_catalog_status) | **GET** /experimental/retail-media/catalogs/{catalogId}/status | /experimental/retail-media/catalogs/{catalogId}/status
[**get_creative**](CampaignApi.md#get_creative) | **GET** /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} | /experimental/retail-media/accounts/{account-id}/creatives/{creative-id}
[**get_product_button_by_line_item_and_product_button_id**](CampaignApi.md#get_product_button_by_line_item_and_product_button_id) | **GET** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}
[**get_product_buttons_by_line_item_id**](CampaignApi.md#get_product_buttons_by_line_item_id) | **GET** /experimental/retail-media/line-items/{line-item-id}/product-buttons | /experimental/retail-media/line-items/{line-item-id}/product-buttons
[**get_targets_by_line_item_id**](CampaignApi.md#get_targets_by_line_item_id) | **GET** /experimental/retail-media/line-items/{line-item-id}/targets | /experimental/retail-media/line-items/{line-item-id}/targets
[**line_items_demand_search**](CampaignApi.md#line_items_demand_search) | **POST** /experimental/retail-media/line-items/demand-search | /experimental/retail-media/line-items/demand-search
[**line_items_supply_search**](CampaignApi.md#line_items_supply_search) | **POST** /experimental/retail-media/line-items/supply-search | /experimental/retail-media/line-items/supply-search
[**search_account_creatives**](CampaignApi.md#search_account_creatives) | **POST** /experimental/retail-media/accounts/{account-id}/creatives/search | /experimental/retail-media/accounts/{account-id}/creatives/search
[**search_campaigns**](CampaignApi.md#search_campaigns) | **POST** /experimental/retail-media/accounts/{account-id}/campaigns/search | /experimental/retail-media/accounts/{account-id}/campaigns/search
[**set_bidding_strategy_by_line_item_id**](CampaignApi.md#set_bidding_strategy_by_line_item_id) | **POST** /experimental/retail-media/line-items/{line-item-id}/set-bidding-strategy | /experimental/retail-media/line-items/{line-item-id}/set-bidding-strategy
[**submit_line_item**](CampaignApi.md#submit_line_item) | **POST** /experimental/retail-media/line-items/{line-item-id}/submit | /experimental/retail-media/line-items/{line-item-id}/submit
[**update_auction_line_item**](CampaignApi.md#update_auction_line_item) | **PUT** /experimental/retail-media/auction-line-items/{lineItemId} | /experimental/retail-media/auction-line-items/{lineItemId}
[**update_campaign**](CampaignApi.md#update_campaign) | **PATCH** /experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id} | /experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id}
[**update_creative**](CampaignApi.md#update_creative) | **PUT** /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} | /experimental/retail-media/accounts/{account-id}/creatives/{creative-id}
[**update_line_item**](CampaignApi.md#update_line_item) | **PATCH** /experimental/retail-media/line-items/{line-item-id} | /experimental/retail-media/line-items/{line-item-id}
[**update_preferred_line_item_by_line_item_id**](CampaignApi.md#update_preferred_line_item_by_line_item_id) | **PUT** /experimental/retail-media/preferred-line-items/{line-item-id} | /experimental/retail-media/preferred-line-items/{line-item-id}
[**update_product_button_by_line_item_and_product_button_id**](CampaignApi.md#update_product_button_by_line_item_and_product_button_id) | **PUT** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}
[**update_targets_by_line_item_id**](CampaignApi.md#update_targets_by_line_item_id) | **POST** /experimental/retail-media/line-items/{line-item-id}/targets/update | /experimental/retail-media/line-items/{line-item-id}/targets/update
[**upsert_creatives**](CampaignApi.md#upsert_creatives) | **POST** /experimental/retail-media/line-items/{line-item-id}/creatives/upsert | /experimental/retail-media/line-items/{line-item-id}/creatives/upsert


# **add_products**
> AddProductsResultModelResponse add_products(line_item_id, add_products_model_request)

/experimental/retail-media/line-items/{line-item-id}/products/add

Add products to a line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.add_products_model_request import AddProductsModelRequest
from criteo_api_retailmedia_experimental.model.add_products_result_model_response import AddProductsResultModelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item id.
    add_products_model_request = AddProductsModelRequest(
        data=AddProductsModelResource(
            attributes=AddProductsModel(
                display_product_details=[
                    ProductModel(
                        product_id="product_id_example",
                    ),
                ],
                product_type="DisplayProduct",
            ),
            type="type_example",
        ),
    ) # AddProductsModelRequest | The products to add.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/products/add
        api_response = api_instance.add_products(line_item_id, add_products_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->add_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item id. |
 **add_products_model_request** | [**AddProductsModelRequest**](AddProductsModelRequest.md)| The products to add. |

### Return type

[**AddProductsResultModelResponse**](AddProductsResultModelResponse.md)

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

/experimental/retail-media/line-items/{line-item-id}/product-buttons/create

Add Specific Product Buttons

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.product_button_request_list_request import ProductButtonRequestListRequest
from criteo_api_retailmedia_experimental.model.product_button_response_list_response import ProductButtonResponseListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/line-items/{line-item-id}/product-buttons/create
        api_response = api_instance.append_product_button_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->append_product_button_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/line-items/{line-item-id}/product-buttons/create
        api_response = api_instance.append_product_button_by_line_item_id(line_item_id, product_button_request_list_request=product_button_request_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **create_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem create_auction_line_item(campaign_id, value_resource_input_of_sponsored_products_line_item_create_request_model)

/experimental/retail-media/campaigns/{campaignId}/auction-line-items

Creates new auction line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from criteo_api_retailmedia_experimental.model.value_resource_input_of_sponsored_products_line_item_create_request_model import ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
                            end_time="23:20",
                            start_time="23:20",
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
        # /experimental/retail-media/campaigns/{campaignId}/auction-line-items
        api_response = api_instance.create_auction_line_item(campaign_id, value_resource_input_of_sponsored_products_line_item_create_request_model)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **create_campaign**
> CampaignResponseModelResponse create_campaign(account_id, campaign_create_model_request)

/experimental/retail-media/accounts/{account-id}/campaigns

Creates a campaign under the specified account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.campaign_response_model_response import CampaignResponseModelResponse
from criteo_api_retailmedia_experimental.model.campaign_create_model_request import CampaignCreateModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The external id of the account.
    campaign_create_model_request = CampaignCreateModelRequest(
        data=CampaignCreateModelResource(
            attributes=CampaignCreateModel(
                attribution_settings=AttributionSettingsCreateModel(
                    click_attribution_scope="SameSku",
                    click_attribution_window="OneWeek",
                    view_attribution_scope="SameSku",
                    view_attribution_window="None",
                ),
                bill_by_retailer_id="bill_by_retailer_id_example",
                buy_type="Auction",
                campaign_type="SponsoredProducts",
                company_name="company_name_example",
                drawable_balance_ids=[
                    "drawable_balance_ids_example",
                ],
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
                onsite_display_details=OnsiteDisplayDetailsCreateModel(
                    budget=OnsiteDisplayBudgetCreateModel(
                        amount=3.14,
                    ),
                ),
                regulated_category="None",
                schedule_details=ScheduleDetailsCreateModel(
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                sponsored_products_details=SponsoredProductsDetailsCreateModel(
                    budget=SponsoredProductsBudgetCreateModel(
                        amount=3.14,
                        cappings=[
                            BudgetCappingRequestModel(
                                amount=3.14,
                                type="Daily",
                            ),
                        ],
                        pacing=PacingRequestModel(
                            type="Automatic",
                        ),
                    ),
                    objective="Manual",
                ),
            ),
            type="type_example",
        ),
    ) # CampaignCreateModelRequest | The campaign to create.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/accounts/{account-id}/campaigns
        api_response = api_instance.create_campaign(account_id, campaign_create_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->create_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external id of the account. |
 **campaign_create_model_request** | [**CampaignCreateModelRequest**](CampaignCreateModelRequest.md)| The campaign to create. |

### Return type

[**CampaignResponseModelResponse**](CampaignResponseModelResponse.md)

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

/experimental/retail-media/accounts/{account-id}/creatives

Create a creative for an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.creative_create_model2 import CreativeCreateModel2
from criteo_api_retailmedia_experimental.model.creative2_response import Creative2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/creatives
        api_response = api_instance.create_creative(account_id, creative_create_model2)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **create_line_item**
> ExperimentalLineItemModelResponse create_line_item(experimental_create_line_item_model_request)

/experimental/retail-media/line-items

Create a new line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.experimental_line_item_model_response import ExperimentalLineItemModelResponse
from criteo_api_retailmedia_experimental.model.experimental_create_line_item_model_request import ExperimentalCreateLineItemModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    experimental_create_line_item_model_request = ExperimentalCreateLineItemModelRequest(
        data=ExperimentalCreateLineItemModelResource(
            attributes=ExperimentalCreateLineItemModel(
                campaign_id="campaign_id_example",
                is_paused=True,
                name="name_example",
                onsite_display_details=ExperimentalCreateOnsiteDisplayLineItemDetails(
                    auction_details=ExperimentalCreateOnsiteDisplayAuctionLineItemDetails(
                        is_dynamic_match=True,
                    ),
                    frequency_capping=ExperimentalFrequencyCappingModel(
                        capping_count=1,
                        capping_duration_type="Unknown",
                    ),
                ),
                retailer_id="retailer_id_example",
                serve_to_opt_out_user=True,
            ),
            type="type_example",
        ),
    ) # ExperimentalCreateLineItemModelRequest | Line item details

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items
        api_response = api_instance.create_line_item(experimental_create_line_item_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->create_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experimental_create_line_item_model_request** | [**ExperimentalCreateLineItemModelRequest**](ExperimentalCreateLineItemModelRequest.md)| Line item details |

### Return type

[**ExperimentalLineItemModelResponse**](ExperimentalLineItemModelResponse.md)

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

# **create_preferred_line_item_by_campaign_id**
> PreferredLineItemV2Response create_preferred_line_item_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)

/experimental/retail-media/campaigns/{campaign-id}/preferred-line-items

Creates a new preferred line item with the specified settings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.preferred_line_item_create_model_v2_request import PreferredLineItemCreateModelV2Request
from criteo_api_retailmedia_experimental.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items
        api_response = api_instance.create_preferred_line_item_by_campaign_id(campaign_id, preferred_line_item_create_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **create_targets_by_line_item_id**
> TargetListResponse create_targets_by_line_item_id(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/targets/create

Creates a given target

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.create_target_request_model_list_request import CreateTargetRequestModelListRequest
from criteo_api_retailmedia_experimental.model.target_list_response import TargetListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Unique identifier for the line item
    create_target_request_model_list_request = CreateTargetRequestModelListRequest(
        data=[
            CreateTargetRequestModelResource(
                attributes=CreateTargetRequestModel(
                    bid_multiplier=3.14,
                    category_target_details=CategoryTargetDetails(
                        category_id="category_id_example",
                        include_children=True,
                    ),
                    geography_target_details=GeographyTargetDetails(
                        geo_location_id="geo_location_id_example",
                    ),
                    manual_keyword_target_details=ManualKeywordTargetDetails(
                        keyword_input="keyword_input_example",
                        match_type="Broad",
                    ),
                    negative=True,
                    page_type_target_details=PageTypeTargetDetails(
                        page_type="Unknown",
                    ),
                    target_type="Unknown",
                ),
                type="type_example",
            ),
        ],
    ) # CreateTargetRequestModelListRequest | Target to configure on the line item (optional)

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/targets/create
        api_response = api_instance.create_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->create_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/line-items/{line-item-id}/targets/create
        api_response = api_instance.create_targets_by_line_item_id(line_item_id, create_target_request_model_list_request=create_target_request_model_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->create_targets_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Unique identifier for the line item |
 **create_target_request_model_list_request** | [**CreateTargetRequestModelListRequest**](CreateTargetRequestModelListRequest.md)| Target to configure on the line item | [optional]

### Return type

[**TargetListResponse**](TargetListResponse.md)

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

# **delete_creatives**
> Outcome delete_creatives(line_item_id, delete_creatives_model_request)

/experimental/retail-media/line-items/{line-item-id}/creatives/delete

Delete creatives and their product collections from a line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.delete_creatives_model_request import DeleteCreativesModelRequest
from criteo_api_retailmedia_experimental.model.outcome import Outcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The external line item id.
    delete_creatives_model_request = DeleteCreativesModelRequest(
        data=DeleteCreativesModelResource(
            attributes=DeleteCreativesModel(
                creative_ids=[
                    "creative_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # DeleteCreativesModelRequest | The stable creative identifiers to delete.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/creatives/delete
        api_response = api_instance.delete_creatives(line_item_id, delete_creatives_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->delete_creatives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The external line item id. |
 **delete_creatives_model_request** | [**DeleteCreativesModelRequest**](DeleteCreativesModelRequest.md)| The stable creative identifiers to delete. |

### Return type

[**Outcome**](Outcome.md)

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

# **delete_product_button_by_line_item_and_product_button_id**
> ProductButtonResponseListResponse delete_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Delete Specific Product Button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.product_button_response_list_response import ProductButtonResponseListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | LineItemId for productButton delete
    product_button_id = "product-button-id_example" # str | productButtonId used for delete

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}
        api_response = api_instance.delete_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **delete_products**
> Outcome delete_products(line_item_id, delete_product_model_request)

/experimental/retail-media/line-items/{line-item-id}/products/delete

Delete products from a line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.outcome import Outcome
from criteo_api_retailmedia_experimental.model.delete_product_model_request import DeleteProductModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item id.
    delete_product_model_request = DeleteProductModelRequest(
        data=DeleteProductModelResource(
            attributes=DeleteProductModel(
                product_ids=[
                    "product_ids_example",
                ],
                product_type="DisplayProduct",
            ),
            type="type_example",
        ),
    ) # DeleteProductModelRequest | The products to delete.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/products/delete
        api_response = api_instance.delete_products(line_item_id, delete_product_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->delete_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item id. |
 **delete_product_model_request** | [**DeleteProductModelRequest**](DeleteProductModelRequest.md)| The products to delete. |

### Return type

[**Outcome**](Outcome.md)

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

# **fetch_creatives**
> FetchCreativesModelResponse fetch_creatives(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/creatives

Retrieve the creatives and product collections associated with a line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.fetch_creatives_model_response import FetchCreativesModelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The external line item id.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/creatives
        api_response = api_instance.fetch_creatives(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->fetch_creatives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The external line item id. |

### Return type

[**FetchCreativesModelResponse**](FetchCreativesModelResponse.md)

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

# **get_bidding_strategy_by_line_item_id**
> BiddingSettingsResponse get_bidding_strategy_by_line_item_id(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/bidding-strategy

Returns the current bidding configuration for a Display auction line item, including the active  bidding strategy and any preserved Standard and Adaptive strategy settings. Other line item types are  not currently supported by this endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.bidding_settings_response import BiddingSettingsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The identifier of the line item whose bidding settings are requested.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/bidding-strategy
        api_response = api_instance.get_bidding_strategy_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->get_bidding_strategy_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The identifier of the line item whose bidding settings are requested. |

### Return type

[**BiddingSettingsResponse**](BiddingSettingsResponse.md)

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

# **get_campaign**
> CampaignResponseModelResponse get_campaign(account_id, campaign_id)

/experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id}

Gets a campaign by its external id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.campaign_response_model_response import CampaignResponseModelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The external id of the account.
    campaign_id = "campaign-id_example" # str | The external id of the campaign.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id}
        api_response = api_instance.get_campaign(account_id, campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external id of the account. |
 **campaign_id** | **str**| The external id of the campaign. |

### Return type

[**CampaignResponseModelResponse**](CampaignResponseModelResponse.md)

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

/experimental/retail-media/accounts/{account-id}/line-items/cap-out-history

Get the cap out history for line items

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.value_resource_outcome_line_item_budget_cap_out_history_response import ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse
from criteo_api_retailmedia_experimental.model.value_resource_input_line_item_budget_cap_out_history_request import ValueResourceInputLineItemBudgetCapOutHistoryRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history
        api_response = api_instance.get_capout_history(account_id, value_resource_input_line_item_budget_cap_out_history_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/catalogs/{catalogId}/status

Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.entity_resource_outcome_of_catalog_status_v2 import EntityResourceOutcomeOfCatalogStatusV2
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/catalogs/{catalogId}/status
        api_response = api_instance.get_catalog_status(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/accounts/{account-id}/creatives/{creative-id}

Get the specified creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.creative2_response import Creative2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_id = "creative-id_example" # str | Creative to get

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/accounts/{account-id}/creatives/{creative-id}
        api_response = api_instance.get_creative(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **get_product_button_by_line_item_and_product_button_id**
> ProductButtonResponseListResponse get_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Get Specific Product Button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.product_button_response_list_response import ProductButtonResponseListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | LineItemId for productButton retrieval
    product_button_id = "product-button-id_example" # str | productButtonId used for retrieval

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}
        api_response = api_instance.get_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/line-items/{line-item-id}/product-buttons

Get LineItem Product Buttons

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.product_button_response_list_response import ProductButtonResponseListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | LineItemId for productButton retrieval

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/product-buttons
        api_response = api_instance.get_product_buttons_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **get_targets_by_line_item_id**
> TargetListResponseWithPageMetadata get_targets_by_line_item_id(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/targets

Returns a list of targets for a given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.target_list_response_with_page_metadata import TargetListResponseWithPageMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Unique identifier of the Line Item for which targets will be fetched
    limit = 500 # int | The number of elements to be returned. Defaults to 500. (optional) if omitted the server will use the default value of 500
    offset = 0 # int | The (zero-based) starting offset in the collection. Defaults to 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/targets
        api_response = api_instance.get_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->get_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/line-items/{line-item-id}/targets
        api_response = api_instance.get_targets_by_line_item_id(line_item_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->get_targets_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Unique identifier of the Line Item for which targets will be fetched |
 **limit** | **int**| The number of elements to be returned. Defaults to 500. | [optional] if omitted the server will use the default value of 500
 **offset** | **int**| The (zero-based) starting offset in the collection. Defaults to 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**TargetListResponseWithPageMetadata**](TargetListResponseWithPageMetadata.md)

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

# **line_items_demand_search**
> LineItemListResponseWithPagination line_items_demand_search(demand_search_request)

/experimental/retail-media/line-items/demand-search

Search line items accessible from demand accounts.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.demand_search_request import DemandSearchRequest
from criteo_api_retailmedia_experimental.model.line_item_list_response_with_pagination import LineItemListResponseWithPagination
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    demand_search_request = DemandSearchRequest(
        data=DemandSearchResource(
            attributes=DemandSearch(
                account_ids=[
                    "account_ids_example",
                ],
                campaign_ids=[
                    "campaign_ids_example",
                ],
                include_children_accounts=True,
                limit=1,
                line_item_ids=[
                    "line_item_ids_example",
                ],
                offset=1,
            ),
            type="type_example",
        ),
    ) # DemandSearchRequest | Search criteria and pagination.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/demand-search
        api_response = api_instance.line_items_demand_search(demand_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->line_items_demand_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **demand_search_request** | [**DemandSearchRequest**](DemandSearchRequest.md)| Search criteria and pagination. |

### Return type

[**LineItemListResponseWithPagination**](LineItemListResponseWithPagination.md)

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

# **line_items_supply_search**
> LineItemListResponseWithPagination line_items_supply_search(supply_search_request)

/experimental/retail-media/line-items/supply-search

Search line items accessible from a supply account and its retailers.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.supply_search_request import SupplySearchRequest
from criteo_api_retailmedia_experimental.model.line_item_list_response_with_pagination import LineItemListResponseWithPagination
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    supply_search_request = SupplySearchRequest(
        data=SupplySearchResource(
            attributes=SupplySearch(
                campaign_ids=[
                    "campaign_ids_example",
                ],
                limit=1,
                line_item_ids=[
                    "line_item_ids_example",
                ],
                offset=1,
                relationship="Direct",
                retailer_ids=[
                    "retailer_ids_example",
                ],
                supply_account_id="supply_account_id_example",
            ),
            type="type_example",
        ),
    ) # SupplySearchRequest | Search criteria and pagination.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/supply-search
        api_response = api_instance.line_items_supply_search(supply_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->line_items_supply_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_search_request** | [**SupplySearchRequest**](SupplySearchRequest.md)| Search criteria and pagination. |

### Return type

[**LineItemListResponseWithPagination**](LineItemListResponseWithPagination.md)

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
> EntityResourceCollectionOutcomeCreativeSearchResponseAndMetadata search_account_creatives(account_id, entity_resource_input_creative_search_request)

/experimental/retail-media/accounts/{account-id}/creatives/search

Get account creatives

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.entity_resource_input_creative_search_request import EntityResourceInputCreativeSearchRequest
from criteo_api_retailmedia_experimental.model.entity_resource_collection_outcome_creative_search_response_and_metadata import EntityResourceCollectionOutcomeCreativeSearchResponseAndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/creatives/search
        api_response = api_instance.search_account_creatives(account_id, entity_resource_input_creative_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->search_account_creatives: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/accounts/{account-id}/creatives/search
        api_response = api_instance.search_account_creatives(account_id, entity_resource_input_creative_search_request, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

[**EntityResourceCollectionOutcomeCreativeSearchResponseAndMetadata**](EntityResourceCollectionOutcomeCreativeSearchResponseAndMetadata.md)

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

# **search_campaigns**
> CampaignResponseModelListResponseWithCampaignSearchMetadataModel search_campaigns(account_id)

/experimental/retail-media/accounts/{account-id}/campaigns/search

Searches campaigns under an account using optional filters and pagination.  Budgets are sourced from the search index, so they lag a campaign that has just changed.  Search does not perform Kobalos enrichment, so drawable balance ids are not included.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.campaign_response_model_list_response_with_campaign_search_metadata_model import CampaignResponseModelListResponseWithCampaignSearchMetadataModel
from criteo_api_retailmedia_experimental.model.campaign_search_model_request import CampaignSearchModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The external id of the account.
    campaign_search_model_request = CampaignSearchModelRequest(
        data=CampaignSearchModelResource(
            attributes=CampaignSearchModel(
                buy_type_filter=[
                    "Auction",
                ],
                campaign_id_filter=[
                    "campaign_id_filter_example",
                ],
                campaign_status_filter=[
                    "Active",
                ],
                campaign_type_filter=[
                    "SponsoredProducts",
                ],
                limit=1,
                offset=1,
            ),
            type="type_example",
        ),
    ) # CampaignSearchModelRequest | Optional search filters and pagination. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/accounts/{account-id}/campaigns/search
        api_response = api_instance.search_campaigns(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->search_campaigns: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/accounts/{account-id}/campaigns/search
        api_response = api_instance.search_campaigns(account_id, campaign_search_model_request=campaign_search_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->search_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external id of the account. |
 **campaign_search_model_request** | [**CampaignSearchModelRequest**](CampaignSearchModelRequest.md)| Optional search filters and pagination. | [optional]

### Return type

[**CampaignResponseModelListResponseWithCampaignSearchMetadataModel**](CampaignResponseModelListResponseWithCampaignSearchMetadataModel.md)

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

# **set_bidding_strategy_by_line_item_id**
> BiddingSettingsResponse set_bidding_strategy_by_line_item_id(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/set-bidding-strategy

Replaces the submitted Standard page-type bids and updates the supplied strategy settings. Omitted  settings are preserved. Other line item types are not currently supported by this endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.bidding_settings_response import BiddingSettingsResponse
from criteo_api_retailmedia_experimental.model.bidding_settings_request import BiddingSettingsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The identifier of the line item whose bidding settings are being updated.
    bidding_settings_request = BiddingSettingsRequest(
        data=BiddingSettingsResource(
            attributes=BiddingSettings(
                cpm=CpmBiddingSettings(
                    adaptive_bidding_settings=AdaptiveBiddingSettings(
                        max_bid=3.14,
                    ),
                    bid_strategy="Standard",
                    standard_bidding_settings=StandardBiddingSettings(
                        auction_bids=[
                            LineItemAuctionBid(
                                bid=3.14,
                                page_type="Unknown",
                            ),
                        ],
                    ),
                ),
            ),
            type="type_example",
        ),
    ) # BiddingSettingsRequest | The bidding settings to apply. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/set-bidding-strategy
        api_response = api_instance.set_bidding_strategy_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->set_bidding_strategy_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/line-items/{line-item-id}/set-bidding-strategy
        api_response = api_instance.set_bidding_strategy_by_line_item_id(line_item_id, bidding_settings_request=bidding_settings_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->set_bidding_strategy_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The identifier of the line item whose bidding settings are being updated. |
 **bidding_settings_request** | [**BiddingSettingsRequest**](BiddingSettingsRequest.md)| The bidding settings to apply. | [optional]

### Return type

[**BiddingSettingsResponse**](BiddingSettingsResponse.md)

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

# **submit_line_item**
> submit_line_item(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/submit

Submits a Commerce Display line item for retailer review, transitioning its eligible reviewable  properties to In Review. A successful submission responds with 204 No Content and an empty body.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.submit_line_item_request_model_request import SubmitLineItemRequestModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The external id of the line item to submit.
    submit_line_item_request_model_request = SubmitLineItemRequestModelRequest(
        data=SubmitLineItemRequestModelResource(
            attributes=SubmitLineItemRequestModel(
                comment="comment_example",
            ),
            type="type_example",
        ),
    ) # SubmitLineItemRequestModelRequest | The submission details, including an optional comment for the reviewer. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/submit
        api_instance.submit_line_item(line_item_id)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->submit_line_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/line-items/{line-item-id}/submit
        api_instance.submit_line_item(line_item_id, submit_line_item_request_model_request=submit_line_item_request_model_request)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->submit_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The external id of the line item to submit. |
 **submit_line_item_request_model_request** | [**SubmitLineItemRequestModelRequest**](SubmitLineItemRequestModelRequest.md)| The submission details, including an optional comment for the reviewer. | [optional]

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auction_line_item**
> EntityResourceOutcomeOfSponsoredProductsLineItem update_auction_line_item(line_item_id, value_resource_input_of_sponsored_products_line_item_update_request_model)

/experimental/retail-media/auction-line-items/{lineItemId}

Updates a Sponsored Products Line Item given a line item id and a request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.entity_resource_outcome_of_sponsored_products_line_item import EntityResourceOutcomeOfSponsoredProductsLineItem
from criteo_api_retailmedia_experimental.model.value_resource_input_of_sponsored_products_line_item_update_request_model import ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The external line item ID of the sponsored products line item.
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
                            end_time="23:20",
                            start_time="23:20",
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
        # /experimental/retail-media/auction-line-items/{lineItemId}
        api_response = api_instance.update_auction_line_item(line_item_id, value_resource_input_of_sponsored_products_line_item_update_request_model)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->update_auction_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The external line item ID of the sponsored products line item. |
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

# **update_campaign**
> CampaignResponseModelResponse update_campaign(account_id, campaign_id, campaign_update_model_request)

/experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id}

Selectively updates a campaign. Omitted properties remain unchanged.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.campaign_update_model_request import CampaignUpdateModelRequest
from criteo_api_retailmedia_experimental.model.campaign_response_model_response import CampaignResponseModelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | The external id of the account.
    campaign_id = "campaign-id_example" # str | The external id of the campaign.
    campaign_update_model_request = CampaignUpdateModelRequest(
        data=CampaignUpdateModelResource(
            attributes=CampaignUpdateModel(
                attribution_settings=AttributionSettingsUpdateModel(
                    click_attribution_scope="SameSku",
                    click_attribution_window="OneWeek",
                    view_attribution_scope="SameSku",
                    view_attribution_window="None",
                ),
                company_name=StringNillableV2(
                    value="value_example",
                ),
                name="name_example",
                on_behalf_company_name=StringNillableV2(
                    value="value_example",
                ),
                onsite_display_details=OnsiteDisplayDetailsUpdateModel(
                    budget=OnsiteDisplayBudgetUpdateModel(
                        amount=3.14,
                    ),
                ),
                schedule_details=ScheduleDetailsUpdateModel(
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                sponsored_products_details=SponsoredProductsDetailsUpdateModel(
                    budget=SponsoredProductsBudgetUpdateModel(
                        amount=3.14,
                        cappings=[
                            BudgetCappingRequestModel(
                                amount=3.14,
                                type="Daily",
                            ),
                        ],
                        pacing=PacingRequestModel(
                            type="Automatic",
                        ),
                    ),
                ),
            ),
            type="type_example",
        ),
    ) # CampaignUpdateModelRequest | The campaign fields to update.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/accounts/{account-id}/campaigns/{campaign-id}
        api_response = api_instance.update_campaign(account_id, campaign_id, campaign_update_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->update_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external id of the account. |
 **campaign_id** | **str**| The external id of the campaign. |
 **campaign_update_model_request** | [**CampaignUpdateModelRequest**](CampaignUpdateModelRequest.md)| The campaign fields to update. |

### Return type

[**CampaignResponseModelResponse**](CampaignResponseModelResponse.md)

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

/experimental/retail-media/accounts/{account-id}/creatives/{creative-id}

Update a creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.creative_update_model2 import CreativeUpdateModel2
from criteo_api_retailmedia_experimental.model.creative2_response import Creative2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/creatives/{creative-id}
        api_response = api_instance.update_creative(account_id, creative_id, creative_update_model2)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **update_line_item**
> ExperimentalLineItemModelResponse update_line_item(line_item_id, experimental_update_line_item_model_request)

/experimental/retail-media/line-items/{line-item-id}

Update an existing line item.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.experimental_line_item_model_response import ExperimentalLineItemModelResponse
from criteo_api_retailmedia_experimental.model.experimental_update_line_item_model_request import ExperimentalUpdateLineItemModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item id
    experimental_update_line_item_model_request = ExperimentalUpdateLineItemModelRequest(
        data=ExperimentalUpdateLineItemModelResource(
            attributes=ExperimentalUpdateLineItemModel(
                is_paused=True,
                name="name_example",
                onsite_display_details=ExperimentalUpdateOnsiteDisplayLineItemDetails(
                    auction_details=ExperimentalUpdateOnsiteDisplayAuctionLineItemDetails(
                        is_dynamic_match=True,
                    ),
                    frequency_capping=ExperimentalFrequencyCappingModelNillableV2(
                        value=ExperimentalFrequencyCappingModel(
                            capping_count=1,
                            capping_duration_type="Unknown",
                        ),
                    ),
                ),
                serve_to_opt_out_user=True,
            ),
            type="type_example",
        ),
    ) # ExperimentalUpdateLineItemModelRequest | Line item details

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}
        api_response = api_instance.update_line_item(line_item_id, experimental_update_line_item_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->update_line_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item id |
 **experimental_update_line_item_model_request** | [**ExperimentalUpdateLineItemModelRequest**](ExperimentalUpdateLineItemModelRequest.md)| Line item details |

### Return type

[**ExperimentalLineItemModelResponse**](ExperimentalLineItemModelResponse.md)

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

# **update_preferred_line_item_by_line_item_id**
> PreferredLineItemV2Response update_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)

/experimental/retail-media/preferred-line-items/{line-item-id}

Updates the preferred line item for the given line item id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.preferred_line_item_update_model_v2_request import PreferredLineItemUpdateModelV2Request
from criteo_api_retailmedia_experimental.model.preferred_line_item_v2_response import PreferredLineItemV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/preferred-line-items/{line-item-id}
        api_response = api_instance.update_preferred_line_item_by_line_item_id(line_item_id, preferred_line_item_update_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Update Specific Product Button

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.product_button_request_request import ProductButtonRequestRequest
from criteo_api_retailmedia_experimental.model.product_button_response_list_response import ProductButtonResponseListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}
        api_response = api_instance.update_product_button_by_line_item_and_product_button_id(line_item_id, product_button_id, product_button_request_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **update_targets_by_line_item_id**
> TargetListResponse update_targets_by_line_item_id(line_item_id)

/experimental/retail-media/line-items/{line-item-id}/targets/update

Updates targets in bulk. The request has PATCH-like semantics: immutable target details identify  each target, while mutable fields supplied in the request are updated.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.target_list_request import TargetListRequest
from criteo_api_retailmedia_experimental.model.target_list_response import TargetListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Unique identifier for the line item.
    target_list_request = TargetListRequest(
        data=[
            TargetResource(
                attributes=Target(
                    approval_status="Unknown",
                    bid_multiplier=3.14,
                    category_target_details=CategoryTargetDetails(
                        category_id="category_id_example",
                        include_children=True,
                    ),
                    geography_target_details=GeographyTargetDetails(
                        geo_location_id="geo_location_id_example",
                    ),
                    manual_keyword_target_details=ManualKeywordTargetDetails(
                        keyword_input="keyword_input_example",
                        match_type="Broad",
                    ),
                    negative=True,
                    page_type_target_details=PageTypeTargetDetails(
                        page_type="Unknown",
                    ),
                    target_type="Unknown",
                ),
                type="type_example",
            ),
        ],
    ) # TargetListRequest | Targets to update. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/targets/update
        api_response = api_instance.update_targets_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->update_targets_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/line-items/{line-item-id}/targets/update
        api_response = api_instance.update_targets_by_line_item_id(line_item_id, target_list_request=target_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->update_targets_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Unique identifier for the line item. |
 **target_list_request** | [**TargetListRequest**](TargetListRequest.md)| Targets to update. | [optional]

### Return type

[**TargetListResponse**](TargetListResponse.md)

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

# **upsert_creatives**
> CreativesModelResponse upsert_creatives(line_item_id, upsert_creatives_model_request)

/experimental/retail-media/line-items/{line-item-id}/creatives/upsert

Resolves each supplied stable creative identifier to its latest revision and  associates those revisions with the line item's proposal.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import campaign_api
from criteo_api_retailmedia_experimental.model.upsert_creatives_model_request import UpsertCreativesModelRequest
from criteo_api_retailmedia_experimental.model.creatives_model_response import CreativesModelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | The line item id.
    upsert_creatives_model_request = UpsertCreativesModelRequest(
        data=UpsertCreativesModelResource(
            attributes=UpsertCreativesModel(
                auction_creative_details=AuctionCreativeDetailsInputModel(
                    line_item_creatives=[
                        LineItemCreativeInputModel(
                            creative=CreativeInputModel(
                                id="id_example",
                            ),
                            creative_product_collections=[
                                CreativeProductCollectionInputModel(
                                    is_mandatory=True,
                                    products=[
                                        DisplayProductInputModel(
                                            id="id_example",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                creative_type="Unknown",
                preferred_deals_creative_details=PreferredDealsCreativeDetailsInputModel(
                    line_item_creative=LineItemCreativeInputModel(
                        creative=CreativeInputModel(
                            id="id_example",
                        ),
                        creative_product_collections=[
                            CreativeProductCollectionInputModel(
                                is_mandatory=True,
                                products=[
                                    DisplayProductInputModel(
                                        id="id_example",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ),
            type="type_example",
        ),
    ) # UpsertCreativesModelRequest | The creatives to upsert.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/line-items/{line-item-id}/creatives/upsert
        api_response = api_instance.upsert_creatives(line_item_id, upsert_creatives_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CampaignApi->upsert_creatives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item id. |
 **upsert_creatives_model_request** | [**UpsertCreativesModelRequest**](UpsertCreativesModelRequest.md)| The creatives to upsert. |

### Return type

[**CreativesModelResponse**](CreativesModelResponse.md)

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

