# criteo_api_retailmedia_v2022_01.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_output**](AnalyticsApi.md#get_report_output) | **GET** /2022-01/retail-media/reports/{reportId}/output | 
[**get_report_status**](AnalyticsApi.md#get_report_status) | **GET** /2022-01/retail-media/reports/{reportId}/status | 
[**request_campaign_report**](AnalyticsApi.md#request_campaign_report) | **POST** /2022-01/retail-media/reports/campaigns | 
[**request_line_item_report**](AnalyticsApi.md#request_line_item_report) | **POST** /2022-01/retail-media/reports/line-items | 


# **get_report_output**
> int get_report_output(report_id)



Request the report output

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2022_01
from criteo_api_retailmedia_v2022_01.api import analytics_api
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "ee439121-13e3-4734-9f67-c504dd921a41" # str | report id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_report_output(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_01.ApiException as e:
        print("Exception when calling AnalyticsApi->get_report_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| report id |

### Return type

**int**

### Authorization

[oauth](../README.md#oauth)

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
```python
import time
import criteo_api_retailmedia_v2022_01
from criteo_api_retailmedia_v2022_01.api import analytics_api
from criteo_api_retailmedia_v2022_01.model.envelope_report_status import EnvelopeReportStatus
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "ee439121-13e3-4734-9f67-c504dd921a41" # str | report id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_report_status(report_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_01.ApiException as e:
        print("Exception when calling AnalyticsApi->get_report_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| report id |

### Return type

[**EnvelopeReportStatus**](EnvelopeReportStatus.md)

### Authorization

[oauth](../README.md#oauth)

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
```python
import time
import criteo_api_retailmedia_v2022_01
from criteo_api_retailmedia_v2022_01.api import analytics_api
from criteo_api_retailmedia_v2022_01.model.envelope_report_request import EnvelopeReportRequest
from criteo_api_retailmedia_v2022_01.model.bad_request import BadRequest
from criteo_api_retailmedia_v2022_01.model.envelope_report_status import EnvelopeReportStatus
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_01.ApiClient(configuration) as api_client:
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
                start_date=dateutil_parser('1970-01-01').date(),
                time_zone="time_zone_example",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # EnvelopeReportRequest | // Body of the request {   \"data\": {     \"type\": \"RetailMediaReportRequest\",     \"attributes\": {       \"reportType\": string, // the name of the report being requested       //only one of \"id\" or \"ids\" can be provided for a request       \"id\": string, // the campaign id to select       \"ids\": Array[string], //the campaign ids to select       \"startDate\": string, // YYYY-MM-DD format       \"endDate\": string, // YYYY-MM-DD format       \"timeZone\": string, // examples: 'Europe/London', 'Asia/Tokyo', 'America/New_York'       // both attribution windows must be specified when one is specified       \"clickAttributionWindow\": \"7D\", \"14D\", or \"30D\"  // optional. defaults to campaign's click attribution window       \"viewAttributionWindow\": \"none\", \"1D\", \"7D\", \"14D\", \"30D\" // optional. defaults to campaign's view attribution window       \"format\": One of \"json\" (default),\"json-compact\",\"json-newline\" or \"csv\" // output format, defaults to json-compact     }   } }

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.request_campaign_report(envelope_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_01.ApiException as e:
        print("Exception when calling AnalyticsApi->request_campaign_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope_report_request** | [**EnvelopeReportRequest**](EnvelopeReportRequest.md)| // Body of the request {   \&quot;data\&quot;: {     \&quot;type\&quot;: \&quot;RetailMediaReportRequest\&quot;,     \&quot;attributes\&quot;: {       \&quot;reportType\&quot;: string, // the name of the report being requested       //only one of \&quot;id\&quot; or \&quot;ids\&quot; can be provided for a request       \&quot;id\&quot;: string, // the campaign id to select       \&quot;ids\&quot;: Array[string], //the campaign ids to select       \&quot;startDate\&quot;: string, // YYYY-MM-DD format       \&quot;endDate\&quot;: string, // YYYY-MM-DD format       \&quot;timeZone\&quot;: string, // examples: &#39;Europe/London&#39;, &#39;Asia/Tokyo&#39;, &#39;America/New_York&#39;       // both attribution windows must be specified when one is specified       \&quot;clickAttributionWindow\&quot;: \&quot;7D\&quot;, \&quot;14D\&quot;, or \&quot;30D\&quot;  // optional. defaults to campaign&#39;s click attribution window       \&quot;viewAttributionWindow\&quot;: \&quot;none\&quot;, \&quot;1D\&quot;, \&quot;7D\&quot;, \&quot;14D\&quot;, \&quot;30D\&quot; // optional. defaults to campaign&#39;s view attribution window       \&quot;format\&quot;: One of \&quot;json\&quot; (default),\&quot;json-compact\&quot;,\&quot;json-newline\&quot; or \&quot;csv\&quot; // output format, defaults to json-compact     }   } } |

### Return type

[**EnvelopeReportStatus**](EnvelopeReportStatus.md)

### Authorization

[oauth](../README.md#oauth)

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
```python
import time
import criteo_api_retailmedia_v2022_01
from criteo_api_retailmedia_v2022_01.api import analytics_api
from criteo_api_retailmedia_v2022_01.model.envelope_report_request import EnvelopeReportRequest
from criteo_api_retailmedia_v2022_01.model.bad_request import BadRequest
from criteo_api_retailmedia_v2022_01.model.envelope_report_status import EnvelopeReportStatus
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_01.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_01.ApiClient(configuration) as api_client:
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
                start_date=dateutil_parser('1970-01-01').date(),
                time_zone="time_zone_example",
                view_attribution_window="none",
            ),
            type="type_example",
        ),
    ) # EnvelopeReportRequest | // Body of the request {   \"data\": {     \"type\": \"RetailMediaReportRequest\",     \"attributes\": {       \"reportType\": string, // the name of the report being requested       //only one of \"id\" or \"ids\" can be provided for a request       \"id\": string, // the line item id to select       \"ids: Array[string] // the line item ids to select       \"startDate\": string, // YYYY-MM-DD format       \"endDate\": string, // YYYY-MM-DD format       \"timeZone\": string, // examples: 'Europe/London', 'Asia/Tokyo', 'America/New_York'       // both attribution windows must be specified when one is specified       \"clickAttributionWindow\": \"7D\", \"14D\", or \"30D\"  // optional. defaults to campaign's click attribution window       \"viewAttributionWindow\": \"none\", \"1D\", \"7D\", \"14D\", \"30D\" // optional. defaults to campaign's view attribution window       \"format\": One of \"json\" (default),\"json-compact\",\"json-newline\" or \"csv\" // output format, defaults to json-compact     }   } }

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.request_line_item_report(envelope_report_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_01.ApiException as e:
        print("Exception when calling AnalyticsApi->request_line_item_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope_report_request** | [**EnvelopeReportRequest**](EnvelopeReportRequest.md)| // Body of the request {   \&quot;data\&quot;: {     \&quot;type\&quot;: \&quot;RetailMediaReportRequest\&quot;,     \&quot;attributes\&quot;: {       \&quot;reportType\&quot;: string, // the name of the report being requested       //only one of \&quot;id\&quot; or \&quot;ids\&quot; can be provided for a request       \&quot;id\&quot;: string, // the line item id to select       \&quot;ids: Array[string] // the line item ids to select       \&quot;startDate\&quot;: string, // YYYY-MM-DD format       \&quot;endDate\&quot;: string, // YYYY-MM-DD format       \&quot;timeZone\&quot;: string, // examples: &#39;Europe/London&#39;, &#39;Asia/Tokyo&#39;, &#39;America/New_York&#39;       // both attribution windows must be specified when one is specified       \&quot;clickAttributionWindow\&quot;: \&quot;7D\&quot;, \&quot;14D\&quot;, or \&quot;30D\&quot;  // optional. defaults to campaign&#39;s click attribution window       \&quot;viewAttributionWindow\&quot;: \&quot;none\&quot;, \&quot;1D\&quot;, \&quot;7D\&quot;, \&quot;14D\&quot;, \&quot;30D\&quot; // optional. defaults to campaign&#39;s view attribution window       \&quot;format\&quot;: One of \&quot;json\&quot; (default),\&quot;json-compact\&quot;,\&quot;json-newline\&quot; or \&quot;csv\&quot; // output format, defaults to json-compact     }   } } |

### Return type

[**EnvelopeReportStatus**](EnvelopeReportStatus.md)

### Authorization

[oauth](../README.md#oauth)

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

