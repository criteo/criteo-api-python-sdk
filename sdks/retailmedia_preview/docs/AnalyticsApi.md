# criteo_api_retailmedia_preview.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_async_campaign_report**](AnalyticsApi.md#generate_async_campaign_report) | **POST** /preview/retail-media/reports/campaigns | 
[**generate_async_line_items_report**](AnalyticsApi.md#generate_async_line_items_report) | **POST** /preview/retail-media/reports/line-items | 
[**generate_async_revenue_report**](AnalyticsApi.md#generate_async_revenue_report) | **POST** /preview/retail-media/reports/revenue | 
[**generate_attributed_transactions_report**](AnalyticsApi.md#generate_attributed_transactions_report) | **POST** /preview/retail-media/reports/sync/attributed-transactions | 
[**generate_campaign_reports**](AnalyticsApi.md#generate_campaign_reports) | **POST** /preview/retail-media/reports/sync/campaigns | 
[**generate_line_items_reports**](AnalyticsApi.md#generate_line_items_reports) | **POST** /preview/retail-media/reports/sync/line-items | 
[**get_async_export_output**](AnalyticsApi.md#get_async_export_output) | **GET** /preview/retail-media/reports/{reportId}/output | 
[**get_async_export_status**](AnalyticsApi.md#get_async_export_status) | **GET** /preview/retail-media/reports/{reportId}/status | 
[**get_sku_by_product_id**](AnalyticsApi.md#get_sku_by_product_id) | **POST** /preview/retail-media/catalogs/sku/search/accounts/{accountId}/retailers/{retailerId}/by-id | 


# **generate_async_campaign_report**
> AsyncReportResponse generate_async_campaign_report(async_campaign_report_request)



Return an async Campaign Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.async_campaign_report_request import AsyncCampaignReportRequest
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
    async_campaign_report_request = AsyncCampaignReportRequest(
        data=AsyncCampaignReportResource(
            type="type_example",
            attributes=AsyncCampaignReport(
                metrics=[
                    "impressions",
                ],
                dimensions=[
                    "date",
                ],
                click_attribution_window="7D",
                view_attribution_window="1D",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
                campaign_type="sponsoredProducts",
                sales_channel="offline",
                format="json",
                report_type="summary",
                ids=[
                    "ids_example",
                ],
                id="id_example",
            ),
        ),
    ) # AsyncCampaignReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_campaign_report(async_campaign_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_campaign_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_campaign_report_request** | [**AsyncCampaignReportRequest**](AsyncCampaignReportRequest.md)|  |

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
> AsyncReportResponse generate_async_line_items_report(async_line_item_report_request)



Return an async Line Item Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.async_line_item_report_request import AsyncLineItemReportRequest
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
    async_line_item_report_request = AsyncLineItemReportRequest(
        data=AsyncLineItemReportResource(
            type="type_example",
            attributes=AsyncLineItemReport(
                metrics=[
                    "impressions",
                ],
                dimensions=[
                    "date",
                ],
                click_attribution_window="7D",
                view_attribution_window="1D",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
                campaign_type="sponsoredProducts",
                sales_channel="offline",
                format="json",
                report_type="summary",
                ids=[
                    "ids_example",
                ],
                id="id_example",
            ),
        ),
    ) # AsyncLineItemReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_line_items_report(async_line_item_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_async_line_items_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_line_item_report_request** | [**AsyncLineItemReportRequest**](AsyncLineItemReportRequest.md)|  |

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

# **generate_async_revenue_report**
> AsyncReportResponse generate_async_revenue_report(async_revenue_report_request)



Return an async Revenue Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.async_revenue_report_request import AsyncRevenueReportRequest
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
    async_revenue_report_request = AsyncRevenueReportRequest(
        data=AsyncRevenueReportResource(
            type="type_example",
            attributes=AsyncRevenueReport(
                report_type="advertiser",
                revenue_type="auction",
                ids=[
                    "ids_example",
                ],
                id="id_example",
                metrics=[
                    "clicks",
                ],
                dimensions=[
                    "date",
                ],
                format="json",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
                campaign_type="sponsoredProducts",
                sales_channel="offline",
                sold_by="directSold",
                campaign_sub_type="auctionAndPreferred",
            ),
        ),
    ) # AsyncRevenueReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_revenue_report(async_revenue_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_attributed_transactions_report**
> ReportResponse generate_attributed_transactions_report(attributed_transaction_report_request)



Return an Attributed Transactions Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.attributed_transaction_report_request import AttributedTransactionReportRequest
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
    attributed_transaction_report_request = AttributedTransactionReportRequest(
        data=AttributedTransactionReportResource(
            type="type_example",
            attributes=AttributedTransactionsReport(
                campaign_ids=[
                    "campaign_ids_example",
                ],
                line_item_ids=[
                    "line_item_ids_example",
                ],
                dimensions=[
                    "campaignName",
                ],
                metrics=[
                    "attributedUnits",
                ],
                account_id="account_id_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                click_attribution_window="7D",
                view_attribution_window="none",
            ),
        ),
    ) # AttributedTransactionReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_attributed_transactions_report(attributed_transaction_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_attributed_transactions_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributed_transaction_report_request** | [**AttributedTransactionReportRequest**](AttributedTransactionReportRequest.md)|  |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_campaign_reports**
> ReportResponse generate_campaign_reports(campaign_report_request)



Return a Campaign Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.campaign_report_request import CampaignReportRequest
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
    campaign_report_request = CampaignReportRequest(
        data=CampaignReportResource(
            type="type_example",
            attributes=CampaignReport(
                report_type="summary",
                campaign_ids=[
                    "campaign_ids_example",
                ],
                metrics=[
                    "impressions",
                ],
                dimensions=[
                    "date",
                ],
                account_id="account_id_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
                click_attribution_window="7D",
                view_attribution_window="none",
                campaign_type="sponsoredProducts",
                sales_channel="offline",
            ),
        ),
    ) # CampaignReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_campaign_reports(campaign_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_campaign_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_report_request** | [**CampaignReportRequest**](CampaignReportRequest.md)|  |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_line_items_reports**
> ReportResponse generate_line_items_reports(line_item_report_request)



Return a Line Item Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.line_item_report_request import LineItemReportRequest
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
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
    line_item_report_request = LineItemReportRequest(
        data=LineItemReportResource(
            type="type_example",
            attributes=LineItemReport(
                report_type="summary",
                line_item_ids=[
                    "line_item_ids_example",
                ],
                campaign_ids=[
                    "campaign_ids_example",
                ],
                metrics=[
                    "impressions",
                ],
                dimensions=[
                    "date",
                ],
                account_id="account_id_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
                click_attribution_window="7D",
                view_attribution_window="1D",
                campaign_type="sponsoredProducts",
                sales_channel="offline",
            ),
        ),
    ) # LineItemReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_line_items_reports(line_item_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->generate_line_items_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_report_request** | [**LineItemReportRequest**](LineItemReportRequest.md)|  |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_export_output**
> str get_async_export_output(report_id)



Return the output of an async report

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

**str**

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



Return the status of an async report

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

# **get_sku_by_product_id**
> ResourceCollectionOutcomeOfSkuSearchResult get_sku_by_product_id(account_id, retailer_id)



Gets a list of SKUs based on a privided list of Product Ids

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import analytics_api
from criteo_api_retailmedia_preview.model.resource_collection_outcome_of_sku_search_result import ResourceCollectionOutcomeOfSkuSearchResult
from criteo_api_retailmedia_preview.model.sku_search_request import SkuSearchRequest
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
    account_id = "accountId_example" # str | account id
    retailer_id = 1 # int | retailer id
    offset = 0 # int | skip a number of matches before retrning results, used with limit (optional) if omitted the server will use the default value of 0
    limit = 100 # int | max number of results to return (optional) if omitted the server will use the default value of 100
    sku_search_request = SkuSearchRequest(
        data=SkuSearchRequestBody(
            product_id_type="SkuKey",
            query_ids=[
                "query_ids_example",
            ],
        ),
    ) # SkuSearchRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sku_by_product_id(account_id, retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_sku_by_product_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sku_by_product_id(account_id, retailer_id, offset=offset, limit=limit, sku_search_request=sku_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_sku_by_product_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id |
 **retailer_id** | **int**| retailer id |
 **offset** | **int**| skip a number of matches before retrning results, used with limit | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| max number of results to return | [optional] if omitted the server will use the default value of 100
 **sku_search_request** | [**SkuSearchRequest**](SkuSearchRequest.md)|  | [optional]

### Return type

[**ResourceCollectionOutcomeOfSkuSearchResult**](ResourceCollectionOutcomeOfSkuSearchResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

