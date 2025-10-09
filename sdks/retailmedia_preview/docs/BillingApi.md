# criteo_api_retailmedia_preview.BillingApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_partner_billing_report_request_v1**](BillingApi.md#create_partner_billing_report_request_v1) | **POST** /preview/retail-media/billing/partner-report | 
[**get_partner_billing_report_output_v1**](BillingApi.md#get_partner_billing_report_output_v1) | **GET** /preview/retail-media/billing/partner-report/{requestId}/output | 
[**get_partner_billing_report_status_v1**](BillingApi.md#get_partner_billing_report_status_v1) | **GET** /preview/retail-media/billing/partner-report/{requestId}/status | 


# **create_partner_billing_report_request_v1**
> EntityResourceOutcomePartnerBillingReportStatusV1 create_partner_billing_report_request_v1()



Create a Partner Billing Report request.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import billing_api
from criteo_api_retailmedia_preview.model.value_resource_input_partner_billing_report_request_v1 import ValueResourceInputPartnerBillingReportRequestV1
from criteo_api_retailmedia_preview.model.entity_resource_outcome_partner_billing_report_status_v1 import EntityResourceOutcomePartnerBillingReportStatusV1
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
        api_response = api_instance.create_partner_billing_report_request_v1(value_resource_input_partner_billing_report_request_v1=value_resource_input_partner_billing_report_request_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BillingApi->create_partner_billing_report_request_v1: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partner_billing_report_output_v1**
> file_type get_partner_billing_report_output_v1(request_id)



Get the output of an existing Partner Billing Report.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)
    request_id = "requestId_example" # str | The id of a Partner Billing Report request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_partner_billing_report_output_v1(request_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BillingApi->get_partner_billing_report_output_v1: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partner_billing_report_status_v1**
> EntityResourceOutcomePartnerBillingReportStatusV1 get_partner_billing_report_status_v1(request_id)



Get the status of an existing Partner Billing Report.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import billing_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_partner_billing_report_status_v1 import EntityResourceOutcomePartnerBillingReportStatusV1
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
    api_instance = billing_api.BillingApi(api_client)
    request_id = "requestId_example" # str | The id of a Partner Billing Report request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_partner_billing_report_status_v1(request_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BillingApi->get_partner_billing_report_status_v1: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

