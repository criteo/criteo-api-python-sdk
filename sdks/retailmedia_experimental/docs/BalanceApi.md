# criteo_api_retailmedia_experimental.BalanceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_page_of_balances_v1**](BalanceApi.md#get_page_of_balances_v1) | **GET** /experimental/retail-media/accounts/{accountId}/balances | /experimental/retail-media/accounts/{accountId}/balances


# **get_page_of_balances_v1**
> EntityResourceCollectionOutcomeBalanceV1AndMetadata get_page_of_balances_v1(account_id)

/experimental/retail-media/accounts/{accountId}/balances

Gets page of balance objects for the given account id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import balance_api
from criteo_api_retailmedia_experimental.model.entity_resource_collection_outcome_balance_v1_and_metadata import EntityResourceCollectionOutcomeBalanceV1AndMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{accountId}/balances
        api_response = api_instance.get_page_of_balances_v1(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling BalanceApi->get_page_of_balances_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/accounts/{accountId}/balances
        api_response = api_instance.get_page_of_balances_v1(account_id, limit=limit, limit_to_id=limit_to_id, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

