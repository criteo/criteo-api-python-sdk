# criteo_api_retailmedia_v2025_07.BillingApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_07_retail_media_billing_partner_report_post**](BillingApi.md#call_07_retail_media_billing_partner_report_post) | **POST** /2025-07/retail-media/billing/partner-report | 
[**call_07_retail_media_billing_partner_report_request_id_output_get**](BillingApi.md#call_07_retail_media_billing_partner_report_request_id_output_get) | **GET** /2025-07/retail-media/billing/partner-report/{requestId}/output | 
[**call_07_retail_media_billing_partner_report_request_id_status_get**](BillingApi.md#call_07_retail_media_billing_partner_report_request_id_status_get) | **GET** /2025-07/retail-media/billing/partner-report/{requestId}/status | 


# **call_07_retail_media_billing_partner_report_post**
> EntityResourceOutcomePartnerBillingReportStatusV1 call_07_retail_media_billing_partner_report_post()



Create a Partner Billing Report request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import billing_api
from criteo_api_retailmedia_v2025_07.model.value_resource_input_partner_billing_report_request_v1 import ValueResourceInputPartnerBillingReportRequestV1
from criteo_api_retailmedia_v2025_07.model.entity_resource_outcome_partner_billing_report_status_v1 import EntityResourceOutcomePartnerBillingReportStatusV1
from criteo_api_retailmedia_v2025_07.model.outcome import Outcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = billing_api.BillingApi(api_client)
    value_resource_input_partner_billing_report_request_v1 = ValueResourceInputPartnerBillingReportRequestV1(
        data=ValueResourcePartnerBillingReportRequestV1(
            attributes=PartnerBillingReportRequestV1(
                account_ids=[
                    "account_ids_example",
                ],
                end_date=dateutil_parser('1970-01-01').date(),
                format="json",
                retailer_ids=[
                    1,
                ],
                start_date=dateutil_parser('1970-01-01').date(),
            ),
            type="type_example",
        ),
    ) # ValueResourceInputPartnerBillingReportRequestV1 | Partner Billing Report request object. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.call_07_retail_media_billing_partner_report_post(value_resource_input_partner_billing_report_request_v1=value_resource_input_partner_billing_report_request_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling BillingApi->call_07_retail_media_billing_partner_report_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value_resource_input_partner_billing_report_request_v1** | [**ValueResourceInputPartnerBillingReportRequestV1**](ValueResourceInputPartnerBillingReportRequestV1.md)| Partner Billing Report request object. | [optional]

### Return type

[**EntityResourceOutcomePartnerBillingReportStatusV1**](EntityResourceOutcomePartnerBillingReportStatusV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_07_retail_media_billing_partner_report_request_id_output_get**
> file_type call_07_retail_media_billing_partner_report_request_id_output_get(request_id)



Get the output of an existing Partner Billing Report.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import billing_api
from criteo_api_retailmedia_v2025_07.model.outcome import Outcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = billing_api.BillingApi(api_client)
    request_id = "requestId_example" # str | The id of a Partner Billing Report request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.call_07_retail_media_billing_partner_report_request_id_output_get(request_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling BillingApi->call_07_retail_media_billing_partner_report_request_id_output_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The id of a Partner Billing Report request. |

### Return type

**file_type**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_07_retail_media_billing_partner_report_request_id_status_get**
> EntityResourceOutcomePartnerBillingReportStatusV1 call_07_retail_media_billing_partner_report_request_id_status_get(request_id)



Get the status of an existing Partner Billing Report.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import billing_api
from criteo_api_retailmedia_v2025_07.model.entity_resource_outcome_partner_billing_report_status_v1 import EntityResourceOutcomePartnerBillingReportStatusV1
from criteo_api_retailmedia_v2025_07.model.outcome import Outcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = billing_api.BillingApi(api_client)
    request_id = "requestId_example" # str | The id of a Partner Billing Report request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.call_07_retail_media_billing_partner_report_request_id_status_get(request_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling BillingApi->call_07_retail_media_billing_partner_report_request_id_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The id of a Partner Billing Report request. |

### Return type

[**EntityResourceOutcomePartnerBillingReportStatusV1**](EntityResourceOutcomePartnerBillingReportStatusV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

