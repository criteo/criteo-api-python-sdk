# criteo_api_retailmedia_preview.ThirdPartyAccountsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grant_third_party_consent**](ThirdPartyAccountsApi.md#grant_third_party_consent) | **POST** /preview/retail-media/accounts/{accountId}/grant-third-party-consent | 
[**preview_retail_media_third_party_accounts_account_id_brands_add_post**](ThirdPartyAccountsApi.md#preview_retail_media_third_party_accounts_account_id_brands_add_post) | **POST** /preview/retail-media/third-party-accounts/{accountId}/brands/add | 
[**preview_retail_media_third_party_accounts_account_id_brands_brand_id_remove_post**](ThirdPartyAccountsApi.md#preview_retail_media_third_party_accounts_account_id_brands_brand_id_remove_post) | **POST** /preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove | 
[**preview_retail_media_third_party_accounts_account_id_create_brand_account_post**](ThirdPartyAccountsApi.md#preview_retail_media_third_party_accounts_account_id_create_brand_account_post) | **POST** /preview/retail-media/third-party-accounts/{accountId}/create-brand-account | 
[**preview_retail_media_third_party_accounts_account_id_create_seller_account_post**](ThirdPartyAccountsApi.md#preview_retail_media_third_party_accounts_account_id_create_seller_account_post) | **POST** /preview/retail-media/third-party-accounts/{accountId}/create-seller-account | 
[**preview_retail_media_third_party_accounts_account_id_sellers_put**](ThirdPartyAccountsApi.md#preview_retail_media_third_party_accounts_account_id_sellers_put) | **PUT** /preview/retail-media/third-party-accounts/{accountId}/sellers | 


# **grant_third_party_consent**
> grant_third_party_consent(account_id)



Grant third-party consent to a business application on behalf of a Private Market demand account

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import third_party_accounts_api
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
    api_instance = third_party_accounts_api.ThirdPartyAccountsApi(api_client)
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
    ) # GrantConsentInput | The request input containing clientId, callbackURL, and callbackState (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_instance.grant_third_party_consent(account_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->grant_third_party_consent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_instance.grant_third_party_consent(account_id, grant_consent_input=grant_consent_input)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->grant_third_party_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The demand account ID on which to grant consent |
 **grant_consent_input** | [**GrantConsentInput**](GrantConsentInput.md)| The request input containing clientId, callbackURL, and callbackState | [optional]

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

# **preview_retail_media_third_party_accounts_account_id_brands_add_post**
> ValueResourceOutcomeOfRetailMediaBrands preview_retail_media_third_party_accounts_account_id_brands_add_post(account_id)



add the provided brands to an account. This will not remove any existing brands.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import third_party_accounts_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_of_retail_media_brands import ValueResourceOutcomeOfRetailMediaBrands
from criteo_api_retailmedia_preview.model.value_resource_input_of_retail_media_brands import ValueResourceInputOfRetailMediaBrands
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
    api_instance = third_party_accounts_api.ThirdPartyAccountsApi(api_client)
    account_id = "accountId_example" # str | account to add brands to
    value_resource_input_of_retail_media_brands = ValueResourceInputOfRetailMediaBrands(
        data=ValueResourceOfRetailMediaBrands(
            attributes=ExternalRetailMediaBrands(
                brand_ids=[
                    1,
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaBrands | list of bands to add to an account (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_brands_add_post(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_brands_add_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_brands_add_post(account_id, value_resource_input_of_retail_media_brands=value_resource_input_of_retail_media_brands)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_brands_add_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account to add brands to |
 **value_resource_input_of_retail_media_brands** | [**ValueResourceInputOfRetailMediaBrands**](ValueResourceInputOfRetailMediaBrands.md)| list of bands to add to an account | [optional]

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

# **preview_retail_media_third_party_accounts_account_id_brands_brand_id_remove_post**
> ValueResourceOutcomeOfRetailMediaBrands preview_retail_media_third_party_accounts_account_id_brands_brand_id_remove_post(account_id, brand_id)



Attempt to remove the provided brand from the account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import third_party_accounts_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_of_retail_media_brands import ValueResourceOutcomeOfRetailMediaBrands
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
    api_instance = third_party_accounts_api.ThirdPartyAccountsApi(api_client)
    account_id = "accountId_example" # str | account id to remove brand from
    brand_id = "brandId_example" # str | brand to remove

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_brands_brand_id_remove_post(account_id, brand_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_brands_brand_id_remove_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id to remove brand from |
 **brand_id** | **str**| brand to remove |

### Return type

[**ValueResourceOutcomeOfRetailMediaBrands**](ValueResourceOutcomeOfRetailMediaBrands.md)

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

# **preview_retail_media_third_party_accounts_account_id_create_brand_account_post**
> EntityResourceOutcomeOfRetailMediaAccountV2 preview_retail_media_third_party_accounts_account_id_create_brand_account_post(account_id)



Create a private market demand brand account under a given parent account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import third_party_accounts_api
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_retail_media_account_v2 import EntityResourceOutcomeOfRetailMediaAccountV2
from criteo_api_retailmedia_preview.model.value_resource_input_of_retail_media_brand_account_creation_v2 import ValueResourceInputOfRetailMediaBrandAccountCreationV2
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
    api_instance = third_party_accounts_api.ThirdPartyAccountsApi(api_client)
    account_id = "accountId_example" # str | parent supply account to create account under
    value_resource_input_of_retail_media_brand_account_creation_v2 = ValueResourceInputOfRetailMediaBrandAccountCreationV2(
        data=ValueResourceOfRetailMediaBrandAccountCreationV2(
            attributes=ExternalRetailMediaBrandAccountCreationV2(
                brands=[
                    1,
                ],
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
                paying_company_name="paying_company_name_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaBrandAccountCreationV2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_create_brand_account_post(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_create_brand_account_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_create_brand_account_post(account_id, value_resource_input_of_retail_media_brand_account_creation_v2=value_resource_input_of_retail_media_brand_account_creation_v2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_create_brand_account_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| parent supply account to create account under |
 **value_resource_input_of_retail_media_brand_account_creation_v2** | [**ValueResourceInputOfRetailMediaBrandAccountCreationV2**](ValueResourceInputOfRetailMediaBrandAccountCreationV2.md)|  | [optional]

### Return type

[**EntityResourceOutcomeOfRetailMediaAccountV2**](EntityResourceOutcomeOfRetailMediaAccountV2.md)

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

# **preview_retail_media_third_party_accounts_account_id_create_seller_account_post**
> EntityResourceOutcomeOfRetailMediaAccountV2 preview_retail_media_third_party_accounts_account_id_create_seller_account_post(account_id)



Create a private market demand seller account under a given parent account.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import third_party_accounts_api
from criteo_api_retailmedia_preview.model.value_resource_input_of_retail_media_seller_account_creation_v2 import ValueResourceInputOfRetailMediaSellerAccountCreationV2
from criteo_api_retailmedia_preview.model.entity_resource_outcome_of_retail_media_account_v2 import EntityResourceOutcomeOfRetailMediaAccountV2
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
    api_instance = third_party_accounts_api.ThirdPartyAccountsApi(api_client)
    account_id = "accountId_example" # str | parent supply account to create account under
    value_resource_input_of_retail_media_seller_account_creation_v2 = ValueResourceInputOfRetailMediaSellerAccountCreationV2(
        data=ValueResourceOfRetailMediaSellerAccountCreationV2(
            attributes=ExternalRetailMediaSellerAccountCreationV2(
                name="name_example",
                on_behalf_company_name="on_behalf_company_name_example",
                paying_company_name="paying_company_name_example",
                sellers=[
                    ExternalRetailMediaSeller(
                        retailer_id=1,
                        seller_id="seller_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfRetailMediaSellerAccountCreationV2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_create_seller_account_post(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_create_seller_account_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_create_seller_account_post(account_id, value_resource_input_of_retail_media_seller_account_creation_v2=value_resource_input_of_retail_media_seller_account_creation_v2)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_create_seller_account_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| parent supply account to create account under |
 **value_resource_input_of_retail_media_seller_account_creation_v2** | [**ValueResourceInputOfRetailMediaSellerAccountCreationV2**](ValueResourceInputOfRetailMediaSellerAccountCreationV2.md)|  | [optional]

### Return type

[**EntityResourceOutcomeOfRetailMediaAccountV2**](EntityResourceOutcomeOfRetailMediaAccountV2.md)

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

# **preview_retail_media_third_party_accounts_account_id_sellers_put**
> ValueResourceCollectionOutcomeOfRetailMediaSeller preview_retail_media_third_party_accounts_account_id_sellers_put(account_id, value_resource_collection_input_of_retail_media_seller)



Update the list of sellers mapped to the account. This will override any existing mappings.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import third_party_accounts_api
from criteo_api_retailmedia_preview.model.value_resource_collection_input_of_retail_media_seller import ValueResourceCollectionInputOfRetailMediaSeller
from criteo_api_retailmedia_preview.model.value_resource_collection_outcome_of_retail_media_seller import ValueResourceCollectionOutcomeOfRetailMediaSeller
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
    api_instance = third_party_accounts_api.ThirdPartyAccountsApi(api_client)
    account_id = "accountId_example" # str | accountId to update sellers for
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
    ) # ValueResourceCollectionInputOfRetailMediaSeller | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_third_party_accounts_account_id_sellers_put(account_id, value_resource_collection_input_of_retail_media_seller)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling ThirdPartyAccountsApi->preview_retail_media_third_party_accounts_account_id_sellers_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId to update sellers for |
 **value_resource_collection_input_of_retail_media_seller** | [**ValueResourceCollectionInputOfRetailMediaSeller**](ValueResourceCollectionInputOfRetailMediaSeller.md)|  |

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

