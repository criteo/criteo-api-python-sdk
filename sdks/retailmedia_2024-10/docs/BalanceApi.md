# criteo_api_retailmedia_v2024_10.BalanceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api202110_external_balance_campaigns_by_balance_id**](BalanceApi.md#get_api202110_external_balance_campaigns_by_balance_id) | **GET** /2024-10/retail-media/balances/{balance-id}/campaigns | 
[**get_api_v2_external_account_balances_by_account_id**](BalanceApi.md#get_api_v2_external_account_balances_by_account_id) | **GET** /2024-10/retail-media/accounts/{account-id}/balances | 
[**get_api_v2_external_account_by_account_id_balancesbalance_id**](BalanceApi.md#get_api_v2_external_account_by_account_id_balancesbalance_id) | **GET** /2024-10/retail-media/accounts/{account-id}/balances/{balance-id} | 
[**get_balance_history**](BalanceApi.md#get_balance_history) | **GET** /2024-10/retail-media/balances/{balanceId}/history | 
[**patch_api_v2_external_account_by_account_id_balancesbalance_id**](BalanceApi.md#patch_api_v2_external_account_by_account_id_balancesbalance_id) | **PATCH** /2024-10/retail-media/accounts/{account-id}/balances/{balance-id} | 
[**post_api_v2_external_account_add_funds_by_account_id_balancesbalance_id**](BalanceApi.md#post_api_v2_external_account_add_funds_by_account_id_balancesbalance_id) | **POST** /2024-10/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds | 
[**post_api_v2_external_account_balances_by_account_id**](BalanceApi.md#post_api_v2_external_account_balances_by_account_id) | **POST** /2024-10/retail-media/accounts/{account-id}/balances | 
[**post_api_v2_external_account_change_dates_by_account_id_balancesbalance_id**](BalanceApi.md#post_api_v2_external_account_change_dates_by_account_id_balancesbalance_id) | **POST** /2024-10/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates | 


# **get_api202110_external_balance_campaigns_by_balance_id**
> BalanceCampaign202110PagedListResponse get_api202110_external_balance_campaigns_by_balance_id(balance_id)



Gets page of campaigns for the given balanceId

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    balance_id = "balance-id_example" # str | The balance to get campaigns from
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202110_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->get_api202110_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api202110_external_balance_campaigns_by_balance_id(balance_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->get_api202110_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to get campaigns from |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**BalanceCampaign202110PagedListResponse**](BalanceCampaign202110PagedListResponse.md)

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

# **get_api_v2_external_account_balances_by_account_id**
> PagedResourceCollectionOutcomeOfBalanceResponseV2 get_api_v2_external_account_balances_by_account_id(account_id)



Gets page of balance objects for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.paged_resource_collection_outcome_of_balance_response_v2 import PagedResourceCollectionOutcomeOfBalanceResponseV2
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account to get balances for
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_account_balances_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->get_api_v2_external_account_balances_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v2_external_account_balances_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->get_api_v2_external_account_balances_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to get balances for |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

### Return type

[**PagedResourceCollectionOutcomeOfBalanceResponseV2**](PagedResourceCollectionOutcomeOfBalanceResponseV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v2_external_account_by_account_id_balancesbalance_id**
> BalanceResponseV2Response get_api_v2_external_account_by_account_id_balancesbalance_id(account_id, balance_id)



Get a balance for the given account id and balance id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.balance_response_v2_response import BalanceResponseV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v2_external_account_by_account_id_balancesbalance_id(account_id, balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->get_api_v2_external_account_by_account_id_balancesbalance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance id |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_history**
> PageOfBalanceHistoryChangeDataCaptureV1 get_balance_history(balance_id)



Gets the balance's historical change data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.page_of_balance_history_change_data_capture_v1 import PageOfBalanceHistoryChangeDataCaptureV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_balance_history(balance_id, limit=limit, limit_to_change_types=limit_to_change_types, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
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

# **patch_api_v2_external_account_by_account_id_balancesbalance_id**
> BalanceResponseV2Response patch_api_v2_external_account_by_account_id_balancesbalance_id(account_id, balance_id, update_balance_model_v2_request)



Modify a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.balance_response_v2_response import BalanceResponseV2Response
from criteo_api_retailmedia_v2024_10.model.update_balance_model_v2_request import UpdateBalanceModelV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance to change the dates
    update_balance_model_v2_request = UpdateBalanceModelV2Request(
        data=ResourceOfUpdateBalanceModelV2(
            attributes=UpdateBalanceModelV2(
                end_date="end_date_example",
                memo="memo_example",
                name="name_example",
                po_number="po_number_example",
                start_date="start_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # UpdateBalanceModelV2Request | An object that represents the available options to modify a balance.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_api_v2_external_account_by_account_id_balancesbalance_id(account_id, balance_id, update_balance_model_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->patch_api_v2_external_account_by_account_id_balancesbalance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to change the dates |
 **update_balance_model_v2_request** | [**UpdateBalanceModelV2Request**](UpdateBalanceModelV2Request.md)| An object that represents the available options to modify a balance. |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v2_external_account_add_funds_by_account_id_balancesbalance_id**
> BalanceResponseV2Response post_api_v2_external_account_add_funds_by_account_id_balancesbalance_id(account_id, balance_id, add_funds_to_balance_v2_request)



Add funds to a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.balance_response_v2_response import BalanceResponseV2Response
from criteo_api_retailmedia_v2024_10.model.add_funds_to_balance_v2_request import AddFundsToBalanceV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance to add funds to
    add_funds_to_balance_v2_request = AddFundsToBalanceV2Request(
        data=ResourceOfAddFundsToBalanceV2(
            attributes=AddFundsToBalanceV2(
                delta_amount=3.14,
                memo="memo_example",
                po_number="po_number_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AddFundsToBalanceV2Request | An object that represents the available options of adding funds to a balance.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_account_add_funds_by_account_id_balancesbalance_id(account_id, balance_id, add_funds_to_balance_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v2_external_account_add_funds_by_account_id_balancesbalance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to add funds to |
 **add_funds_to_balance_v2_request** | [**AddFundsToBalanceV2Request**](AddFundsToBalanceV2Request.md)| An object that represents the available options of adding funds to a balance. |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v2_external_account_balances_by_account_id**
> BalanceResponseV2Response post_api_v2_external_account_balances_by_account_id(account_id, create_balance_v2_request)



Create balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.balance_response_v2_response import BalanceResponseV2Response
from criteo_api_retailmedia_v2024_10.model.create_balance_v2_request import CreateBalanceV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account to create balances for
    create_balance_v2_request = CreateBalanceV2Request(
        data=ResourceOfCreateBalanceV2(
            attributes=CreateBalanceV2(
                deposited=3.14,
                end_date=dateutil_parser('1970-01-01').date(),
                memo="memo_example",
                name="name_example",
                po_number="po_number_example",
                spend_type="Onsite",
                start_date=dateutil_parser('1970-01-01').date(),
            ),
            id="id_example",
            type="type_example",
        ),
    ) # CreateBalanceV2Request | An object that represents the available options to set when creating a Retail Media Balance

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_account_balances_by_account_id(account_id, create_balance_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v2_external_account_balances_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to create balances for |
 **create_balance_v2_request** | [**CreateBalanceV2Request**](CreateBalanceV2Request.md)| An object that represents the available options to set when creating a Retail Media Balance |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v2_external_account_change_dates_by_account_id_balancesbalance_id**
> BalanceResponseV2Response post_api_v2_external_account_change_dates_by_account_id_balancesbalance_id(account_id, balance_id, change_dates_of_balance_v2_request)



Change dates of a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_10
from criteo_api_retailmedia_v2024_10.api import balance_api
from criteo_api_retailmedia_v2024_10.model.balance_response_v2_response import BalanceResponseV2Response
from criteo_api_retailmedia_v2024_10.model.change_dates_of_balance_v2_request import ChangeDatesOfBalanceV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance to change the dates
    change_dates_of_balance_v2_request = ChangeDatesOfBalanceV2Request(
        data=ResourceOfChangeDatesOfBalanceV2(
            attributes=ChangeDatesOfBalanceV2(
                end_date="end_date_example",
                memo="memo_example",
                start_date="start_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ChangeDatesOfBalanceV2Request | An object that represents the available options to modify schedule of a balance.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v2_external_account_change_dates_by_account_id_balancesbalance_id(account_id, balance_id, change_dates_of_balance_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_10.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v2_external_account_change_dates_by_account_id_balancesbalance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to change the dates |
 **change_dates_of_balance_v2_request** | [**ChangeDatesOfBalanceV2Request**](ChangeDatesOfBalanceV2Request.md)| An object that represents the available options to modify schedule of a balance. |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

