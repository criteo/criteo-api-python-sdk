# criteo_api_marketingsolutions_v2024_07.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adset_report**](AnalyticsApi.md#get_adset_report) | **POST** /2024-07/statistics/report | 
[**get_placements_report**](AnalyticsApi.md#get_placements_report) | **POST** /2024-07/placements/report | 
[**get_transactions_report**](AnalyticsApi.md#get_transactions_report) | **POST** /2024-07/transactions/report | 
[**get_transparency_report**](AnalyticsApi.md#get_transparency_report) | **POST** /2024-07/log-level/advertisers/{advertiser-id}/report | 


# **get_adset_report**
> file_type get_adset_report()



This Statistics endpoint provides adset related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import analytics_api
from criteo_api_marketingsolutions_v2024_07.model.statistics_report_query_message import StatisticsReportQueryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    statistics_report_query_message = StatisticsReportQueryMessage(
        ad_set_ids=[
            "ad_set_ids_example",
        ],
        ad_set_names=[
            "ad_set_names_example",
        ],
        ad_set_status=[
            "ad_set_status_example",
        ],
        advertiser_ids="advertiser_ids_example",
        currency="currency_example",
        dimensions=[
            "AdsetId",
        ],
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        format="json",
        metrics=[
            "Clicks",
        ],
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        timezone="UTC",
    ) # StatisticsReportQueryMessage |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_adset_report(statistics_report_query_message=statistics_report_query_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling AnalyticsApi->get_adset_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_report_query_message** | [**StatisticsReportQueryMessage**](StatisticsReportQueryMessage.md)|  | [optional]

### Return type

**file_type**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, text/xml, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placements_report**
> file_type get_placements_report()



Your ads are placed in different domains (publishers) and environments (websites and apps). Thanks to the placements endpoint, you can analyse the performances for each publisher, comparing displays, clicks and sales generated.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import analytics_api
from criteo_api_marketingsolutions_v2024_07.model.placements_report_query_message_list_request import PlacementsReportQueryMessageListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    placements_report_query_message_list_request = PlacementsReportQueryMessageListRequest(
        data=[
            PlacementsReportQueryMessageResource(
                attributes=PlacementsReportQueryMessage(
                    adset_ids="adset_ids_example",
                    advertiser_ids="advertiser_ids_example",
                    campaign_ids="campaign_ids_example",
                    currency="currency_example",
                    dimensions=[
                        "AdsetId",
                    ],
                    disclosed=True,
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    environment="environment_example",
                    format="json",
                    metrics=[
                        "metrics_example",
                    ],
                    placement="placement_example",
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    timezone="UTC",
                ),
                type="type_example",
            ),
        ],
    ) # PlacementsReportQueryMessageListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_placements_report(placements_report_query_message_list_request=placements_report_query_message_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling AnalyticsApi->get_placements_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placements_report_query_message_list_request** | [**PlacementsReportQueryMessageListRequest**](PlacementsReportQueryMessageListRequest.md)|  | [optional]

### Return type

**file_type**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/csv, text/xml, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_report**
> file_type get_transactions_report()



This Transactions endpoint provides transactions id related data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import analytics_api
from criteo_api_marketingsolutions_v2024_07.model.transactions_report_query_message_list_request import TransactionsReportQueryMessageListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    transactions_report_query_message_list_request = TransactionsReportQueryMessageListRequest(
        data=[
            TransactionsReportQueryMessageResource(
                attributes=TransactionsReportQueryMessage(
                    advertiser_ids="advertiser_ids_example",
                    currency="currency_example",
                    end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    event_type="event_type_example",
                    format="json",
                    start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    timezone="UTC",
                ),
                type="type_example",
            ),
        ],
    ) # TransactionsReportQueryMessageListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transactions_report(transactions_report_query_message_list_request=transactions_report_query_message_list_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling AnalyticsApi->get_transactions_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_report_query_message_list_request** | [**TransactionsReportQueryMessageListRequest**](TransactionsReportQueryMessageListRequest.md)|  | [optional]

### Return type

**file_type**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, text/csv, text/xml, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transparency_report**
> TransparencyReportListResponse get_transparency_report(advertiser_id)



This Statistics endpoint provides publisher data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import analytics_api
from criteo_api_marketingsolutions_v2024_07.model.transparency_query_message import TransparencyQueryMessage
from criteo_api_marketingsolutions_v2024_07.model.transparency_report_list_response import TransparencyReportListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    advertiser_id = 1 # int | The advertiser id to fetch the transparency data.
    transparency_query_message = TransparencyQueryMessage(
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        should_display_product_ids=False,
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # TransparencyQueryMessage | The query message. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transparency_report(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling AnalyticsApi->get_transparency_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transparency_report(advertiser_id, transparency_query_message=transparency_query_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling AnalyticsApi->get_transparency_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| The advertiser id to fetch the transparency data. |
 **transparency_query_message** | [**TransparencyQueryMessage**](TransparencyQueryMessage.md)| The query message. | [optional]

### Return type

[**TransparencyReportListResponse**](TransparencyReportListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

