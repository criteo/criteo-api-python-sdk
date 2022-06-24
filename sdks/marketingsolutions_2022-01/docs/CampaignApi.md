# criteo_api_marketingsolutions_v2022_01.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ad_set**](CampaignApi.md#get_ad_set) | **GET** /2022-01/marketing-solutions/ad-sets/{adSetId} | 
[**get_campaign**](CampaignApi.md#get_campaign) | **GET** /2022-01/marketing-solutions/campaigns/{campaign-id} | 
[**patch_ad_sets**](CampaignApi.md#patch_ad_sets) | **PATCH** /2022-01/marketing-solutions/ad-sets | 
[**patch_campaigns**](CampaignApi.md#patch_campaigns) | **PATCH** /2022-01/marketing-solutions/campaigns | 
[**search_ad_sets**](CampaignApi.md#search_ad_sets) | **POST** /2022-01/marketing-solutions/ad-sets/search | 
[**search_campaigns**](CampaignApi.md#search_campaigns) | **POST** /2022-01/marketing-solutions/campaigns/search | 
[**start_ad_sets**](CampaignApi.md#start_ad_sets) | **POST** /2022-01/marketing-solutions/ad-sets/start | 
[**stop_ad_sets**](CampaignApi.md#stop_ad_sets) | **POST** /2022-01/marketing-solutions/ad-sets/stop | 


# **get_ad_set**
> ResponseReadAdSet get_ad_set(ad_set_id)



Get the data for the specified ad set

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.response_read_ad_set import ResponseReadAdSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    ad_set_id = "adSetId_example" # str | Id of the ad set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad_set(ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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

# **get_campaign**
> CampaignResponse get_campaign(campaign_id)



Get the data for the specified campaign

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.campaign_response import CampaignResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaign-id_example" # str | Id of the campaign

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_campaign(campaign_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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

# **patch_ad_sets**
> ResponseAdSetId patch_ad_sets()



Patch a list of AdSets.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.requests_patch_ad_set import RequestsPatchAdSet
from criteo_api_marketingsolutions_v2022_01.model.response_ad_set_id import ResponseAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
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
                                value=,
                            ),
                            subdivisions=NillableAdSetTargetingRule(
                                value=,
                            ),
                            zip_codes=NillableAdSetTargetingRule(
                                value=,
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
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.patch_campaign_list_request import PatchCampaignListRequest
from criteo_api_marketingsolutions_v2022_01.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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

# **search_ad_sets**
> ResponsesReadAdSet search_ad_sets()



Search for ad sets

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.responses_read_ad_set import ResponsesReadAdSet
from criteo_api_marketingsolutions_v2022_01.model.request_ad_set_search import RequestAdSetSearch
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.campaign_search_request import CampaignSearchRequest
from criteo_api_marketingsolutions_v2022_01.model.campaign_list_response import CampaignListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2022_01.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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
import criteo_api_marketingsolutions_v2022_01
from criteo_api_marketingsolutions_v2022_01.api import campaign_api
from criteo_api_marketingsolutions_v2022_01.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2022_01.model.requests_ad_set_id import RequestsAdSetId
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2022_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_01.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_v2022_01.ApiException as e:
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

