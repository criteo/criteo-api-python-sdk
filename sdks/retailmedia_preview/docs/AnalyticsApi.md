# criteo_api_retailmedia_preview.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_async_accounts_report**](AnalyticsApi.md#generate_async_accounts_report) | **POST** /preview/retail-media/reports/accounts | 
[**generate_async_campaigns_report**](AnalyticsApi.md#generate_async_campaigns_report) | **POST** /preview/retail-media/reports/campaigns | 
[**generate_async_fill_rate_report**](AnalyticsApi.md#generate_async_fill_rate_report) | **POST** /preview/retail-media/reports/fillrate | 
[**generate_async_line_items_report**](AnalyticsApi.md#generate_async_line_items_report) | **POST** /preview/retail-media/reports/line-items | 
[**generate_async_offsite_report**](AnalyticsApi.md#generate_async_offsite_report) | **POST** /preview/retail-media/reports/offsite | 
[**generate_sync_attributed_transactions_report**](AnalyticsApi.md#generate_sync_attributed_transactions_report) | **POST** /preview/retail-media/reports/sync/attributed-transactions | 
[**generate_sync_campaigns_report**](AnalyticsApi.md#generate_sync_campaigns_report) | **POST** /preview/retail-media/reports/sync/campaigns | 
[**generate_sync_line_items_report**](AnalyticsApi.md#generate_sync_line_items_report) | **POST** /preview/retail-media/reports/sync/line-items | 
[**get_async_export_output**](AnalyticsApi.md#get_async_export_output) | **GET** /preview/retail-media/reports/{reportId}/output | 
[**get_async_export_status**](AnalyticsApi.md#get_async_export_status) | **GET** /preview/retail-media/reports/{reportId}/status | 


# **generate_async_accounts_report**
> AsyncReportResponse generate_async_accounts_report(async_accounts_report_request)



Returns an asynchronous Accounts Report This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_preview.model.async_accounts_report_request import AsyncAccountsReportRequest
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_accounts_report_request = AsyncAccountsReportRequest(
        data=AsyncAccountsReportResource(
            attributes=AsyncAccountsReport(
                account_ids=[
                    "account_ids_example",
                ],
                aggregation_level="campaign",
                campaign_type="all",
                click_attribution_window="none",
                dimensions=[
                    "date",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json-compact",
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
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncAccountsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_accounts_report(async_accounts_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_accounts_report: %s\n" % e)
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_async_campaigns_report**
> AsyncReportResponse generate_async_campaigns_report(async_campaigns_report_request)



Return an asynchronous Campaigns Report This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_campaigns_report_request import AsyncCampaignsReportRequest
from criteo_api_retailmedia_preview.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_campaigns_report_request = AsyncCampaignsReportRequest(
        data=AsyncCampaignsReportResource(
            attributes=AsyncCampaignsReport(
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
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncCampaignsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_campaigns_report(async_campaigns_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_campaigns_report: %s\n" % e)
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_async_fill_rate_report**
> AsyncReportResponse generate_async_fill_rate_report(async_fill_rate_report_request)



Returns an asynchronous Fill Rate Report This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_fill_rate_report_request import AsyncFillRateReportRequest
from criteo_api_retailmedia_preview.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_fill_rate_report_request = AsyncFillRateReportRequest(
        data=AsyncFillRateReportResource(
            attributes=AsyncFillRateReport(
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
        api_response = api_instance.generate_async_fill_rate_report(async_fill_rate_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_async_line_items_report**
> AsyncReportResponse generate_async_line_items_report(async_line_items_report_request)



Returns an asynchronous Line Items Report This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_line_items_report_request import AsyncLineItemsReportRequest
from criteo_api_retailmedia_preview.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_line_items_report_request = AsyncLineItemsReportRequest(
        data=AsyncLineItemsReportResource(
            attributes=AsyncLineItemsReport(
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
                timezone="UTC",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # AsyncLineItemsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_line_items_report(async_line_items_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_line_items_report: %s\n" % e)
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_async_offsite_report**
> AsyncReportResponse generate_async_offsite_report(async_offsite_report_request)



Returns an asynchronous Offsite Report This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_offsite_report_request import AsyncOffsiteReportRequest
from criteo_api_retailmedia_preview.model.async_report_response import AsyncReportResponse
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
        api_response = api_instance.generate_async_offsite_report(async_offsite_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sync_attributed_transactions_report**
> ReportResponse generate_sync_attributed_transactions_report(sync_attributed_transactions_report_request)



Returns a synchronous Attributed Transactions Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.sync_attributed_transactions_report_request import SyncAttributedTransactionsReportRequest
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
        api_response = api_instance.generate_sync_attributed_transactions_report(sync_attributed_transactions_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sync_campaigns_report**
> ReportResponse generate_sync_campaigns_report(sync_campaigns_report_request)



Returns a synchronous Campaigns Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.sync_campaigns_report_request import SyncCampaignsReportRequest
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
        api_response = api_instance.generate_sync_campaigns_report(sync_campaigns_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sync_line_items_report**
> ReportResponse generate_sync_line_items_report(sync_line_items_report_request)



Returns a synchronous Line Items Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.sync_line_items_report_request import SyncLineItemsReportRequest
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
        api_response = api_instance.generate_sync_line_items_report(sync_line_items_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_export_output**
> file_type get_async_export_output(report_id)



Returns the output of an async report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_output(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_export_status**
> AsyncReportResponse get_async_export_status(report_id)



Returns the status of an async report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_report_response import AsyncReportResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_status(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

