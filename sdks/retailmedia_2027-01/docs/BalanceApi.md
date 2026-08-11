# criteo_api_retailmedia_v2027_01.BalanceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_funds_by_account_and_balance_id**](BalanceApi.md#add_funds_by_account_and_balance_id) | **POST** /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds | /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds
[**change_dates_by_account_and_balance_id**](BalanceApi.md#change_dates_by_account_and_balance_id) | **POST** /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates | /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates
[**create_balance_by_account_id**](BalanceApi.md#create_balance_by_account_id) | **POST** /2027-01/retail-media/accounts/{account-id}/balances | /2027-01/retail-media/accounts/{account-id}/balances
[**get_balance_by_account_and_balance_id**](BalanceApi.md#get_balance_by_account_and_balance_id) | **GET** /2027-01/retail-media/accounts/{account-id}/balances/{balance-id} | /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}
[**get_balance_history_v1**](BalanceApi.md#get_balance_history_v1) | **GET** /2027-01/retail-media/balances/{balanceId}/history | /2027-01/retail-media/balances/{balanceId}/history
[**get_balance_v1**](BalanceApi.md#get_balance_v1) | **GET** /2027-01/retail-media/balances/{balanceId} | /2027-01/retail-media/balances/{balanceId}
[**get_campaigns_by_balance_id**](BalanceApi.md#get_campaigns_by_balance_id) | **GET** /2027-01/retail-media/balances/{balance-id}/campaigns | /2027-01/retail-media/balances/{balance-id}/campaigns
[**get_page_of_balances_v1**](BalanceApi.md#get_page_of_balances_v1) | **GET** /2027-01/retail-media/accounts/{accountId}/balances | /2027-01/retail-media/accounts/{accountId}/balances
[**update_balance_v1**](BalanceApi.md#update_balance_v1) | **PATCH** /2027-01/retail-media/accounts/{account-id}/balances/{balance-id} | /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}


# **add_funds_by_account_and_balance_id**
> BalanceResponseV3Response add_funds_by_account_and_balance_id(account_id, balance_id, add_funds_to_balance_v3_request)

/2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds

Add funds to a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.add_funds_to_balance_v3_request import AddFundsToBalanceV3Request
from criteo_api_retailmedia_v2027_01.model.balance_response_v3_response import BalanceResponseV3Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance to add funds to
    add_funds_to_balance_v3_request = AddFundsToBalanceV3Request(
        data=ResourceOfAddFundsToBalanceV3(
            attributes=AddFundsToBalanceV3(
                delta_amount=3.14,
                memo="memo_example",
                retailer_po_number="retailer_po_number_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AddFundsToBalanceV3Request | An object that represents the available options of adding funds to a balance.

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds
        api_response = api_instance.add_funds_by_account_and_balance_id(account_id, balance_id, add_funds_to_balance_v3_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->add_funds_by_account_and_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to add funds to |
 **add_funds_to_balance_v3_request** | [**AddFundsToBalanceV3Request**](AddFundsToBalanceV3Request.md)| An object that represents the available options of adding funds to a balance. |

### Return type

[**BalanceResponseV3Response**](BalanceResponseV3Response.md)

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

# **change_dates_by_account_and_balance_id**
> BalanceResponseV2Response change_dates_by_account_and_balance_id(account_id, balance_id, change_dates_of_balance_v2_request)

/2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates

Change dates of a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.balance_response_v2_response import BalanceResponseV2Response
from criteo_api_retailmedia_v2027_01.model.change_dates_of_balance_v2_request import ChangeDatesOfBalanceV2Request
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
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
        # /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates
        api_response = api_instance.change_dates_by_account_and_balance_id(account_id, balance_id, change_dates_of_balance_v2_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->change_dates_by_account_and_balance_id: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_balance_by_account_id**
> BalanceResponseV3Response create_balance_by_account_id(account_id, create_balance_v3_request)

/2027-01/retail-media/accounts/{account-id}/balances

Create balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.create_balance_v3_request import CreateBalanceV3Request
from criteo_api_retailmedia_v2027_01.model.balance_response_v3_response import BalanceResponseV3Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account to create balances for
    create_balance_v3_request = CreateBalanceV3Request(
        data=ResourceOfCreateBalanceV3(
            attributes=CreateBalanceV3(
                deposited=3.14,
                end_date="end_date_example",
                memo="memo_example",
                name="name_example",
                retailer_po_number="retailer_po_number_example",
                spend_type="Onsite",
                start_date="start_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # CreateBalanceV3Request | An object that represents the available options to set when creating a Retail Media Balance

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/accounts/{account-id}/balances
        api_response = api_instance.create_balance_by_account_id(account_id, create_balance_v3_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->create_balance_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to create balances for |
 **create_balance_v3_request** | [**CreateBalanceV3Request**](CreateBalanceV3Request.md)| An object that represents the available options to set when creating a Retail Media Balance |

### Return type

[**BalanceResponseV3Response**](BalanceResponseV3Response.md)

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

# **get_balance_by_account_and_balance_id**
> BalanceResponseV2Response get_balance_by_account_and_balance_id(account_id, balance_id)

/2027-01/retail-media/accounts/{account-id}/balances/{balance-id}

Get a balance for the given account id and balance id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.balance_response_v2_response import BalanceResponseV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "account-id_example" # str | The account of the balance
    balance_id = "balance-id_example" # str | The balance id

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}
        api_response = api_instance.get_balance_by_account_and_balance_id(account_id, balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_by_account_and_balance_id: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_history_v1**
> ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata get_balance_history_v1(balance_id)

/2027-01/retail-media/balances/{balanceId}/history

Gets the balance's historical change data.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.value_resource_collection_outcome_balance_history_change_data_capture_v1_and_metadata import ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    balance_id = "balanceId_example" # str | Balance id.
    limit = 25 # int | The number of elements to be returned. (optional) if omitted the server will use the default value of 25
    limit_to_change_types = "limitToChangeTypes_example" # str | Comma separated change types string that will be queried. (optional)
    offset = 0 # int | The (zero-based) starting offset in the collection. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/balances/{balanceId}/history
        api_response = api_instance.get_balance_history_v1(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_history_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /2027-01/retail-media/balances/{balanceId}/history
        api_response = api_instance.get_balance_history_v1(balance_id, limit=limit, limit_to_change_types=limit_to_change_types, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_history_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| Balance id. |
 **limit** | **int**| The number of elements to be returned. | [optional] if omitted the server will use the default value of 25
 **limit_to_change_types** | **str**| Comma separated change types string that will be queried. | [optional]
 **offset** | **int**| The (zero-based) starting offset in the collection. | [optional] if omitted the server will use the default value of 0

### Return type

[**ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata**](ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata.md)

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

# **get_balance_v1**
> EntityResourceOutcomeBalanceV1 get_balance_v1(balance_id)

/2027-01/retail-media/balances/{balanceId}

Get a balance for the given balance id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.entity_resource_outcome_balance_v1 import EntityResourceOutcomeBalanceV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    balance_id = "balanceId_example" # str | The balance id.

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/balances/{balanceId}
        api_response = api_instance.get_balance_v1(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_balance_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance id. |

### Return type

[**EntityResourceOutcomeBalanceV1**](EntityResourceOutcomeBalanceV1.md)

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

# **get_campaigns_by_balance_id**
> BalanceCampaign202110PagedListResponse get_campaigns_by_balance_id(balance_id)

/2027-01/retail-media/balances/{balance-id}/campaigns

Gets page of campaigns for the given balanceId

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    balance_id = "balance-id_example" # str | The balance to get campaigns from
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/balances/{balance-id}/campaigns
        api_response = api_instance.get_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /2027-01/retail-media/balances/{balance-id}/campaigns
        api_response = api_instance.get_campaigns_by_balance_id(balance_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to get campaigns from |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

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

# **get_page_of_balances_v1**
> EntityResourceCollectionOutcomeBalanceV1AndMetadata get_page_of_balances_v1(account_id)

/2027-01/retail-media/accounts/{accountId}/balances

Gets page of balance objects for the given account id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.entity_resource_collection_outcome_balance_v1_and_metadata import EntityResourceCollectionOutcomeBalanceV1AndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_api.BalanceApi(api_client)
    account_id = "accountId_example" # str | The account to get balances for.
    limit = 25 # int | The number of elements to be returned. (optional) if omitted the server will use the default value of 25
    limit_to_id = [
        "limit-to-id_example",
    ] # [str] | The balance ids which the result is limited to. (optional)
    offset = 0 # int | The (zero-based) starting offset in the collection. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/accounts/{accountId}/balances
        api_response = api_instance.get_page_of_balances_v1(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_page_of_balances_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /2027-01/retail-media/accounts/{accountId}/balances
        api_response = api_instance.get_page_of_balances_v1(account_id, limit=limit, limit_to_id=limit_to_id, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->get_page_of_balances_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to get balances for. |
 **limit** | **int**| The number of elements to be returned. | [optional] if omitted the server will use the default value of 25
 **limit_to_id** | **[str]**| The balance ids which the result is limited to. | [optional]
 **offset** | **int**| The (zero-based) starting offset in the collection. | [optional] if omitted the server will use the default value of 0

### Return type

[**EntityResourceCollectionOutcomeBalanceV1AndMetadata**](EntityResourceCollectionOutcomeBalanceV1AndMetadata.md)

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
> EntityResourceOutcomeOfBalanceResponseV1 update_balance_v1(account_id, balance_id, value_resource_input_of_update_balance_model_v1)

/2027-01/retail-media/accounts/{account-id}/balances/{balance-id}

Modify a balance for the given account id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import balance_api
from criteo_api_retailmedia_v2027_01.model.value_resource_input_of_update_balance_model_v1 import ValueResourceInputOfUpdateBalanceModelV1
from criteo_api_retailmedia_v2027_01.model.entity_resource_outcome_of_balance_response_v1 import EntityResourceOutcomeOfBalanceResponseV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
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
                retailer_po_number="retailer_po_number_example",
                start_date="start_date_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfUpdateBalanceModelV1 | An object that represents the available options to modify a balance.

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/accounts/{account-id}/balances/{balance-id}
        api_response = api_instance.update_balance_v1(account_id, balance_id, value_resource_input_of_update_balance_model_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling BalanceApi->update_balance_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account of the balance |
 **balance_id** | **str**| The balance to change the dates |
 **value_resource_input_of_update_balance_model_v1** | [**ValueResourceInputOfUpdateBalanceModelV1**](ValueResourceInputOfUpdateBalanceModelV1.md)| An object that represents the available options to modify a balance. |

### Return type

[**EntityResourceOutcomeOfBalanceResponseV1**](EntityResourceOutcomeOfBalanceResponseV1.md)

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

