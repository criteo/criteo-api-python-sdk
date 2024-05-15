# criteo_api_retailmedia_v2024_04.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_async_campaigns_report**](AnalyticsApi.md#generate_async_campaigns_report) | **POST** /2024-04/retail-media/reports/campaigns | 
[**generate_async_line_items_report**](AnalyticsApi.md#generate_async_line_items_report) | **POST** /2024-04/retail-media/reports/line-items | 
[**generate_async_revenue_report**](AnalyticsApi.md#generate_async_revenue_report) | **POST** /2024-04/retail-media/reports/revenue | 
[**get_async_export_output**](AnalyticsApi.md#get_async_export_output) | **GET** /2024-04/retail-media/reports/{reportId}/output | 
[**get_async_export_status**](AnalyticsApi.md#get_async_export_status) | **GET** /2024-04/retail-media/reports/{reportId}/status | 


# **generate_async_campaigns_report**
> AsyncReportResponse generate_async_campaigns_report(async_campaigns_report_request)



Return an asynchronous Campaigns Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import analytics_api
from criteo_api_retailmedia_v2024_04.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2024_04.model.async_campaigns_report_request import AsyncCampaignsReportRequest
from criteo_api_retailmedia_v2024_04.model.report_outcome import ReportOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_campaigns_report_request = AsyncCampaignsReportRequest(
        data=AsyncCampaignsReportResource(
            type="type_example",
            attributes=AsyncCampaignsReport(
                ids=[
                    "ids_example",
                ],
                id="id_example",
                campaign_type="all",
                sales_channel="all",
                format="json-compact",
                report_type="summary",
                click_attribution_window="none",
                view_attribution_window="none",
                dimensions=[
                    "date",
                ],
                metrics=[
                    "impressions",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
            ),
        ),
    ) # AsyncCampaignsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_campaigns_report(async_campaigns_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
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

# **generate_async_line_items_report**
> AsyncReportResponse generate_async_line_items_report(async_line_items_report_request)



Returns an asynchronous Line Items Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import analytics_api
from criteo_api_retailmedia_v2024_04.model.async_line_items_report_request import AsyncLineItemsReportRequest
from criteo_api_retailmedia_v2024_04.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2024_04.model.report_outcome import ReportOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_line_items_report_request = AsyncLineItemsReportRequest(
        data=AsyncLineItemsReportResource(
            type="type_example",
            attributes=AsyncLineItemsReport(
                ids=[
                    "ids_example",
                ],
                id="id_example",
                campaign_type="all",
                sales_channel="all",
                format="json-compact",
                report_type="summary",
                click_attribution_window="none",
                view_attribution_window="none",
                dimensions=[
                    "date",
                ],
                metrics=[
                    "impressions",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
            ),
        ),
    ) # AsyncLineItemsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_line_items_report(async_line_items_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
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

# **generate_async_revenue_report**
> AsyncReportResponse generate_async_revenue_report(async_revenue_report_request)



Returns an asynchronous Revenue Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import analytics_api
from criteo_api_retailmedia_v2024_04.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2024_04.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_v2024_04.model.async_revenue_report_request import AsyncRevenueReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    async_revenue_report_request = AsyncRevenueReportRequest(
        data=AsyncRevenueReportResource(
            type="type_example",
            attributes=AsyncRevenueReport(
                ids=[
                    "ids_example",
                ],
                id="id_example",
                report_type="advertiser",
                revenue_type="auction",
                sold_by="directSold",
                buy_type="auction",
                sku_relations=[
                    "sameSku",
                ],
                format="json",
                campaign_type="all",
                sales_channel="all",
                click_attribution_window="none",
                view_attribution_window="none",
                dimensions=[
                    "date",
                ],
                metrics=[
                    "numberOfCampaigns",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
            ),
        ),
    ) # AsyncRevenueReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_async_revenue_report(async_revenue_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
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

# **get_async_export_output**
> str get_async_export_output(report_id)



Returns the output of an async report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import analytics_api
from criteo_api_retailmedia_v2024_04.model.report_outcome import ReportOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_output(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
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



Returns the status of an async report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import analytics_api
from criteo_api_retailmedia_v2024_04.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2024_04.model.report_outcome import ReportOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_status(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
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

