# criteo_api_retailmedia_experimental.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_async_accounts_report_v2**](AnalyticsApi.md#generate_async_accounts_report_v2) | **POST** /experimental/retail-media/reports/accounts | /experimental/retail-media/reports/accounts
[**generate_async_campaigns_report_v2**](AnalyticsApi.md#generate_async_campaigns_report_v2) | **POST** /experimental/retail-media/reports/campaigns | /experimental/retail-media/reports/campaigns
[**generate_async_line_items_report_v2**](AnalyticsApi.md#generate_async_line_items_report_v2) | **POST** /experimental/retail-media/reports/line-items | /experimental/retail-media/reports/line-items
[**generate_async_offsite_report**](AnalyticsApi.md#generate_async_offsite_report) | **POST** /experimental/retail-media/reports/offsite | /experimental/retail-media/reports/offsite
[**generate_digital_shelf_intelligence_insight**](AnalyticsApi.md#generate_digital_shelf_intelligence_insight) | **POST** /experimental/retail-media/insights/digital-shelf-intelligence | /experimental/retail-media/insights/digital-shelf-intelligence
[**generate_share_of_voice_insight**](AnalyticsApi.md#generate_share_of_voice_insight) | **POST** /experimental/retail-media/insights/share-of-voice | /experimental/retail-media/insights/share-of-voice
[**generate_sync_real_time_performance_report**](AnalyticsApi.md#generate_sync_real_time_performance_report) | **POST** /experimental/retail-media/reports/sync/real-time-performance | /experimental/retail-media/reports/sync/real-time-performance
[**get_insight_report_output**](AnalyticsApi.md#get_insight_report_output) | **GET** /experimental/retail-media/insights/{insight-id}/output | /experimental/retail-media/insights/{insight-id}/output
[**get_insight_report_status**](AnalyticsApi.md#get_insight_report_status) | **GET** /experimental/retail-media/insights/{insight-id}/status | /experimental/retail-media/insights/{insight-id}/status


# **generate_async_accounts_report_v2**
> AsyncReportResponse generate_async_accounts_report_v2(async_accounts_report_request)

/experimental/retail-media/reports/accounts

Returns an asynchronous Accounts Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_experimental.model.async_accounts_report_request import AsyncAccountsReportRequest
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_accounts_report_request = AsyncAccountsReportRequest(
        data=AsyncAccountsReportResource(
            attributes=AsyncAccountsReport(
                account_ids=[
                    "account_ids_example",
                ],
                activation_platforms=[
                    "CommerceMax",
                ],
                aggregation_level="campaign",
                budget_models=[
                    "CriteoBudget",
                ],
                buy_types=[
                    "auction",
                ],
                campaign_type="all",
                click_attribution_window="none",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json-compact",
                media_type="all",
                metrics=[
                    "impressions",
                ],
                report_type="summary",
                sales_channel="all",
                search_term_targetings=[
                    "unknown",
                ],
                search_term_types=[
                    "unknown",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                targeted_keyword_types=[
                    "unknown",
                ],
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncAccountsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/reports/accounts
        api_response = api_instance.generate_async_accounts_report_v2(async_accounts_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_accounts_report_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_accounts_report_request** | [**AsyncAccountsReportRequest**](AsyncAccountsReportRequest.md)|  |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

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

# **generate_async_campaigns_report_v2**
> AsyncReportResponse generate_async_campaigns_report_v2(async_campaigns_report_request)

/experimental/retail-media/reports/campaigns

Return an asynchronous Campaigns Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.async_campaigns_report_request import AsyncCampaignsReportRequest
from criteo_api_retailmedia_experimental.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_campaigns_report_request = AsyncCampaignsReportRequest(
        data=AsyncCampaignsReportResource(
            attributes=AsyncCampaignsReport(
                activation_platforms=[
                    "CommerceMax",
                ],
                budget_models=[
                    "CriteoBudget",
                ],
                buy_types=[
                    "auction",
                ],
                campaign_type="all",
                click_attribution_window="none",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json-compact",
                id="id_example",
                ids=[
                    "ids_example",
                ],
                media_type="all",
                metrics=[
                    "impressions",
                ],
                report_type="summary",
                sales_channel="all",
                search_term_targetings=[
                    "unknown",
                ],
                search_term_types=[
                    "unknown",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                targeted_keyword_types=[
                    "unknown",
                ],
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncCampaignsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/reports/campaigns
        api_response = api_instance.generate_async_campaigns_report_v2(async_campaigns_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_campaigns_report_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_campaigns_report_request** | [**AsyncCampaignsReportRequest**](AsyncCampaignsReportRequest.md)|  |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

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

# **generate_async_line_items_report_v2**
> AsyncReportResponse generate_async_line_items_report_v2(async_line_items_report_request)

/experimental/retail-media/reports/line-items

Returns an asynchronous Line Items Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.async_line_items_report_request import AsyncLineItemsReportRequest
from criteo_api_retailmedia_experimental.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_line_items_report_request = AsyncLineItemsReportRequest(
        data=AsyncLineItemsReportResource(
            attributes=AsyncLineItemsReport(
                activation_platforms=[
                    "CommerceMax",
                ],
                budget_models=[
                    "CriteoBudget",
                ],
                buy_types=[
                    "auction",
                ],
                campaign_type="all",
                click_attribution_window="none",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json-compact",
                id="id_example",
                ids=[
                    "ids_example",
                ],
                media_type="all",
                metrics=[
                    "impressions",
                ],
                report_type="summary",
                sales_channel="all",
                search_term_targetings=[
                    "unknown",
                ],
                search_term_types=[
                    "unknown",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                targeted_keyword_types=[
                    "unknown",
                ],
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncLineItemsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/reports/line-items
        api_response = api_instance.generate_async_line_items_report_v2(async_line_items_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_line_items_report_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_line_items_report_request** | [**AsyncLineItemsReportRequest**](AsyncLineItemsReportRequest.md)|  |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

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

# **generate_async_offsite_report**
> AsyncReportResponse generate_async_offsite_report(async_offsite_report_request)

/experimental/retail-media/reports/offsite

Returns an asynchronous Offsite Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.async_offsite_report_request import AsyncOffsiteReportRequest
from criteo_api_retailmedia_experimental.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_offsite_report_request = AsyncOffsiteReportRequest(
        data=AsyncOffsiteReportResource(
            attributes=AsyncOffsiteReport(
                account_ids=[
                    "account_ids_example",
                ],
                buy_type="auction",
                campaign_ids=[
                    "campaign_ids_example",
                ],
                campaign_type="all",
                click_attribution_window="none",
                creative_ids=[
                    "creative_ids_example",
                ],
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json-compact",
                line_item_ids=[
                    "line_item_ids_example",
                ],
                media_type="all",
                metrics=[
                    "audience",
                ],
                retailer_ids=[
                    "retailer_ids_example",
                ],
                sales_channel="all",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncOffsiteReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/reports/offsite
        api_response = api_instance.generate_async_offsite_report(async_offsite_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_offsite_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_offsite_report_request** | [**AsyncOffsiteReportRequest**](AsyncOffsiteReportRequest.md)|  |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

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

# **generate_digital_shelf_intelligence_insight**
> AsyncInsightResponse generate_digital_shelf_intelligence_insight(digital_shelf_intelligence_insight_request)

/experimental/retail-media/insights/digital-shelf-intelligence

Requests a Digital Shelf Intelligence insight report. This is an asynchronous, non-transactional operation:  it does not return the analytic data. It enqueues an export job and returns the created insight  report, whose id is then used to poll the insight status endpoint until the report is ready and to  download the result from the insight output endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.digital_shelf_intelligence_insight_request import DigitalShelfIntelligenceInsightRequest
from criteo_api_retailmedia_experimental.model.async_insight_response import AsyncInsightResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    digital_shelf_intelligence_insight_request = DigitalShelfIntelligenceInsightRequest(
        data=DigitalShelfIntelligenceInsightResource(
            attributes=DigitalShelfIntelligenceInsight(
                account_id="account_id_example",
                aggregation_level="brand",
                end_date="end_date_example",
                filters=DigitalShelfIntelligenceFilters(
                    brand_ids=[
                        "brand_ids_example",
                    ],
                    categories=[
                        "categories_example",
                    ],
                    retailer_ids=[
                        "retailer_ids_example",
                    ],
                    sku_ids=[
                        SkuFilter(
                            retailer_id="retailer_id_example",
                            retailer_sku_ids=[
                                "retailer_sku_ids_example",
                            ],
                        ),
                    ],
                ),
                format="json-compact",
                metrics=[
                    "considerationIndex",
                ],
                start_date="start_date_example",
            ),
            type="type_example",
        ),
    ) # DigitalShelfIntelligenceInsightRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/insights/digital-shelf-intelligence
        api_response = api_instance.generate_digital_shelf_intelligence_insight(digital_shelf_intelligence_insight_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_digital_shelf_intelligence_insight: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_shelf_intelligence_insight_request** | [**DigitalShelfIntelligenceInsightRequest**](DigitalShelfIntelligenceInsightRequest.md)|  |

### Return type

[**AsyncInsightResponse**](AsyncInsightResponse.md)

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

# **generate_share_of_voice_insight**
> AsyncInsightResponse generate_share_of_voice_insight(share_of_voice_insight_request)

/experimental/retail-media/insights/share-of-voice

Requests a Share of Voice insight report. This is an asynchronous, non-transactional operation:  it does not return the analytic data. It enqueues an export job and returns the created insight  report, whose id is then used to poll the insight status endpoint until the report is ready and to  download the result from the insight output endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.share_of_voice_insight_request import ShareOfVoiceInsightRequest
from criteo_api_retailmedia_experimental.model.async_insight_response import AsyncInsightResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    share_of_voice_insight_request = ShareOfVoiceInsightRequest(
        data=ShareOfVoiceInsightResource(
            attributes=ShareOfVoiceInsight(
                account_id="account_id_example",
                aggregation_level="category",
                dimensions=[
                    "date",
                ],
                end_date="end_date_example",
                filters=ShareOfVoiceFilters(
                    account_ids=[
                        "account_ids_example",
                    ],
                    activation_platforms=[
                        "commerceMax",
                    ],
                    brand_ids=[
                        "brand_ids_example",
                    ],
                    budget_models=[
                        "criteoBudget",
                    ],
                    campaign_type="all",
                    keywords=[
                        "keywords_example",
                    ],
                    keyword_types=[
                        "unknown",
                    ],
                    retailer_ids=[
                        "retailer_ids_example",
                    ],
                    served_categories=[
                        "served_categories_example",
                    ],
                ),
                format="json-compact",
                metrics=[
                    "impressions",
                ],
                start_date="start_date_example",
            ),
            type="type_example",
        ),
    ) # ShareOfVoiceInsightRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/insights/share-of-voice
        api_response = api_instance.generate_share_of_voice_insight(share_of_voice_insight_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_share_of_voice_insight: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_of_voice_insight_request** | [**ShareOfVoiceInsightRequest**](ShareOfVoiceInsightRequest.md)|  |

### Return type

[**AsyncInsightResponse**](AsyncInsightResponse.md)

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

# **generate_sync_real_time_performance_report**
> ReportResponse generate_sync_real_time_performance_report(sync_real_time_performance_report_request)

/experimental/retail-media/reports/sync/real-time-performance

Returns a synchronous Real Time Performance Report. Returns empty rows; metadata includes dataCompleteThrough (latest time from streaming table in the request timezone).  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.report_response import ReportResponse
from criteo_api_retailmedia_experimental.model.sync_real_time_performance_report_request import SyncRealTimePerformanceReportRequest
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    sync_real_time_performance_report_request = SyncRealTimePerformanceReportRequest(
        data=SyncRealTimePerformanceReportResource(
            attributes=SyncRealTimePerformanceReport(
                account_ids=[
                    "account_ids_example",
                ],
                campaign_ids=[
                    "campaign_ids_example",
                ],
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                line_item_ids=[
                    "line_item_ids_example",
                ],
                metrics=[
                    "impressions",
                ],
                retailer_ids=[
                    "retailer_ids_example",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
            ),
            type="type_example",
        ),
    ) # SyncRealTimePerformanceReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/reports/sync/real-time-performance
        api_response = api_instance.generate_sync_real_time_performance_report(sync_real_time_performance_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_sync_real_time_performance_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_real_time_performance_report_request** | [**SyncRealTimePerformanceReportRequest**](SyncRealTimePerformanceReportRequest.md)|  |

### Return type

[**ReportResponse**](ReportResponse.md)

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

# **get_insight_report_output**
> file_type get_insight_report_output(insight_id)

/experimental/retail-media/insights/{insight-id}/output

Downloads the file output of a completed insight report. The report must have reached the `Success`  status; otherwise an error is returned. Check readiness first with the insight status endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    insight_id = "insight-id_example" # str | The ID of the asynchronous insight report. Must be a valid ID format.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/insights/{insight-id}/output
        api_response = api_instance.get_insight_report_output(insight_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->get_insight_report_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The ID of the asynchronous insight report. Must be a valid ID format. |

### Return type

**file_type**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_insight_report_status**
> AsyncInsightResponse get_insight_report_status(insight_id)

/experimental/retail-media/insights/{insight-id}/status

Returns the current status of an asynchronously generated insight report. Poll this endpoint until the  status is `Success`, then download the report from the insight output endpoint.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import analytics_api
from criteo_api_retailmedia_experimental.model.async_insight_response import AsyncInsightResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    insight_id = "insight-id_example" # str | The ID of the asynchronous insight report. Must be a valid ID format.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/insights/{insight-id}/status
        api_response = api_instance.get_insight_report_status(insight_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->get_insight_report_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The ID of the asynchronous insight report. Must be a valid ID format. |

### Return type

[**AsyncInsightResponse**](AsyncInsightResponse.md)

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

