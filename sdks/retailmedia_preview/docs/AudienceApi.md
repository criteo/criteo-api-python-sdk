# criteo_api_retailmedia_preview.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_v1**](AudienceApi.md#bulk_create_v1) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/create | 
[**bulk_delete_v1**](AudienceApi.md#bulk_delete_v1) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/delete | 
[**bulk_update_v1**](AudienceApi.md#bulk_update_v1) | **PATCH** /preview/retail-media/accounts/{account-id}/audience-segments | 
[**delete_contact_list_identifiers**](AudienceApi.md#delete_contact_list_identifiers) | **POST** /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | 
[**get_contact_list_statistics_v1**](AudienceApi.md#get_contact_list_statistics_v1) | **GET** /preview/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | 
[**legacy_get_audience_v1**](AudienceApi.md#legacy_get_audience_v1) | **GET** /preview/retail-media/accounts/{accountId}/audiences | 
[**legacy_get_audience_v2**](AudienceApi.md#legacy_get_audience_v2) | **GET** /preview/retail-media/v2/accounts/{accountId}/audiences | 
[**search_v1**](AudienceApi.md#search_v1) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/search | 
[**update_contact_list_identifiers**](AudienceApi.md#update_contact_list_identifiers) | **POST** /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | 


# **bulk_create_v1**
> RmAudienceSegmentEntityV1ListResponse bulk_create_v1(account_id, rm_audience_segment_bulk_create_input_v1)



Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_entity_v1_list_response import RmAudienceSegmentEntityV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_segment_bulk_create_input_v1 import RmAudienceSegmentBulkCreateInputV1
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    rm_audience_segment_bulk_create_input_v1 = RmAudienceSegmentBulkCreateInputV1(
        data=[
            RmAudienceSegmentCreateEntityV1Resource(
                type="type_example",
                attributes=RmAudienceSegmentCreateEntityV1(
                    name="name_example",
                    description="description_example",
                    retailer_id="retailer_id_example",
                    contact_list=RmContactListCreateV1(
                        identifier_type="Email",
                    ),
                ),
            ),
        ],
    ) # RmAudienceSegmentBulkCreateInputV1 | Segment creation parameter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_v1(account_id, rm_audience_segment_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->bulk_create_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_segment_bulk_create_input_v1** | [**RmAudienceSegmentBulkCreateInputV1**](RmAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter |

### Return type

[**RmAudienceSegmentEntityV1ListResponse**](RmAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_v1**
> RmAudienceSegmentIdEntityV1ListResponse bulk_delete_v1(account_id, rm_audience_segment_bulk_delete_input_v1)



Delete the segments associated to the given audience IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_id_entity_v1_list_response import RmAudienceSegmentIdEntityV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_segment_bulk_delete_input_v1 import RmAudienceSegmentBulkDeleteInputV1
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account id
    rm_audience_segment_bulk_delete_input_v1 = RmAudienceSegmentBulkDeleteInputV1(
        data=[
            RmAudienceSegmentDeleteEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # RmAudienceSegmentBulkDeleteInputV1 | Segment delete request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_delete_v1(account_id, rm_audience_segment_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->bulk_delete_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id |
 **rm_audience_segment_bulk_delete_input_v1** | [**RmAudienceSegmentBulkDeleteInputV1**](RmAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. |

### Return type

[**RmAudienceSegmentIdEntityV1ListResponse**](RmAudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_v1**
> RmAudienceSegmentEntityV1ListResponse bulk_update_v1(account_id, rm_audience_segment_bulk_update_input_v1)



Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_entity_v1_list_response import RmAudienceSegmentEntityV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_segment_bulk_update_input_v1 import RmAudienceSegmentBulkUpdateInputV1
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account id
    rm_audience_segment_bulk_update_input_v1 = RmAudienceSegmentBulkUpdateInputV1(
        data=[
            RmAudienceSegmentUpdateEntityV1Resource(
                attributes=RmAudienceSegmentUpdateEntityV1(
                    name="name_example",
                    description=NillableString(
                        value="value_example",
                    ),
                    contact_list={},
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # RmAudienceSegmentBulkUpdateInputV1 | Segment Update request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_v1(account_id, rm_audience_segment_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->bulk_update_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id |
 **rm_audience_segment_bulk_update_input_v1** | [**RmAudienceSegmentBulkUpdateInputV1**](RmAudienceSegmentBulkUpdateInputV1.md)| Segment Update request |

### Return type

[**RmAudienceSegmentEntityV1ListResponse**](RmAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_list_identifiers**
> delete_contact_list_identifiers(audience_segment_id)



Delete all identifiers from a retail-media contact list audience-segment, with external audience segment id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.error_code_response import ErrorCodeResponse
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
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = 1 # int | The id of the contact list audience-segment to amend, we only accept external Id here

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_contact_list_identifiers(audience_segment_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->delete_contact_list_identifiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **int**| The id of the contact list audience-segment to amend, we only accept external Id here |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Contact List identifiers were deleted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_list_statistics_v1**
> RmContactListStatisticsEntityV1Response get_contact_list_statistics_v1(account_id, audience_segment_id)



Returns the statistics of a contact list segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_contact_list_statistics_entity_v1_response import RmContactListStatisticsEntityV1Response
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    audience_segment_id = "audience-segment-id_example" # str | Segment Id.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_contact_list_statistics_v1(account_id, audience_segment_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->get_contact_list_statistics_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **audience_segment_id** | **str**| Segment Id. |

### Return type

[**RmContactListStatisticsEntityV1Response**](RmContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_get_audience_v1**
> RmLegacyAudienceGetEntityV1ListResponse legacy_get_audience_v1(account_id)



Get a page of Audiences. (deprecated Public API)

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_legacy_audience_get_entity_v1_list_response import RmLegacyAudienceGetEntityV1ListResponse
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = 1 # int | ID of the account to which this audience belongs.
    limit_to_id = [
        1,
    ] # [int] | Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2 (optional)
    page_size = 1 # int | Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. (optional)
    page_index = 1 # int | Returns the specified page of results given a pageSize; pages are 0-indexed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legacy_get_audience_v1(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.legacy_get_audience_v1(account_id, limit_to_id=limit_to_id, page_size=page_size, page_index=page_index)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| ID of the account to which this audience belongs. |
 **limit_to_id** | **[int]**| Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId&#x3D;1&amp;limitToId&#x3D;2 | [optional]
 **page_size** | **int**| Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. | [optional]
 **page_index** | **int**| Returns the specified page of results given a pageSize; pages are 0-indexed. | [optional]

### Return type

[**RmLegacyAudienceGetEntityV1ListResponse**](RmLegacyAudienceGetEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of audiences for the supplied account or shared by related retailers. |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_get_audience_v2**
> RmLegacyAudienceGetEntityV2ListResponse legacy_get_audience_v2(account_id)



Get a page of Audiences. (deprecated Public API)

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_legacy_audience_get_entity_v2_list_response import RmLegacyAudienceGetEntityV2ListResponse
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = 1 # int | ID of the account to which this audience belongs.
    limit_to_id = [
        1,
    ] # [int] | Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2 (optional)
    page_size = 1 # int | Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. (optional)
    page_index = 1 # int | Returns the specified page of results given a pageSize; pages are 0-indexed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legacy_get_audience_v2(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.legacy_get_audience_v2(account_id, limit_to_id=limit_to_id, page_size=page_size, page_index=page_index)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| ID of the account to which this audience belongs. |
 **limit_to_id** | **[int]**| Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId&#x3D;1&amp;limitToId&#x3D;2 | [optional]
 **page_size** | **int**| Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. | [optional]
 **page_index** | **int**| Returns the specified page of results given a pageSize; pages are 0-indexed. | [optional]

### Return type

[**RmLegacyAudienceGetEntityV2ListResponse**](RmLegacyAudienceGetEntityV2ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of audiences for the supplied account or shared by related retailers. |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_v1**
> RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse search_v1(account_id, rm_audience_segment_search_input_v1)



Search segments based on the provided filters.( by ids or retailer ids)

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_entity_v1_rm_audience_segment_search_metadata_v1_list_response import RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_segment_search_input_v1 import RmAudienceSegmentSearchInputV1
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
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    rm_audience_segment_search_input_v1 = RmAudienceSegmentSearchInputV1(
        data=RmAudienceSegmentSearchEntityV1Resource(
            type="type_example",
            attributes=RmAudienceSegmentSearchEntityV1(
                audience_segment_ids=[
                    "audience_segment_ids_example",
                ],
                retailer_ids=[
                    "retailer_ids_example",
                ],
            ),
        ),
    ) # RmAudienceSegmentSearchInputV1 | Segment creation parameter
    limit = 50 # int | The number of elements to be returned. The default is 50 and the maximum is 100. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The (zero-based) offset into the collection. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_v1(account_id, rm_audience_segment_search_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->search_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_v1(account_id, rm_audience_segment_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->search_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_segment_search_input_v1** | [**RmAudienceSegmentSearchInputV1**](RmAudienceSegmentSearchInputV1.md)| Segment creation parameter |
 **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse**](RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_list_identifiers**
> RetailMediaContactlistOperation update_contact_list_identifiers(audience_segment_id, retail_media_contactlist_amendment_request)



Add/remove identifiers to or from a retail-media contact list audience-segment, with external audience segment id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.retail_media_contactlist_amendment_request import RetailMediaContactlistAmendmentRequest
from criteo_api_retailmedia_preview.model.retail_media_contactlist_operation import RetailMediaContactlistOperation
from criteo_api_retailmedia_preview.model.error_code_response import ErrorCodeResponse
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
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = 1 # int | The id of the contact list audience-segment to amend, we only accept external Id here
    retail_media_contactlist_amendment_request = RetailMediaContactlistAmendmentRequest(
        data=RetailMediaContactlistAmendment(
            type="AddRemoveContactlist",
            attributes=RetailMediaContactlistAmendmentAttributes(
                operation="add",
                identifier_type="Email",
                identifiers=[
                    "identifiers_example",
                ],
            ),
        ),
    ) # RetailMediaContactlistAmendmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_contact_list_identifiers(audience_segment_id, retail_media_contactlist_amendment_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->update_contact_list_identifiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **int**| The id of the contact list audience-segment to amend, we only accept external Id here |
 **retail_media_contactlist_amendment_request** | [**RetailMediaContactlistAmendmentRequest**](RetailMediaContactlistAmendmentRequest.md)|  |

### Return type

[**RetailMediaContactlistOperation**](RetailMediaContactlistOperation.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of created request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

