# criteo_api_marketingsolutions_v2025_10.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ad_set**](CampaignApi.md#create_ad_set) | **POST** /2025-10/marketing-solutions/ad-sets | 
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /2025-10/marketing-solutions/campaigns | 
[**create_marketplace_seller_budgets**](CampaignApi.md#create_marketplace_seller_budgets) | **POST** /2025-10/marketing-solutions/marketplace-performance-outcomes/budgets | 
[**create_marketplace_seller_campaigns_by_seller**](CampaignApi.md#create_marketplace_seller_campaigns_by_seller) | **POST** /2025-10/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns | 
[**get_ad_set**](CampaignApi.md#get_ad_set) | **GET** /2025-10/marketing-solutions/ad-sets/{ad-set-id} | 
[**get_ad_set_category_bids**](CampaignApi.md#get_ad_set_category_bids) | **GET** /2025-10/marketing-solutions/ad-sets/{ad-set-id}/category-bids | 
[**get_campaign**](CampaignApi.md#get_campaign) | **GET** /2025-10/marketing-solutions/campaigns/{campaign-id} | 
[**get_display_multipliers**](CampaignApi.md#get_display_multipliers) | **GET** /2025-10/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | 
[**get_marketplace_ad_sets_by_advertiser**](CampaignApi.md#get_marketplace_ad_sets_by_advertiser) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets | 
[**get_marketplace_advertiser**](CampaignApi.md#get_marketplace_advertiser) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId} | 
[**get_marketplace_advertiser_preview_limits**](CampaignApi.md#get_marketplace_advertiser_preview_limits) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit | 
[**get_marketplace_advertisers**](CampaignApi.md#get_marketplace_advertisers) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers | 
[**get_marketplace_budgets_by_advertiser**](CampaignApi.md#get_marketplace_budgets_by_advertiser) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets | 
[**get_marketplace_budgets_by_seller**](CampaignApi.md#get_marketplace_budgets_by_seller) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets | 
[**get_marketplace_budgets_by_seller_campaign**](CampaignApi.md#get_marketplace_budgets_by_seller_campaign) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets | 
[**get_marketplace_campaigns_by_advertiser**](CampaignApi.md#get_marketplace_campaigns_by_advertiser) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns | 
[**get_marketplace_campaigns_stats**](CampaignApi.md#get_marketplace_campaigns_stats) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/stats/campaigns | 
[**get_marketplace_seller**](CampaignApi.md#get_marketplace_seller) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId} | 
[**get_marketplace_seller_ad_preview**](CampaignApi.md#get_marketplace_seller_ad_preview) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview | 
[**get_marketplace_seller_budget**](CampaignApi.md#get_marketplace_seller_budget) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} | 
[**get_marketplace_seller_budgets**](CampaignApi.md#get_marketplace_seller_budgets) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/budgets | 
[**get_marketplace_seller_campaign**](CampaignApi.md#get_marketplace_seller_campaign) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} | 
[**get_marketplace_seller_campaigns**](CampaignApi.md#get_marketplace_seller_campaigns) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/seller-campaigns | 
[**get_marketplace_seller_campaigns_by_advertiser**](CampaignApi.md#get_marketplace_seller_campaigns_by_advertiser) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns | 
[**get_marketplace_seller_campaigns_by_seller**](CampaignApi.md#get_marketplace_seller_campaigns_by_seller) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns | 
[**get_marketplace_seller_campaigns_stats**](CampaignApi.md#get_marketplace_seller_campaigns_stats) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns | 
[**get_marketplace_sellers**](CampaignApi.md#get_marketplace_sellers) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/sellers | 
[**get_marketplace_sellers_by_advertiser**](CampaignApi.md#get_marketplace_sellers_by_advertiser) | **POST** /2025-10/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers | 
[**get_marketplace_sellers_stats**](CampaignApi.md#get_marketplace_sellers_stats) | **GET** /2025-10/marketing-solutions/marketplace-performance-outcomes/stats/sellers | 
[**patch_ad_set_category_bids**](CampaignApi.md#patch_ad_set_category_bids) | **PATCH** /2025-10/marketing-solutions/ad-sets/{ad-set-id}/category-bids | 
[**patch_ad_sets**](CampaignApi.md#patch_ad_sets) | **PATCH** /2025-10/marketing-solutions/ad-sets | 
[**patch_campaigns**](CampaignApi.md#patch_campaigns) | **PATCH** /2025-10/marketing-solutions/campaigns | 
[**patch_display_multipliers**](CampaignApi.md#patch_display_multipliers) | **PATCH** /2025-10/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | 
[**search_ad_sets**](CampaignApi.md#search_ad_sets) | **POST** /2025-10/marketing-solutions/ad-sets/search | 
[**search_campaigns**](CampaignApi.md#search_campaigns) | **POST** /2025-10/marketing-solutions/campaigns/search | 
[**start_ad_sets**](CampaignApi.md#start_ad_sets) | **POST** /2025-10/marketing-solutions/ad-sets/start | 
[**stop_ad_sets**](CampaignApi.md#stop_ad_sets) | **POST** /2025-10/marketing-solutions/ad-sets/stop | 
[**update_ad_set_audience**](CampaignApi.md#update_ad_set_audience) | **PUT** /2025-10/marketing-solutions/ad-sets/{ad-set-id}/audience | 
[**update_marketplace_seller_budget**](CampaignApi.md#update_marketplace_seller_budget) | **PATCH** /2025-10/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} | 
[**update_marketplace_seller_budgets**](CampaignApi.md#update_marketplace_seller_budgets) | **PATCH** /2025-10/marketing-solutions/marketplace-performance-outcomes/budgets | 
[**update_marketplace_seller_campaign**](CampaignApi.md#update_marketplace_seller_campaign) | **PATCH** /2025-10/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} | 
[**update_marketplace_seller_campaigns**](CampaignApi.md#update_marketplace_seller_campaigns) | **PATCH** /2025-10/marketing-solutions/marketplace-performance-outcomes/seller-campaigns | 


# **create_ad_set**
> ResponseReadAdSetV24Q3 create_ad_set(create_ad_set_v24_q3_request)



Create the specified ad set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.response_read_ad_set_v24_q3 import ResponseReadAdSetV24Q3
from criteo_api_marketingsolutions_v2025_10.model.create_ad_set_v24_q3_request import CreateAdSetV24Q3Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_ad_set_v24_q3_request = CreateAdSetV24Q3Request(
        data=CreateAdSetV24Q3Resource(
            attributes=CreateAdSetV24Q3(
                attribution_configuration=CreateAdSetAttributionConfigurationV24Q3(
                    attribution_method="unknown",
                    lookback_window="unknown",
                ),
                bidding=CreateAdSetBiddingV24Q3(
                    bid_amount=3.14,
                    cost_controller="COS",
                ),
                budget=CreateAdSetBudgetV24Q3(
                    budget_amount=3.14,
                    budget_delivery_smoothing="accelerated",
                    budget_delivery_week="undefined",
                    budget_renewal="undefined",
                    budget_strategy="capped",
                ),
                campaign_id="campaign_id_example",
                dataset_id="dataset_id_example",
                media_type="display",
                name="name_example",
                objective="customAction",
                schedule=CreateAdSetScheduleV24Q3(
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                targeting=CreateAdSetTargetingV24Q3(
                    delivery_limitations=AdSetDeliveryLimitationsV24Q3(
                        devices=[
                            "other",
                        ],
                        environments=[
                            "web",
                        ],
                        operating_systems=[
                            "android",
                        ],
                    ),
                    frequency_capping=AdSetFrequencyCappingV24Q3(
                        frequency="hourly",
                        maximum_impressions=1,
                    ),
                    geo_location=CreateAdSetGeoLocationV24Q3(
                        countries=AdSetTargetingRuleV24Q3(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                        subdivisions=AdSetTargetingRuleV24Q3(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                        zip_codes=AdSetTargetingRuleV24Q3(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                    ),
                ),
                tracking_code="tracking_code_example",
            ),
            type="AdSet",
        ),
    ) # CreateAdSetV24Q3Request | the ad sets to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ad_set(create_ad_set_v24_q3_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->create_ad_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ad_set_v24_q3_request** | [**CreateAdSetV24Q3Request**](CreateAdSetV24Q3Request.md)| the ad sets to create |

### Return type

[**ResponseReadAdSetV24Q3**](ResponseReadAdSetV24Q3.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The ad set that has been created and errors / warnings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign**
> CampaignV23Q1Response create_campaign(create_campaign_request)



Create the specified campaign

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.campaign_v23_q1_response import CampaignV23Q1Response
from criteo_api_marketingsolutions_v2025_10.model.create_campaign_request import CreateCampaignRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_campaign_request = CreateCampaignRequest(
        data=CreateCampaignResource(
            attributes=CreateCampaign(
                advertiser_id="advertiser_id_example",
                budget_automation=BudgetAutomation(
                    budget_configuration=BudgetAutomationConfiguration(
                        ad_set_objectives="conversions",
                    ),
                    enabled=True,
                ),
                goal="Unspecified",
                name="name_example",
                spend_limit=CreateCampaignSpendLimit(
                    spend_limit_amount=3.14,
                    spend_limit_renewal="undefined",
                    spend_limit_type="capped",
                ),
            ),
            type="Campaign",
        ),
    ) # CreateCampaignRequest | the campaigns to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_campaign(create_campaign_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->create_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_campaign_request** | [**CreateCampaignRequest**](CreateCampaignRequest.md)| the campaigns to create |

### Return type

[**CampaignV23Q1Response**](CampaignV23Q1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The campaign that has been created and errors / warnings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_marketplace_seller_budgets**
> [SellerBudgetMessage] create_marketplace_seller_budgets(create_seller_budget_mapi_message)



Create one or more new budgets to enable spending with the given limitations.  All three types of budgets can be created this way.                The following constraints apply when creating a new budget.                • <b>sellerId</b>: the seller MUST be supplied<br />  • <b>campaignIds</b>: a non-empty array of campaign ids MUST be supplied<br />  • <b>budgetType</b>: a budget type MUST be supplied<br />  • <b>amount</b>: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative<br />  • <b>startDate</b>: a future start date MUST be supplied<br />  • <b>endDate</b>: an end date MAY be supplied and if supplied MUST be greater than the start date<br />                Other attributes MUST NOT be supplied.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from criteo_api_marketingsolutions_v2025_10.model.create_seller_budget_mapi_message import CreateSellerBudgetMapiMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_seller_budget_mapi_message = [
        CreateSellerBudgetMapiMessage(
            amount="amount_example",
            budget_type="budget_type_example",
            campaign_ids=[
                1,
            ],
            end_date="end_date_example",
            seller_id="seller_id_example",
            start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ] # [CreateSellerBudgetMapiMessage] | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.create_marketplace_seller_budgets(create_seller_budget_mapi_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->create_marketplace_seller_budgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_seller_budget_mapi_message** | [**[CreateSellerBudgetMapiMessage]**](CreateSellerBudgetMapiMessage.md)|  |

### Return type

[**[SellerBudgetMessage]**](SellerBudgetMessage.md)

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

# **create_marketplace_seller_campaigns_by_seller**
> SellerCampaignMessage create_marketplace_seller_campaigns_by_seller(seller_id, create_seller_campaign_message_mapi)



Associate an existing Seller with an existing Campaign allowing for budget creation

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from criteo_api_marketingsolutions_v2025_10.model.create_seller_campaign_message_mapi import CreateSellerCampaignMessageMapi
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_id = "sellerId_example" # str | Supply a generated Id of an existing Seller
    create_seller_campaign_message_mapi = CreateSellerCampaignMessageMapi(
        bid=3.14,
        campaign_id=1,
    ) # CreateSellerCampaignMessageMapi | Supply the campaign Id and bid to create the mapping

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.create_marketplace_seller_campaigns_by_seller(seller_id, create_seller_campaign_message_mapi)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->create_marketplace_seller_campaigns_by_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Supply a generated Id of an existing Seller |
 **create_seller_campaign_message_mapi** | [**CreateSellerCampaignMessageMapi**](CreateSellerCampaignMessageMapi.md)| Supply the campaign Id and bid to create the mapping |

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

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

# **get_ad_set**
> ResponseReadAdSetV24Q3 get_ad_set(ad_set_id)



Get the data for the specified ad set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.response_read_ad_set_v24_q3 import ResponseReadAdSetV24Q3
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the ad set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the ad set |

### Return type

[**ResponseReadAdSetV24Q3**](ResponseReadAdSetV24Q3.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the ad set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_set_category_bids**
> AdSetCategoryBidListResponse get_ad_set_category_bids(ad_set_id)



Get the Category Bids for all valid Categories associated to an Ad Set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.ad_set_category_bid_list_response import AdSetCategoryBidListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set_category_bids(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set_category_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |

### Return type

[**AdSetCategoryBidListResponse**](AdSetCategoryBidListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Category Bids for all valid Categories associated to an Ad Set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> CampaignV23Q1Response get_campaign(campaign_id)



Get the data for the specified campaign

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.campaign_v23_q1_response import CampaignV23Q1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | Id of the campaign

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Id of the campaign |

### Return type

[**CampaignV23Q1Response**](CampaignV23Q1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the campaign |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_display_multipliers**
> AdSetDisplayMultiplierListResponse get_display_multipliers(ad_set_id)



Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.ad_set_display_multiplier_list_response import AdSetDisplayMultiplierListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_display_multipliers(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_display_multipliers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |

### Return type

[**AdSetDisplayMultiplierListResponse**](AdSetDisplayMultiplierListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Display Multipliers for all valid Categories associated to an Ad Set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_ad_sets_by_advertiser**
> [AdvertiserAdsetMessage] get_marketplace_ad_sets_by_advertiser(advertiser_id)



Get the collection of adsets associated with the advertiserId.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.advertiser_adset_message import AdvertiserAdsetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_ad_sets_by_advertiser(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_ad_sets_by_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |

### Return type

[**[AdvertiserAdsetMessage]**](AdvertiserAdsetMessage.md)

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

# **get_marketplace_advertiser**
> AdvertiserInfoMessage get_marketplace_advertiser(advertiser_id)



Get an advertiser.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.advertiser_info_message import AdvertiserInfoMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_advertiser(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |

### Return type

[**AdvertiserInfoMessage**](AdvertiserInfoMessage.md)

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

# **get_marketplace_advertiser_preview_limits**
> [AdvertiserQuotaMessage] get_marketplace_advertiser_preview_limits()



Get the collection of advertisers preview limits associated with the authorized user.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.advertiser_quota_message import AdvertiserQuotaMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 
        api_response = api_instance.get_marketplace_advertiser_preview_limits()
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_advertiser_preview_limits: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AdvertiserQuotaMessage]**](AdvertiserQuotaMessage.md)

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

# **get_marketplace_advertisers**
> [AdvertiserInfoMessage] get_marketplace_advertisers()



Get the collection of advertisers associated with the user.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.advertiser_info_message import AdvertiserInfoMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 
        api_response = api_instance.get_marketplace_advertisers()
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_advertisers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AdvertiserInfoMessage]**](AdvertiserInfoMessage.md)

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

# **get_marketplace_budgets_by_advertiser**
> [SellerBudgetMessage] get_marketplace_budgets_by_advertiser(advertiser_id)



Get CRP budgets for a specific advertiser

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser
    budget_id = 1 # int | Return only budgets with given Id (optional)
    end_after_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
    seller_id = 1 # int | Return only budgets belonging to given sellerId (optional)
    start_before_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
    status = "Archived" # str | Return only budgets with the given status. (optional)
    type = "type_example" # str | Return only budgets with the given budget type. (optional)
    with_balance = True # bool | Return only budgets with the given status. (optional)
    with_spend = True # bool | Return budgets with any positive spend. (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_budgets_by_advertiser(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_budgets_by_advertiser: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_budgets_by_advertiser(advertiser_id, budget_id=budget_id, end_after_date=end_after_date, seller_id=seller_id, start_before_date=start_before_date, status=status, type=type, with_balance=with_balance, with_spend=with_spend)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_budgets_by_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |
 **budget_id** | **int**| Return only budgets with given Id | [optional]
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional]
 **seller_id** | **int**| Return only budgets belonging to given sellerId | [optional]
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional]
 **status** | **str**| Return only budgets with the given status. | [optional]
 **type** | **str**| Return only budgets with the given budget type. | [optional]
 **with_balance** | **bool**| Return only budgets with the given status. | [optional]
 **with_spend** | **bool**| Return budgets with any positive spend. | [optional]

### Return type

[**[SellerBudgetMessage]**](SellerBudgetMessage.md)

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

# **get_marketplace_budgets_by_seller**
> [SellerBudgetMessage] get_marketplace_budgets_by_seller(seller_id)



Return a collection of budgets for this seller filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used. See the budgets endpoint for additional details.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_id = "sellerId_example" # str | Return only budgets belonging to the given seller.
    campaign_id = 1 # int | Return only budgets that pay for a given campaign. (optional)
    end_after_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
    start_before_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
    status = "Archived" # str | Return only budgets with the given status. (optional)
    type = "type_example" # str | Return only budgets with the given budget type. (optional)
    with_balance = True # bool | Return only budgets with the given status. (optional)
    with_spend = True # bool | Return budgets with any positive spend. (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_budgets_by_seller(seller_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_budgets_by_seller: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_budgets_by_seller(seller_id, campaign_id=campaign_id, end_after_date=end_after_date, start_before_date=start_before_date, status=status, type=type, with_balance=with_balance, with_spend=with_spend)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_budgets_by_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Return only budgets belonging to the given seller. |
 **campaign_id** | **int**| Return only budgets that pay for a given campaign. | [optional]
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional]
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional]
 **status** | **str**| Return only budgets with the given status. | [optional]
 **type** | **str**| Return only budgets with the given budget type. | [optional]
 **with_balance** | **bool**| Return only budgets with the given status. | [optional]
 **with_spend** | **bool**| Return budgets with any positive spend. | [optional]

### Return type

[**[SellerBudgetMessage]**](SellerBudgetMessage.md)

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

# **get_marketplace_budgets_by_seller_campaign**
> [SellerBudgetMessage] get_marketplace_budgets_by_seller_campaign(seller_campaign_id)



Return a collection of budgets for this seller campaign filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used.                See the budgets endpoint for additional details.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_campaign_id = "sellerCampaignId_example" # str | Return only budgets belonging to the given seller campaign.
    end_after_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
    start_before_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
    status = "Archived" # str | Return only budgets with the given status. (optional)
    type = "type_example" # str | Return only budgets with the given budget type. (optional)
    with_balance = True # bool | Return only budgets with a positive balance. (optional)
    with_spend = True # bool | Return budgets with a positive spend. (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_budgets_by_seller_campaign(seller_campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_budgets_by_seller_campaign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_budgets_by_seller_campaign(seller_campaign_id, end_after_date=end_after_date, start_before_date=start_before_date, status=status, type=type, with_balance=with_balance, with_spend=with_spend)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_budgets_by_seller_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**| Return only budgets belonging to the given seller campaign. |
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional]
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional]
 **status** | **str**| Return only budgets with the given status. | [optional]
 **type** | **str**| Return only budgets with the given budget type. | [optional]
 **with_balance** | **bool**| Return only budgets with a positive balance. | [optional]
 **with_spend** | **bool**| Return budgets with a positive spend. | [optional]

### Return type

[**[SellerBudgetMessage]**](SellerBudgetMessage.md)

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

# **get_marketplace_campaigns_by_advertiser**
> [AdvertiserCampaignMessage] get_marketplace_campaigns_by_advertiser(advertiser_id)



Get the collection of CRP campaigns associated with the advertiserId.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.advertiser_campaign_message import AdvertiserCampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_campaigns_by_advertiser(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_campaigns_by_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |

### Return type

[**[AdvertiserCampaignMessage]**](AdvertiserCampaignMessage.md)

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

# **get_marketplace_campaigns_stats**
> str get_marketplace_campaigns_stats()



## Dimensions                Get performance statistics aggregated for _campaigns_. The campaign id appears  in the output as the first column.                Aggregation can be done by `hour`, `day`, `month`, or `year` aligned with the user timezone  if provided. The aggregation interval size is controlled by `intervalSize`. The time  interval appears in the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by campaign, date or count.                Filtering the results to events associated with a specific campaign is done by setting  the `campaignId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {     \"columns\": [ \"campaignId\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\" ],     \"data\": [         [168423, \"2019-05-01\", 3969032, 13410, 1111.295, 985, 190758099, 0.073, 1.128, 0.000, 171653.880 ],         [168423, \"2019-06-01\", 8479603, 25619, 2190.705, 740, 152783656, 0.028, 2.960, 0.000, 69741.775 ]         ],     \"rows\": 2  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  column comes first and consists of the campaign id.  The interval column comes next and defines the aggregation period.  The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Show only metrics for this advertiser. (optional)
    campaign_id = "campaignId_example" # str | Show only metrics for this campaign (default all campaigns) (optional)
    click_attribution_policy = "AnySeller" # str | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS (optional) if omitted the server will use the default value of "AnySeller"
    count = 1 # int | Return up to the first count rows of data (default is all rows) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter out all events that occur after date (default is today’s date) (optional)
    interval_size = "Day" # str | Specify the aggregation interval for events used to compute stats (default is \"day\") (optional) if omitted the server will use the default value of "Day"
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter out all events that occur before date (default is the value of `endDate`) (optional)
    time_zone_id = "timeZoneId_example" # str | Specify the timezone used in the aggregations (IANA code). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_campaigns_stats(advertiser_id=advertiser_id, campaign_id=campaign_id, click_attribution_policy=click_attribution_policy, count=count, end_date=end_date, interval_size=interval_size, start_date=start_date, time_zone_id=time_zone_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_campaigns_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Show only metrics for this advertiser. | [optional]
 **campaign_id** | **str**| Show only metrics for this campaign (default all campaigns) | [optional]
 **click_attribution_policy** | **str**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] if omitted the server will use the default value of "AnySeller"
 **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional]
 **end_date** | **datetime**| Filter out all events that occur after date (default is today’s date) | [optional]
 **interval_size** | **str**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] if omitted the server will use the default value of "Day"
 **start_date** | **datetime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional]
 **time_zone_id** | **str**| Specify the timezone used in the aggregations (IANA code). | [optional]

### Return type

**str**

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

# **get_marketplace_seller**
> SellerBase get_marketplace_seller(seller_id)



Return details for the selected seller. For example,                    {          \"id\" : \"123456\"          \"sellerName\": \"HBogart\",      }

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_base import SellerBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_id = "sellerId_example" # str | Id of the seller.

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_seller(seller_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Id of the seller. |

### Return type

[**SellerBase**](SellerBase.md)

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

# **get_marketplace_seller_ad_preview**
> str get_marketplace_seller_ad_preview(advertiser_id, seller_id)



Get a preview of an HTML ad with products belonging to the provided seller  • <b>advertiserId</b>: Valid crp advertiserId, seller belongs to provided advertiser<br />  • <b>sellerId</b>: Products from given SellerId will fill the ad preview, must be existing crp sellerId<br />  • <b>height</b>: height may be supplied to request a specific ad preview height. Default height: 250<br />  • <b>width</b>: width may be supplied to request a specific ad preview width. Default width: 300<br />                Ad preview api calls are capped to 1000 per day per advertiser by default. Current usage, limit, and period can be found using v2/crp/advertisers/preview-limit

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser
    seller_id = 1 # int | Id of the seller
    campaign_id = 1 # int | Seller CampaignId (optional)
    height = 1 # int | Height of the ad to display (optional)
    width = 1 # int | Width of the ad to display (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_seller_ad_preview(advertiser_id, seller_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_ad_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_seller_ad_preview(advertiser_id, seller_id, campaign_id=campaign_id, height=height, width=width)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_ad_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |
 **seller_id** | **int**| Id of the seller |
 **campaign_id** | **int**| Seller CampaignId | [optional]
 **height** | **int**| Height of the ad to display | [optional]
 **width** | **int**| Width of the ad to display | [optional]

### Return type

**str**

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

# **get_marketplace_seller_budget**
> SellerBudgetMessage get_marketplace_seller_budget(budget_id)



Return a budget. For example,                    {          \"id\": \"1759183\",          \"sellerId\": \"321392\",          \"campaignIds\": [              143962          ],          \"budgetType\": \"Capped\",          \"amount\": 1000,          \"startDate\": \"2021-01-11\",          \"endDate\": \"2021-01-12\",          \"spend\": null,          \"status\": \"Active\"      }                A budget limits the spend of a seller for one or more campaigns.                There are three types of budget:<br /><b>Uncapped</b> budgets put no limit on the total amount of spend.<br /><b>Capped</b> budgets limit the total spend to a fixed amount.<br /><b>Daily</b> budgets limit daily spend to a fixed amount.<br />                In addition, budgets can limit the spend to a specific range of dates using  the start and end date attributes. Finally a budget must be active to be used.                <b>Spend</b> approximates the current spend against this budget. There may be a lag  between when an ad is clicked and the time it accrues to the spend. Daily budgets  show spend against the most recent day only.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    budget_id = 1 # int | Id of the budget.

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_seller_budget(budget_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**| Id of the budget. |

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

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

# **get_marketplace_seller_budgets**
> [SellerBudgetMessage] get_marketplace_seller_budgets()



Return a collection of budgets filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used.                <b>Date filter.</b> Filtering can return only budgets that were active for a  date range by specifying the startBeforeDate and endAfterDate. Leaving off the startBeforeDate  value makes budgets with any startDate qualify, whereas when leaving off the endAfterDate value will only return  budgets whose endDate has not already passed. To get budgets that were active  on a specific date, set both values to that day.                <b>Spend.</b> If the endAfterDate is supplied, the spend excludes spend that  happened after that date. In the case of a daily budget, only the spend for  the final day is displayed.                See the budgets endpoint for additional details.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Return only budgets belonging to the specified advertiser (optional)
    campaign_id = 1 # int | Return only budgets that pay for a given campaign. (optional)
    end_after_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended. (optional)
    seller_id = "sellerId_example" # str | Return only budgets belonging to the given seller. (optional)
    start_before_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format. (optional)
    status = "Archived" # str | Return only budgets with the given status. (optional)
    type = "type_example" # str | Return only budgets with the given budget type. (optional)
    with_balance = True # bool | Return only budgets with the given status. (optional)
    with_spend = True # bool | Return budgets with any positive spend. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_seller_budgets(advertiser_id=advertiser_id, campaign_id=campaign_id, end_after_date=end_after_date, seller_id=seller_id, start_before_date=start_before_date, status=status, type=type, with_balance=with_balance, with_spend=with_spend)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_budgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Return only budgets belonging to the specified advertiser | [optional]
 **campaign_id** | **int**| Return only budgets that pay for a given campaign. | [optional]
 **end_after_date** | **datetime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional]
 **seller_id** | **str**| Return only budgets belonging to the given seller. | [optional]
 **start_before_date** | **datetime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional]
 **status** | **str**| Return only budgets with the given status. | [optional]
 **type** | **str**| Return only budgets with the given budget type. | [optional]
 **with_balance** | **bool**| Return only budgets with the given status. | [optional]
 **with_spend** | **bool**| Return budgets with any positive spend. | [optional]

### Return type

[**[SellerBudgetMessage]**](SellerBudgetMessage.md)

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

# **get_marketplace_seller_campaign**
> [SellerCampaignMessage] get_marketplace_seller_campaign(seller_campaign_id)



Return details for a seller campaign. For example,                    {          \"id\": \"543210.123456\",          \"sellerId\": \"543210\",          \"campaignId\": 123456,          \"bid\": 1.55,          \"suspendedSince\": \"2018-07-30T15:15:24.813\",          \"suspensionReasons\": [              \"NoMoreBudget\"          ]      }                An active seller campaign is one for which the value of <b>suspendedSince</b> is null and  the <b>bid</b> is positive. The currency of the bid is the <b>bidCurrency</b> of the  associated campaign.                Any active seller campaign must also have an active total (capped or uncapped) budget.  It may optionally have an active daily budget as well to further limit spending.                Suspension reasons:  - ManuallyStopped: The Seller-Campaign has been manually paused. This is not related to the other suspension reasons.  - NoBudgetDefined: No valid budget has been linked to the Seller-Campaign.  - NoCpcDefined: No CPC has been set for the Seller-Campaign.  - NoMoreBudget: The current budget of the Seller-Campaign has been exhausted.  - RemovedFromCatalog: All the products of the Seller-Campaign have been deleted from the catalog.  - NotYetStarted: The Seller-Campaign has just been created and has not yet been processed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_campaign_id = "sellerCampaignId_example" # str | Id of the seller campaign.

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_seller_campaign(seller_campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**| Id of the seller campaign. |

### Return type

[**[SellerCampaignMessage]**](SellerCampaignMessage.md)

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

# **get_marketplace_seller_campaigns**
> [SellerCampaignMessage] get_marketplace_seller_campaigns()



Return a collection of seller campaigns filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Return only seller belonging to the specified advertiser (optional)
    budget_status = "Archived" # str | Return only seller campaigns whose budget has the given status. (optional)
    campaign_id = 1 # int | Return only seller campaigns associated with the given campaign. (optional)
    seller_id = "sellerId_example" # str | Return only seller campaigns belonging to the given seller. (optional)
    seller_status = "Inactive" # str | Return only seller campaigns for sellers with the given status. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_seller_campaigns(advertiser_id=advertiser_id, budget_status=budget_status, campaign_id=campaign_id, seller_id=seller_id, seller_status=seller_status)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Return only seller belonging to the specified advertiser | [optional]
 **budget_status** | **str**| Return only seller campaigns whose budget has the given status. | [optional]
 **campaign_id** | **int**| Return only seller campaigns associated with the given campaign. | [optional]
 **seller_id** | **str**| Return only seller campaigns belonging to the given seller. | [optional]
 **seller_status** | **str**| Return only seller campaigns for sellers with the given status. | [optional]

### Return type

[**[SellerCampaignMessage]**](SellerCampaignMessage.md)

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

# **get_marketplace_seller_campaigns_by_advertiser**
> [SellerCampaignMessage] get_marketplace_seller_campaigns_by_advertiser(advertiser_id)



Get CRP seller campaigns for a specific advertiser

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_seller_campaigns_by_advertiser(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_campaigns_by_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |

### Return type

[**[SellerCampaignMessage]**](SellerCampaignMessage.md)

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

# **get_marketplace_seller_campaigns_by_seller**
> [SellerCampaignMessage] get_marketplace_seller_campaigns_by_seller(seller_id)



Return a collection of seller campaigns for this seller filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used. See the seller campaigns endpoint for additional details.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_id = "sellerId_example" # str | Return only seller campaigns belonging to the given seller.
    budget_status = "Archived" # str | Return only seller campaigns whose budget has the given status. (optional)
    campaign_id = 1 # int | Return only seller campaigns associated with the given campaign. (optional)
    seller_status = "Inactive" # str | Return only seller campaigns for sellers with the given status. (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_seller_campaigns_by_seller(seller_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_campaigns_by_seller: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_seller_campaigns_by_seller(seller_id, budget_status=budget_status, campaign_id=campaign_id, seller_status=seller_status)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_campaigns_by_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Return only seller campaigns belonging to the given seller. |
 **budget_status** | **str**| Return only seller campaigns whose budget has the given status. | [optional]
 **campaign_id** | **int**| Return only seller campaigns associated with the given campaign. | [optional]
 **seller_status** | **str**| Return only seller campaigns for sellers with the given status. | [optional]

### Return type

[**[SellerCampaignMessage]**](SellerCampaignMessage.md)

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

# **get_marketplace_seller_campaigns_stats**
> str get_marketplace_seller_campaigns_stats()



## Dimensions                Get performance statistics aggregated for _seller campaigns_.The campaign id, seller id, and  seller name appear in the first three columns of the output. These are followed by the interval  size column.                Aggregation can be done by `hour`, `day`, `month`, or `year` aligned with the user timezone if  provided. The aggregation interval size is controlled by `intervalSize`. The remaining columns  are metrics.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by date or count.                Filtering the results to events associated with a specific campaign is done by setting  the `campaignId` filter parameter to the desired value.                Filtering the results to events associated with a specific seller is done by setting  the `sellerId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {      \"columns\": [          \"campaignId\", \"sellerId\", \"sellerName\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\"      ],      \"data\": [          [168423, 1110222, \"118883955\", \"2019-05-01\", 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110222, \"118883955\", \"2019-06-01\", 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \"117980027\", \"2019-05-01\", 12502, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \"117980027\", \"2019-06-01\", 20266, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0]      ],      \"rows\": 4  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the campaign id, seller id, and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Show only metrics for this advertiser. (optional)
    campaign_id = "campaignId_example" # str | Show only metrics for this campaign (default all campaigns) (optional)
    click_attribution_policy = "AnySeller" # str | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS (optional) if omitted the server will use the default value of "AnySeller"
    count = 1 # int | Return up to the first count rows of data (default is all rows) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter out all events that occur after date (default is today’s date) (optional)
    interval_size = "Day" # str | Specify the aggregation interval for events used to compute stats (default is \"day\") (optional) if omitted the server will use the default value of "Day"
    seller_id = "sellerId_example" # str | Show only metrics for this seller (default all sellers) (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter out all events that occur before date (default is the value of `endDate`) (optional)
    time_zone_id = "timeZoneId_example" # str | Specify the timezone used in the aggregations (IANA code). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_seller_campaigns_stats(advertiser_id=advertiser_id, campaign_id=campaign_id, click_attribution_policy=click_attribution_policy, count=count, end_date=end_date, interval_size=interval_size, seller_id=seller_id, start_date=start_date, time_zone_id=time_zone_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_seller_campaigns_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Show only metrics for this advertiser. | [optional]
 **campaign_id** | **str**| Show only metrics for this campaign (default all campaigns) | [optional]
 **click_attribution_policy** | **str**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] if omitted the server will use the default value of "AnySeller"
 **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional]
 **end_date** | **datetime**| Filter out all events that occur after date (default is today’s date) | [optional]
 **interval_size** | **str**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] if omitted the server will use the default value of "Day"
 **seller_id** | **str**| Show only metrics for this seller (default all sellers) | [optional]
 **start_date** | **datetime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional]
 **time_zone_id** | **str**| Specify the timezone used in the aggregations (IANA code). | [optional]

### Return type

**str**

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

# **get_marketplace_sellers**
> [SellerBase] get_marketplace_sellers()



Return a collection of sellers filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_base import SellerBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Return only sellers belonging to the specified advertiser (optional)
    campaign_id = 1 # int | Return only sellers belonging to the specified campaign (optional)
    seller_name = "sellerName_example" # str | Return only sellers with the matching name. (optional)
    seller_status = "Inactive" # str | Return only sellers with specific status. (optional)
    with_budget_status = "Archived" # str | Return only sellers with specific budget status. (optional)
    with_products = True # bool | Return only sellers with or without products in catalog. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_sellers(advertiser_id=advertiser_id, campaign_id=campaign_id, seller_name=seller_name, seller_status=seller_status, with_budget_status=with_budget_status, with_products=with_products)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_sellers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Return only sellers belonging to the specified advertiser | [optional]
 **campaign_id** | **int**| Return only sellers belonging to the specified campaign | [optional]
 **seller_name** | **str**| Return only sellers with the matching name. | [optional]
 **seller_status** | **str**| Return only sellers with specific status. | [optional]
 **with_budget_status** | **str**| Return only sellers with specific budget status. | [optional]
 **with_products** | **bool**| Return only sellers with or without products in catalog. | [optional]

### Return type

[**[SellerBase]**](SellerBase.md)

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

# **get_marketplace_sellers_by_advertiser**
> [SellerBase] get_marketplace_sellers_by_advertiser(advertiser_id, request_body)



Create new sellers for an advertiser

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_base import SellerBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Id of the advertiser
    request_body = [
        "request_body_example",
    ] # [str] | Names of the sellers to associate with new Ids
    partner_id = 1 # int | Id of the partner (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_marketplace_sellers_by_advertiser(advertiser_id, request_body)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_sellers_by_advertiser: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_sellers_by_advertiser(advertiser_id, request_body, partner_id=partner_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_sellers_by_advertiser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Id of the advertiser |
 **request_body** | **[str]**| Names of the sellers to associate with new Ids |
 **partner_id** | **int**| Id of the partner | [optional]

### Return type

[**[SellerBase]**](SellerBase.md)

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

# **get_marketplace_sellers_stats**
> str get_marketplace_sellers_stats()



## Dimensions                Get performance statistics aggregated for _sellers_. The seller id appears  in the output in the first column and the seller name appears in the second.                Aggregation can be done by `hour`, `day`, `month`, or `year` aligned with the user timezone  if provided. The aggregation interval size is controlled by `intervalSize`. The time interval  appears in the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by seller id, date or count.                Filtering the results to events associated with a specific seller is done by setting  the `sellerId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {      \"columns\": [\"sellerId\", \"sellerName\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\"],      \"data\": [         [1200972, \"sellerA\", \"2019-05-01\", 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],         [1200972, \"sellerA\", \"2019-06-01\", 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],         [1200974, \"sellerB\", \"2019-05-01\", 10102, 47, 3.29, 3, 396000.0, 0.063, 1.096, 8.308E-6, 120364.741],         [1200974, \"sellerB\", \"2019-06-01\", 11576, 54, 3.78, 1, 132000.0, 0.018, 3.78, 2.863E-5, 34920.634]      ],      \"rows\": 4  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the seller id and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining metrics depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | Show only metrics for this advertiser. (optional)
    click_attribution_policy = "AnySeller" # str | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS (optional) if omitted the server will use the default value of "AnySeller"
    count = 1 # int | Return up to the first count rows of data (default is all rows) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter out all events that occur after date (default is today’s date) (optional)
    interval_size = "Day" # str | Specify the aggregation interval for events used to compute stats (default is \"day\") (optional) if omitted the server will use the default value of "Day"
    seller_id = "sellerId_example" # str | Show only metrics for this seller (default all sellers) (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter out all events that occur before date (default is the value of `endDate`) (optional)
    time_zone_id = "timeZoneId_example" # str | Specify the timezone used in the aggregations (IANA code). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_marketplace_sellers_stats(advertiser_id=advertiser_id, click_attribution_policy=click_attribution_policy, count=count, end_date=end_date, interval_size=interval_size, seller_id=seller_id, start_date=start_date, time_zone_id=time_zone_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->get_marketplace_sellers_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Show only metrics for this advertiser. | [optional]
 **click_attribution_policy** | **str**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] if omitted the server will use the default value of "AnySeller"
 **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional]
 **end_date** | **datetime**| Filter out all events that occur after date (default is today’s date) | [optional]
 **interval_size** | **str**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] if omitted the server will use the default value of "Day"
 **seller_id** | **str**| Show only metrics for this seller (default all sellers) | [optional]
 **start_date** | **datetime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional]
 **time_zone_id** | **str**| Specify the timezone used in the aggregations (IANA code). | [optional]

### Return type

**str**

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

# **patch_ad_set_category_bids**
> PatchAdSetCategoryBidResultListResponse patch_ad_set_category_bids(ad_set_id, patch_ad_set_category_bid_list_request)



Patch Category Bids for one or more Categories in a single request. Partial success policy is followed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.patch_ad_set_category_bid_result_list_response import PatchAdSetCategoryBidResultListResponse
from criteo_api_marketingsolutions_v2025_10.model.patch_ad_set_category_bid_list_request import PatchAdSetCategoryBidListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set
    patch_ad_set_category_bid_list_request = PatchAdSetCategoryBidListRequest(
        data=[
            PatchAdSetCategoryBidResource(
                attributes=PatchAdSetCategoryBid(
                    bid_amount=3.14,
                ),
                id="id_example",
                type="AdSetCategoryBid",
            ),
        ],
    ) # PatchAdSetCategoryBidListRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ad_set_category_bids(ad_set_id, patch_ad_set_category_bid_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->patch_ad_set_category_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |
 **patch_ad_set_category_bid_list_request** | [**PatchAdSetCategoryBidListRequest**](PatchAdSetCategoryBidListRequest.md)|  |

### Return type

[**PatchAdSetCategoryBidResultListResponse**](PatchAdSetCategoryBidResultListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of updated Category Bids for given Categories associated to an Ad Set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ad_sets**
> ResponsesAdSetIdV24Q3 patch_ad_sets(requests_patch_ad_set_v24_q3)



Patch a list of AdSets.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.requests_patch_ad_set_v24_q3 import RequestsPatchAdSetV24Q3
from criteo_api_marketingsolutions_v2025_10.model.responses_ad_set_id_v24_q3 import ResponsesAdSetIdV24Q3
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    requests_patch_ad_set_v24_q3 = RequestsPatchAdSetV24Q3(
        data=[
            WriteModelPatchAdSetV24Q3(
                attributes=PatchAdSetV24Q3(
                    attribution_configuration=PatchAdSetAttributionConfigurationV24Q3(
                        attribution_method="unknown",
                        lookback_window="unknown",
                    ),
                    bidding=PatchAdSetBiddingV24Q3(
                        bid_amount=NillableDecimal(
                            value=3.14,
                        ),
                    ),
                    budget=PatchAdSetBudgetV24Q3(
                        budget_amount=NillableDecimal(
                            value=3.14,
                        ),
                        budget_delivery_smoothing="accelerated",
                        budget_delivery_week="undefined",
                        budget_renewal="undefined",
                        budget_strategy="capped",
                    ),
                    name="name_example",
                    scheduling=PatchAdSetSchedulingV24Q3(
                        end_date=NillableDateTime(
                            value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                        start_date=NillableDateTime(
                            value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                    ),
                    targeting=AdSetTargetingV24Q3(
                        delivery_limitations=AdSetDeliveryLimitationsV24Q3(
                            devices=[
                                "other",
                            ],
                            environments=[
                                "web",
                            ],
                            operating_systems=[
                                "android",
                            ],
                        ),
                        frequency_capping=AdSetTargetingV24Q3FrequencyCapping(
                            value=AdSetFrequencyCappingV24Q3(
                                frequency="hourly",
                                maximum_impressions=1,
                            ),
                        ),
                        geo_location=AdSetGeoLocationV24Q3(
                            countries=NillableAdSetTargetingRuleV24Q3(
                                value=NillableAdSetTargetingRuleV24Q3Value(),
                            ),
                            subdivisions=NillableAdSetTargetingRuleV24Q3(
                                value=NillableAdSetTargetingRuleV24Q3Value(),
                            ),
                            zip_codes=NillableAdSetTargetingRuleV24Q3(
                                value=NillableAdSetTargetingRuleV24Q3Value(),
                            ),
                        ),
                    ),
                ),
                id="id_example",
                type="PatchAdSetV24Q3",
            ),
        ],
    ) # RequestsPatchAdSetV24Q3 | List of adsets to patch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ad_sets(requests_patch_ad_set_v24_q3)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->patch_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_patch_ad_set_v24_q3** | [**RequestsPatchAdSetV24Q3**](RequestsPatchAdSetV24Q3.md)| List of adsets to patch. |

### Return type

[**ResponsesAdSetIdV24Q3**](ResponsesAdSetIdV24Q3.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of patched adSets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_campaigns**
> PatchResultCampaignListResponse patch_campaigns(patch_campaign_list_request)



Patch a list of Campaigns.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from criteo_api_marketingsolutions_v2025_10.model.patch_campaign_list_request import PatchCampaignListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    patch_campaign_list_request = PatchCampaignListRequest(
        data=[
            PatchCampaignWriteResource(
                attributes=PatchCampaign(
                    budget_automation=PatchMarketingCampaignBudgetAutomation(
                        budget_configuration=BudgetAutomationConfiguration(
                            ad_set_objectives="conversions",
                        ),
                        enabled=True,
                    ),
                    spend_limit=PatchCampaignSpendLimit(
                        spend_limit_amount=NillableDecimal(
                            value=3.14,
                        ),
                        spend_limit_renewal="undefined",
                        spend_limit_type="capped",
                    ),
                ),
                id="id_example",
                type="Campaign",
            ),
        ],
    ) # PatchCampaignListRequest | List of campaigns to patch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_campaigns(patch_campaign_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->patch_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_campaign_list_request** | [**PatchCampaignListRequest**](PatchCampaignListRequest.md)| List of campaigns to patch. |

### Return type

[**PatchResultCampaignListResponse**](PatchResultCampaignListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of patched campaigns. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_display_multipliers**
> PatchAdSetDisplayMultiplierResultListResponse patch_display_multipliers(ad_set_id, patch_ad_set_display_multiplier_list_request)



Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.patch_ad_set_display_multiplier_result_list_response import PatchAdSetDisplayMultiplierResultListResponse
from criteo_api_marketingsolutions_v2025_10.model.patch_ad_set_display_multiplier_list_request import PatchAdSetDisplayMultiplierListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set
    patch_ad_set_display_multiplier_list_request = PatchAdSetDisplayMultiplierListRequest(
        data=[
            PatchAdSetDisplayMultiplierResource(
                attributes=PatchAdSetDisplayMultiplier(
                    display_multiplier=3.14,
                ),
                id="id_example",
                type="AdSetDisplayMultiplier",
            ),
        ],
    ) # PatchAdSetDisplayMultiplierListRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_display_multipliers(ad_set_id, patch_ad_set_display_multiplier_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->patch_display_multipliers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |
 **patch_ad_set_display_multiplier_list_request** | [**PatchAdSetDisplayMultiplierListRequest**](PatchAdSetDisplayMultiplierListRequest.md)|  |

### Return type

[**PatchAdSetDisplayMultiplierResultListResponse**](PatchAdSetDisplayMultiplierResultListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of updated Display Multipliers for given Categories associated to an Ad Set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ad_sets**
> ResponsesReadAdSetV24Q3 search_ad_sets()



Search for ad sets

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.ad_set_search_request_v24_q3 import AdSetSearchRequestV24Q3
from criteo_api_marketingsolutions_v2025_10.model.responses_read_ad_set_v24_q3 import ResponsesReadAdSetV24Q3
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_search_request_v24_q3 = AdSetSearchRequestV24Q3(
        filters=AdSetSearchFilterV24Q3(
            ad_set_ids=[
                "ad_set_ids_example",
            ],
            advertiser_ids=[
                "advertiser_ids_example",
            ],
            campaign_ids=[
                "campaign_ids_example",
            ],
        ),
    ) # AdSetSearchRequestV24Q3 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_ad_sets(ad_set_search_request_v24_q3=ad_set_search_request_v24_q3)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->search_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_search_request_v24_q3** | [**AdSetSearchRequestV24Q3**](AdSetSearchRequestV24Q3.md)|  | [optional]

### Return type

[**ResponsesReadAdSetV24Q3**](ResponsesReadAdSetV24Q3.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the ad sets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_campaigns**
> CampaignV23Q1ListResponse search_campaigns()



Search for campaigns

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.campaign_search_request_v23_q1 import CampaignSearchRequestV23Q1
from criteo_api_marketingsolutions_v2025_10.model.campaign_v23_q1_list_response import CampaignV23Q1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_search_request_v23_q1 = CampaignSearchRequestV23Q1(
        filters=CampaignSearchFiltersV23Q1(
            advertiser_ids=[
                "advertiser_ids_example",
            ],
            campaign_ids=[
                "campaign_ids_example",
            ],
        ),
    ) # CampaignSearchRequestV23Q1 | filters on campaigns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_campaigns(campaign_search_request_v23_q1=campaign_search_request_v23_q1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->search_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_search_request_v23_q1** | [**CampaignSearchRequestV23Q1**](CampaignSearchRequestV23Q1.md)| filters on campaigns | [optional]

### Return type

[**CampaignV23Q1ListResponse**](CampaignV23Q1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the campaigns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ad_sets**
> ResponsesAdSetId start_ad_sets()



Start the specified list of ad sets

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2025_10.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    requests_ad_set_id = RequestsAdSetId(
        data=[
            WriteModelAdSetId(
                id="id_example",
                type="AdSetId",
            ),
        ],
    ) # RequestsAdSetId | All the ad sets to start (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.start_ad_sets(requests_ad_set_id=requests_ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->start_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_ad_set_id** | [**RequestsAdSetId**](RequestsAdSetId.md)| All the ad sets to start | [optional]

### Return type

[**ResponsesAdSetId**](ResponsesAdSetId.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ad sets that have been started and errors / warnings by ad set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_ad_sets**
> ResponsesAdSetId stop_ad_sets()



Stop the specified list of ad sets

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2025_10.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    requests_ad_set_id = RequestsAdSetId(
        data=[
            WriteModelAdSetId(
                id="id_example",
                type="AdSetId",
            ),
        ],
    ) # RequestsAdSetId | All the ad sets to stop (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.stop_ad_sets(requests_ad_set_id=requests_ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->stop_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_ad_set_id** | [**RequestsAdSetId**](RequestsAdSetId.md)| All the ad sets to stop | [optional]

### Return type

[**ResponsesAdSetId**](ResponsesAdSetId.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ad sets that have been stopped and errors / warnings by ad set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ad_set_audience**
> AdSetAudienceLinkEntityV1Response update_ad_set_audience(ad_set_id, ad_set_audience_link_input_entity_v1)



Link or unlink an audience with an ad set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.ad_set_audience_link_entity_v1_response import AdSetAudienceLinkEntityV1Response
from criteo_api_marketingsolutions_v2025_10.model.ad_set_audience_link_input_entity_v1 import AdSetAudienceLinkInputEntityV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | The ad set ID.
    ad_set_audience_link_input_entity_v1 = AdSetAudienceLinkInputEntityV1(
        data=AdSetAudienceLinkEntityV1Resource(
            attributes=AdSetAudienceLinkEntityV1(
                audience_id="audience_id_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AdSetAudienceLinkInputEntityV1 | Ad set-Audience update request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ad_set_audience(ad_set_id, ad_set_audience_link_input_entity_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->update_ad_set_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| The ad set ID. |
 **ad_set_audience_link_input_entity_v1** | [**AdSetAudienceLinkInputEntityV1**](AdSetAudienceLinkInputEntityV1.md)| Ad set-Audience update request. |

### Return type

[**AdSetAudienceLinkEntityV1Response**](AdSetAudienceLinkEntityV1Response.md)

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

# **update_marketplace_seller_budget**
> SellerBudgetMessage update_marketplace_seller_budget(budget_id, update_seller_budget_message_base)



Modify an existing active budget to change its limitations or status.  All three types of budgets can be modified.                See the additional restrictions listed in the PATCH budgets endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from criteo_api_marketingsolutions_v2025_10.model.update_seller_budget_message_base import UpdateSellerBudgetMessageBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    budget_id = 1 # int | Id of the budget
    update_seller_budget_message_base = UpdateSellerBudgetMessageBase(
        amount="amount_example",
        campaign_ids=[
            1,
        ],
        end_date="end_date_example",
        is_suspended=True,
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # UpdateSellerBudgetMessageBase | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.update_marketplace_seller_budget(budget_id, update_seller_budget_message_base)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->update_marketplace_seller_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**| Id of the budget |
 **update_seller_budget_message_base** | [**UpdateSellerBudgetMessageBase**](UpdateSellerBudgetMessageBase.md)|  |

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

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

# **update_marketplace_seller_budgets**
> [SellerBudgetMessage] update_marketplace_seller_budgets(update_seller_budget_message)



Modify one or more existing active budgets to change their limitations or status.  All three types of budgets can be modified.                The following constraints apply when modifying an existing budget.                • <b>campaignIds</b>: a non-empty subset of the original campaign ids MAY be supplied<br />  • <b>amount</b>: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative<br />  • <b>startDate</b>: a future start date MAY be supplied for budgets that have not yet started<br />  • <b>endDate</b>: an end date MAY be supplied and if supplied MUST be a future date greater than the start date<br />                Other attributes MUST NOT be supplied.                Adding new campaigns to a budget is not allowed. In addition, reducing the amount for  a Capped budget to a value less than the current spend not allowed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_budget_message import SellerBudgetMessage
from criteo_api_marketingsolutions_v2025_10.model.update_seller_budget_message import UpdateSellerBudgetMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    update_seller_budget_message = [
        UpdateSellerBudgetMessage(
            amount="amount_example",
            budget_id=1,
            campaign_ids=[
                1,
            ],
            end_date="end_date_example",
            is_suspended=True,
            start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ] # [UpdateSellerBudgetMessage] | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.update_marketplace_seller_budgets(update_seller_budget_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->update_marketplace_seller_budgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_seller_budget_message** | [**[UpdateSellerBudgetMessage]**](UpdateSellerBudgetMessage.md)|  |

### Return type

[**[SellerBudgetMessage]**](SellerBudgetMessage.md)

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

# **update_marketplace_seller_campaign**
> SellerCampaignMessage update_marketplace_seller_campaign(seller_campaign_id)



Patching a seller campaign allows the bid to be modified. The bid must be a non-negative value.  Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_campaign_id = "sellerCampaignId_example" # str | Id of the existing seller campaign to update
    bid = 3.14 # float | The new bid for the seller campaign. (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.update_marketplace_seller_campaign(seller_campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->update_marketplace_seller_campaign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.update_marketplace_seller_campaign(seller_campaign_id, bid=bid)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->update_marketplace_seller_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_id** | **str**| Id of the existing seller campaign to update |
 **bid** | **float**| The new bid for the seller campaign. | [optional]

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

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

# **update_marketplace_seller_campaigns**
> [SellerCampaignMessage] update_marketplace_seller_campaigns(seller_campaign_update)



Patching a collection of seller campaigns allows their bids to be modified.  Each bid must be a non-negative value. Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import campaign_api
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_message import SellerCampaignMessage
from criteo_api_marketingsolutions_v2025_10.model.seller_campaign_update import SellerCampaignUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    seller_campaign_update = [
        SellerCampaignUpdate(
            bid=3.14,
            id="id_example",
        ),
    ] # [SellerCampaignUpdate] | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.update_marketplace_seller_campaigns(seller_campaign_update)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling CampaignApi->update_marketplace_seller_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_campaign_update** | [**[SellerCampaignUpdate]**](SellerCampaignUpdate.md)|  |

### Return type

[**[SellerCampaignMessage]**](SellerCampaignMessage.md)

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

