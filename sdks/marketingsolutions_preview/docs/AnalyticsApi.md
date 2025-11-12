# criteo_api_marketingsolutions_preview.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adset_report**](AnalyticsApi.md#get_adset_report) | **POST** /preview/statistics/report | 
[**get_async_adset_report**](AnalyticsApi.md#get_async_adset_report) | **POST** /preview/reports/async-statistics | 
[**get_async_audience_report**](AnalyticsApi.md#get_async_audience_report) | **POST** /preview/reports/async-audience-performance | 
[**get_async_export_output**](AnalyticsApi.md#get_async_export_output) | **GET** /preview/reports/{report-id}/output | 
[**get_async_export_status**](AnalyticsApi.md#get_async_export_status) | **GET** /preview/reports/{report-id}/status | 
[**get_categories_report**](AnalyticsApi.md#get_categories_report) | **POST** /preview/categories/report | 
[**get_creatives_report**](AnalyticsApi.md#get_creatives_report) | **POST** /preview/reports/creatives | 
[**get_placements_report**](AnalyticsApi.md#get_placements_report) | **POST** /preview/placements/report | 
[**get_realtime_statistics_report**](AnalyticsApi.md#get_realtime_statistics_report) | **POST** /preview/reports/realtime | 
[**get_top_products_report**](AnalyticsApi.md#get_top_products_report) | **POST** /preview/reports/top-products | 
[**get_transactions_report**](AnalyticsApi.md#get_transactions_report) | **POST** /preview/transactions/report | 
[**get_transparency_report**](AnalyticsApi.md#get_transparency_report) | **POST** /preview/log-level/advertisers/{advertiser-id}/report | 


# **get_adset_report**
> file_type get_adset_report()



This Statistics endpoint provides adset related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.statistics_report_query_message import StatisticsReportQueryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

# **get_async_adset_report**
> MarketingSolutionsReportStatusResponse get_async_adset_report(generate_statistics_report_request)



This Statistics endpoint provides an export Id that let you retrieve data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.generate_statistics_report_request import GenerateStatisticsReportRequest
from criteo_api_marketingsolutions_preview.model.marketing_solutions_report_status_response import MarketingSolutionsReportStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    generate_statistics_report_request = GenerateStatisticsReportRequest(
        data=GenerateStatisticsReportResource(
            attributes=GenerateStatisticsReport(
                ad_set_ids=[
                    "ad_set_ids_example",
                ],
                ad_set_names=[
                    "ad_set_names_example",
                ],
                ad_set_status=[
                    "ad_set_status_example",
                ],
                advertiser_ids=[
                    "advertiser_ids_example",
                ],
                currency="currency_example",
                dimensions=[
                    "AdvertiserId",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                metrics=[
                    "Clicks",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
            ),
            type="type_example",
        ),
    ) # GenerateStatisticsReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_adset_report(generate_statistics_report_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_async_adset_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_statistics_report_request** | [**GenerateStatisticsReportRequest**](GenerateStatisticsReportRequest.md)|  |

### Return type

[**MarketingSolutionsReportStatusResponse**](MarketingSolutionsReportStatusResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_audience_report**
> MarketingSolutionsReportStatusResponse get_async_audience_report()



This Statistics endpoint provides an export Id that lets you retrieve data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.generate_audience_performance_report_request import GenerateAudiencePerformanceReportRequest
from criteo_api_marketingsolutions_preview.model.marketing_solutions_report_status_response import MarketingSolutionsReportStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    generate_audience_performance_report_request = GenerateAudiencePerformanceReportRequest(
        data=GenerateAudiencePerformanceReportResource(
            attributes=GenerateAudiencePerformanceReport(
                ad_set_ids=[
                    "ad_set_ids_example",
                ],
                advertiser_id="advertiser_id_example",
                audience_ids=[
                    "audience_ids_example",
                ],
                currency="currency_example",
                dimension="Top30BrandsByDisplays",
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                metrics=[
                    "Clicks",
                ],
                segments_ids=[
                    "segments_ids_example",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
            ),
            type="type_example",
        ),
    ) # GenerateAudiencePerformanceReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_async_audience_report(generate_audience_performance_report_request=generate_audience_performance_report_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_async_audience_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_audience_performance_report_request** | [**GenerateAudiencePerformanceReportRequest**](GenerateAudiencePerformanceReportRequest.md)|  | [optional]

### Return type

[**MarketingSolutionsReportStatusResponse**](MarketingSolutionsReportStatusResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_export_output**
> ExportResult get_async_export_output(report_id)



This endpoint gives you the output of the report.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.export_result import ExportResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "report-id_example" # str | Id of the report

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_output(report_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_async_export_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Id of the report |

### Return type

[**ExportResult**](ExportResult.md)

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
> MarketingSolutionsReportStatusResponse get_async_export_status(report_id)



This endpoint gives you the status of the report.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.marketing_solutions_report_status_response import MarketingSolutionsReportStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    report_id = "report-id_example" # str | Id of the report

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_async_export_status(report_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_async_export_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Id of the report |

### Return type

[**MarketingSolutionsReportStatusResponse**](MarketingSolutionsReportStatusResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_report**
> file_type get_categories_report()



With this endpoint you can analyse what are the categories of the placements' domains your ads are placed in.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.generate_categories_report_request_attributes_request import GenerateCategoriesReportRequestAttributesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    generate_categories_report_request_attributes_request = GenerateCategoriesReportRequestAttributesRequest(
        data=GenerateCategoriesReportRequestAttributesResource(
            attributes=GenerateCategoriesReportRequestAttributes(
                adset_id="adset_id_example",
                advertiser_ids=[
                    "advertiser_ids_example",
                ],
                campaign_id="campaign_id_example",
                category="category_example",
                domain="domain_example",
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                format="json",
                should_display_domain_dimension=True,
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
            ),
            type="type_example",
        ),
    ) # GenerateCategoriesReportRequestAttributesRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_categories_report(generate_categories_report_request_attributes_request=generate_categories_report_request_attributes_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_categories_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_categories_report_request_attributes_request** | [**GenerateCategoriesReportRequestAttributesRequest**](GenerateCategoriesReportRequestAttributesRequest.md)|  | [optional]

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

# **get_creatives_report**
> JsonReportRowsListResponse get_creatives_report(generate_creatives_report_request_attributes_request)



With Creatives endpoint, you can analyse the daily performances of your creatives on the main metrics: clicks, ctr, displays.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.json_report_rows_list_response import JsonReportRowsListResponse
from criteo_api_marketingsolutions_preview.model.generate_creatives_report_request_attributes_request import GenerateCreativesReportRequestAttributesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    generate_creatives_report_request_attributes_request = GenerateCreativesReportRequestAttributesRequest(
        data=GenerateCreativesReportRequestAttributesResource(
            attributes=GenerateCreativesReportRequestAttributes(
                ad_formats=[
                    "ad_formats_example",
                ],
                ad_ids=[
                    "ad_ids_example",
                ],
                ad_names=[
                    "ad_names_example",
                ],
                ad_set_ids=[
                    "ad_set_ids_example",
                ],
                ad_set_status=[
                    "ad_set_status_example",
                ],
                advertiser_ids=[
                    "advertiser_ids_example",
                ],
                campaign_ids=[
                    "campaign_ids_example",
                ],
                coupon_ids=[
                    "coupon_ids_example",
                ],
                coupon_names=[
                    "coupon_names_example",
                ],
                dimensions=[
                    "AdFormat",
                ],
                display_sizes=[
                    "display_sizes_example",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                metrics=[
                    "Clicks",
                ],
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="timezone_example",
            ),
            type="type_example",
        ),
    ) # GenerateCreativesReportRequestAttributesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_creatives_report(generate_creatives_report_request_attributes_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_creatives_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_creatives_report_request_attributes_request** | [**GenerateCreativesReportRequestAttributesRequest**](GenerateCreativesReportRequestAttributesRequest.md)|  |

### Return type

[**JsonReportRowsListResponse**](JsonReportRowsListResponse.md)

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

# **get_placements_report**
> file_type get_placements_report()



Your ads are placed in different domains (publishers) and environments (websites and apps). Thanks to the placements endpoint, you can analyse the performances for each publisher, comparing displays, clicks and sales generated.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.placements_report_query_message_list_request import PlacementsReportQueryMessageListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

# **get_realtime_statistics_report**
> JsonReportRowsListResponse get_realtime_statistics_report()



With Realtime endpoint, you can analyse the realtime values of the main metrics: displays, clicks, cost.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.json_report_rows_list_response import JsonReportRowsListResponse
from criteo_api_marketingsolutions_preview.model.generate_realtime_statistics_report_request_attributes_request import GenerateRealtimeStatisticsReportRequestAttributesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    generate_realtime_statistics_report_request_attributes_request = GenerateRealtimeStatisticsReportRequestAttributesRequest(
        data=GenerateRealtimeStatisticsReportRequestAttributesResource(
            attributes=GenerateRealtimeStatisticsReportRequestAttributes(
                adset_ids=[
                    "adset_ids_example",
                ],
                advertiser_ids=[
                    "advertiser_ids_example",
                ],
                campaign_ids=[
                    "campaign_ids_example",
                ],
                currency="EUR",
                dimensions=["AdvertiserId","Advertiser","CampaignId","Campaign","AdsetId","Adset","Day","Hour"],
                lookback_window=12,
                metrics=["Displays","Clicks","Cost"],
                timezone="UTC",
            ),
            type="type_example",
        ),
    ) # GenerateRealtimeStatisticsReportRequestAttributesRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_realtime_statistics_report(generate_realtime_statistics_report_request_attributes_request=generate_realtime_statistics_report_request_attributes_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_realtime_statistics_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_realtime_statistics_report_request_attributes_request** | [**GenerateRealtimeStatisticsReportRequestAttributesRequest**](GenerateRealtimeStatisticsReportRequestAttributesRequest.md)|  | [optional]

### Return type

[**JsonReportRowsListResponse**](JsonReportRowsListResponse.md)

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

# **get_top_products_report**
> JsonReportRowsListResponse get_top_products_report(generate_top_products_report_request_attributes_request)



With the topProducts endpoint, you can analyse the performances for each publisher, by top displays, top clicks or top sales.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.generate_top_products_report_request_attributes_request import GenerateTopProductsReportRequestAttributesRequest
from criteo_api_marketingsolutions_preview.model.json_report_rows_list_response import JsonReportRowsListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    generate_top_products_report_request_attributes_request = GenerateTopProductsReportRequestAttributesRequest(
        data=GenerateTopProductsReportRequestAttributesResource(
            attributes=GenerateTopProductsReportRequestAttributes(
                ad_set_ids=[
                    "ad_set_ids_example",
                ],
                ad_set_status=[
                    "ad_set_status_example",
                ],
                advertiser_id="advertiser_id_example",
                brands=[
                    "brands_example",
                ],
                campaign_ids=[
                    "campaign_ids_example",
                ],
                category_ids=[
                    "category_ids_example",
                ],
                currency="EUR",
                dimensions=[
                    "Campaign",
                ],
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                limit=1,
                metrics=[
                    "Clicks",
                ],
                rank_products_by="Clicks",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                timezone="UTC",
            ),
            type="type_example",
        ),
    ) # GenerateTopProductsReportRequestAttributesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_top_products_report(generate_top_products_report_request_attributes_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_top_products_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_top_products_report_request_attributes_request** | [**GenerateTopProductsReportRequestAttributesRequest**](GenerateTopProductsReportRequestAttributesRequest.md)|  |

### Return type

[**JsonReportRowsListResponse**](JsonReportRowsListResponse.md)

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

# **get_transactions_report**
> file_type get_transactions_report()



This Transactions endpoint provides transactions id related data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.transactions_report_query_message_list_request import TransactionsReportQueryMessageListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
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
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import analytics_api
from criteo_api_marketingsolutions_preview.model.transparency_report_list_response import TransparencyReportListResponse
from criteo_api_marketingsolutions_preview.model.transparency_query_message import TransparencyQueryMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
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
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling AnalyticsApi->get_transparency_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transparency_report(advertiser_id, transparency_query_message=transparency_query_message)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

