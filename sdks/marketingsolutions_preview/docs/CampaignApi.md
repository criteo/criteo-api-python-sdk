# criteo_api_marketingsolutions_preview.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ad_set_v24_q1**](CampaignApi.md#create_ad_set_v24_q1) | **POST** /preview/marketing-solutions/ad-sets | 
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /preview/marketing-solutions/campaigns | 
[**delete_advertiser_bundle_rules**](CampaignApi.md#delete_advertiser_bundle_rules) | **DELETE** /preview/advertisers/{advertiserId}/targeting/bundle-rules | 
[**delete_advertiser_domain_rules**](CampaignApi.md#delete_advertiser_domain_rules) | **DELETE** /preview/advertisers/{advertiserId}/targeting/domain-rules | 
[**delete_campaign_bundle_rules**](CampaignApi.md#delete_campaign_bundle_rules) | **DELETE** /preview/campaigns/{campaignId}/targeting/bundle-rules | 
[**delete_campaign_domain_rules**](CampaignApi.md#delete_campaign_domain_rules) | **DELETE** /preview/campaigns/{campaignId}/targeting/domain-rules | 
[**delete_oc_ibrand_safety_rule**](CampaignApi.md#delete_oc_ibrand_safety_rule) | **DELETE** /preview/brand-safety/oci | 
[**delete_oc_itargeting_rule**](CampaignApi.md#delete_oc_itargeting_rule) | **DELETE** /preview/targeting/oci | 
[**disable_ad_set_targeting_deal_ids**](CampaignApi.md#disable_ad_set_targeting_deal_ids) | **POST** /preview/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable | 
[**disable_ad_set_targeting_video_positioning**](CampaignApi.md#disable_ad_set_targeting_video_positioning) | **POST** /preview/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable | 
[**get_ad_set_targeting_deal_ids**](CampaignApi.md#get_ad_set_targeting_deal_ids) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids | 
[**get_ad_set_targeting_video_positioning**](CampaignApi.md#get_ad_set_targeting_video_positioning) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning | 
[**get_ad_set_v24_q1**](CampaignApi.md#get_ad_set_v24_q1) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id} | 
[**get_advertiser_bundle_rules**](CampaignApi.md#get_advertiser_bundle_rules) | **GET** /preview/advertisers/{advertiserId}/targeting/bundle-rules | 
[**get_advertiser_domain_rules**](CampaignApi.md#get_advertiser_domain_rules) | **GET** /preview/advertisers/{advertiserId}/targeting/domain-rules | 
[**get_campaign_bundle_rules**](CampaignApi.md#get_campaign_bundle_rules) | **GET** /preview/campaigns/{campaignId}/targeting/bundle-rules | 
[**get_campaign_domain_rules**](CampaignApi.md#get_campaign_domain_rules) | **GET** /preview/campaigns/{campaignId}/targeting/domain-rules | 
[**get_campaign_v23_q1**](CampaignApi.md#get_campaign_v23_q1) | **GET** /preview/marketing-solutions/campaigns/{campaign-id} | 
[**get_category_bid_list**](CampaignApi.md#get_category_bid_list) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id}/category-bids | 
[**get_display_multipliers**](CampaignApi.md#get_display_multipliers) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | 
[**get_oc_ibrand_safety_rule**](CampaignApi.md#get_oc_ibrand_safety_rule) | **GET** /preview/brand-safety/oci | 
[**get_oc_itargeting_rule**](CampaignApi.md#get_oc_itargeting_rule) | **GET** /preview/targeting/oci | 
[**get_supply_vendor_list**](CampaignApi.md#get_supply_vendor_list) | **GET** /preview/marketing-solutions/ad-sets/targeting/supply-vendors | 
[**patch_ad_sets_v24_q1**](CampaignApi.md#patch_ad_sets_v24_q1) | **PATCH** /preview/marketing-solutions/ad-sets | 
[**patch_campaigns**](CampaignApi.md#patch_campaigns) | **PATCH** /preview/marketing-solutions/campaigns | 
[**patch_category_bid_list**](CampaignApi.md#patch_category_bid_list) | **PATCH** /preview/marketing-solutions/ad-sets/{ad-set-id}/category-bids | 
[**patch_display_multipliers**](CampaignApi.md#patch_display_multipliers) | **PATCH** /preview/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | 
[**post_advertiser_bundle_rules**](CampaignApi.md#post_advertiser_bundle_rules) | **POST** /preview/advertisers/{advertiserId}/targeting/bundle-rules | 
[**post_advertiser_domain_rules**](CampaignApi.md#post_advertiser_domain_rules) | **POST** /preview/advertisers/{advertiserId}/targeting/domain-rules | 
[**post_campaign_bundle_rules**](CampaignApi.md#post_campaign_bundle_rules) | **POST** /preview/campaigns/{campaignId}/targeting/bundle-rules | 
[**post_campaign_domain_rules**](CampaignApi.md#post_campaign_domain_rules) | **POST** /preview/campaigns/{campaignId}/targeting/domain-rules | 
[**put_advertiser_bundle_rules**](CampaignApi.md#put_advertiser_bundle_rules) | **PUT** /preview/advertisers/{advertiserId}/targeting/bundle-rules | 
[**put_advertiser_domain_rules**](CampaignApi.md#put_advertiser_domain_rules) | **PUT** /preview/advertisers/{advertiserId}/targeting/domain-rules | 
[**put_campaign_bundle_rules**](CampaignApi.md#put_campaign_bundle_rules) | **PUT** /preview/campaigns/{campaignId}/targeting/bundle-rules | 
[**put_campaign_domain_rules**](CampaignApi.md#put_campaign_domain_rules) | **PUT** /preview/campaigns/{campaignId}/targeting/domain-rules | 
[**search_ad_sets_v24_q1**](CampaignApi.md#search_ad_sets_v24_q1) | **POST** /preview/marketing-solutions/ad-sets/search | 
[**search_campaigns_v23_q1**](CampaignApi.md#search_campaigns_v23_q1) | **POST** /preview/marketing-solutions/campaigns/search | 
[**set_ad_set_targeting_deal_ids**](CampaignApi.md#set_ad_set_targeting_deal_ids) | **PUT** /preview/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids | 
[**set_ad_set_targeting_video_positioning**](CampaignApi.md#set_ad_set_targeting_video_positioning) | **PUT** /preview/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning | 
[**start_ad_sets**](CampaignApi.md#start_ad_sets) | **POST** /preview/marketing-solutions/ad-sets/start | 
[**stop_ad_sets**](CampaignApi.md#stop_ad_sets) | **POST** /preview/marketing-solutions/ad-sets/stop | 
[**update_ad_set_audience**](CampaignApi.md#update_ad_set_audience) | **PUT** /preview/marketing-solutions/ad-sets/{ad-set-id}/audience | 
[**upsert_oc_ibrand_safety_rule**](CampaignApi.md#upsert_oc_ibrand_safety_rule) | **POST** /preview/brand-safety/oci | 
[**upsert_oc_itargeting_rule**](CampaignApi.md#upsert_oc_itargeting_rule) | **POST** /preview/targeting/oci | 


# **create_ad_set_v24_q1**
> ResponseReadAdSetV24Q1 create_ad_set_v24_q1(create_ad_set_v24_q1_request)



Create the specified ad set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.response_read_ad_set_v24_q1 import ResponseReadAdSetV24Q1
from criteo_api_marketingsolutions_preview.model.create_ad_set_v24_q1_request import CreateAdSetV24Q1Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_ad_set_v24_q1_request = CreateAdSetV24Q1Request(
        data=CreateAdSetV24Q1Resource(
            attributes=CreateAdSetV24Q1(
                name="name_example",
                dataset_id="dataset_id_example",
                campaign_id="campaign_id_example",
                objective="customAction",
                schedule=CreateAdSetScheduleV24Q1(
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                bidding=CreateAdSetBiddingV24Q1(
                    bid_amount=3.14,
                    cost_controller="COS",
                ),
                targeting=CreateAdSetTargetingV24Q1(
                    delivery_limitations=AdSetDeliveryLimitationsV24Q1(
                        environments=[
                            "web",
                        ],
                        devices=[
                            "other",
                        ],
                        operating_systems=[
                            "android",
                        ],
                    ),
                    geo_location=CreateAdSetGeoLocationV24Q1(
                        countries=AdSetTargetingRuleV24Q1(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                        subdivisions=AdSetTargetingRuleV24Q1(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                        zip_codes=AdSetTargetingRuleV24Q1(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                    ),
                    frequency_capping=AdSetFrequencyCappingV24Q1(
                        frequency="hourly",
                        maximum_impressions=1,
                    ),
                ),
                budget=CreateAdSetBudgetV24Q1(
                    budget_strategy="capped",
                    budget_renewal="undefined",
                    budget_delivery_smoothing="accelerated",
                    budget_delivery_week="undefined",
                    budget_amount=3.14,
                ),
                tracking_code="tracking_code_example",
                media_type="display",
            ),
            type="AdSet",
        ),
    ) # CreateAdSetV24Q1Request | the ad sets to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ad_set_v24_q1(create_ad_set_v24_q1_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->create_ad_set_v24_q1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ad_set_v24_q1_request** | [**CreateAdSetV24Q1Request**](CreateAdSetV24Q1Request.md)| the ad sets to create |

### Return type

[**ResponseReadAdSetV24Q1**](ResponseReadAdSetV24Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The ad set that has been created and errors / warnings |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign**
> CampaignV23Q1Response create_campaign(create_campaign_request)



Create the specified campaign

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.campaign_v23_q1_response import CampaignV23Q1Response
from criteo_api_marketingsolutions_preview.model.create_campaign_request import CreateCampaignRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_campaign_request = CreateCampaignRequest(
        data=CreateCampaignResource(
            attributes=CreateCampaign(
                name="name_example",
                advertiser_id="advertiser_id_example",
                goal="Unspecified",
                spend_limit=CreateCampaignSpendLimit(
                    spend_limit_type="capped",
                    spend_limit_renewal="undefined",
                    spend_limit_amount=3.14,
                ),
            ),
            type="Campaign",
        ),
    ) # CreateCampaignRequest | the campaigns to create

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_campaign(create_campaign_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The campaign that has been created and errors / warnings |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_advertiser_bundle_rules**
> ApiResponseOfTargetingEntity delete_advertiser_bundle_rules(advertiser_id)



Removes some bundles from the current list of targeted bundles for a given advertiser.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to delete from the list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_advertiser_bundle_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_advertiser_bundle_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_advertiser_bundle_rules(advertiser_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_advertiser_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_advertiser_domain_rules**
> ApiResponseOfTargetingEntity delete_advertiser_domain_rules(advertiser_id)



Removes some domains from the current list of targeted domains for a given advertiser.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to delete from the list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_advertiser_domain_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_advertiser_domain_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_advertiser_domain_rules(advertiser_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_advertiser_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_bundle_rules**
> ApiResponseOfTargetingEntity delete_campaign_bundle_rules(campaign_id)



Removes some bundles from the current list of targeted bundles for a given campaign.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to delete from the list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_campaign_bundle_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_campaign_bundle_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_campaign_bundle_rules(campaign_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_campaign_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_domain_rules**
> ApiResponseOfTargetingEntity delete_campaign_domain_rules(campaign_id)



Removes some domains from the current list of targeted domains for a given campaign.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to delete from the list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_campaign_domain_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_campaign_domain_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_campaign_domain_rules(campaign_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_campaign_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oc_ibrand_safety_rule**
> delete_oc_ibrand_safety_rule(target_type, target_id)



Delete OCI brand-safety rule.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.target_type import TargetType
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_response import OciBrandSafetyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    target_type = TargetType("Campaign") # TargetType | Defines a target for a rule.
    target_id = 1 # int | Unique target identifier.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_oc_ibrand_safety_rule(target_type, target_id)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_oc_ibrand_safety_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type** | **TargetType**| Defines a target for a rule. |
 **target_id** | **int**| Unique target identifier. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Rule deleted |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oc_itargeting_rule**
> delete_oc_itargeting_rule(target_type, target_id)



Delete OCI targeting rule.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.target_type import TargetType
from criteo_api_marketingsolutions_preview.model.oci_targeting_response import OciTargetingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    target_type = TargetType("Campaign") # TargetType | Defines a target for a rule.
    target_id = 1 # int | Unique target identifier.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_oc_itargeting_rule(target_type, target_id)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_oc_itargeting_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type** | **TargetType**| Defines a target for a rule. |
 **target_id** | **int**| Unique target identifier. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Rule deleted |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_ad_set_targeting_deal_ids**
> AdSetTargetingDealIdsDisableResultResponse disable_ad_set_targeting_deal_ids(ad_set_id)



Disable the Deal Id Targeting configuration for the ad set whose id is specified

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_deal_ids_disable_result_response import AdSetTargetingDealIdsDisableResultResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.disable_ad_set_targeting_deal_ids(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->disable_ad_set_targeting_deal_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |

### Return type

[**AdSetTargetingDealIdsDisableResultResponse**](AdSetTargetingDealIdsDisableResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the errors/warnings if any |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_ad_set_targeting_video_positioning**
> AdSetTargetingVideoPositioningDisableResultResponse disable_ad_set_targeting_video_positioning(ad_set_id)



Disable the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_video_positioning_disable_result_response import AdSetTargetingVideoPositioningDisableResultResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.disable_ad_set_targeting_video_positioning(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->disable_ad_set_targeting_video_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |

### Return type

[**AdSetTargetingVideoPositioningDisableResultResponse**](AdSetTargetingVideoPositioningDisableResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the errors/warnings if any |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_set_targeting_deal_ids**
> AdSetTargetingDealIdsResponse get_ad_set_targeting_deal_ids(ad_set_id)



Get the Deal Id Targeting configuration for the ad set whose id is specified

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_deal_ids_response import AdSetTargetingDealIdsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set_targeting_deal_ids(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set_targeting_deal_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |

### Return type

[**AdSetTargetingDealIdsResponse**](AdSetTargetingDealIdsResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Deal Id Targeting configuration |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_set_targeting_video_positioning**
> AdSetTargetingVideoPositioningResponse get_ad_set_targeting_video_positioning(ad_set_id)



Get the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_video_positioning_response import AdSetTargetingVideoPositioningResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set_targeting_video_positioning(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set_targeting_video_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |

### Return type

[**AdSetTargetingVideoPositioningResponse**](AdSetTargetingVideoPositioningResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Video Positioning Targeting configuration |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_set_v24_q1**
> ResponseReadAdSetV24Q1 get_ad_set_v24_q1(ad_set_id)



Get the data for the specified ad set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.response_read_ad_set_v24_q1 import ResponseReadAdSetV24Q1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the ad set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set_v24_q1(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set_v24_q1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the ad set |

### Return type

[**ResponseReadAdSetV24Q1**](ResponseReadAdSetV24Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the ad set |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_bundle_rules**
> ApiResponseOfTargetingEntity get_advertiser_bundle_rules(advertiser_id)



Returns a list of all targeted bundles for an advertiser.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_bundle_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_advertiser_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_domain_rules**
> ApiResponseOfTargetingEntity get_advertiser_domain_rules(advertiser_id)



Returns a list of all targeted domains for an advertiser.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_domain_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_advertiser_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_bundle_rules**
> ApiResponseOfTargetingEntity get_campaign_bundle_rules(campaign_id)



Returns a list of all targeted bundles for a campaign.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign_bundle_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_domain_rules**
> ApiResponseOfTargetingEntity get_campaign_domain_rules(campaign_id)



Returns a list of all targeted domains for a campaign.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign_domain_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_v23_q1**
> CampaignV23Q1Response get_campaign_v23_q1(campaign_id)



Get the data for the specified campaign

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.campaign_v23_q1_response import CampaignV23Q1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | Id of the campaign

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign_v23_q1(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign_v23_q1: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the campaign |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_bid_list**
> AdSetCategoryBidListResponse get_category_bid_list(ad_set_id)



Get the Category Bids for all valid Categories associated to an Ad Set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_category_bid_list_response import AdSetCategoryBidListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_category_bid_list(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_category_bid_list: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Category Bids for all valid Categories associated to an Ad Set. |  -  |
**401** | The API client is not properly authenticated. |  -  |
**400** | Bad Request |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_display_multipliers**
> AdSetDisplayMultiplierListResponse get_display_multipliers(ad_set_id)



Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_display_multiplier_list_response import AdSetDisplayMultiplierListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_display_multipliers(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
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
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Display Multipliers for all valid Categories associated to an Ad Set. |  -  |
**401** | The API client is not properly authenticated. |  -  |
**400** | Bad Request |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oc_ibrand_safety_rule**
> OciBrandSafetyResponse get_oc_ibrand_safety_rule(target_type, target_id)



Get OCI brand-safety rule for the specified target

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.target_type import TargetType
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_response import OciBrandSafetyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    target_type = TargetType("Campaign") # TargetType | Defines a target for a rule.
    target_id = 1 # int | Unique target identifier.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_oc_ibrand_safety_rule(target_type, target_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_oc_ibrand_safety_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type** | **TargetType**| Defines a target for a rule. |
 **target_id** | **int**| Unique target identifier. |

### Return type

[**OciBrandSafetyResponse**](OciBrandSafetyResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rule found |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oc_itargeting_rule**
> OciTargetingResponse get_oc_itargeting_rule(target_type, target_id)



Get OCI targeting rule for specified target.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.target_type import TargetType
from criteo_api_marketingsolutions_preview.model.oci_targeting_response import OciTargetingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    target_type = TargetType("Campaign") # TargetType | Defines a target for a rule.
    target_id = 1 # int | Unique target identifier.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_oc_itargeting_rule(target_type, target_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_oc_itargeting_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type** | **TargetType**| Defines a target for a rule. |
 **target_id** | **int**| Unique target identifier. |

### Return type

[**OciTargetingResponse**](OciTargetingResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rule found |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supply_vendor_list**
> SupplyVendorListResponse get_supply_vendor_list()



Fetch the list of available supply vendors for any Ad Set targetings

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.supply_vendor_list_response import SupplyVendorListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_supply_vendor_list()
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_supply_vendor_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SupplyVendorListResponse**](SupplyVendorListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the errors/warnings if any |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ad_sets_v24_q1**
> ResponsesAdSetIdV24Q1 patch_ad_sets_v24_q1()



Patch a list of AdSets.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.responses_ad_set_id_v24_q1 import ResponsesAdSetIdV24Q1
from criteo_api_marketingsolutions_preview.model.requests_patch_ad_set_v24_q1 import RequestsPatchAdSetV24Q1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    requests_patch_ad_set_v24_q1 = RequestsPatchAdSetV24Q1(
        data=[
            WriteModelPatchAdSetV24Q1(
                id="id_example",
                type="PatchAdSetV24Q1",
                attributes=PatchAdSetV24Q1(
                    name="name_example",
                    scheduling=PatchAdSetSchedulingV24Q1(
                        start_date=NillableDateTime(
                            value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                        end_date=NillableDateTime(
                            value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                    ),
                    bidding=PatchAdSetBiddingV24Q1(
                        bid_amount=NillableDecimal(
                            value=3.14,
                        ),
                    ),
                    targeting=AdSetTargetingV24Q1(
                        delivery_limitations=AdSetDeliveryLimitationsV24Q1(
                            environments=[
                                "web",
                            ],
                            devices=[
                                "other",
                            ],
                            operating_systems=[
                                "android",
                            ],
                        ),
                        geo_location=AdSetGeoLocationV24Q1(
                            countries=NillableAdSetTargetingRuleV24Q1(
                                value=NillableAdSetTargetingRuleV24Q1Value(),
                            ),
                            subdivisions=NillableAdSetTargetingRuleV24Q1(
                                value=NillableAdSetTargetingRuleV24Q1Value(),
                            ),
                            zip_codes=NillableAdSetTargetingRuleV24Q1(
                                value=NillableAdSetTargetingRuleV24Q1Value(),
                            ),
                        ),
                        frequency_capping=AdSetFrequencyCappingV24Q1(
                            frequency="hourly",
                            maximum_impressions=1,
                        ),
                    ),
                    budget=PatchAdSetBudgetV24Q1(
                        budget_strategy="capped",
                        budget_renewal="undefined",
                        budget_delivery_smoothing="accelerated",
                        budget_delivery_week="undefined",
                        budget_amount=NillableDecimal(
                            value=3.14,
                        ),
                    ),
                ),
            ),
        ],
    ) # RequestsPatchAdSetV24Q1 | List of adsets to patch. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_ad_sets_v24_q1(requests_patch_ad_set_v24_q1=requests_patch_ad_set_v24_q1)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_ad_sets_v24_q1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_patch_ad_set_v24_q1** | [**RequestsPatchAdSetV24Q1**](RequestsPatchAdSetV24Q1.md)| List of adsets to patch. | [optional]

### Return type

[**ResponsesAdSetIdV24Q1**](ResponsesAdSetIdV24Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of patched adSets. |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_campaigns**
> PatchResultCampaignListResponse patch_campaigns()



Patch a list of Campaigns.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from criteo_api_marketingsolutions_preview.model.patch_campaign_list_request import PatchCampaignListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    patch_campaign_list_request = PatchCampaignListRequest(
        data=[
            PatchCampaignWriteResource(
                id="id_example",
                type="Campaign",
                attributes=PatchCampaign(
                    spend_limit=PatchCampaignSpendLimit(
                        spend_limit_type="capped",
                        spend_limit_renewal="undefined",
                        spend_limit_amount=NillableDecimal(
                            value=3.14,
                        ),
                    ),
                ),
            ),
        ],
    ) # PatchCampaignListRequest | List of campaigns to patch. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_campaigns(patch_campaign_list_request=patch_campaign_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_campaign_list_request** | [**PatchCampaignListRequest**](PatchCampaignListRequest.md)| List of campaigns to patch. | [optional]

### Return type

[**PatchResultCampaignListResponse**](PatchResultCampaignListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of patched campaigns. |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_category_bid_list**
> PatchAdSetCategoryBidResultListResponse patch_category_bid_list(ad_set_id)



Patch Category Bids for one or more Categories in a single request. Partial success policy is followed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid_result_list_response import PatchAdSetCategoryBidResultListResponse
from criteo_api_marketingsolutions_preview.model.patch_ad_set_category_bid_list_request import PatchAdSetCategoryBidListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    ) # PatchAdSetCategoryBidListRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_category_bid_list(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_category_bid_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_category_bid_list(ad_set_id, patch_ad_set_category_bid_list_request=patch_ad_set_category_bid_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_category_bid_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |
 **patch_ad_set_category_bid_list_request** | [**PatchAdSetCategoryBidListRequest**](PatchAdSetCategoryBidListRequest.md)|  | [optional]

### Return type

[**PatchAdSetCategoryBidResultListResponse**](PatchAdSetCategoryBidResultListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of updated Category Bids for given Categories associated to an Ad Set. |  -  |
**401** | The API client is not properly authenticated. |  -  |
**400** | Bad Request |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_display_multipliers**
> PatchAdSetDisplayMultiplierResultListResponse patch_display_multipliers(ad_set_id)



Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier_list_request import PatchAdSetDisplayMultiplierListRequest
from criteo_api_marketingsolutions_preview.model.patch_ad_set_display_multiplier_result_list_response import PatchAdSetDisplayMultiplierResultListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    ) # PatchAdSetDisplayMultiplierListRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_display_multipliers(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_display_multipliers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_display_multipliers(ad_set_id, patch_ad_set_display_multiplier_list_request=patch_ad_set_display_multiplier_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_display_multipliers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |
 **patch_ad_set_display_multiplier_list_request** | [**PatchAdSetDisplayMultiplierListRequest**](PatchAdSetDisplayMultiplierListRequest.md)|  | [optional]

### Return type

[**PatchAdSetDisplayMultiplierResultListResponse**](PatchAdSetDisplayMultiplierResultListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of updated Display Multipliers for given Categories associated to an Ad Set. |  -  |
**401** | The API client is not properly authenticated. |  -  |
**400** | Bad Request |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_advertiser_bundle_rules**
> ApiResponseOfTargetingEntity post_advertiser_bundle_rules(advertiser_id)



Inserts a list of targeted bundles for an advertiser and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Description of the targeting rule to setup (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_advertiser_bundle_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_advertiser_bundle_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_advertiser_bundle_rules(advertiser_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_advertiser_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_advertiser_domain_rules**
> ApiResponseOfTargetingEntity post_advertiser_domain_rules(advertiser_id)



Inserts a list of targeted domains for an advertiser and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Description of the targeting rule to setup (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_advertiser_domain_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_advertiser_domain_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_advertiser_domain_rules(advertiser_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_advertiser_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

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

# **post_campaign_bundle_rules**
> ApiResponseOfTargetingEntity post_campaign_bundle_rules(campaign_id)



Inserts a list of targeted bundles for a campaign and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Description of the targeting rule to setup (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_campaign_bundle_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_campaign_bundle_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_campaign_bundle_rules(campaign_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_campaign_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_campaign_domain_rules**
> ApiResponseOfTargetingEntity post_campaign_domain_rules(campaign_id)



Inserts a list of targeted domains for a campaign and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Description of the targeting rule to setup (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_campaign_domain_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_campaign_domain_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_campaign_domain_rules(campaign_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_campaign_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_advertiser_bundle_rules**
> ApiResponseOfTargetingEntity put_advertiser_bundle_rules(advertiser_id)



Updates the targeted bundles for an advertiser by adding a list of bundles to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_advertiser_bundle_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_advertiser_bundle_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_advertiser_bundle_rules(advertiser_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_advertiser_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_advertiser_domain_rules**
> ApiResponseOfTargetingEntity put_advertiser_domain_rules(advertiser_id)



Updates the targeted domains for an advertiser by adding a list of domains to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_advertiser_domain_rules(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_advertiser_domain_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_advertiser_domain_rules(advertiser_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_advertiser_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_campaign_bundle_rules**
> ApiResponseOfTargetingEntity put_campaign_bundle_rules(campaign_id)



Updates the targeted bundles for a campaign by adding a list of bundles to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_campaign_bundle_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_campaign_bundle_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_campaign_bundle_rules(campaign_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_campaign_bundle_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_campaign_domain_rules**
> ApiResponseOfTargetingEntity put_campaign_domain_rules(campaign_id)



Updates the targeted domains for a campaign by adding a list of domains to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.api_request_of_targeting_entity import ApiRequestOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_response_of_targeting_entity import ApiResponseOfTargetingEntity
from criteo_api_marketingsolutions_preview.model.api_error_response import ApiErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="DOMAIN",
                mode="BLOCKLIST",
                data=[
                    EntityFilter(
                        value="value_example",
                        read_only=True,
                        active=True,
                    ),
                ],
            ),
        ),
    ) # ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_campaign_domain_rules(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_campaign_domain_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_campaign_domain_rules(campaign_id, api_request_of_targeting_entity=api_request_of_targeting_entity)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_campaign_domain_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id |
 **api_request_of_targeting_entity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | [optional]

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ad_sets_v24_q1**
> ResponsesReadAdSetV24Q1 search_ad_sets_v24_q1()



Search for ad sets

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_search_request_v24_q1 import AdSetSearchRequestV24Q1
from criteo_api_marketingsolutions_preview.model.responses_read_ad_set_v24_q1 import ResponsesReadAdSetV24Q1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_search_request_v24_q1 = AdSetSearchRequestV24Q1(
        filters=AdSetSearchFilterV24Q1(
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
    ) # AdSetSearchRequestV24Q1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_ad_sets_v24_q1(ad_set_search_request_v24_q1=ad_set_search_request_v24_q1)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_ad_sets_v24_q1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_search_request_v24_q1** | [**AdSetSearchRequestV24Q1**](AdSetSearchRequestV24Q1.md)|  | [optional]

### Return type

[**ResponsesReadAdSetV24Q1**](ResponsesReadAdSetV24Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the ad sets |  -  |
**400** | Bad Request |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |
**401** | The API client is not properly authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_campaigns_v23_q1**
> CampaignV23Q1ListResponse search_campaigns_v23_q1()



Search for campaigns

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.campaign_v23_q1_list_response import CampaignV23Q1ListResponse
from criteo_api_marketingsolutions_preview.model.campaign_search_request_v23_q1 import CampaignSearchRequestV23Q1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_search_request_v23_q1 = CampaignSearchRequestV23Q1(
        filters=CampaignSearchFiltersV23Q1(
            campaign_ids=[
                "campaign_ids_example",
            ],
            advertiser_ids=[
                "advertiser_ids_example",
            ],
        ),
    ) # CampaignSearchRequestV23Q1 | filters on campaigns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_campaigns_v23_q1(campaign_search_request_v23_q1=campaign_search_request_v23_q1)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_campaigns_v23_q1: %s\n" % e)
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the campaigns |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | The API client is not properly authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ad_set_targeting_deal_ids**
> AdSetTargetingDealIdsSetResultResponse set_ad_set_targeting_deal_ids(ad_set_id)



Set the Deal Id Targeting configuration for the ad set whose id is specified

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.set_ad_set_targeting_deal_ids_request import SetAdSetTargetingDealIdsRequest
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_deal_ids_set_result_response import AdSetTargetingDealIdsSetResultResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set
    set_ad_set_targeting_deal_ids_request = SetAdSetTargetingDealIdsRequest(
        data=SetAdSetTargetingDealIdsResource(
            type="type_example",
            attributes=SetAdSetTargetingDealIds(
                deal_ids=[
                    DealId(
                        deal_identifier="deal_identifier_example",
                        supply_vendor_id="supply_vendor_id_example",
                    ),
                ],
            ),
        ),
    ) # SetAdSetTargetingDealIdsRequest | the new Deal Id Targeting configuration (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_ad_set_targeting_deal_ids(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_ad_set_targeting_deal_ids: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_ad_set_targeting_deal_ids(ad_set_id, set_ad_set_targeting_deal_ids_request=set_ad_set_targeting_deal_ids_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_ad_set_targeting_deal_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |
 **set_ad_set_targeting_deal_ids_request** | [**SetAdSetTargetingDealIdsRequest**](SetAdSetTargetingDealIdsRequest.md)| the new Deal Id Targeting configuration | [optional]

### Return type

[**AdSetTargetingDealIdsSetResultResponse**](AdSetTargetingDealIdsSetResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the errors/warnings if any |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ad_set_targeting_video_positioning**
> AdSetTargetingVideoPositioningSetResultResponse set_ad_set_targeting_video_positioning(ad_set_id)



Set the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.set_ad_set_targeting_video_positioning_request import SetAdSetTargetingVideoPositioningRequest
from criteo_api_marketingsolutions_preview.model.ad_set_targeting_video_positioning_set_result_response import AdSetTargetingVideoPositioningSetResultResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "ad-set-id_example" # str | Id of the Ad Set
    set_ad_set_targeting_video_positioning_request = SetAdSetTargetingVideoPositioningRequest(
        data=SetAdSetTargetingVideoPositioningResource(
            type="type_example",
            attributes=SetAdSetTargetingVideoPositioning(
                video_placement=[
                    "InBanner",
                ],
                playback_method=[
                    "AutoSoundOn",
                ],
                skippable="Required",
                video_in_stream_position=[
                    "PreRoll",
                ],
                video_player_size=[
                    "Small",
                ],
                video_aspect_ratio=[
                    "Horizontal",
                ],
            ),
        ),
    ) # SetAdSetTargetingVideoPositioningRequest | the new Video Positioning Targeting configuration (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_ad_set_targeting_video_positioning(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_ad_set_targeting_video_positioning: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_ad_set_targeting_video_positioning(ad_set_id, set_ad_set_targeting_video_positioning_request=set_ad_set_targeting_video_positioning_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_ad_set_targeting_video_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the Ad Set |
 **set_ad_set_targeting_video_positioning_request** | [**SetAdSetTargetingVideoPositioningRequest**](SetAdSetTargetingVideoPositioningRequest.md)| the new Video Positioning Targeting configuration | [optional]

### Return type

[**AdSetTargetingVideoPositioningSetResultResponse**](AdSetTargetingVideoPositioningSetResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the errors/warnings if any |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ad_sets**
> ResponsesAdSetId start_ad_sets()



Start the specified list of ad sets

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_preview.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ad sets that have been started and errors / warnings by ad set |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_ad_sets**
> ResponsesAdSetId stop_ad_sets()



Stop the specified list of ad sets

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_preview.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ad sets that have been stopped and errors / warnings by ad set |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ad_set_audience**
> AdSetAudienceLinkEntityV1Response update_ad_set_audience(ad_set_id, ad_set_audience_link_input_entity_v1)



Link or unlink an audience with an ad set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.ad_set_audience_link_entity_v1_response import AdSetAudienceLinkEntityV1Response
from criteo_api_marketingsolutions_preview.model.ad_set_audience_link_input_entity_v1 import AdSetAudienceLinkInputEntityV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_oc_ibrand_safety_rule**
> OciBrandSafetyResponse upsert_oc_ibrand_safety_rule(oci_brand_safety_rule)



Create or update a new or replace existing OCI brand-safety rule.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_rule import OciBrandSafetyRule
from criteo_api_marketingsolutions_preview.model.oci_brand_safety_response import OciBrandSafetyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    oci_brand_safety_rule = OciBrandSafetyRule(
        target=Target(
            type=TargetType("Campaign"),
            id=1,
        ),
        blacklisted=[
            OciBrandSafetySegment("gv_adult"),
        ],
    ) # OciBrandSafetyRule | OCI brand-safety rule input

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.upsert_oc_ibrand_safety_rule(oci_brand_safety_rule)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->upsert_oc_ibrand_safety_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oci_brand_safety_rule** | [**OciBrandSafetyRule**](OciBrandSafetyRule.md)| OCI brand-safety rule input |

### Return type

[**OciBrandSafetyResponse**](OciBrandSafetyResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rule created |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_oc_itargeting_rule**
> OciTargetingResponse upsert_oc_itargeting_rule(oci_targeting_rule)



Create or update new or update existing OCI targeting rule.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.oci_targeting_rule import OciTargetingRule
from criteo_api_marketingsolutions_preview.model.oci_targeting_response import OciTargetingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    oci_targeting_rule = OciTargetingRule(
        target=Target(
            type=TargetType("Campaign"),
            id=1,
        ),
        rule=OciTargetingNode(
            operator=TargetingOperator("Or"),
            value="value_example",
            children=[
                OciTargetingNode(),
            ],
        ),
    ) # OciTargetingRule | OCI targeting rule input

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.upsert_oc_itargeting_rule(oci_targeting_rule)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->upsert_oc_itargeting_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oci_targeting_rule** | [**OciTargetingRule**](OciTargetingRule.md)| OCI targeting rule input |

### Return type

[**OciTargetingResponse**](OciTargetingResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rule created |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

