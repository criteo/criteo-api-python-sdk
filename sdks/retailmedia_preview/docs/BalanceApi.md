# criteo_api_retailmedia_preview.BalanceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_balance_by_account_id**](BalanceApi.md#create_balance_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/balances | 
[**get_balance_history**](BalanceApi.md#get_balance_history) | **GET** /preview/retail-media/balances/{balanceId}/history | 
[**update_balance_v1**](BalanceApi.md#update_balance_v1) | **PATCH** /preview/retail-media/accounts/{account-id}/balances/{balance-id} | 


# **create_balance_by_account_id**
> create_balance_by_account_id(account_id, value_resource_input_of_create_balance_v1)



Create balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import balance_api
from criteo_api_retailmedia_preview.model.value_resource_input_of_create_balance_v1 import ValueResourceInputOfCreateBalanceV1
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
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account to create balances for
    value_resource_input_of_create_balance_v1 = ValueResourceInputOfCreateBalanceV1(
        data=ValueResourceOfCreateBalanceV1(
            attributes=CreateBalanceV1(
                deposited=3.14,
                end_date="end_date_example",
                memo="memo_example",
                name="name_example",
                po_number="po_number_example",
                spend_type="unknown",
                start_date="start_date_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfCreateBalanceV1 | An object that represents the available options to set when creating a Retail Media Balance

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_balance_by_account_id(account_id, value_resource_input_of_create_balance_v1)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BalanceApi->create_balance_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to create balances for |
 **value_resource_input_of_create_balance_v1** | [**ValueResourceInputOfCreateBalanceV1**](ValueResourceInputOfCreateBalanceV1.md)| An object that represents the available options to set when creating a Retail Media Balance |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_history**
> PageOfBalanceHistoryChangeDataCaptureV1 get_balance_history(balance_id)



Gets the balance's historical change data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import balance_api
from criteo_api_retailmedia_preview.model.page_of_balance_history_change_data_capture_v1 import PageOfBalanceHistoryChangeDataCaptureV1
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
    api_instance = balance_api.BalanceApi(api_client)
    balance_id = "balanceId_example" # str | Balance id.
    limit = 25 # int | The number of elements to be returned. (optional) if omitted the server will use the default value of 25
    limit_to_change_types = "limitToChangeTypes_example" # str | Comma separated change types string that will be queried. (optional)
    offset = 0 # int | The (zero-based) starting offset in the collection. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_balance_history(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_balance_history(balance_id, limit=limit, limit_to_change_types=limit_to_change_types, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| Balance id. |
 **limit** | **int**| The number of elements to be returned. | [optional] if omitted the server will use the default value of 25
 **limit_to_change_types** | **str**| Comma separated change types string that will be queried. | [optional]
 **offset** | **int**| The (zero-based) starting offset in the collection. | [optional] if omitted the server will use the default value of 0

### Return type

[**PageOfBalanceHistoryChangeDataCaptureV1**](PageOfBalanceHistoryChangeDataCaptureV1.md)

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

# **update_balance_v1**
> update_balance_v1(account_id, balance_id, value_resource_input_of_update_balance_model_v1)



Modify a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import balance_api
from criteo_api_retailmedia_preview.model.value_resource_input_of_update_balance_model_v1 import ValueResourceInputOfUpdateBalanceModelV1
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
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance to change the dates
    value_resource_input_of_update_balance_model_v1 = ValueResourceInputOfUpdateBalanceModelV1(
        data=ValueResourceOfUpdateBalanceModelV1(
            attributes=UpdateBalanceModelV1(
                end_date=NillableOfNullableOfDateOnly(
                    value="value_example",
                ),
                memo="memo_example",
                name="name_example",
                po_number="po_number_example",
                start_date="start_date_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfUpdateBalanceModelV1 | An object that represents the available options to modify a balance.

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_balance_v1(account_id, balance_id, value_resource_input_of_update_balance_model_v1)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling BalanceApi->update_balance_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to change the dates |
 **value_resource_input_of_update_balance_model_v1** | [**ValueResourceInputOfUpdateBalanceModelV1**](ValueResourceInputOfUpdateBalanceModelV1.md)| An object that represents the available options to modify a balance. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

