# criteo_api_marketingsolutions_v2025_10.RecoApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_set**](RecoApi.md#create_product_set) | **POST** /2025-10/product-sets | 
[**disable_product_filtering**](RecoApi.md#disable_product_filtering) | **DELETE** /2025-10/ads/{ad-id}/product-filter | 
[**enable_product_filtering**](RecoApi.md#enable_product_filtering) | **POST** /2025-10/ads/{ad-id}/product-filter | 
[**fetch_product_filtering_config**](RecoApi.md#fetch_product_filtering_config) | **GET** /2025-10/ads/{ad-id}/product-filter | 
[**fetch_product_filtering_usages**](RecoApi.md#fetch_product_filtering_usages) | **GET** /2025-10/product-sets/{product-set-id}/product-filters | 
[**fetch_product_set**](RecoApi.md#fetch_product_set) | **GET** /2025-10/product-sets/{product-set-id} | 
[**fetch_product_sets**](RecoApi.md#fetch_product_sets) | **GET** /2025-10/product-sets/dataset/{dataset-id} | 
[**patch_product_set**](RecoApi.md#patch_product_set) | **PATCH** /2025-10/product-sets/{product-set-id} | 
[**remove_product_set**](RecoApi.md#remove_product_set) | **DELETE** /2025-10/product-sets/{product-set-id} | 


# **create_product_set**
> ResourceOutcomeOfProductSet create_product_set()



Create a new product set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.resource_outcome_of_product_set import ResourceOutcomeOfProductSet
from criteo_api_marketingsolutions_v2025_10.model.value_resource_input_of_create_product_set_request import ValueResourceInputOfCreateProductSetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    value_resource_input_of_create_product_set_request = ValueResourceInputOfCreateProductSetRequest(
        data=ValueResourceOfCreateProductSetRequest(
            attributes=CreateProductSetRequest(
                dataset_id="dataset_id_example",
                is_draft=True,
                name="name_example",
                rules=[
                    ProductSetRule(
                        field="OBSOLETE_Extradata",
                        operator="IsIn",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfCreateProductSetRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_product_set(value_resource_input_of_create_product_set_request=value_resource_input_of_create_product_set_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->create_product_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value_resource_input_of_create_product_set_request** | [**ValueResourceInputOfCreateProductSetRequest**](ValueResourceInputOfCreateProductSetRequest.md)|  | [optional]

### Return type

[**ResourceOutcomeOfProductSet**](ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product set created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_product_filtering**
> ValueResourceOutcomeOfProductFilterConfig disable_product_filtering(ad_id)



Disable product filtering for a given ad

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.value_resource_outcome_of_product_filter_config import ValueResourceOutcomeOfProductFilterConfig
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    ad_id = "ad-id_example" # str | ID of the ad

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.disable_product_filtering(ad_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->disable_product_filtering: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_id** | **str**| ID of the ad |

### Return type

[**ValueResourceOutcomeOfProductFilterConfig**](ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_product_filtering**
> ValueResourceOutcomeOfProductFilterConfig enable_product_filtering(ad_id)



Enable product filtering for a given ad

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.value_resource_input_of_create_product_filter_request import ValueResourceInputOfCreateProductFilterRequest
from criteo_api_marketingsolutions_v2025_10.model.value_resource_outcome_of_product_filter_config import ValueResourceOutcomeOfProductFilterConfig
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    ad_id = "ad-id_example" # str | ID of the ad
    value_resource_input_of_create_product_filter_request = ValueResourceInputOfCreateProductFilterRequest(
        data=ValueResourceOfCreateProductFilterRequest(
            attributes=CreateProductFilterRequest(
                product_set_id="product_set_id_example",
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfCreateProductFilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.enable_product_filtering(ad_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->enable_product_filtering: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.enable_product_filtering(ad_id, value_resource_input_of_create_product_filter_request=value_resource_input_of_create_product_filter_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->enable_product_filtering: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_id** | **str**| ID of the ad |
 **value_resource_input_of_create_product_filter_request** | [**ValueResourceInputOfCreateProductFilterRequest**](ValueResourceInputOfCreateProductFilterRequest.md)|  | [optional]

### Return type

[**ValueResourceOutcomeOfProductFilterConfig**](ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_product_filtering_config**
> ValueResourceOutcomeOfProductFilterConfig fetch_product_filtering_config(ad_id)



Fetch product filtering configuration for a given ad

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.value_resource_outcome_of_product_filter_config import ValueResourceOutcomeOfProductFilterConfig
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    ad_id = "ad-id_example" # str | ID of the ad

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_product_filtering_config(ad_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->fetch_product_filtering_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_id** | **str**| ID of the ad |

### Return type

[**ValueResourceOutcomeOfProductFilterConfig**](ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. Returns the product filtering configuration if it exists, or empty data if it doesn&#39;t. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_product_filtering_usages**
> ValueResourceCollectionOutcomeOfProductFilterConfig fetch_product_filtering_usages(product_set_id)



Fetch product filtering usages for a given product set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.value_resource_collection_outcome_of_product_filter_config import ValueResourceCollectionOutcomeOfProductFilterConfig
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    product_set_id = "product-set-id_example" # str | ID of the product set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_product_filtering_usages(product_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->fetch_product_filtering_usages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **str**| ID of the product set |

### Return type

[**ValueResourceCollectionOutcomeOfProductFilterConfig**](ValueResourceCollectionOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_product_set**
> ResourceOutcomeOfProductSet fetch_product_set(product_set_id)



Fetch an existing product set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.resource_outcome_of_product_set import ResourceOutcomeOfProductSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    product_set_id = "product-set-id_example" # str | ID of the product set

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_product_set(product_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->fetch_product_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **str**| ID of the product set |

### Return type

[**ResourceOutcomeOfProductSet**](ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product set fetched successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_product_sets**
> ResourceCollectionOutcomeOfProductSet fetch_product_sets(dataset_id)



Fetch product sets of a given dataset

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.resource_collection_outcome_of_product_set import ResourceCollectionOutcomeOfProductSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    dataset_id = "dataset-id_example" # str | The ID of the dataset that should be used for product set retrieval

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_product_sets(dataset_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->fetch_product_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset that should be used for product set retrieval |

### Return type

[**ResourceCollectionOutcomeOfProductSet**](ResourceCollectionOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products sets fetched successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_product_set**
> ResourceOutcomeOfProductSet patch_product_set(product_set_id)



Patch an existing product set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.resource_outcome_of_product_set import ResourceOutcomeOfProductSet
from criteo_api_marketingsolutions_v2025_10.model.value_resource_input_of_patch_product_set_request import ValueResourceInputOfPatchProductSetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    product_set_id = "product-set-id_example" # str | ID of the product set
    value_resource_input_of_patch_product_set_request = ValueResourceInputOfPatchProductSetRequest(
        data=ValueResourceOfPatchProductSetRequest(
            attributes=PatchProductSetRequest(
                is_draft=True,
                minimum_number_of_products=1,
                name="name_example",
                rules=[
                    ProductSetRule(
                        field="OBSOLETE_Extradata",
                        operator="IsIn",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputOfPatchProductSetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_product_set(product_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->patch_product_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_product_set(product_set_id, value_resource_input_of_patch_product_set_request=value_resource_input_of_patch_product_set_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->patch_product_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **str**| ID of the product set |
 **value_resource_input_of_patch_product_set_request** | [**ValueResourceInputOfPatchProductSetRequest**](ValueResourceInputOfPatchProductSetRequest.md)|  | [optional]

### Return type

[**ResourceOutcomeOfProductSet**](ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product set modified successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_product_set**
> Outcome remove_product_set(product_set_id)



Remove a product set

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_10
from criteo_api_marketingsolutions_v2025_10.api import reco_api
from criteo_api_marketingsolutions_v2025_10.model.outcome import Outcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = reco_api.RecoApi(api_client)
    product_set_id = "product-set-id_example" # str | ID of the product set to remove

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_product_set(product_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_10.ApiException as e:
        print("Exception when calling RecoApi->remove_product_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **str**| ID of the product set to remove |

### Return type

[**Outcome**](Outcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | ProductSet removed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

