# criteo_api_retailmedia_v2025_10.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_contact_list_by_audience_segment**](AudienceApi.md#add_remove_contact_list_by_audience_segment) | **POST** /2025-10/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | 
[**bulk_create_audience_segments**](AudienceApi.md#bulk_create_audience_segments) | **POST** /2025-10/retail-media/accounts/{account-id}/audience-segments/create | 
[**bulk_delete_audience_segments**](AudienceApi.md#bulk_delete_audience_segments) | **POST** /2025-10/retail-media/accounts/{account-id}/audience-segments/delete | 
[**bulk_update_audience_segments**](AudienceApi.md#bulk_update_audience_segments) | **PATCH** /2025-10/retail-media/accounts/{account-id}/audience-segments | 
[**clear_contact_list_by_audience_segment**](AudienceApi.md#clear_contact_list_by_audience_segment) | **POST** /2025-10/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | 
[**get_audience_segment_contact_list_statistics**](AudienceApi.md#get_audience_segment_contact_list_statistics) | **GET** /2025-10/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | 
[**search_audience_segments**](AudienceApi.md#search_audience_segments) | **POST** /2025-10/retail-media/accounts/{account-id}/audience-segments/search | 
[**search_audiences**](AudienceApi.md#search_audiences) | **POST** /2025-10/retail-media/accounts/{account-id}/audiences/search | 


# **add_remove_contact_list_by_audience_segment**
> RetailMediaContactlistOperation add_remove_contact_list_by_audience_segment(audience_segment_id, retail_media_contactlist_amendment_request)



Add/remove identifiers to or from a retail-media contact list audience-segment, with external audience segment id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.retail_media_contactlist_operation import RetailMediaContactlistOperation
from criteo_api_retailmedia_v2025_10.model.retail_media_contactlist_amendment_request import RetailMediaContactlistAmendmentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend, we only accept external Id here
    retail_media_contactlist_amendment_request = RetailMediaContactlistAmendmentRequest(
        data=RetailMediaContactlistAmendment(
            attributes=RetailMediaContactlistAmendmentAttributes(
                identifiers=[
                    "identifiers_example",
                ],
                identifier_type="Email",
                operation="add",
            ),
            type="AddRemoveContactlist",
        ),
    ) # RetailMediaContactlistAmendmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_remove_contact_list_by_audience_segment(audience_segment_id, retail_media_contactlist_amendment_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->add_remove_contact_list_by_audience_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The id of the contact list audience-segment to amend, we only accept external Id here |
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_audience_segments**
> RmAudienceSegmentEntityV1ListResponse bulk_create_audience_segments(account_id, rm_audience_segment_bulk_create_input_v1)



Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_bulk_create_input_v1 import RmAudienceSegmentBulkCreateInputV1
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_entity_v1_list_response import RmAudienceSegmentEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    rm_audience_segment_bulk_create_input_v1 = RmAudienceSegmentBulkCreateInputV1(
        data=[
            RmAudienceSegmentCreateEntityV1Resource(
                attributes=RmAudienceSegmentCreateEntityV1(
                    contact_list=RmContactListCreateV1(
                        identifier_type="Email",
                    ),
                    description="description_example",
                    events=RmEventsCreateV1(
                        brand_ids=[
                            "brand_ids_example",
                        ],
                        category_ids=[
                            "category_ids_example",
                        ],
                        lookback_days="Last7Days",
                        max_price=3.14,
                        min_price=3.14,
                        shopper_activity="View",
                    ),
                    name="name_example",
                    retailer_id="retailer_id_example",
                ),
                type="type_example",
            ),
        ],
    ) # RmAudienceSegmentBulkCreateInputV1 | Segment creation parameter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_audience_segments(account_id, rm_audience_segment_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->bulk_create_audience_segments: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_audience_segments**
> RmAudienceSegmentIdEntityV1ListResponse bulk_delete_audience_segments(account_id, rm_audience_segment_bulk_delete_input_v1)



Delete the segments associated to the given IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_bulk_delete_input_v1 import RmAudienceSegmentBulkDeleteInputV1
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_id_entity_v1_list_response import RmAudienceSegmentIdEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
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
        api_response = api_instance.bulk_delete_audience_segments(account_id, rm_audience_segment_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->bulk_delete_audience_segments: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_audience_segments**
> RmAudienceSegmentEntityV1ListResponse bulk_update_audience_segments(account_id, rm_audience_segment_bulk_update_input_v1)



Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_bulk_update_input_v1 import RmAudienceSegmentBulkUpdateInputV1
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_entity_v1_list_response import RmAudienceSegmentEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account id
    rm_audience_segment_bulk_update_input_v1 = RmAudienceSegmentBulkUpdateInputV1(
        data=[
            RmAudienceSegmentUpdateEntityV1Resource(
                attributes=RmAudienceSegmentUpdateEntityV1(
                    contact_list={},
                    description=NillableString(
                        value="value_example",
                    ),
                    events=RmEventsUpdateV1(
                        brand_ids=[
                            "brand_ids_example",
                        ],
                        category_ids=[
                            "category_ids_example",
                        ],
                        lookback_days="Last7Days",
                        max_price=NillableDecimal(
                            value=3.14,
                        ),
                        min_price=NillableDecimal(
                            value=3.14,
                        ),
                        shopper_activity="View",
                    ),
                    name="name_example",
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # RmAudienceSegmentBulkUpdateInputV1 | Segment Update request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_audience_segments(account_id, rm_audience_segment_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->bulk_update_audience_segments: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_contact_list_by_audience_segment**
> clear_contact_list_by_audience_segment(audience_segment_id)



Delete all identifiers from a retail-media contact list audience-segment, with external audience segment id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend, we only accept external Id here

    # example passing only required values which don't have defaults set
    try:
        api_instance.clear_contact_list_by_audience_segment(audience_segment_id)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->clear_contact_list_by_audience_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The id of the contact list audience-segment to amend, we only accept external Id here |

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
> RmContactListStatisticsEntityV1Response get_audience_segment_contact_list_statistics(account_id, audience_segment_id)



Returns the statistics of a contact list segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.rm_contact_list_statistics_entity_v1_response import RmContactListStatisticsEntityV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    audience_segment_id = "audience-segment-id_example" # str | Segment Id.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audience_segment_contact_list_statistics(account_id, audience_segment_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->get_audience_segment_contact_list_statistics: %s\n" % e)
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_audience_segments**
> RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse search_audience_segments(account_id, rm_audience_segment_search_input_v1)



Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_entity_v1_rm_audience_segment_search_metadata_v1_list_response import RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse
from criteo_api_retailmedia_v2025_10.model.rm_audience_segment_search_input_v1 import RmAudienceSegmentSearchInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    rm_audience_segment_search_input_v1 = RmAudienceSegmentSearchInputV1(
        data=RmAudienceSegmentSearchEntityV1Resource(
            attributes=RmAudienceSegmentSearchEntityV1(
                audience_segment_ids=[
                    "audience_segment_ids_example",
                ],
                audience_segment_types=[
                    "Unknown",
                ],
                retailer_ids=[
                    "retailer_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # RmAudienceSegmentSearchInputV1 | Segment search filters.
    limit = 50 # int | The number of elements to be returned. The default is 50 and the maximum is 500. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The (zero-based) offset into the collection. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_audience_segments(account_id, rm_audience_segment_search_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->search_audience_segments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audience_segments(account_id, rm_audience_segment_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->search_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_segment_search_input_v1** | [**RmAudienceSegmentSearchInputV1**](RmAudienceSegmentSearchInputV1.md)| Segment search filters. |
 **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse**](RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse.md)

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

# **search_audiences**
> RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse search_audiences(account_id, rm_audience_search_input_v1)



Returns a list of audiences that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2025_10
from criteo_api_retailmedia_v2025_10.api import audience_api
from criteo_api_retailmedia_v2025_10.model.rm_audience_search_input_v1 import RmAudienceSearchInputV1
from criteo_api_retailmedia_v2025_10.model.rm_audience_entity_v1_rm_audience_search_metadata_v1_list_response import RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2025_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2025_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "account-id_example" # str | Account Id
    rm_audience_search_input_v1 = RmAudienceSearchInputV1(
        data=RmAudienceSearchEntityV1Resource(
            attributes=RmAudienceSearchEntityV1(
                audience_ids=[
                    "audience_ids_example",
                ],
                audience_segment_ids=[
                    "audience_segment_ids_example",
                ],
                retailer_ids=[
                    "retailer_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # RmAudienceSearchInputV1 | Audience search filters.
    limit = 50 # int | The number of elements to be returned. The default is 50 and the maximum is 500. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The (zero-based) offset into the collection. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_audiences(account_id, rm_audience_search_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->search_audiences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audiences(account_id, rm_audience_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_v2025_10.ApiException as e:
        print("Exception when calling AudienceApi->search_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_search_input_v1** | [**RmAudienceSearchInputV1**](RmAudienceSearchInputV1.md)| Audience search filters. |
 **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse**](RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse.md)

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

