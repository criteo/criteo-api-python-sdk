# criteo_api_marketingsolutions_preview.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ad_set**](CampaignApi.md#create_ad_set) | **POST** /preview/marketing-solutions/ad-sets | 
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /preview/marketing-solutions/campaigns | 
[**delete_advertiser_bundle_rules**](CampaignApi.md#delete_advertiser_bundle_rules) | **DELETE** /preview/advertisers/{advertiserId}/targeting/bundle-rules | 
[**delete_advertiser_domain_rules**](CampaignApi.md#delete_advertiser_domain_rules) | **DELETE** /preview/advertisers/{advertiserId}/targeting/domain-rules | 
[**delete_campaign_bundle_rules**](CampaignApi.md#delete_campaign_bundle_rules) | **DELETE** /preview/campaigns/{campaignId}/targeting/bundle-rules | 
[**delete_campaign_domain_rules**](CampaignApi.md#delete_campaign_domain_rules) | **DELETE** /preview/campaigns/{campaignId}/targeting/domain-rules | 
[**delete_oc_ibrand_safety_rule**](CampaignApi.md#delete_oc_ibrand_safety_rule) | **DELETE** /preview/brand-safety/oci | 
[**delete_oc_itargeting_rule**](CampaignApi.md#delete_oc_itargeting_rule) | **DELETE** /preview/targeting/oci | 
[**get_ad_set**](CampaignApi.md#get_ad_set) | **GET** /preview/marketing-solutions/ad-sets/{adSetId} | 
[**get_advertiser_bundle_rules**](CampaignApi.md#get_advertiser_bundle_rules) | **GET** /preview/advertisers/{advertiserId}/targeting/bundle-rules | 
[**get_advertiser_domain_rules**](CampaignApi.md#get_advertiser_domain_rules) | **GET** /preview/advertisers/{advertiserId}/targeting/domain-rules | 
[**get_campaign**](CampaignApi.md#get_campaign) | **GET** /preview/marketing-solutions/campaigns/{campaign-id} | 
[**get_campaign_bundle_rules**](CampaignApi.md#get_campaign_bundle_rules) | **GET** /preview/campaigns/{campaignId}/targeting/bundle-rules | 
[**get_campaign_domain_rules**](CampaignApi.md#get_campaign_domain_rules) | **GET** /preview/campaigns/{campaignId}/targeting/domain-rules | 
[**get_category_bid_list**](CampaignApi.md#get_category_bid_list) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id}/category-bids | 
[**get_display_multipliers**](CampaignApi.md#get_display_multipliers) | **GET** /preview/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | 
[**get_oc_ibrand_safety_rule**](CampaignApi.md#get_oc_ibrand_safety_rule) | **GET** /preview/brand-safety/oci | 
[**get_oc_itargeting_rule**](CampaignApi.md#get_oc_itargeting_rule) | **GET** /preview/targeting/oci | 
[**patch_ad_sets**](CampaignApi.md#patch_ad_sets) | **PATCH** /preview/marketing-solutions/ad-sets | 
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
[**search_ad_sets**](CampaignApi.md#search_ad_sets) | **POST** /preview/marketing-solutions/ad-sets/search | 
[**search_campaigns**](CampaignApi.md#search_campaigns) | **POST** /preview/marketing-solutions/campaigns/search | 
[**start_ad_sets**](CampaignApi.md#start_ad_sets) | **POST** /preview/marketing-solutions/ad-sets/start | 
[**stop_ad_sets**](CampaignApi.md#stop_ad_sets) | **POST** /preview/marketing-solutions/ad-sets/stop | 
[**upsert_oc_ibrand_safety_rule**](CampaignApi.md#upsert_oc_ibrand_safety_rule) | **POST** /preview/brand-safety/oci | 
[**upsert_oc_itargeting_rule**](CampaignApi.md#upsert_oc_itargeting_rule) | **POST** /preview/targeting/oci | 


# **create_ad_set**
> ResponseReadAdSet create_ad_set()



Create the specified ad set

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.response_read_ad_set import ResponseReadAdSet
from criteo_api_marketingsolutions_preview.model.create_ad_set_request import CreateAdSetRequest
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_ad_set_request = CreateAdSetRequest(
        data=CreateAdSetResource(
            attributes=CreateAdSet(
                name="name_example",
                dataset_id="dataset_id_example",
                campaign_id="campaign_id_example",
                schedule=CreateAdSetSchedule(
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                bidding=CreateAdSetBidding(
                    bid_amount=3.14,
                    bid_strategy="actions",
                    cost_controller="COS",
                ),
                targeting=CreateAdSetTargeting(
                    delivery_limitations=AdSetDeliveryLimitations(
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
                    geo_location=CreateAdSetGeoLocation(
                        countries=AdSetTargetingRule(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                        subdivisions=AdSetTargetingRule(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                        zip_codes=AdSetTargetingRule(
                            operand="undefined",
                            values=[
                                "values_example",
                            ],
                        ),
                    ),
                    frequency_capping=AdSetFrequencyCapping(
                        frequency="hourly",
                        maximum_impressions=1,
                    ),
                ),
                budget=CreateAdSetBudget(
                    budget_strategy="capped",
                    budget_renewal="undefined",
                    budget_delivery_smoothing="accelerated",
                    budget_delivery_week="undefined",
                    budget_amount=3.14,
                ),
                audience_configuration=CreateAdSetAudienceConfiguration(
                    min_days_since_last_visit=1,
                    max_days_since_last_visit=1,
                    excluded_audience_ids=[
                        "excluded_audience_ids_example",
                    ],
                    audience_website_visitor=AudienceWebsiteVisitor(
                        visitor_types=[
                            "nonVisitor",
                        ],
                    ),
                    audience_custom=AudienceCustom(
                        audience_name="audience_name_example",
                        included_audience_ids=[
                            "included_audience_ids_example",
                        ],
                        visitor_types=[
                            "nonVisitor",
                        ],
                    ),
                ),
                tracking_code="tracking_code_example",
                media_type="display",
            ),
            type="AdSet",
        ),
    ) # CreateAdSetRequest | the ad sets to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ad_set(create_ad_set_request=create_ad_set_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->create_ad_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ad_set_request** | [**CreateAdSetRequest**](CreateAdSetRequest.md)| the ad sets to create | [optional]

### Return type

[**ResponseReadAdSet**](ResponseReadAdSet.md)

### Authorization

[oauth](../README.md#oauth)

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
> CampaignResponse create_campaign()



Create the specified campaign

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.campaign_response import CampaignResponse
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    create_campaign_request = CreateCampaignRequest(
        data=CreateCampaignResource(
            attributes=CreateCampaign(
                name="name_example",
                advertiser_id="advertiser_id_example",
                objective="objective_example",
                spend_limit=CreateCampaignSpendLimit(
                    spend_limit_type="capped",
                    spend_limit_renewal="undefined",
                    spend_limit_amount=3.14,
                ),
            ),
            type="Campaign",
        ),
    ) # CreateCampaignRequest | the campaigns to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_campaign(create_campaign_request=create_campaign_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->create_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_campaign_request** | [**CreateCampaignRequest**](CreateCampaignRequest.md)| the campaigns to create | [optional]

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

# **get_ad_set**
> ResponseReadAdSet get_ad_set(ad_set_id)



Get the data for the specified ad set

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.response_read_ad_set import ResponseReadAdSet
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "adSetId_example" # str | Id of the ad set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the ad set |

### Return type

[**ResponseReadAdSet**](ResponseReadAdSet.md)

### Authorization

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

# **get_campaign**
> CampaignResponse get_campaign(campaign_id)



Get the data for the specified campaign

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.campaign_response import CampaignResponse
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | Id of the campaign

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Id of the campaign |

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[oauth](../README.md#oauth)

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

# **get_campaign_bundle_rules**
> ApiResponseOfTargetingEntity get_campaign_bundle_rules(campaign_id)



Returns a list of all targeted bundles for a campaign.

### Example

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

# **get_category_bid_list**
> AdSetCategoryBidListResponse get_category_bid_list(ad_set_id)



Get the Category Bids for all valid Categories associated to an Ad Set

### Example

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

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Category Bids for all valid Categories associated to an Ad Set. |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_display_multipliers**
> AdSetDisplayMultiplierListResponse get_display_multipliers(ad_set_id)



Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

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

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Display Multipliers for all valid Categories associated to an Ad Set. |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oc_ibrand_safety_rule**
> OciBrandSafetyResponse get_oc_ibrand_safety_rule(target_type, target_id)



Get OCI brand-safety rule for the specified target

### Example

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

# **patch_ad_sets**
> ResponseAdSetId patch_ad_sets()



Patch a list of AdSets.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.response_ad_set_id import ResponseAdSetId
from criteo_api_marketingsolutions_preview.model.requests_patch_ad_set import RequestsPatchAdSet
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    requests_patch_ad_set = RequestsPatchAdSet(
        data=[
            WriteModelPatchAdSet(
                id="id_example",
                type="PatchAdSet",
                attributes=PatchAdSet(
                    name="name_example",
                    scheduling=PatchAdSetScheduling(
                        start_date=NillableDateTime(
                            value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                        end_date=NillableDateTime(
                            value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                    ),
                    bidding=PatchAdSetBidding(
                        bid_amount=NillableDecimal(
                            value=3.14,
                        ),
                    ),
                    targeting=AdSetTargeting(
                        delivery_limitations=AdSetDeliveryLimitations(
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
                        geo_location=AdSetGeoLocation(
                            countries=NillableAdSetTargetingRule(
                                value=AdSetTargetingRule(
                                    operand="undefined",
                                    values=[
                                        "values_example",
                                    ],
                                ),
                            ),
                            subdivisions=NillableAdSetTargetingRule(
                                value=AdSetTargetingRule(
                                    operand="undefined",
                                    values=[
                                        "values_example",
                                    ],
                                ),
                            ),
                            zip_codes=NillableAdSetTargetingRule(
                                value=AdSetTargetingRule(
                                    operand="undefined",
                                    values=[
                                        "values_example",
                                    ],
                                ),
                            ),
                        ),
                        frequency_capping=AdSetFrequencyCapping(
                            frequency="hourly",
                            maximum_impressions=1,
                        ),
                    ),
                    budget=PatchAdSetBudget(
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
    ) # RequestsPatchAdSet | List of adsets to patch. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_ad_sets(requests_patch_ad_set=requests_patch_ad_set)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->patch_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_patch_ad_set** | [**RequestsPatchAdSet**](RequestsPatchAdSet.md)| List of adsets to patch. | [optional]

### Return type

[**ResponseAdSetId**](ResponseAdSetId.md)

### Authorization

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of updated Category Bids for given Categories associated to an Ad Set. |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_display_multipliers**
> PatchAdSetDisplayMultiplierResultListResponse patch_display_multipliers(ad_set_id)



Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

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

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of updated Display Multipliers for given Categories associated to an Ad Set. |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource or the resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_advertiser_bundle_rules**
> ApiResponseOfTargetingEntity post_advertiser_bundle_rules(advertiser_id)



Inserts a list of targeted bundles for an advertiser and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    advertiser_id = 1 # int | The advertiser id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | The campaign id
    api_request_of_targeting_entity = ApiRequestOfTargetingEntity(
        data=EntityWrapperOfTargetingEntity(
            type="type_example",
            attributes=TargetingEntity(
                type="type_example",
                mode="mode_example",
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

[oauth](../README.md#oauth)

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

# **search_ad_sets**
> ResponsesReadAdSet search_ad_sets()



Search for ad sets

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.responses_read_ad_set import ResponsesReadAdSet
from criteo_api_marketingsolutions_preview.model.request_ad_set_search import RequestAdSetSearch
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    request_ad_set_search = RequestAdSetSearch(
        filters=AdSetSearchFilter(
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
    ) # RequestAdSetSearch |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_ad_sets(request_ad_set_search=request_ad_set_search)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_ad_set_search** | [**RequestAdSetSearch**](RequestAdSetSearch.md)|  | [optional]

### Return type

[**ResponsesReadAdSet**](ResponsesReadAdSet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the ad sets |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_campaigns**
> CampaignListResponse search_campaigns()



Search for campaigns

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import campaign_api
from criteo_api_marketingsolutions_preview.model.campaign_search_request import CampaignSearchRequest
from criteo_api_marketingsolutions_preview.model.campaign_list_response import CampaignListResponse
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

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_search_request = CampaignSearchRequest(
        filters=CampaignSearchFilters(
            campaign_ids=[
                "campaign_ids_example",
            ],
            advertiser_ids=[
                "advertiser_ids_example",
            ],
        ),
    ) # CampaignSearchRequest | filters on campaigns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_campaigns(campaign_search_request=campaign_search_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CampaignApi->search_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_search_request** | [**CampaignSearchRequest**](CampaignSearchRequest.md)| filters on campaigns | [optional]

### Return type

[**CampaignListResponse**](CampaignListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data for the campaigns |  -  |
**400** | Bad Request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ad_sets**
> ResponsesAdSetId start_ad_sets()



Start the specified list of ad sets

### Example

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

# **upsert_oc_ibrand_safety_rule**
> OciBrandSafetyResponse upsert_oc_ibrand_safety_rule(oci_brand_safety_rule)



Create or update a new or replace existing OCI brand-safety rule.

### Example

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

[oauth](../README.md#oauth)

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

[oauth](../README.md#oauth)

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

