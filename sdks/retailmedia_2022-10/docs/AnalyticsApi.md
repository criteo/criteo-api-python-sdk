# criteo_api_retailmedia_v2022_10.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_output**](AnalyticsApi.md#get_report_output) | **GET** /2022-10/retail-media/reports/{reportId}/output | 
[**get_report_status**](AnalyticsApi.md#get_report_status) | **GET** /2022-10/retail-media/reports/{reportId}/status | 
[**request_campaign_report**](AnalyticsApi.md#request_campaign_report) | **POST** /2022-10/retail-media/reports/campaigns | 
[**request_line_item_report**](AnalyticsApi.md#request_line_item_report) | **POST** /2022-10/retail-media/reports/line-items | 


# **get_report_output**
> str get_report_output(report_id)



Request the report output

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2022_10
from criteo_api_retailmedia_v2022_10.api import analytics_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | report id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_report_output(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_10.ApiException as e:
        print("Exception when calling AnalyticsApi->get_report_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| report id |

### Return type

**str**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The output |  * Content-Disposition - Returns a filename for the output <br>  |
**401** | Missing Authorization or token invalid |  -  |
**403** | Must have access to RetailMedia accounts |  -  |
**404** | ReportId not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_status**
> EnvelopeReportStatus get_report_status(report_id)



Get the status of the report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2022_10
from criteo_api_retailmedia_v2022_10.api import analytics_api
from criteo_api_retailmedia_v2022_10.model.envelope_report_status import EnvelopeReportStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "reportId_example" # str | report id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_report_status(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_10.ApiException as e:
        print("Exception when calling AnalyticsApi->get_report_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| report id |

### Return type

[**EnvelopeReportStatus**](EnvelopeReportStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the status of the report |  -  |
**401** | Missing Authorization or token invalid |  -  |
**403** | Must have access to RetailMedia accounts |  -  |
**404** | ReportId not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_campaign_report**
> EnvelopeReportStatus request_campaign_report(envelope_report_request)



Request a campaign report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2022_10
from criteo_api_retailmedia_v2022_10.api import analytics_api
from criteo_api_retailmedia_v2022_10.model.bad_request import BadRequest
from criteo_api_retailmedia_v2022_10.model.envelope_report_request import EnvelopeReportRequest
from criteo_api_retailmedia_v2022_10.model.envelope_report_status import EnvelopeReportStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    envelope_report_request = EnvelopeReportRequest(
        data=ReportRequest(
            attributes=ReportRequestAttributes(
                click_attribution_window="7D",
                end_date=dateutil_parser('1970-01-01').date(),
                format="json",
                id="id_example",
                ids=[
                    "ids_example",
                ],
                report_type="summary",
                revenue_type="revenue_type_example",
                start_date=dateutil_parser('1970-01-01').date(),
                time_zone="time_zone_example",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # EnvelopeReportRequest | Envelope of the request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.request_campaign_report(envelope_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_10.ApiException as e:
        print("Exception when calling AnalyticsApi->request_campaign_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope_report_request** | [**EnvelopeReportRequest**](EnvelopeReportRequest.md)| Envelope of the request |

### Return type

[**EnvelopeReportStatus**](EnvelopeReportStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the status of the report |  -  |
**400** | Bad request |  -  |
**401** | Missing Authorization or token invalid |  -  |
**403** | Must have access to RetailMedia accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_line_item_report**
> EnvelopeReportStatus request_line_item_report(envelope_report_request)



Request a line item report

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2022_10
from criteo_api_retailmedia_v2022_10.api import analytics_api
from criteo_api_retailmedia_v2022_10.model.bad_request import BadRequest
from criteo_api_retailmedia_v2022_10.model.envelope_report_request import EnvelopeReportRequest
from criteo_api_retailmedia_v2022_10.model.envelope_report_status import EnvelopeReportStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    envelope_report_request = EnvelopeReportRequest(
        data=ReportRequest(
            attributes=ReportRequestAttributes(
                click_attribution_window="7D",
                end_date=dateutil_parser('1970-01-01').date(),
                format="json",
                id="id_example",
                ids=[
                    "ids_example",
                ],
                report_type="summary",
                revenue_type="revenue_type_example",
                start_date=dateutil_parser('1970-01-01').date(),
                time_zone="time_zone_example",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # EnvelopeReportRequest | Envelope of the request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.request_line_item_report(envelope_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_10.ApiException as e:
        print("Exception when calling AnalyticsApi->request_line_item_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope_report_request** | [**EnvelopeReportRequest**](EnvelopeReportRequest.md)| Envelope of the request |

### Return type

[**EnvelopeReportStatus**](EnvelopeReportStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the status of the report |  -  |
**400** | Bad request |  -  |
**401** | Missing Authorization or token invalid |  -  |
**403** | Must have access to RetailMedia accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

