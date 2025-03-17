# criteo_api_retailmedia_preview.AccountsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_external_v1_account_private_market_child_accounts_by_account_id**](AccountsApi.md#get_api_external_v1_account_private_market_child_accounts_by_account_id) | **GET** /preview/retail-media/account-management/accounts/{accountId}/private-market-child-accounts | 
[**grant_consent**](AccountsApi.md#grant_consent) | **POST** /preview/retail-media/accounts/{accountId}/grant-consent | 
[**search_sellers**](AccountsApi.md#search_sellers) | **POST** /preview/retail-media/accounts/sellers/search | 


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
    offset = 0 # int | The (zero-based) offset into the collection of accounts. The default is 0. (optional) if omitted the server will use the default value of 0
    limit = 25 # int | The number of accounts to be returned. The default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_external_v1_account_private_market_child_accounts_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->get_api_external_v1_account_private_market_child_accounts_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_external_v1_account_private_market_child_accounts_by_account_id(account_id, offset=offset, limit=limit)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->get_api_external_v1_account_private_market_child_accounts_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **offset** | **int**| The (zero-based) offset into the collection of accounts. The default is 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The number of accounts to be returned. The default is 25. | [optional] if omitted the server will use the default value of 25

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

# **grant_consent**
> grant_consent(account_id)



Grant consent to a business application on behalf of a Private Market demand account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import accounts_api
from criteo_api_retailmedia_preview.model.grant_consent_input import GrantConsentInput
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
    account_id = "accountId_example" # str | The demand account ID on which to grant consent
    grant_consent_input = GrantConsentInput(
        data=GrantConsentModelValueResource(
            type="type_example",
            attributes=GrantConsentModel(
                client_id="client_id_example",
                callback_url="callback_url_example",
                callback_state="callback_state_example",
            ),
        ),
    ) # GrantConsentInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_instance.grant_consent(account_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->grant_consent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_instance.grant_consent(account_id, grant_consent_input=grant_consent_input)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->grant_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The demand account ID on which to grant consent |
 **grant_consent_input** | [**GrantConsentInput**](GrantConsentInput.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sellers**
> ValueResourceCollectionOutcomeOfSellerSearchResult search_sellers()



Get the sellers mapped to provided accounts

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import accounts_api
from criteo_api_retailmedia_preview.model.value_resource_input_of_seller_search import ValueResourceInputOfSellerSearch
from criteo_api_retailmedia_preview.model.value_resource_collection_outcome_of_seller_search_result import ValueResourceCollectionOutcomeOfSellerSearchResult
from criteo_api_retailmedia_preview.model.outcome import Outcome
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
    value_resource_input_of_seller_search = ValueResourceInputOfSellerSearch(
        data=ValueResourceOfSellerSearch(
            type="type_example",
            attributes=SellerSearch(
                account_ids=[
                    "account_ids_example",
                ],
                include_details=False,
            ),
        ),
    ) # ValueResourceInputOfSellerSearch |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_sellers(value_resource_input_of_seller_search=value_resource_input_of_seller_search)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AccountsApi->search_sellers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value_resource_input_of_seller_search** | [**ValueResourceInputOfSellerSearch**](ValueResourceInputOfSellerSearch.md)|  | [optional]

### Return type

[**ValueResourceCollectionOutcomeOfSellerSearchResult**](ValueResourceCollectionOutcomeOfSellerSearchResult.md)

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

