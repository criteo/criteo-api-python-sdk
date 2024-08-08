# criteo_api_retailmedia_v2024_04.BalanceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api202110_external_balance_campaigns_by_balance_id**](BalanceApi.md#get_api202110_external_balance_campaigns_by_balance_id) | **GET** /2024-04/retail-media/balances/{balance-id}/campaigns | 
[**get_api_v1_external_account_balances_by_account_id**](BalanceApi.md#get_api_v1_external_account_balances_by_account_id) | **GET** /2024-04/retail-media/accounts/{account-id}/balances | 
[**get_api_v1_external_account_by_account_id_and_balance_id**](BalanceApi.md#get_api_v1_external_account_by_account_id_and_balance_id) | **GET** /2024-04/retail-media/accounts/{account-id}/balances/{balanceId} | 
[**patch_api_v1_external_account_by_account_id_and_balance_id**](BalanceApi.md#patch_api_v1_external_account_by_account_id_and_balance_id) | **PATCH** /2024-04/retail-media/accounts/{account-id}/balances/{balanceId} | 
[**post_api_v1_external_account_add_funds_by_account_id_and_balance_id**](BalanceApi.md#post_api_v1_external_account_add_funds_by_account_id_and_balance_id) | **POST** /2024-04/retail-media/accounts/{account-id}/balances/{balanceId}/add-funds | 
[**post_api_v1_external_account_balances_by_account_id**](BalanceApi.md#post_api_v1_external_account_balances_by_account_id) | **POST** /2024-04/retail-media/accounts/{account-id}/balances | 
[**post_api_v1_external_account_change_dates_by_account_id_and_balance_id**](BalanceApi.md#post_api_v1_external_account_change_dates_by_account_id_and_balance_id) | **POST** /2024-04/retail-media/accounts/{account-id}/balances/{balanceId}/change-dates | 


# **get_api202110_external_balance_campaigns_by_balance_id**
> BalanceCampaign202110PagedListResponse get_api202110_external_balance_campaigns_by_balance_id(balance_id)



Gets page of campaigns for the given balanceId

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
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
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->get_api202110_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api202110_external_balance_campaigns_by_balance_id(balance_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
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

# **get_api_v1_external_account_balances_by_account_id**
> BalanceResponsePagedListResponse get_api_v1_external_account_balances_by_account_id(account_id)



Get page of balances for the given accountId.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.balance_response_paged_list_response import BalanceResponsePagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account to get page of balances for
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_balances_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->get_api_v1_external_account_balances_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_balances_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->get_api_v1_external_account_balances_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to get page of balances for |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

### Return type

[**BalanceResponsePagedListResponse**](BalanceResponsePagedListResponse.md)

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

# **get_api_v1_external_account_by_account_id_and_balance_id**
> BalanceResponse get_api_v1_external_account_by_account_id_and_balance_id(account_id, balance_id)



Get a balance for the given account id and balance id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.balance_response import BalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balanceId_example" # str | The balance id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_by_account_id_and_balance_id(account_id, balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->get_api_v1_external_account_by_account_id_and_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance id |

### Return type

[**BalanceResponse**](BalanceResponse.md)

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

# **patch_api_v1_external_account_by_account_id_and_balance_id**
> BalanceResponse patch_api_v1_external_account_by_account_id_and_balance_id(account_id, balance_id)



Modify a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.update_balance_model_request import UpdateBalanceModelRequest
from criteo_api_retailmedia_v2024_04.model.balance_response import BalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balanceId_example" # str | The balance to change the dates
    update_balance_model_request = UpdateBalanceModelRequest(
        data=ResourceOfUpdateBalanceModel(
            attributes=ExternalUpdateBalanceModel(
                name="name_example",
                po_number="po_number_example",
                sales_force_id="sales_force_id_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                memo="memo_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # UpdateBalanceModelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_api_v1_external_account_by_account_id_and_balance_id(account_id, balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->patch_api_v1_external_account_by_account_id_and_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_api_v1_external_account_by_account_id_and_balance_id(account_id, balance_id, update_balance_model_request=update_balance_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->patch_api_v1_external_account_by_account_id_and_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to change the dates |
 **update_balance_model_request** | [**UpdateBalanceModelRequest**](UpdateBalanceModelRequest.md)|  | [optional]

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_add_funds_by_account_id_and_balance_id**
> BalanceResponse post_api_v1_external_account_add_funds_by_account_id_and_balance_id(account_id, balance_id)



Add funds to a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.add_funds_to_balance_request import AddFundsToBalanceRequest
from criteo_api_retailmedia_v2024_04.model.balance_response import BalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balanceId_example" # str | The balance to add funds to
    add_funds_to_balance_request = AddFundsToBalanceRequest(
        data=ResourceOfAddFundsToBalance(
            attributes=ExternalAddFundsToBalance(
                delta_amount=3.14,
                po_number="po_number_example",
                memo="memo_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AddFundsToBalanceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_add_funds_by_account_id_and_balance_id(account_id, balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v1_external_account_add_funds_by_account_id_and_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_add_funds_by_account_id_and_balance_id(account_id, balance_id, add_funds_to_balance_request=add_funds_to_balance_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v1_external_account_add_funds_by_account_id_and_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to add funds to |
 **add_funds_to_balance_request** | [**AddFundsToBalanceRequest**](AddFundsToBalanceRequest.md)|  | [optional]

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_balances_by_account_id**
> BalanceResponse post_api_v1_external_account_balances_by_account_id(account_id)



Create balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.create_balance_request import CreateBalanceRequest
from criteo_api_retailmedia_v2024_04.model.balance_response import BalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account to create balances for
    create_balance_request = CreateBalanceRequest(
        data=ResourceOfCreateBalance(
            attributes=ExternalCreateBalance(
                name="name_example",
                po_number="po_number_example",
                deposited=3.14,
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                spend_type="Onsite",
                memo="memo_example",
                sales_force_id="sales_force_id_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # CreateBalanceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_balances_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v1_external_account_balances_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_balances_by_account_id(account_id, create_balance_request=create_balance_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v1_external_account_balances_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to create balances for |
 **create_balance_request** | [**CreateBalanceRequest**](CreateBalanceRequest.md)|  | [optional]

### Return type

[**BalanceResponse**](BalanceResponse.md)

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

# **post_api_v1_external_account_change_dates_by_account_id_and_balance_id**
> BalanceResponse post_api_v1_external_account_change_dates_by_account_id_and_balance_id(account_id, balance_id)



Change dates of a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import balance_api
from criteo_api_retailmedia_v2024_04.model.change_dates_of_balance_request import ChangeDatesOfBalanceRequest
from criteo_api_retailmedia_v2024_04.model.balance_response import BalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balanceId_example" # str | The balance to change the dates
    change_dates_of_balance_request = ChangeDatesOfBalanceRequest(
        data=ResourceOfChangeDatesOfBalance(
            attributes=ExternalChangeDatesOfBalance(
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                memo="memo_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ChangeDatesOfBalanceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_change_dates_by_account_id_and_balance_id(account_id, balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v1_external_account_change_dates_by_account_id_and_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_change_dates_by_account_id_and_balance_id(account_id, balance_id, change_dates_of_balance_request=change_dates_of_balance_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling BalanceApi->post_api_v1_external_account_change_dates_by_account_id_and_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to change the dates |
 **change_dates_of_balance_request** | [**ChangeDatesOfBalanceRequest**](ChangeDatesOfBalanceRequest.md)|  | [optional]

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
