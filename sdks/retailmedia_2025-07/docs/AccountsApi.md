# criteo_api_retailmedia_v2025_07.AccountsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_brands**](AccountsApi.md#add_brands) | **POST** /2025-07/retail-media/account-management/accounts/{accountId}/brands/add | 
[**create_private_market_demand_brand_account**](AccountsApi.md#create_private_market_demand_brand_account) | **POST** /2025-07/retail-media/account-management/accounts/{accountId}/create-brand-account | 
[**create_private_market_demand_seller_account**](AccountsApi.md#create_private_market_demand_seller_account) | **POST** /2025-07/retail-media/account-management/accounts/{accountId}/create-seller-account | 
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /2025-07/retail-media/accounts | 
[**get_private_market_child_accounts_by_account_id**](AccountsApi.md#get_private_market_child_accounts_by_account_id) | **GET** /2025-07/retail-media/account-management/accounts/{accountId}/private-market-child-accounts | 
[**grant_consent**](AccountsApi.md#grant_consent) | **POST** /2025-07/retail-media/accounts/{accountId}/grant-consent | 
[**remove_brands**](AccountsApi.md#remove_brands) | **POST** /2025-07/retail-media/account-management/accounts/{accountId}/brands/remove | 
[**search_sellers**](AccountsApi.md#search_sellers) | **POST** /2025-07/retail-media/accounts/sellers/search | 
[**update_sellers**](AccountsApi.md#update_sellers) | **PUT** /2025-07/retail-media/account-management/accounts/{accountId}/sellers | 


# **add_brands**
> ValueResourceOutcomeOfRetailMediaBrands add_brands(account_id)



Add brands to an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.value_resource_input_of_retail_media_brands import ValueResourceInputOfRetailMediaBrands
from criteo_api_retailmedia_v2025_07.model.value_resource_outcome_of_retail_media_brands import ValueResourceOutcomeOfRetailMediaBrands
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | the account id to update
    value_resource_input_of_retail_media_brands = ValueResourceInputOfRetailMediaBrands(
        data=ValueResourceOfRetailMediaBrands(
            attributes=ExternalRetailMediaBrands(
                brand_ids=[
                    1,
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaBrands |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_brands(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->add_brands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_brands(account_id, value_resource_input_of_retail_media_brands=value_resource_input_of_retail_media_brands)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->add_brands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| the account id to update |
 **value_resource_input_of_retail_media_brands** | [**ValueResourceInputOfRetailMediaBrands**](ValueResourceInputOfRetailMediaBrands.md)|  | [optional]

### Return type

[**ValueResourceOutcomeOfRetailMediaBrands**](ValueResourceOutcomeOfRetailMediaBrands.md)

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

# **create_private_market_demand_brand_account**
> EntityResourceOutcomeOfRetailMediaAccount create_private_market_demand_brand_account(account_id)



Creates a new child Demand Brand account for the provided parent Private Market account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.entity_resource_outcome_of_retail_media_account import EntityResourceOutcomeOfRetailMediaAccount
from criteo_api_retailmedia_v2025_07.model.value_resource_input_of_retail_media_brand_account_creation import ValueResourceInputOfRetailMediaBrandAccountCreation
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | The given account id
    value_resource_input_of_retail_media_brand_account_creation = ValueResourceInputOfRetailMediaBrandAccountCreation(
        data=ValueResourceOfRetailMediaBrandAccountCreation(
            attributes=ExternalRetailMediaBrandAccountCreation(
                brands=[
                    1,
                ],
                company_name="company_name_example",
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaBrandAccountCreation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_private_market_demand_brand_account(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->create_private_market_demand_brand_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_private_market_demand_brand_account(account_id, value_resource_input_of_retail_media_brand_account_creation=value_resource_input_of_retail_media_brand_account_creation)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->create_private_market_demand_brand_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **value_resource_input_of_retail_media_brand_account_creation** | [**ValueResourceInputOfRetailMediaBrandAccountCreation**](ValueResourceInputOfRetailMediaBrandAccountCreation.md)|  | [optional]

### Return type

[**EntityResourceOutcomeOfRetailMediaAccount**](EntityResourceOutcomeOfRetailMediaAccount.md)

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

# **create_private_market_demand_seller_account**
> EntityResourceOutcomeOfRetailMediaAccount create_private_market_demand_seller_account(account_id)



Creates a new child Demand Seller account for the provided parent Private Market account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.entity_resource_outcome_of_retail_media_account import EntityResourceOutcomeOfRetailMediaAccount
from criteo_api_retailmedia_v2025_07.model.value_resource_input_of_retail_media_seller_account_creation import ValueResourceInputOfRetailMediaSellerAccountCreation
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | The given account id
    value_resource_input_of_retail_media_seller_account_creation = ValueResourceInputOfRetailMediaSellerAccountCreation(
        data=ValueResourceOfRetailMediaSellerAccountCreation(
            attributes=ExternalRetailMediaSellerAccountCreation(
                company_name="company_name_example",
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
                sellers=[
                    ExternalRetailMediaSeller(
                        retailer_id=1,
                        seller_id="seller_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaSellerAccountCreation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_private_market_demand_seller_account(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->create_private_market_demand_seller_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_private_market_demand_seller_account(account_id, value_resource_input_of_retail_media_seller_account_creation=value_resource_input_of_retail_media_seller_account_creation)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->create_private_market_demand_seller_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **value_resource_input_of_retail_media_seller_account_creation** | [**ValueResourceInputOfRetailMediaSellerAccountCreation**](ValueResourceInputOfRetailMediaSellerAccountCreation.md)|  | [optional]

### Return type

[**EntityResourceOutcomeOfRetailMediaAccount**](EntityResourceOutcomeOfRetailMediaAccount.md)

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

# **get_accounts**
> JsonApiPageResponseOfAccount get_accounts()



Gets page of account objects that the current user can access

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
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
    api_instance = accounts_api.AccountsApi(api_client)
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_accounts(limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] if omitted the server will use the default value of 25

### Return type

[**JsonApiPageResponseOfAccount**](JsonApiPageResponseOfAccount.md)

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

# **get_private_market_child_accounts_by_account_id**
> EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata get_private_market_child_accounts_by_account_id(account_id)



Gets Private Market child accounts that are associated with the given account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.entity_resource_collection_outcome_of_retail_media_child_account_and_metadata import EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | Account Id
    limit = 25 # int | The number of accounts to be returned. The default is 25. (optional) if omitted the server will use the default value of 25
    offset = 0 # int | The (zero-based) offset into the collection of accounts. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_private_market_child_accounts_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->get_private_market_child_accounts_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_private_market_child_accounts_by_account_id(account_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
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

# **grant_consent**
> grant_consent(account_id)



Grant consent to a business application on behalf of a Private Market demand account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.grant_consent_input import GrantConsentInput
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | The demand account ID on which to grant consent
    grant_consent_input = GrantConsentInput(
        data=GrantConsentModelValueResource(
            attributes=GrantConsentModel(
                callback_state="callback_state_example",
                callback_url="callback_url_example",
                client_id="client_id_example",
            ),
            type="type_example",
        ),
    ) # GrantConsentInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_instance.grant_consent(account_id)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->grant_consent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_instance.grant_consent(account_id, grant_consent_input=grant_consent_input)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_brands**
> ValueResourceOutcomeOfRetailMediaBrands remove_brands(account_id)



Remove brands from an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.value_resource_input_of_retail_media_brands import ValueResourceInputOfRetailMediaBrands
from criteo_api_retailmedia_v2025_07.model.value_resource_outcome_of_retail_media_brands import ValueResourceOutcomeOfRetailMediaBrands
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | the account id to update
    value_resource_input_of_retail_media_brands = ValueResourceInputOfRetailMediaBrands(
        data=ValueResourceOfRetailMediaBrands(
            attributes=ExternalRetailMediaBrands(
                brand_ids=[
                    1,
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaBrands |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_brands(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->remove_brands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_brands(account_id, value_resource_input_of_retail_media_brands=value_resource_input_of_retail_media_brands)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->remove_brands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| the account id to update |
 **value_resource_input_of_retail_media_brands** | [**ValueResourceInputOfRetailMediaBrands**](ValueResourceInputOfRetailMediaBrands.md)|  | [optional]

### Return type

[**ValueResourceOutcomeOfRetailMediaBrands**](ValueResourceOutcomeOfRetailMediaBrands.md)

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

# **search_sellers**
> ValueResourceCollectionOutcomeOfSellerSearchResult search_sellers()



Get the sellers mapped to provided accounts

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.value_resource_input_of_seller_search import ValueResourceInputOfSellerSearch
from criteo_api_retailmedia_v2025_07.model.value_resource_collection_outcome_of_seller_search_result import ValueResourceCollectionOutcomeOfSellerSearchResult
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
    api_instance = accounts_api.AccountsApi(api_client)
    value_resource_input_of_seller_search = ValueResourceInputOfSellerSearch(
        data=ValueResourceOfSellerSearch(
            attributes=SellerSearch(
                account_ids=[
                    "account_ids_example",
                ],
                include_details=False,
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfSellerSearch |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_sellers(value_resource_input_of_seller_search=value_resource_input_of_seller_search)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sellers**
> ValueResourceCollectionOutcomeOfRetailMediaSeller update_sellers(account_id)



Replace the sellers associated with an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_07
from criteo_api_retailmedia_v2025_07.api import accounts_api
from criteo_api_retailmedia_v2025_07.model.value_resource_collection_input_of_retail_media_seller import ValueResourceCollectionInputOfRetailMediaSeller
from criteo_api_retailmedia_v2025_07.model.value_resource_collection_outcome_of_retail_media_seller import ValueResourceCollectionOutcomeOfRetailMediaSeller
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | The given account id
    value_resource_collection_input_of_retail_media_seller = ValueResourceCollectionInputOfRetailMediaSeller(
        data=[
            ValueResourceOfRetailMediaSeller(
                attributes=ExternalRetailMediaSeller(
                    retailer_id=1,
                    seller_id="seller_id_example",
                ),
                type="type_example",
            ),
        ],
    ) # ValueResourceCollectionInputOfRetailMediaSeller |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sellers(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->update_sellers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_sellers(account_id, value_resource_collection_input_of_retail_media_seller=value_resource_collection_input_of_retail_media_seller)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_07.ApiException as e:
        print("Exception when calling AccountsApi->update_sellers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **value_resource_collection_input_of_retail_media_seller** | [**ValueResourceCollectionInputOfRetailMediaSeller**](ValueResourceCollectionInputOfRetailMediaSeller.md)|  | [optional]

### Return type

[**ValueResourceCollectionOutcomeOfRetailMediaSeller**](ValueResourceCollectionOutcomeOfRetailMediaSeller.md)

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

