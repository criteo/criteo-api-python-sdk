# criteo_api_commercegrid_v2026_01.SegmentApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_contact_list_by_audience_segment**](SegmentApi.md#add_remove_contact_list_by_audience_segment) | **POST** /2026-01/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove | 
[**bulk_create_audience_segments**](SegmentApi.md#bulk_create_audience_segments) | **POST** /2026-01/commerce-grid/audience-segments/create | 
[**bulk_delete_audience_segments**](SegmentApi.md#bulk_delete_audience_segments) | **POST** /2026-01/commerce-grid/audience-segments/delete | 
[**bulk_update_audience_segments**](SegmentApi.md#bulk_update_audience_segments) | **PATCH** /2026-01/commerce-grid/audience-segments | 
[**clear_contact_list_by_audience_segment**](SegmentApi.md#clear_contact_list_by_audience_segment) | **POST** /2026-01/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear | 
[**get_audience_segment_contact_list_statistics**](SegmentApi.md#get_audience_segment_contact_list_statistics) | **GET** /2026-01/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics | 
[**search_audience_segments**](SegmentApi.md#search_audience_segments) | **POST** /2026-01/commerce-grid/audience-segments/search | 


# **add_remove_contact_list_by_audience_segment**
> CommerceGridContactlistOperation add_remove_contact_list_by_audience_segment(audience_segment_id, commerce_grid_contactlist_amendment_request)



Add/remove identifiers to or from a Commerce Grid audience segment of type Contact List.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from criteo_api_commercegrid_v2026_01.model.commerce_grid_contactlist_operation import CommerceGridContactlistOperation
from criteo_api_commercegrid_v2026_01.model.commerce_grid_contactlist_amendment_request import CommerceGridContactlistAmendmentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The ID of the audience segment of type contact list to amend
    commerce_grid_contactlist_amendment_request = CommerceGridContactlistAmendmentRequest(
        data=CommerceGridContactlistAmendment(
            attributes=CommerceGridContactlistAmendmentAttributes(
                identifiers=[
                    "identifiers_example",
                ],
                identifier_type="Email",
                operation="Add",
            ),
            type="AddRemoveContactlist",
        ),
    ) # CommerceGridContactlistAmendmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_remove_contact_list_by_audience_segment(audience_segment_id, commerce_grid_contactlist_amendment_request)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->add_remove_contact_list_by_audience_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The ID of the audience segment of type contact list to amend |
 **commerce_grid_contactlist_amendment_request** | [**CommerceGridContactlistAmendmentRequest**](CommerceGridContactlistAmendmentRequest.md)|  |

### Return type

[**CommerceGridContactlistOperation**](CommerceGridContactlistOperation.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of the add/remove operation of identifiers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_audience_segments**
> CgAudienceSegmentEntityV1ListResponse bulk_create_audience_segments(cg_audience_segment_bulk_create_input_v1)



Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_bulk_create_input_v1 import CgAudienceSegmentBulkCreateInputV1
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_entity_v1_list_response import CgAudienceSegmentEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    cg_audience_segment_bulk_create_input_v1 = CgAudienceSegmentBulkCreateInputV1(
        data=[
            CgAudienceSegmentCreateEntityV1Resource(
                attributes=CgAudienceSegmentCreateEntityV1(
                    contact_list=CgContactListCreateV1(
                        remote_id="remote_id_example",
                    ),
                    data_provider_id="data_provider_id_example",
                    description="description_example",
                    name="name_example",
                ),
                type="type_example",
            ),
        ],
    ) # CgAudienceSegmentBulkCreateInputV1 | Segment creation parameter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_audience_segments(cg_audience_segment_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->bulk_create_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cg_audience_segment_bulk_create_input_v1** | [**CgAudienceSegmentBulkCreateInputV1**](CgAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter |

### Return type

[**CgAudienceSegmentEntityV1ListResponse**](CgAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_audience_segments**
> CgAudienceSegmentIdEntityV1ListResponse bulk_delete_audience_segments(cg_audience_segment_bulk_delete_input_v1)



Delete the segments associated to the given IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_bulk_delete_input_v1 import CgAudienceSegmentBulkDeleteInputV1
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_id_entity_v1_list_response import CgAudienceSegmentIdEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    cg_audience_segment_bulk_delete_input_v1 = CgAudienceSegmentBulkDeleteInputV1(
        data=[
            CgAudienceSegmentDeleteEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # CgAudienceSegmentBulkDeleteInputV1 | Segment delete request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_delete_audience_segments(cg_audience_segment_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->bulk_delete_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cg_audience_segment_bulk_delete_input_v1** | [**CgAudienceSegmentBulkDeleteInputV1**](CgAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. |

### Return type

[**CgAudienceSegmentIdEntityV1ListResponse**](CgAudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_audience_segments**
> CgAudienceSegmentEntityV1ListResponse bulk_update_audience_segments(cg_audience_segment_bulk_update_input_v1)



Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_bulk_update_input_v1 import CgAudienceSegmentBulkUpdateInputV1
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_entity_v1_list_response import CgAudienceSegmentEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    cg_audience_segment_bulk_update_input_v1 = CgAudienceSegmentBulkUpdateInputV1(
        data=[
            CgAudienceSegmentUpdateEntityV1Resource(
                attributes=CgAudienceSegmentUpdateEntityV1(
                    description=NillableString(
                        value="value_example",
                    ),
                    name="name_example",
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # CgAudienceSegmentBulkUpdateInputV1 | Segment Update request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_audience_segments(cg_audience_segment_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->bulk_update_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cg_audience_segment_bulk_update_input_v1** | [**CgAudienceSegmentBulkUpdateInputV1**](CgAudienceSegmentBulkUpdateInputV1.md)| Segment Update request |

### Return type

[**CgAudienceSegmentEntityV1ListResponse**](CgAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_contact_list_by_audience_segment**
> clear_contact_list_by_audience_segment(audience_segment_id)



Delete all identifiers from a Commerce Grid audience segment of type Contact List.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The ID of the audience segment of type contact list to amend

    # example passing only required values which don't have defaults set
    try:
        api_instance.clear_contact_list_by_audience_segment(audience_segment_id)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->clear_contact_list_by_audience_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The ID of the audience segment of type contact list to amend |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audience_segment_contact_list_statistics**
> CgContactListStatisticsEntityV1Response get_audience_segment_contact_list_statistics(audience_segment_id)



Returns the statistics of a contact list segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from criteo_api_commercegrid_v2026_01.model.cg_contact_list_statistics_entity_v1_response import CgContactListStatisticsEntityV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The segment ID.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audience_segment_contact_list_statistics(audience_segment_id)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->get_audience_segment_contact_list_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The segment ID. |

### Return type

[**CgContactListStatisticsEntityV1Response**](CgContactListStatisticsEntityV1Response.md)

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

# **search_audience_segments**
> CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse search_audience_segments(cg_audience_segment_search_input_v1)



Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_commercegrid_v2026_01
from criteo_api_commercegrid_v2026_01.api import segment_api
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_entity_v1_cg_audience_segment_search_metadata_v1_list_response import CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse
from criteo_api_commercegrid_v2026_01.model.cg_audience_segment_search_input_v1 import CgAudienceSegmentSearchInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_commercegrid_v2026_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_commercegrid_v2026_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_api.SegmentApi(api_client)
    cg_audience_segment_search_input_v1 = CgAudienceSegmentSearchInputV1(
        data=CgAudienceSegmentSearchEntityV1Resource(
            attributes=CgAudienceSegmentSearchEntityV1(
                audience_segment_ids=[
                    "audience_segment_ids_example",
                ],
                audience_segment_types=[
                    "Unknown",
                ],
                data_provider_ids=[
                    "data_provider_ids_example",
                ],
                remote_ids=[
                    "remote_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # CgAudienceSegmentSearchInputV1 | 
    limit = 50 # int | The number of elements to be returned. The default is 50 and the maximum is 100. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The (zero-based) offset into the collection. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_audience_segments(cg_audience_segment_search_input_v1)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->search_audience_segments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audience_segments(cg_audience_segment_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_commercegrid_v2026_01.ApiException as e:
        print("Exception when calling SegmentApi->search_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cg_audience_segment_search_input_v1** | [**CgAudienceSegmentSearchInputV1**](CgAudienceSegmentSearchInputV1.md)|  |
 **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse**](CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse.md)

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

