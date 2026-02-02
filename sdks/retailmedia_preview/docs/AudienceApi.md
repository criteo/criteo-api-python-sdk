# criteo_api_retailmedia_preview.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_contact_list_by_audience_segment**](AudienceApi.md#add_remove_contact_list_by_audience_segment) | **POST** /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | 
[**bulk_create_audience**](AudienceApi.md#bulk_create_audience) | **POST** /preview/retail-media/accounts/{account-id}/audiences/create | 
[**bulk_create_audience_segments**](AudienceApi.md#bulk_create_audience_segments) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/create | 
[**bulk_delete_audience_segments**](AudienceApi.md#bulk_delete_audience_segments) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/delete | 
[**bulk_delete_audiences**](AudienceApi.md#bulk_delete_audiences) | **POST** /preview/retail-media/accounts/{account-id}/audiences/delete | 
[**bulk_update_audience**](AudienceApi.md#bulk_update_audience) | **PATCH** /preview/retail-media/accounts/{account-id}/audiences | 
[**bulk_update_audience_segments**](AudienceApi.md#bulk_update_audience_segments) | **PATCH** /preview/retail-media/accounts/{account-id}/audience-segments | 
[**clear_contact_list_by_audience_segment**](AudienceApi.md#clear_contact_list_by_audience_segment) | **POST** /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | 
[**compute_audience_segments_sizes**](AudienceApi.md#compute_audience_segments_sizes) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/compute-sizes | 
[**compute_audiences_sizes**](AudienceApi.md#compute_audiences_sizes) | **POST** /preview/retail-media/accounts/{account-id}/audiences/compute-sizes | 
[**estimate_audience_segment_size**](AudienceApi.md#estimate_audience_segment_size) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/estimate-size | 
[**estimate_audience_size**](AudienceApi.md#estimate_audience_size) | **POST** /preview/retail-media/accounts/{account-id}/audiences/estimate-size | 
[**get_audience_segment_contact_list_statistics**](AudienceApi.md#get_audience_segment_contact_list_statistics) | **GET** /preview/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | 
[**search_audience_segments**](AudienceApi.md#search_audience_segments) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/search | 
[**search_audiences**](AudienceApi.md#search_audiences) | **POST** /preview/retail-media/accounts/{account-id}/audiences/search | 


# **add_remove_contact_list_by_audience_segment**
> RetailMediaContactlistOperation add_remove_contact_list_by_audience_segment(audience_segment_id, retail_media_contactlist_amendment_request)



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
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **bulk_create_audience**
> RmAudienceEntityV1ListResponse bulk_create_audience(account_id, rm_audience_bulk_create_input_v1)



Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_entity_v1_list_response import RmAudienceEntityV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_bulk_create_input_v1 import RmAudienceBulkCreateInputV1
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
    rm_audience_bulk_create_input_v1 = RmAudienceBulkCreateInputV1(
        data=[
            RmAudienceCreateEntityV1Resource(
                attributes=RmAudienceCreateEntityV1(
                    algebra=RmAlgebraNodeV1(
                        _and=[
                            RmAlgebraNodeV1(),
                        ],
                        audience_segment_id="audience_segment_id_example",
                        _not=RmAlgebraNodeV1(),
                        _or=[
                            RmAlgebraNodeV1(),
                        ],
                    ),
                    description="description_example",
                    name="name_example",
                    retailer_id="retailer_id_example",
                ),
                type="type_example",
            ),
        ],
    ) # RmAudienceBulkCreateInputV1 | Audience creation parameter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_audience(account_id, rm_audience_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->bulk_create_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_bulk_create_input_v1** | [**RmAudienceBulkCreateInputV1**](RmAudienceBulkCreateInputV1.md)| Audience creation parameter |

### Return type

[**RmAudienceEntityV1ListResponse**](RmAudienceEntityV1ListResponse.md)

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

# **bulk_create_audience_segments**
> RmAudienceSegmentEntityV1ListResponse bulk_create_audience_segments(account_id, rm_audience_segment_bulk_create_input_v1)



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
    except criteo_api_retailmedia_preview.ApiException as e:
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
        api_response = api_instance.bulk_delete_audience_segments(account_id, rm_audience_segment_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **bulk_delete_audiences**
> RmAudienceSegmentIdEntityV1ListResponse bulk_delete_audiences(account_id, rm_audience_bulk_delete_input_v1)



Deletes the audiences associated to the given IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_id_entity_v1_list_response import RmAudienceSegmentIdEntityV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_bulk_delete_input_v1 import RmAudienceBulkDeleteInputV1
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
    rm_audience_bulk_delete_input_v1 = RmAudienceBulkDeleteInputV1(
        data=[
            RmAudienceDeleteEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # RmAudienceBulkDeleteInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_delete_audiences(account_id, rm_audience_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->bulk_delete_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_bulk_delete_input_v1** | [**RmAudienceBulkDeleteInputV1**](RmAudienceBulkDeleteInputV1.md)|  |

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
**200** | Success |  -  |
**204** | Success or partial success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_audience**
> RmAudienceEntityV1ListResponse bulk_update_audience(account_id, rm_audience_bulk_update_input_v1)



Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_bulk_update_input_v1 import RmAudienceBulkUpdateInputV1
from criteo_api_retailmedia_preview.model.rm_audience_entity_v1_list_response import RmAudienceEntityV1ListResponse
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
    rm_audience_bulk_update_input_v1 = RmAudienceBulkUpdateInputV1(
        data=[
            RmAudienceUpdateEntityV1Resource(
                attributes=RmAudienceUpdateEntityV1(
                    algebra=RmAlgebraNodeV1(
                        _and=[
                            RmAlgebraNodeV1(),
                        ],
                        audience_segment_id="audience_segment_id_example",
                        _not=RmAlgebraNodeV1(),
                        _or=[
                            RmAlgebraNodeV1(),
                        ],
                    ),
                    description=NillableString(
                        value="value_example",
                    ),
                    name="name_example",
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # RmAudienceBulkUpdateInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_audience(account_id, rm_audience_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->bulk_update_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_bulk_update_input_v1** | [**RmAudienceBulkUpdateInputV1**](RmAudienceBulkUpdateInputV1.md)|  |

### Return type

[**RmAudienceEntityV1ListResponse**](RmAudienceEntityV1ListResponse.md)

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
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
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
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend, we only accept external Id here

    # example passing only required values which don't have defaults set
    try:
        api_instance.clear_contact_list_by_audience_segment(audience_segment_id)
    except criteo_api_retailmedia_preview.ApiException as e:
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

# **compute_audience_segments_sizes**
> RmAudienceSegmentSizeEntityV1ListResponse compute_audience_segments_sizes(account_id, rm_audience_segment_compute_sizes_input_v1)



Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_size_entity_v1_list_response import RmAudienceSegmentSizeEntityV1ListResponse
from criteo_api_retailmedia_preview.model.rm_audience_segment_compute_sizes_input_v1 import RmAudienceSegmentComputeSizesInputV1
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
    rm_audience_segment_compute_sizes_input_v1 = RmAudienceSegmentComputeSizesInputV1(
        data=RmAudienceSegmentComputeSizeEntityV1Resource(
            attributes=RmAudienceSegmentComputeSizeEntityV1(
                channel="Onsite",
                ids=[
                    "ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # RmAudienceSegmentComputeSizesInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.compute_audience_segments_sizes(account_id, rm_audience_segment_compute_sizes_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->compute_audience_segments_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id |
 **rm_audience_segment_compute_sizes_input_v1** | [**RmAudienceSegmentComputeSizesInputV1**](RmAudienceSegmentComputeSizesInputV1.md)|  |

### Return type

[**RmAudienceSegmentSizeEntityV1ListResponse**](RmAudienceSegmentSizeEntityV1ListResponse.md)

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

# **compute_audiences_sizes**
> RmAudienceSizeEntityV1ListResponse compute_audiences_sizes(account_id, rm_audience_compute_sizes_input_v1)



Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_compute_sizes_input_v1 import RmAudienceComputeSizesInputV1
from criteo_api_retailmedia_preview.model.rm_audience_size_entity_v1_list_response import RmAudienceSizeEntityV1ListResponse
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
    rm_audience_compute_sizes_input_v1 = RmAudienceComputeSizesInputV1(
        data=RmAudienceComputeSizeEntityV1Resource(
            attributes=RmAudienceComputeSizeEntityV1(
                channel="Onsite",
                ids=[
                    "ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # RmAudienceComputeSizesInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.compute_audiences_sizes(account_id, rm_audience_compute_sizes_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->compute_audiences_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_compute_sizes_input_v1** | [**RmAudienceComputeSizesInputV1**](RmAudienceComputeSizesInputV1.md)|  |

### Return type

[**RmAudienceSizeEntityV1ListResponse**](RmAudienceSizeEntityV1ListResponse.md)

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

# **estimate_audience_segment_size**
> RmAudienceSegmentSizeEstimationV1Response estimate_audience_segment_size(account_id, rm_audience_segment_estimate_size_input_v1)



Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_segment_size_estimation_v1_response import RmAudienceSegmentSizeEstimationV1Response
from criteo_api_retailmedia_preview.model.rm_audience_segment_estimate_size_input_v1 import RmAudienceSegmentEstimateSizeInputV1
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
    rm_audience_segment_estimate_size_input_v1 = RmAudienceSegmentEstimateSizeInputV1(
        data=RmAudienceSegmentEstimateSizeEntityV1Resource(
            attributes=RmAudienceSegmentEstimateSizeEntityV1(
                channel="Onsite",
                events=RmEventsEstimationV1(
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
                retailer_id="retailer_id_example",
            ),
            type="type_example",
        ),
    ) # RmAudienceSegmentEstimateSizeInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.estimate_audience_segment_size(account_id, rm_audience_segment_estimate_size_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->estimate_audience_segment_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_segment_estimate_size_input_v1** | [**RmAudienceSegmentEstimateSizeInputV1**](RmAudienceSegmentEstimateSizeInputV1.md)|  |

### Return type

[**RmAudienceSegmentSizeEstimationV1Response**](RmAudienceSegmentSizeEstimationV1Response.md)

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

# **estimate_audience_size**
> RmAudienceSizeEstimationV1Response estimate_audience_size(account_id, rm_audience_estimate_size_input_v1)



Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_size_estimation_v1_response import RmAudienceSizeEstimationV1Response
from criteo_api_retailmedia_preview.model.rm_audience_estimate_size_input_v1 import RmAudienceEstimateSizeInputV1
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
    rm_audience_estimate_size_input_v1 = RmAudienceEstimateSizeInputV1(
        data=RmAudienceEstimateSizeEntityV1Resource(
            attributes=RmAudienceEstimateSizeEntityV1(
                algebra=RmAlgebraNodeV1(
                    _and=[
                        RmAlgebraNodeV1(),
                    ],
                    audience_segment_id="audience_segment_id_example",
                    _not=RmAlgebraNodeV1(),
                    _or=[
                        RmAlgebraNodeV1(),
                    ],
                ),
                channel="Onsite",
                retailer_id="retailer_id_example",
            ),
            type="type_example",
        ),
    ) # RmAudienceEstimateSizeInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.estimate_audience_size(account_id, rm_audience_estimate_size_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->estimate_audience_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **rm_audience_estimate_size_input_v1** | [**RmAudienceEstimateSizeInputV1**](RmAudienceEstimateSizeInputV1.md)|  |

### Return type

[**RmAudienceSizeEstimationV1Response**](RmAudienceSizeEstimationV1Response.md)

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

# **get_audience_segment_contact_list_statistics**
> RmContactListStatisticsEntityV1Response get_audience_segment_contact_list_statistics(account_id, audience_segment_id)



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
        api_response = api_instance.get_audience_segment_contact_list_statistics(account_id, audience_segment_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->search_audience_segments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audience_segments(account_id, rm_audience_segment_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import audience_api
from criteo_api_retailmedia_preview.model.rm_audience_search_input_v1 import RmAudienceSearchInputV1
from criteo_api_retailmedia_preview.model.rm_audience_entity_v1_rm_audience_search_metadata_v1_list_response import RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse
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
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling AudienceApi->search_audiences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audiences(account_id, rm_audience_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
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

