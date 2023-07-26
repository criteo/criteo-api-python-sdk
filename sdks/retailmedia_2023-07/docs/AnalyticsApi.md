# criteo_api_retailmedia_v2023_07.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_campaign_reports**](AnalyticsApi.md#generate_campaign_reports) | **POST** /2023-07/retail-media/reports/campaigns | 
[**generate_line_items_reports**](AnalyticsApi.md#generate_line_items_reports) | **POST** /2023-07/retail-media/reports/line-items | 
[**get_async_export_output**](AnalyticsApi.md#get_async_export_output) | **GET** /2023-07/retail-media/reports/{reportId}/output | 
[**get_async_export_status**](AnalyticsApi.md#get_async_export_status) | **GET** /2023-07/retail-media/reports/{reportId}/status | 


# **generate_campaign_reports**
> ReportResponse generate_campaign_reports(campaign_report_request)



Return a Campaign Report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2023_07
from criteo_api_retailmedia_v2023_07.api import analytics_api
from criteo_api_retailmedia_v2023_07.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_v2023_07.model.report_response import ReportResponse
from criteo_api_retailmedia_v2023_07.model.campaign_report_request import CampaignReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2023_07.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2023_07.ApiException as e:
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
import criteo_api_retailmedia_v2023_07
from criteo_api_retailmedia_v2023_07.api import analytics_api
from criteo_api_retailmedia_v2023_07.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_v2023_07.model.line_item_report_request import LineItemReportRequest
from criteo_api_retailmedia_v2023_07.model.report_response import ReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2023_07.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2023_07.ApiException as e:
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
import criteo_api_retailmedia_v2023_07
from criteo_api_retailmedia_v2023_07.api import analytics_api
from criteo_api_retailmedia_v2023_07.model.report_outcome import ReportOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2023_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_output(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2023_07.ApiException as e:
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
import criteo_api_retailmedia_v2023_07
from criteo_api_retailmedia_v2023_07.api import analytics_api
from criteo_api_retailmedia_v2023_07.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2023_07.model.report_outcome import ReportOutcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2023_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2023_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | The ID of the report to retrieve

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_status(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2023_07.ApiException as e:
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

