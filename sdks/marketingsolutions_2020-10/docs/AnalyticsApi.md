# criteo_api_marketingsolutions_v2020_10.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adset_report**](AnalyticsApi.md#get_adset_report) | **POST** /2021-04/statistics/report | 
[**get_transactions_report**](AnalyticsApi.md#get_transactions_report) | **POST** /2021-04/transactions/report | 


# **get_adset_report**
> str get_adset_report()



This Statistics endpoint provides adset related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import analytics_api
from criteo_api_marketingsolutions_v2020_10.model.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_api_marketingsolutions_v2020_10.model.error_message import ErrorMessage
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    statistics_report_query_message = StatisticsReportQueryMessage(
        advertiser_ids="advertiser_ids_example",
        dimensions=[
            "AdsetId",
        ],
        metrics=[
            "metrics_example",
        ],
        currency="currency_example",
        format="format_example",
        timezone="UTC",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # StatisticsReportQueryMessage |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_adset_report(statistics_report_query_message=statistics_report_query_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AnalyticsApi->get_adset_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_report_query_message** | [**StatisticsReportQueryMessage**](StatisticsReportQueryMessage.md)|  | [optional]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

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

# **get_transactions_report**
> str get_transactions_report()



This Transactions endpoint provides transactions id related data.

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import analytics_api
from criteo_api_marketingsolutions_v2020_10.model.error_message import ErrorMessage
from criteo_api_marketingsolutions_v2020_10.model.transactions_report_query_data_message import TransactionsReportQueryDataMessage
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    transactions_report_query_data_message = TransactionsReportQueryDataMessage(
        data=[
            TransactionsReportQueryEntityMessage(
                type="type_example",
                attributes=TransactionsReportQueryMessage(
                    advertiser_ids="advertiser_ids_example",
                    event_type="event_type_example",
                    currency="currency_example",
                    format="format_example",
                    timezone="UTC",
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ),
        ],
    ) # TransactionsReportQueryDataMessage |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transactions_report(transactions_report_query_data_message=transactions_report_query_data_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AnalyticsApi->get_transactions_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_report_query_data_message** | [**TransactionsReportQueryDataMessage**](TransactionsReportQueryDataMessage.md)|  | [optional]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

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

