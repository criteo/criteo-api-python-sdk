# criteo_api_retailmedia_preview.AccountsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_external_v1_account_private_market_child_accounts_by_account_id**](AccountsApi.md#get_api_external_v1_account_private_market_child_accounts_by_account_id) | **GET** /preview/retail-media/account-management/accounts/{accountId}/private-market-child-accounts | 
[**preview_retail_media_accounts_fees_search_post**](AccountsApi.md#preview_retail_media_accounts_fees_search_post) | **POST** /preview/retail-media/accounts/fees/search | 
[**preview_retail_media_accounts_fees_update_post**](AccountsApi.md#preview_retail_media_accounts_fees_update_post) | **POST** /preview/retail-media/accounts/fees/update | 


# **get_api_external_v1_account_private_market_child_accounts_by_account_id**
> EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata get_api_external_v1_account_private_market_child_accounts_by_account_id(account_id)



Gets page of private market child accounts that are associated with the given account

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
        api_response = api_instance.get_api_external_v1_account_private_market_child_accounts_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->get_api_external_v1_account_private_market_child_accounts_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_external_v1_account_private_market_child_accounts_by_account_id(account_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->get_api_external_v1_account_private_market_child_accounts_by_account_id: %s\n" % e)
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

# **preview_retail_media_accounts_fees_search_post**
> ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata preview_retail_media_accounts_fees_search_post()



Get fees for provided accounts

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import accounts_api
from criteo_api_retailmedia_preview.model.outcome import Outcome
from criteo_api_retailmedia_preview.model.value_resource_input_account_fees_search_request import ValueResourceInputAccountFeesSearchRequest
from criteo_api_retailmedia_preview.model.value_resource_collection_outcome_private_market_account_fees_and_metadata import ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata
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
    limit = 50 # int | used for paging, number of results returned per request, Maximum of 500 (optional) if omitted the server will use the default value of 50
    offset = 0 # int | used for paging, number of records to skip (optional) if omitted the server will use the default value of 0
    value_resource_input_account_fees_search_request = ValueResourceInputAccountFeesSearchRequest(
        data=ValueResourceAccountFeesSearchRequest(
            attributes=AccountFeesSearchRequest(
                account_ids=[
                    "account_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputAccountFeesSearchRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_retail_media_accounts_fees_search_post(limit=limit, offset=offset, value_resource_input_account_fees_search_request=value_resource_input_account_fees_search_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->preview_retail_media_accounts_fees_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| used for paging, number of results returned per request, Maximum of 500 | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| used for paging, number of records to skip | [optional] if omitted the server will use the default value of 0
 **value_resource_input_account_fees_search_request** | [**ValueResourceInputAccountFeesSearchRequest**](ValueResourceInputAccountFeesSearchRequest.md)|  | [optional]

### Return type

[**ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata**](ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_retail_media_accounts_fees_update_post**
> ValueResourceOutcomeAccountFeesUpdateResult preview_retail_media_accounts_fees_update_post()



Set fees for provided accounts

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import accounts_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_account_fees_update_result import ValueResourceOutcomeAccountFeesUpdateResult
from criteo_api_retailmedia_preview.model.outcome import Outcome
from criteo_api_retailmedia_preview.model.value_resource_input_account_fees_update_request import ValueResourceInputAccountFeesUpdateRequest
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
    value_resource_input_account_fees_update_request = ValueResourceInputAccountFeesUpdateRequest(
        data=ValueResourceAccountFeesUpdateRequest(
            attributes=AccountFeesUpdateRequest(
                account_ids=[
                    "account_ids_example",
                ],
                fees=PrivateMarketFees(
                    demand_managed=DemandManagedFee(
                        rate=0,
                    ),
                    managed_service=ManagedServiceFee(
                        onsite_display_enabled=True,
                        onsite_sponsored_products_enabled=True,
                        rate=0,
                    ),
                ),
            ),
            type="type_example",
        ),
    ) # ValueResourceInputAccountFeesUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_retail_media_accounts_fees_update_post(value_resource_input_account_fees_update_request=value_resource_input_account_fees_update_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->preview_retail_media_accounts_fees_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value_resource_input_account_fees_update_request** | [**ValueResourceInputAccountFeesUpdateRequest**](ValueResourceInputAccountFeesUpdateRequest.md)|  | [optional]

### Return type

[**ValueResourceOutcomeAccountFeesUpdateResult**](ValueResourceOutcomeAccountFeesUpdateResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

