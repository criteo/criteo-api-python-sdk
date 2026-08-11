# criteo_api_retailmedia_v2027_01.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_async_attributed_transactions_report**](AnalyticsApi.md#generate_async_attributed_transactions_report) | **POST** /2027-01/retail-media/reports/attributed-transactions | /2027-01/retail-media/reports/attributed-transactions
[**generate_async_fill_rate_report**](AnalyticsApi.md#generate_async_fill_rate_report) | **POST** /2027-01/retail-media/reports/fillrate | /2027-01/retail-media/reports/fillrate
[**generate_async_missed_opportunities_report**](AnalyticsApi.md#generate_async_missed_opportunities_report) | **POST** /2027-01/retail-media/reports/missed-opportunities | /2027-01/retail-media/reports/missed-opportunities
[**generate_async_performance_report**](AnalyticsApi.md#generate_async_performance_report) | **POST** /2027-01/retail-media/reports/performance | /2027-01/retail-media/reports/performance
[**generate_async_revenue_report**](AnalyticsApi.md#generate_async_revenue_report) | **POST** /2027-01/retail-media/reports/revenue | /2027-01/retail-media/reports/revenue
[**generate_async_unfilled_placements_report**](AnalyticsApi.md#generate_async_unfilled_placements_report) | **POST** /2027-01/retail-media/reports/unfilled-placements | /2027-01/retail-media/reports/unfilled-placements
[**generate_sync_attributed_transactions_report**](AnalyticsApi.md#generate_sync_attributed_transactions_report) | **POST** /2027-01/retail-media/reports/sync/attributed-transactions | /2027-01/retail-media/reports/sync/attributed-transactions
[**generate_sync_campaigns_report**](AnalyticsApi.md#generate_sync_campaigns_report) | **POST** /2027-01/retail-media/reports/sync/campaigns | /2027-01/retail-media/reports/sync/campaigns
[**generate_sync_line_items_report**](AnalyticsApi.md#generate_sync_line_items_report) | **POST** /2027-01/retail-media/reports/sync/line-items | /2027-01/retail-media/reports/sync/line-items
[**generate_sync_real_time_performance_report**](AnalyticsApi.md#generate_sync_real_time_performance_report) | **POST** /2027-01/retail-media/reports/sync/real-time-performance | /2027-01/retail-media/reports/sync/real-time-performance
[**get_async_export_output**](AnalyticsApi.md#get_async_export_output) | **GET** /2027-01/retail-media/reports/{reportId}/output | /2027-01/retail-media/reports/{reportId}/output
[**get_async_export_status**](AnalyticsApi.md#get_async_export_status) | **GET** /2027-01/retail-media/reports/{reportId}/status | /2027-01/retail-media/reports/{reportId}/status


# **generate_async_attributed_transactions_report**
> AsyncReportResponse generate_async_attributed_transactions_report(async_attributed_transactions_report_request)

/2027-01/retail-media/reports/attributed-transactions

Creates an attributed-transactions async report. The request accepts explicit attributed-transaction dimensions, metrics, and filters.  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2027_01.model.async_attributed_transactions_report_request import AsyncAttributedTransactionsReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_attributed_transactions_report_request = AsyncAttributedTransactionsReportRequest(
        data=AsyncAttributedTransactionsReportResource(
            attributes=AsyncAttributedTransactionsReport(
                click_attribution_window="none",
                click_match_level="campaign",
                dimensions=[
                    "purchasedDate",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                filters=AttributedTransactionsReportFilters(
                    account_ids=[
                        "account_ids_example",
                    ],
                    campaign_ids=[
                        "campaign_ids_example",
                    ],
                    line_item_ids=[
                        "line_item_ids_example",
                    ],
                    media_types=[
                        "unknown",
                    ],
                ),
                format="json",
                metrics=[
                    "attributedUnits",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                view_attribution_window="none",
                view_match_level="campaign",
            ),
            type="type_example",
        ),
    ) # AsyncAttributedTransactionsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/attributed-transactions
        api_response = api_instance.generate_async_attributed_transactions_report(async_attributed_transactions_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_attributed_transactions_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_attributed_transactions_report_request** | [**AsyncAttributedTransactionsReportRequest**](AsyncAttributedTransactionsReportRequest.md)|  |

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

# **generate_async_fill_rate_report**
> AsyncReportResponse generate_async_fill_rate_report(async_fill_rate_report_request)

/2027-01/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2027_01.model.async_fill_rate_report_request import AsyncFillRateReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_fill_rate_report_request = AsyncFillRateReportRequest(
        data=AsyncFillRateReportResource(
            attributes=AsyncFillRateReport(
                ad_server_type="all",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json",
                metrics=[
                    "pageViews",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                supply_account_ids=[
                    "supply_account_ids_example",
                ],
                timezone="UTC",
            ),
            type="type_example",
        ),
    ) # AsyncFillRateReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/fillrate
        api_response = api_instance.generate_async_fill_rate_report(async_fill_rate_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_fill_rate_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_fill_rate_report_request** | [**AsyncFillRateReportRequest**](AsyncFillRateReportRequest.md)|  |

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

# **generate_async_missed_opportunities_report**
> AsyncReportResponse generate_async_missed_opportunities_report(async_missed_opportunities_report_request)

/2027-01/retail-media/reports/missed-opportunities

Creates a missed-opportunities async report. The request accepts explicit missed-opportunities dimensions, metrics, and filters.  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2027_01.model.async_missed_opportunities_report_request import AsyncMissedOpportunitiesReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_missed_opportunities_report_request = AsyncMissedOpportunitiesReportRequest(
        data=AsyncMissedOpportunitiesReportResource(
            attributes=AsyncMissedOpportunitiesReport(
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                filters=MissedOpportunitiesReportFilters(
                    account_ids=[
                        "account_ids_example",
                    ],
                    campaign_ids=[
                        "campaign_ids_example",
                    ],
                    line_item_ids=[
                        "line_item_ids_example",
                    ],
                ),
                format="json",
                metrics=[
                    "daypartingScheduled",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            type="type_example",
        ),
    ) # AsyncMissedOpportunitiesReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/missed-opportunities
        api_response = api_instance.generate_async_missed_opportunities_report(async_missed_opportunities_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_missed_opportunities_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_missed_opportunities_report_request** | [**AsyncMissedOpportunitiesReportRequest**](AsyncMissedOpportunitiesReportRequest.md)|  |

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

# **generate_async_performance_report**
> AsyncReportResponse generate_async_performance_report(async_performance_report_request)

/2027-01/retail-media/reports/performance

Creates a performance DSP analytics async report. Dimensions and metrics select the output schema, and filters constrain eligible data.  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_performance_report_request import AsyncPerformanceReportRequest
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_performance_report_request = AsyncPerformanceReportRequest(
        data=AsyncPerformanceReportResource(
            attributes=AsyncPerformanceReport(
                click_attribution_window="none",
                click_match_level="campaign",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                filters=PerformanceReportFilters(
                    account_ids=[
                        "account_ids_example",
                    ],
                    activation_platforms=[
                        "CommerceMax",
                    ],
                    budget_models=[
                        "CriteoBudget",
                    ],
                    buy_types=[
                        "auction",
                    ],
                    campaign_ids=[
                        "campaign_ids_example",
                    ],
                    campaign_types=[
                        "all",
                    ],
                    line_item_ids=[
                        "line_item_ids_example",
                    ],
                    media_types=[
                        "unknown",
                    ],
                    sales_channels=[
                        "online",
                    ],
                    search_term_targetings=[
                        "unknown",
                    ],
                    search_term_types=[
                        "unknown",
                    ],
                    targeted_keyword_types=[
                        "unknown",
                    ],
                ),
                format="json",
                metrics=[
                    "impressions",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                view_attribution_window="none",
                view_match_level="campaign",
            ),
            type="type_example",
        ),
    ) # AsyncPerformanceReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/performance
        api_response = api_instance.generate_async_performance_report(async_performance_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_performance_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_performance_report_request** | [**AsyncPerformanceReportRequest**](AsyncPerformanceReportRequest.md)|  |

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

# **generate_async_revenue_report**
> AsyncReportResponse generate_async_revenue_report(async_revenue_report_request)

/2027-01/retail-media/reports/revenue

Returns an asynchronous Revenue Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_revenue_report_request import AsyncRevenueReportRequest
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_revenue_report_request = AsyncRevenueReportRequest(
        data=AsyncRevenueReportResource(
            attributes=AsyncRevenueReport(
                account_ids=[
                    "account_ids_example",
                ],
                activation_platforms=[
                    "CommerceMax",
                ],
                advertiser_types=[
                    "retailer",
                ],
                budget_models=[
                    "CriteoBudget",
                ],
                buy_type="auction",
                campaign_ids=[
                    "campaign_ids_example",
                ],
                campaign_type="all",
                click_attribution_window="none",
                click_match_level="campaign",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json",
                id="id_example",
                ids=[
                    "ids_example",
                ],
                line_item_ids=[
                    "line_item_ids_example",
                ],
                media_type="all",
                metrics=[
                    "numberOfCampaigns",
                ],
                report_type="advertiser",
                retailer_ids=[
                    "retailer_ids_example",
                ],
                revenue_type="auction",
                sales_channel="all",
                sku_relations=[
                    "sameSku",
                ],
                sold_by="directSold",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                targeted_keyword_types=[
                    "unknown",
                ],
                timezone="UTC",
                view_attribution_window="none",
                view_match_level="campaign",
            ),
            type="type_example",
        ),
    ) # AsyncRevenueReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/revenue
        api_response = api_instance.generate_async_revenue_report(async_revenue_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_revenue_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_revenue_report_request** | [**AsyncRevenueReportRequest**](AsyncRevenueReportRequest.md)|  |

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

# **generate_async_unfilled_placements_report**
> AsyncReportResponse generate_async_unfilled_placements_report(async_unfilled_placements_report_request)

/2027-01/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2027_01.model.async_unfilled_placements_report_request import AsyncUnfilledPlacementsReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_unfilled_placements_report_request = AsyncUnfilledPlacementsReportRequest(
        data=AsyncUnfilledPlacementsReportResource(
            attributes=AsyncUnfilledPlacementsReport(
                ad_server_type="all",
                campaign_type="all",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json",
                metrics=[
                    "totalUnfilledPlacements",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                supply_account_ids=[
                    "supply_account_ids_example",
                ],
                timezone="UTC",
            ),
            type="type_example",
        ),
    ) # AsyncUnfilledPlacementsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/unfilled-placements
        api_response = api_instance.generate_async_unfilled_placements_report(async_unfilled_placements_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_unfilled_placements_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_unfilled_placements_report_request** | [**AsyncUnfilledPlacementsReportRequest**](AsyncUnfilledPlacementsReportRequest.md)|  |

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

# **generate_sync_attributed_transactions_report**
> ReportResponse generate_sync_attributed_transactions_report(sync_attributed_transactions_report_request)

/2027-01/retail-media/reports/sync/attributed-transactions

Returns a synchronous Attributed Transactions Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.sync_attributed_transactions_report_request import SyncAttributedTransactionsReportRequest
from criteo_api_retailmedia_v2027_01.model.report_response import ReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    sync_attributed_transactions_report_request = SyncAttributedTransactionsReportRequest(
        data=SyncAttributedTransactionsReportResource(
            attributes=SyncAttributedTransactionsReport(
                account_id="account_id_example",
                campaign_ids=[
                    "campaign_ids_example",
                ],
                campaign_type="all",
                click_attribution_window="none",
                dimensions=[
                    "purchasedDate",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                line_item_ids=[
                    "line_item_ids_example",
                ],
                media_type="all",
                metrics=[
                    "attributedUnits",
                ],
                sales_channel="all",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # SyncAttributedTransactionsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/sync/attributed-transactions
        api_response = api_instance.generate_sync_attributed_transactions_report(sync_attributed_transactions_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_sync_attributed_transactions_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_attributed_transactions_report_request** | [**SyncAttributedTransactionsReportRequest**](SyncAttributedTransactionsReportRequest.md)|  |

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

# **generate_sync_campaigns_report**
> ReportResponse generate_sync_campaigns_report(sync_campaigns_report_request)

/2027-01/retail-media/reports/sync/campaigns

Returns a synchronous Campaigns Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.report_response import ReportResponse
from criteo_api_retailmedia_v2027_01.model.sync_campaigns_report_request import SyncCampaignsReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    sync_campaigns_report_request = SyncCampaignsReportRequest(
        data=SyncCampaignsReportResource(
            attributes=SyncCampaignsReport(
                account_id="account_id_example",
                campaign_ids=[
                    "campaign_ids_example",
                ],
                campaign_type="all",
                click_attribution_window="none",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                metrics=[
                    "impressions",
                ],
                report_type="summary",
                sales_channel="all",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # SyncCampaignsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/sync/campaigns
        api_response = api_instance.generate_sync_campaigns_report(sync_campaigns_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_sync_campaigns_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_campaigns_report_request** | [**SyncCampaignsReportRequest**](SyncCampaignsReportRequest.md)|  |

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

# **generate_sync_line_items_report**
> ReportResponse generate_sync_line_items_report(sync_line_items_report_request)

/2027-01/retail-media/reports/sync/line-items

Returns a synchronous Line Items Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.sync_line_items_report_request import SyncLineItemsReportRequest
from criteo_api_retailmedia_v2027_01.model.report_response import ReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    sync_line_items_report_request = SyncLineItemsReportRequest(
        data=SyncLineItemsReportResource(
            attributes=SyncLineItemsReport(
                account_id="account_id_example",
                campaign_ids=[
                    "campaign_ids_example",
                ],
                campaign_type="all",
                click_attribution_window="none",
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
                report_type="summary",
                sales_channel="all",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # SyncLineItemsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/sync/line-items
        api_response = api_instance.generate_sync_line_items_report(sync_line_items_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_sync_line_items_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_line_items_report_request** | [**SyncLineItemsReportRequest**](SyncLineItemsReportRequest.md)|  |

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

# **generate_sync_real_time_performance_report**
> ReportResponse generate_sync_real_time_performance_report(sync_real_time_performance_report_request)

/2027-01/retail-media/reports/sync/real-time-performance

Returns a synchronous Real Time Performance Report. Returns empty rows; metadata includes dataCompleteThrough (latest time from streaming table in the request timezone).  <br />  This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.sync_real_time_performance_report_request import SyncRealTimePerformanceReportRequest
from criteo_api_retailmedia_v2027_01.model.report_response import ReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
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
        # /2027-01/retail-media/reports/sync/real-time-performance
        api_response = api_instance.generate_sync_real_time_performance_report(sync_real_time_performance_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
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

# **get_async_export_output**
> file_type get_async_export_output(report_id)

/2027-01/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/{reportId}/output
        api_response = api_instance.get_async_export_output(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->get_async_export_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The ID of the report to retrieve |

### Return type

**file_type**

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

# **get_async_export_status**
> AsyncReportResponse get_async_export_status(report_id)

/2027-01/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import analytics_api
from criteo_api_retailmedia_v2027_01.model.async_report_response import AsyncReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/reports/{reportId}/status
        api_response = api_instance.get_async_export_status(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling AnalyticsApi->get_async_export_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The ID of the report to retrieve |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

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

