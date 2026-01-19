# criteo_api_retailmedia_preview.AccountsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_private_market_child_accounts_by_account_id**](AccountsApi.md#get_private_market_child_accounts_by_account_id) | **GET** /preview/retail-media/account-management/accounts/{accountId}/private-market-child-accounts | 


# **get_private_market_child_accounts_by_account_id**
> EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata get_private_market_child_accounts_by_account_id(account_id)



Gets Private Market child accounts that are associated with the given account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import accounts_api
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_of_retail_media_child_account_and_metadata import EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | Account Id
    limit = 25 # int | The number of accounts to be returned. The default is 25. (optional) if omitted the server will use the default value of 25
    offset = 0 # int | The (zero-based) offset into the collection of accounts. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_private_market_child_accounts_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->get_private_market_child_accounts_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_private_market_child_accounts_by_account_id(account_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->get_private_market_child_accounts_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **limit** | **int**| The number of accounts to be returned. The default is 25. | [optional] if omitted the server will use the default value of 25
 **offset** | **int**| The (zero-based) offset into the collection of accounts. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata**](EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata.md)

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

