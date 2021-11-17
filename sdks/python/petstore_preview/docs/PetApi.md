# criteo_api_petstore_preview.PetApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pet**](PetApi.md#add_pet) | **POST** /pet | Add a new pet to the store
[**delete_pet**](PetApi.md#delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
[**find_pets_by_status**](PetApi.md#find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
[**find_pets_by_tags**](PetApi.md#find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
[**get_pet_by_id**](PetApi.md#get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
[**update_pet_with_form**](PetApi.md#update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
[**upload_file**](PetApi.md#upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image


# **add_pet**
> Pet add_pet(pet)

Add a new pet to the store

Add a new pet to the store

### Example

* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from criteo_api_petstore_preview.model.pet import Pet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    pet = Pet(
        id=10,
        name="doggie",
        category=Category(
            id=1,
            name="Dogs",
        ),
        photo_urls=[
            "photo_urls_example",
        ],
        tags=[
            Tag(
                id=1,
                name="name_example",
            ),
        ],
        status="available",
    ) # Pet | Create a new pet in the store

    # example passing only required values which don't have defaults set
    try:
        # Add a new pet to the store
        api_response = api_instance.add_pet(pet)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->add_pet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet** | [**Pet**](Pet.md)| Create a new pet in the store |

### Return type

[**Pet**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pet**
> delete_pet(pet_id)

Deletes a pet

### Example

* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    pet_id = 1 # int | Pet id to delete
    api_key = "api_key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a pet
        api_instance.delete_pet(pet_id)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->delete_pet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a pet
        api_instance.delete_pet(pet_id, api_key=api_key)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->delete_pet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| Pet id to delete |
 **api_key** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid pet value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_pets_by_status**
> [Pet] find_pets_by_status()

Finds Pets by status

Multiple status values can be provided with comma separated strings

### Example

* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from criteo_api_petstore_preview.model.pet import Pet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    status = "available" # str | Status values that need to be considered for filter (optional) if omitted the server will use the default value of "available"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Finds Pets by status
        api_response = api_instance.find_pets_by_status(status=status)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->find_pets_by_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Status values that need to be considered for filter | [optional] if omitted the server will use the default value of "available"

### Return type

[**[Pet]**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_pets_by_tags**
> [Pet] find_pets_by_tags()

Finds Pets by tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example

* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from criteo_api_petstore_preview.model.pet import Pet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    tags = [
        "tags_example",
    ] # [str] | Tags to filter by (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Finds Pets by tags
        api_response = api_instance.find_pets_by_tags(tags=tags)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->find_pets_by_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **[str]**| Tags to filter by | [optional]

### Return type

[**[Pet]**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid tag value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pet_by_id**
> Pet get_pet_by_id(pet_id)

Find pet by ID

Returns a single pet

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from criteo_api_petstore_preview.model.pet import Pet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    pet_id = 1 # int | ID of pet to return

    # example passing only required values which don't have defaults set
    try:
        # Find pet by ID
        api_response = api_instance.get_pet_by_id(pet_id)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->get_pet_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet to return |

### Return type

[**Pet**](Pet.md)

### Authorization

[api_key](../README.md#api_key), [petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Pet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pet_with_form**
> update_pet_with_form(pet_id)

Updates a pet in the store with form data

### Example

* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    pet_id = 1 # int | ID of pet that needs to be updated
    name = "name_example" # str | Name of pet that needs to be updated (optional)
    status = "status_example" # str | Status of pet that needs to be updated (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a pet in the store with form data
        api_instance.update_pet_with_form(pet_id)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a pet in the store with form data
        api_instance.update_pet_with_form(pet_id, name=name, status=status)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet that needs to be updated |
 **name** | **str**| Name of pet that needs to be updated | [optional]
 **status** | **str**| Status of pet that needs to be updated | [optional]

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ApiResponse upload_file(pet_id)

uploads an image

### Example

* OAuth Authentication (petstore_auth):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import pet_api
from criteo_api_petstore_preview.model.api_response import ApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: petstore_auth
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)
    pet_id = 1 # int | ID of pet to update
    additional_metadata = "additionalMetadata_example" # str | Additional Metadata (optional)
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # uploads an image
        api_response = api_instance.upload_file(pet_id)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->upload_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # uploads an image
        api_response = api_instance.upload_file(pet_id, additional_metadata=additional_metadata, body=body)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling PetApi->upload_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet to update |
 **additional_metadata** | **str**| Additional Metadata | [optional]
 **body** | **file_type**|  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

