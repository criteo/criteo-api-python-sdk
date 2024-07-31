# criteo_api_retailmedia_v2024_04.AccountsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_brands**](AccountsApi.md#add_brands) | **POST** /2024-04/retail-media/account-management/accounts/{accountId}/brands/add | 
[**create_private_market_demand_brand_account**](AccountsApi.md#create_private_market_demand_brand_account) | **POST** /2024-04/retail-media/account-management/accounts/{accountId}/create-brand-account | 
[**get_api_v1_external_accounts**](AccountsApi.md#get_api_v1_external_accounts) | **GET** /2024-04/retail-media/accounts | 
[**remove_brands**](AccountsApi.md#remove_brands) | **POST** /2024-04/retail-media/account-management/accounts/{accountId}/brands/remove | 


# **add_brands**
> ValueResourceOfRetailMediaBrands add_brands(account_id)



Add brands to an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import accounts_api
from criteo_api_retailmedia_v2024_04.model.value_resource_input_of_retail_media_brands import ValueResourceInputOfRetailMediaBrands
from criteo_api_retailmedia_v2024_04.model.value_resource_of_retail_media_brands import ValueResourceOfRetailMediaBrands
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | the account id to update
    value_resource_input_of_retail_media_brands = ValueResourceInputOfRetailMediaBrands(
        data=ValueResourceOfRetailMediaBrands(
            type="type_example",
            attributes=RetailMediaBrands(
                brand_ids=[
                    1,
                ],
            ),
        ),
    ) # ValueResourceInputOfRetailMediaBrands | brands to associate to account (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_brands(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->add_brands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_brands(account_id, value_resource_input_of_retail_media_brands=value_resource_input_of_retail_media_brands)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->add_brands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| the account id to update |
 **value_resource_input_of_retail_media_brands** | [**ValueResourceInputOfRetailMediaBrands**](ValueResourceInputOfRetailMediaBrands.md)| brands to associate to account | [optional]

### Return type

[**ValueResourceOfRetailMediaBrands**](ValueResourceOfRetailMediaBrands.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_private_market_demand_brand_account**
> ResourceOutcomeOfRetailMediaAccount create_private_market_demand_brand_account(account_id)



Creates a new child Demand Brand Account for the provided parent private market account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import accounts_api
from criteo_api_retailmedia_v2024_04.model.resource_outcome_of_retail_media_account import ResourceOutcomeOfRetailMediaAccount
from criteo_api_retailmedia_v2024_04.model.value_resource_input_of_retail_media_brand_account_creation import ValueResourceInputOfRetailMediaBrandAccountCreation
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | Account Id for the parent private market account
    value_resource_input_of_retail_media_brand_account_creation = ValueResourceInputOfRetailMediaBrandAccountCreation(
        data=ValueResourceOfRetailMediaBrandAccountCreation(
            type="type_example",
            attributes=RetailMediaBrandAccountCreation(
                name="name_example",
                company_name="company_name_example",
                brands=[
                    1,
                ],
            ),
        ),
    ) # ValueResourceInputOfRetailMediaBrandAccountCreation | Initial creation and configuration options for the new account (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_private_market_demand_brand_account(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->create_private_market_demand_brand_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_private_market_demand_brand_account(account_id, value_resource_input_of_retail_media_brand_account_creation=value_resource_input_of_retail_media_brand_account_creation)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->create_private_market_demand_brand_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id for the parent private market account |
 **value_resource_input_of_retail_media_brand_account_creation** | [**ValueResourceInputOfRetailMediaBrandAccountCreation**](ValueResourceInputOfRetailMediaBrandAccountCreation.md)| Initial creation and configuration options for the new account | [optional]

### Return type

[**ResourceOutcomeOfRetailMediaAccount**](ResourceOutcomeOfRetailMediaAccount.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_accounts**
> JsonApiPageResponseOfAccount get_api_v1_external_accounts()



Gets page of account objects that the current user can access

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import accounts_api
from criteo_api_retailmedia_v2024_04.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
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
    api_instance = accounts_api.AccountsApi(api_client)
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 0 # int | The 0 indexed page index you would like to receive given the page size (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | The maximum number of items you would like to receive in this request (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_accounts(limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->get_api_v1_external_accounts: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_brands**
> ValueResourceOfRetailMediaBrands remove_brands(account_id)



Remove a brand from an account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_04
from criteo_api_retailmedia_v2024_04.api import accounts_api
from criteo_api_retailmedia_v2024_04.model.value_resource_input_of_retail_media_brands import ValueResourceInputOfRetailMediaBrands
from criteo_api_retailmedia_v2024_04.model.value_resource_of_retail_media_brands import ValueResourceOfRetailMediaBrands
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_id = "accountId_example" # str | The account id to update
    value_resource_input_of_retail_media_brands = ValueResourceInputOfRetailMediaBrands(
        data=ValueResourceOfRetailMediaBrands(
            type="type_example",
            attributes=RetailMediaBrands(
                brand_ids=[
                    1,
                ],
            ),
        ),
    ) # ValueResourceInputOfRetailMediaBrands | Brands to remove from account (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_brands(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->remove_brands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_brands(account_id, value_resource_input_of_retail_media_brands=value_resource_input_of_retail_media_brands)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_04.ApiException as e:
        print("Exception when calling AccountsApi->remove_brands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id to update |
 **value_resource_input_of_retail_media_brands** | [**ValueResourceInputOfRetailMediaBrands**](ValueResourceInputOfRetailMediaBrands.md)| Brands to remove from account | [optional]

### Return type

[**ValueResourceOfRetailMediaBrands**](ValueResourceOfRetailMediaBrands.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

