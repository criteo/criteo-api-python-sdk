# criteo_api_marketingsolutions_v2020_10.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ad_set**](CampaignApi.md#get_ad_set) | **GET** /2021-04/marketing-solutions/ad-sets/{adSetId} | 
[**get_bids**](CampaignApi.md#get_bids) | **GET** /legacy/marketing/v1/campaigns/bids | Gets a the bids for campaigns and their categories
[**get_categories**](CampaignApi.md#get_categories) | **GET** /legacy/marketing/v1/campaigns/{campaignId}/categories | Gets categories
[**get_category**](CampaignApi.md#get_category) | **GET** /legacy/marketing/v1/campaigns/{campaignId}/categories/{categoryHashCode} | Gets a specific category
[**patch_ad_sets**](CampaignApi.md#patch_ad_sets) | **PATCH** /2021-04/marketing-solutions/ad-sets | 
[**search_ad_sets**](CampaignApi.md#search_ad_sets) | **POST** /2021-04/marketing-solutions/ad-sets/search | 
[**start_ad_sets**](CampaignApi.md#start_ad_sets) | **POST** /2021-04/marketing-solutions/ad-sets/start | 
[**stop_ad_sets**](CampaignApi.md#stop_ad_sets) | **POST** /2021-04/marketing-solutions/ad-sets/stop | 
[**update_bids**](CampaignApi.md#update_bids) | **PUT** /legacy/marketing/v1/campaigns/bids | Update bids for campaigns and their categories


# **get_ad_set**
> ResponseReadAdSet get_ad_set(ad_set_id)



Get the data for the specified ad set

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.response_read_ad_set import ResponseReadAdSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "adSetId_example" # str | Id of the ad set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->get_ad_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_set_id** | **str**| Id of the ad set |

### Return type

[**ResponseReadAdSet**](ResponseReadAdSet.md)

### Authorization

[Authorization](../README.md#Authorization)

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

# **get_bids**
> [CampaignBidMessage] get_bids()

Gets a the bids for campaigns and their categories

Get the campaigns' bids, as well as the bids of their categories

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.campaign_bid_message import CampaignBidMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_ids = "campaignIds_example" # str | Optional. The ids of the campaigns we want to get the bids on. If not specified, advertiserIds will be used. (optional)
    advertiser_ids = "advertiserIds_example" # str | Optional. The ids of the advertisers' campaigns we want to get the bids on. If campaignIds not specified, and neither is advertiserIds, all the advertisers in the user's portfolio are used. (optional)
    category_hash_codes = "categoryHashCodes_example" # str | Optional. Filters only specified categories. By default no filtering is applied. (optional)
    bid_type = "Unknown" # str | Optional. Filters by bid type. By default no filtering is applied. (optional)
    campaign_status = "Running" # str | Optional. Filters by campaign status. By default no filtering is applied. (optional)
    pending_changes = True # bool | Optional. Filters only pending changes or settled ones. By default no filtering is applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a the bids for campaigns and their categories
        api_response = api_instance.get_bids(campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, category_hash_codes=category_hash_codes, bid_type=bid_type, campaign_status=campaign_status, pending_changes=pending_changes)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->get_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_ids** | **str**| Optional. The ids of the campaigns we want to get the bids on. If not specified, advertiserIds will be used. | [optional]
 **advertiser_ids** | **str**| Optional. The ids of the advertisers&#39; campaigns we want to get the bids on. If campaignIds not specified, and neither is advertiserIds, all the advertisers in the user&#39;s portfolio are used. | [optional]
 **category_hash_codes** | **str**| Optional. Filters only specified categories. By default no filtering is applied. | [optional]
 **bid_type** | **str**| Optional. Filters by bid type. By default no filtering is applied. | [optional]
 **campaign_status** | **str**| Optional. Filters by campaign status. By default no filtering is applied. | [optional]
 **pending_changes** | **bool**| Optional. Filters only pending changes or settled ones. By default no filtering is applied. | [optional]

### Return type

[**[CampaignBidMessage]**](CampaignBidMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bids returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | There is not even one valid advertiserId or campaignId requested. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> CategoryMessage get_categories(campaign_id)

Gets categories

Get the list of categories linked to the requested campaign.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.category_message import CategoryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | Mandatory. The id of the campaign the categories are linked to.
    enabled_only = True # bool | Optional. Returns only categories you can bid on. Defaults to false. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets categories
        api_response = api_instance.get_categories(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->get_categories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets categories
        api_response = api_instance.get_categories(campaign_id, enabled_only=enabled_only)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->get_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Mandatory. The id of the campaign the categories are linked to. |
 **enabled_only** | **bool**| Optional. Returns only categories you can bid on. Defaults to false. | [optional]

### Return type

[**CategoryMessage**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | One of the requested campaigns doesn&#39;t belong to the API user&#39;s portfolio which prevents from accessing its data. |  -  |
**404** | The requested campaign was not found. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> CategoryMessage get_category(campaign_id, category_hash_code)

Gets a specific category

Get a specific category linked to the requested campaign.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.category_message import CategoryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = 1 # int | Mandatory. The id of the campaign the categories are linked to.
    category_hash_code = 1 # int | Mandatory. The id of the category to return.

    # example passing only required values which don't have defaults set
    try:
        # Gets a specific category
        api_response = api_instance.get_category(campaign_id, category_hash_code)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->get_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Mandatory. The id of the campaign the categories are linked to. |
 **category_hash_code** | **int**| Mandatory. The id of the category to return. |

### Return type

[**CategoryMessage**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | One of the requested campaigns doesn&#39;t belong to the API user&#39;s portfolio which prevents from accessing its data. |  -  |
**404** | The requested category was not found for the campaign. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ad_sets**
> ResponseAdSetId patch_ad_sets()



Patch a list of AdSets.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.requests_patch_ad_set import RequestsPatchAdSet
from criteo_api_marketingsolutions_v2020_10.model.response_ad_set_id import ResponseAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->patch_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_patch_ad_set** | [**RequestsPatchAdSet**](RequestsPatchAdSet.md)| List of adsets to patch. | [optional]

### Return type

[**ResponseAdSetId**](ResponseAdSetId.md)

### Authorization

[Authorization](../README.md#Authorization)

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

# **search_ad_sets**
> ResponsesReadAdSet search_ad_sets()



Search for ad sets

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.responses_read_ad_set import ResponsesReadAdSet
from criteo_api_marketingsolutions_v2020_10.model.request_ad_set_search import RequestAdSetSearch
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->search_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_ad_set_search** | [**RequestAdSetSearch**](RequestAdSetSearch.md)|  | [optional]

### Return type

[**ResponsesReadAdSet**](ResponsesReadAdSet.md)

### Authorization

[Authorization](../README.md#Authorization)

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

# **start_ad_sets**
> ResponsesAdSetId start_ad_sets()



Start the specified list of ad sets

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2020_10.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->start_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_ad_set_id** | [**RequestsAdSetId**](RequestsAdSetId.md)| All the ad sets to start | [optional]

### Return type

[**ResponsesAdSetId**](ResponsesAdSetId.md)

### Authorization

[Authorization](../README.md#Authorization)

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

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2020_10.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->stop_ad_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests_ad_set_id** | [**RequestsAdSetId**](RequestsAdSetId.md)| All the ad sets to stop | [optional]

### Return type

[**ResponsesAdSetId**](ResponsesAdSetId.md)

### Authorization

[Authorization](../README.md#Authorization)

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

# **update_bids**
> [CampaignMessage] update_bids(bid_changes)

Update bids for campaigns and their categories

If a campaign bid is updated, all (if any) category bids for this campaign will be updated with the new value if they are initially equal to the campaign bid.  If the category bid is not wanted to be cascaded to the categories with the same bid value, new change bids must be added in the request for the categories where the value should be kept (with the initial value).

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import campaign_api
from criteo_api_marketingsolutions_v2020_10.model.campaign_bid_change_request import CampaignBidChangeRequest
from criteo_api_marketingsolutions_v2020_10.model.campaign_bid_change_response_message_with_details import CampaignBidChangeResponseMessageWithDetails
from criteo_api_marketingsolutions_v2020_10.model.campaign_message import CampaignMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    bid_changes = [
        CampaignBidChangeRequest(
            campaign_id=1,
            bid_value=3.14,
            categories=[
                CategoryBidChangeRequest(
                    category_hashcode=1,
                    bid_value=3.14,
                ),
            ],
        ),
    ] # [CampaignBidChangeRequest] | Specifies the list of bid changes to be applied.

    # example passing only required values which don't have defaults set
    try:
        # Update bids for campaigns and their categories
        api_response = api_instance.update_bids(bid_changes)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling CampaignApi->update_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid_changes** | [**[CampaignBidChangeRequest]**](CampaignBidChangeRequest.md)| Specifies the list of bid changes to be applied. |

### Return type

[**[CampaignMessage]**](CampaignMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign bids updated OK. |  -  |
**400** | Invalid input. Please check returned message for details. |  -  |
**401** | Authentication failed. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

