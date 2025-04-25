# criteo_api_marketingsolutions_v2025_04.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_audience_segments**](AudienceApi.md#bulk_create_audience_segments) | **POST** /2025-04/marketing-solutions/audience-segments/create | 
[**bulk_create_audiences**](AudienceApi.md#bulk_create_audiences) | **POST** /2025-04/marketing-solutions/audiences/create | 
[**bulk_delete_audience_segments**](AudienceApi.md#bulk_delete_audience_segments) | **POST** /2025-04/marketing-solutions/audience-segments/delete | 
[**bulk_delete_audiences**](AudienceApi.md#bulk_delete_audiences) | **POST** /2025-04/marketing-solutions/audiences/delete | 
[**bulk_update_audience_segments**](AudienceApi.md#bulk_update_audience_segments) | **PATCH** /2025-04/marketing-solutions/audience-segments | 
[**bulk_update_audiences**](AudienceApi.md#bulk_update_audiences) | **PATCH** /2025-04/marketing-solutions/audiences | 
[**call_04_audiences_audience_segment_id_contactlist_delete**](AudienceApi.md#call_04_audiences_audience_segment_id_contactlist_delete) | **DELETE** /2025-04/audiences/{audience-segment-id}/contactlist | 
[**call_04_audiences_audience_segment_id_contactlist_patch**](AudienceApi.md#call_04_audiences_audience_segment_id_contactlist_patch) | **PATCH** /2025-04/audiences/{audience-segment-id}/contactlist | 
[**call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_delete**](AudienceApi.md#call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_delete) | **DELETE** /2025-04/marketing-solutions/audience-segments/{audience-segment-id}/contact-list | 
[**call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_patch**](AudienceApi.md#call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_patch) | **PATCH** /2025-04/marketing-solutions/audience-segments/{audience-segment-id}/contact-list | 
[**compute_audience_segments_sizes**](AudienceApi.md#compute_audience_segments_sizes) | **POST** /2025-04/marketing-solutions/audience-segments/compute-sizes | 
[**compute_audiences_sizes**](AudienceApi.md#compute_audiences_sizes) | **POST** /2025-04/marketing-solutions/audiences/compute-sizes | 
[**estimate_audience_segment_size**](AudienceApi.md#estimate_audience_segment_size) | **POST** /2025-04/marketing-solutions/audience-segments/estimate-size | 
[**estimate_audience_size**](AudienceApi.md#estimate_audience_size) | **POST** /2025-04/marketing-solutions/audiences/estimate-size | 
[**get_audience_segment_contact_list_statistics**](AudienceApi.md#get_audience_segment_contact_list_statistics) | **GET** /2025-04/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics | 
[**get_audience_segments_in_market_brands**](AudienceApi.md#get_audience_segments_in_market_brands) | **GET** /2025-04/marketing-solutions/audience-segments/in-market-brands | 
[**get_audience_segments_in_market_interests**](AudienceApi.md#get_audience_segments_in_market_interests) | **GET** /2025-04/marketing-solutions/audience-segments/in-market-interests | 
[**search_audience_segments**](AudienceApi.md#search_audience_segments) | **POST** /2025-04/marketing-solutions/audience-segments/search | 
[**search_audiences**](AudienceApi.md#search_audiences) | **POST** /2025-04/marketing-solutions/audiences/search | 


# **bulk_create_audience_segments**
> AudienceSegmentEntityV1ListResponse bulk_create_audience_segments(audience_segment_bulk_create_input_v1)



Creates all segments with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_entity_v1_list_response import AudienceSegmentEntityV1ListResponse
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_bulk_create_input_v1 import AudienceSegmentBulkCreateInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_bulk_create_input_v1 = AudienceSegmentBulkCreateInputV1(
        data=[
            AudienceSegmentCreateEntityV1Resource(
                attributes=AudienceSegmentCreateEntityV1(
                    advertiser_id="advertiser_id_example",
                    contact_list={},
                    description="description_example",
                    in_market=InMarketCreateV1(
                        brand_ids=[
                            "brand_ids_example",
                        ],
                        buying_power=[
                            "Low",
                        ],
                        country="country_example",
                        gender="Male",
                        interest_ids=[
                            "interest_ids_example",
                        ],
                        price_range=[
                            "Low",
                        ],
                    ),
                    location=LocationCreateV1(
                        points_of_interest=[
                            PointOfInterestV1(
                                latitude=3.14,
                                longitude=3.14,
                                name="name_example",
                            ),
                        ],
                        radius_in_km=1,
                    ),
                    lookalike=LookalikeCreateV1(
                        seed_segment_id="seed_segment_id_example",
                        target_size=1,
                    ),
                    name="name_example",
                    prospecting=ProspectingCreateV1(
                        days_since_last_visit_max=1,
                        days_since_last_visit_min=1,
                        users_type="Prospects",
                    ),
                    retargeting=RetargetingCreateV1(
                        days_since_last_visit_max=1,
                        days_since_last_visit_min=1,
                        visitors_type="All",
                    ),
                ),
                type="type_example",
            ),
        ],
    ) # AudienceSegmentBulkCreateInputV1 | Segment creation parameter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_audience_segments(audience_segment_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->bulk_create_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_bulk_create_input_v1** | [**AudienceSegmentBulkCreateInputV1**](AudienceSegmentBulkCreateInputV1.md)| Segment creation parameter |

### Return type

[**AudienceSegmentEntityV1ListResponse**](AudienceSegmentEntityV1ListResponse.md)

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

# **bulk_create_audiences**
> AudienceEntityV1ListResponse bulk_create_audiences(audience_bulk_create_input_v1)



Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_bulk_create_input_v1 import AudienceBulkCreateInputV1
from criteo_api_marketingsolutions_v2025_04.model.audience_entity_v1_list_response import AudienceEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_bulk_create_input_v1 = AudienceBulkCreateInputV1(
        data=[
            AudienceCreateEntityV1Resource(
                attributes=AudienceCreateEntityV1(
                    advertiser_id="advertiser_id_example",
                    algebra=AlgebraNodeV1(
                        _and=[
                            AlgebraNodeV1(),
                        ],
                        audience_segment_id="audience_segment_id_example",
                        _not=AlgebraNodeV1(),
                        _or=[
                            AlgebraNodeV1(),
                        ],
                    ),
                    description="description_example",
                    name="name_example",
                ),
                type="type_example",
            ),
        ],
    ) # AudienceBulkCreateInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_audiences(audience_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->bulk_create_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_bulk_create_input_v1** | [**AudienceBulkCreateInputV1**](AudienceBulkCreateInputV1.md)|  |

### Return type

[**AudienceEntityV1ListResponse**](AudienceEntityV1ListResponse.md)

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

# **bulk_delete_audience_segments**
> AudienceSegmentIdEntityV1ListResponse bulk_delete_audience_segments(audience_segment_bulk_delete_input_v1)



Delete the segments associated to the given audience IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_id_entity_v1_list_response import AudienceSegmentIdEntityV1ListResponse
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_bulk_delete_input_v1 import AudienceSegmentBulkDeleteInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_bulk_delete_input_v1 = AudienceSegmentBulkDeleteInputV1(
        data=[
            AudienceSegmentDeleteEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # AudienceSegmentBulkDeleteInputV1 | Segment delete request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_delete_audience_segments(audience_segment_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->bulk_delete_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_bulk_delete_input_v1** | [**AudienceSegmentBulkDeleteInputV1**](AudienceSegmentBulkDeleteInputV1.md)| Segment delete request. |

### Return type

[**AudienceSegmentIdEntityV1ListResponse**](AudienceSegmentIdEntityV1ListResponse.md)

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

# **bulk_delete_audiences**
> AudienceIdEntityV1ListResponse bulk_delete_audiences(audience_bulk_delete_input_v1)



Deletes the audiences associated to the given audience IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_id_entity_v1_list_response import AudienceIdEntityV1ListResponse
from criteo_api_marketingsolutions_v2025_04.model.audience_bulk_delete_input_v1 import AudienceBulkDeleteInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_bulk_delete_input_v1 = AudienceBulkDeleteInputV1(
        data=[
            AudienceDeleteEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # AudienceBulkDeleteInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_delete_audiences(audience_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->bulk_delete_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_bulk_delete_input_v1** | [**AudienceBulkDeleteInputV1**](AudienceBulkDeleteInputV1.md)|  |

### Return type

[**AudienceIdEntityV1ListResponse**](AudienceIdEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Success or partial success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_audience_segments**
> AudienceSegmentEntityV1ListResponse bulk_update_audience_segments(audience_segment_bulk_update_input_v1)



Updates the properties of all segments with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_entity_v1_list_response import AudienceSegmentEntityV1ListResponse
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_bulk_update_input_v1 import AudienceSegmentBulkUpdateInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_bulk_update_input_v1 = AudienceSegmentBulkUpdateInputV1(
        data=[
            AudienceSegmentUpdateEntityV1Resource(
                attributes=AudienceSegmentUpdateEntityV1(
                    description=NillableString(
                        value="value_example",
                    ),
                    in_market=InMarketUpdateV1(
                        brand_ids=[
                            "brand_ids_example",
                        ],
                        buying_power=[
                            "Low",
                        ],
                        country="country_example",
                        gender=NillableGenderV1(
                            value="Male",
                        ),
                        interest_ids=[
                            "interest_ids_example",
                        ],
                        price_range=[
                            "Low",
                        ],
                    ),
                    location=LocationUpdateV1(
                        points_of_interest=[
                            PointOfInterestV1(
                                latitude=3.14,
                                longitude=3.14,
                                name="name_example",
                            ),
                        ],
                        radius_in_km=1,
                        registry_type="PointOfInterest",
                    ),
                    lookalike=LookalikeUpdateV1(
                        target_size=1,
                    ),
                    name="name_example",
                    prospecting=ProspectingUpdateV1(
                        days_since_last_visit_max=NillableInt32(
                            value=1,
                        ),
                        days_since_last_visit_min=NillableInt32(
                            value=1,
                        ),
                        users_type="Prospects",
                    ),
                    retargeting=RetargetingUpdateV1(
                        days_since_last_visit_max=1,
                        days_since_last_visit_min=1,
                        visitors_type="All",
                    ),
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # AudienceSegmentBulkUpdateInputV1 | Segment Update request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_audience_segments(audience_segment_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->bulk_update_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_bulk_update_input_v1** | [**AudienceSegmentBulkUpdateInputV1**](AudienceSegmentBulkUpdateInputV1.md)| Segment Update request |

### Return type

[**AudienceSegmentEntityV1ListResponse**](AudienceSegmentEntityV1ListResponse.md)

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

# **bulk_update_audiences**
> AudienceEntityV1ListResponse bulk_update_audiences(audience_bulk_update_input_v1)



Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_bulk_update_input_v1 import AudienceBulkUpdateInputV1
from criteo_api_marketingsolutions_v2025_04.model.audience_entity_v1_list_response import AudienceEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_bulk_update_input_v1 = AudienceBulkUpdateInputV1(
        data=[
            AudienceUpdateEntityV1Resource(
                attributes=AudienceUpdateEntityV1(
                    algebra=AlgebraNodeV1(
                        _and=[
                            AlgebraNodeV1(),
                        ],
                        audience_segment_id="audience_segment_id_example",
                        _not=AlgebraNodeV1(),
                        _or=[
                            AlgebraNodeV1(),
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
    ) # AudienceBulkUpdateInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_audiences(audience_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->bulk_update_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_bulk_update_input_v1** | [**AudienceBulkUpdateInputV1**](AudienceBulkUpdateInputV1.md)|  |

### Return type

[**AudienceEntityV1ListResponse**](AudienceEntityV1ListResponse.md)

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

# **call_04_audiences_audience_segment_id_contactlist_delete**
> DeleteAudienceContactListResponse call_04_audiences_audience_segment_id_contactlist_delete(audience_segment_id)



Delete all identifiers from a contact list audience-segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_api_marketingsolutions_v2025_04.model.error_code_response import ErrorCodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.call_04_audiences_audience_segment_id_contactlist_delete(audience_segment_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->call_04_audiences_audience_segment_id_contactlist_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The id of the contact list audience-segment to amend |

### Return type

[**DeleteAudienceContactListResponse**](DeleteAudienceContactListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Contact List was emptied |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_04_audiences_audience_segment_id_contactlist_patch**
> ModifyAudienceResponse call_04_audiences_audience_segment_id_contactlist_patch(audience_segment_id, contactlist_amendment_request)



Add/remove identifiers to or from a contact list audience-segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_v2025_04.model.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_api_marketingsolutions_v2025_04.model.error_code_response import ErrorCodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend
    contactlist_amendment_request = ContactlistAmendmentRequest(
        data=ContactlistAmendment(
            attributes=ContactlistAmendmentAttributes(
                gum_caller_id=1,
                identifiers=[
                    "identifiers_example",
                ],
                identifier_type="email",
                operation="add",
            ),
            type="ContactlistAmendment",
        ),
    ) # ContactlistAmendmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.call_04_audiences_audience_segment_id_contactlist_patch(audience_segment_id, contactlist_amendment_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->call_04_audiences_audience_segment_id_contactlist_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The id of the contact list audience-segment to amend |
 **contactlist_amendment_request** | [**ContactlistAmendmentRequest**](ContactlistAmendmentRequest.md)|  |

### Return type

[**ModifyAudienceResponse**](ModifyAudienceResponse.md)

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
**404** | Audience 123 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_delete**
> DeleteAudienceContactListResponse call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_delete(audience_segment_id)



Delete all identifiers from a contact list audience-segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_api_marketingsolutions_v2025_04.model.error_code_response import ErrorCodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_delete(audience_segment_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The id of the contact list audience-segment to amend |

### Return type

[**DeleteAudienceContactListResponse**](DeleteAudienceContactListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Contact List was emptied |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_patch**
> ModifyAudienceResponse call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_patch(audience_segment_id, contactlist_amendment_request)



Add/remove identifiers to or from a contact list audience-segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_v2025_04.model.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_api_marketingsolutions_v2025_04.model.error_code_response import ErrorCodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = "audience-segment-id_example" # str | The id of the contact list audience-segment to amend
    contactlist_amendment_request = ContactlistAmendmentRequest(
        data=ContactlistAmendment(
            attributes=ContactlistAmendmentAttributes(
                gum_caller_id=1,
                identifiers=[
                    "identifiers_example",
                ],
                identifier_type="email",
                operation="add",
            ),
            type="ContactlistAmendment",
        ),
    ) # ContactlistAmendmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_patch(audience_segment_id, contactlist_amendment_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->call_04_marketing_solutions_audience_segments_audience_segment_id_contact_list_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **str**| The id of the contact list audience-segment to amend |
 **contactlist_amendment_request** | [**ContactlistAmendmentRequest**](ContactlistAmendmentRequest.md)|  |

### Return type

[**ModifyAudienceResponse**](ModifyAudienceResponse.md)

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
**404** | Audience 123 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_audience_segments_sizes**
> AudienceSegmentSizeEntityV1ListResponse compute_audience_segments_sizes(audience_segment_compute_sizes_input_v1)



Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_compute_sizes_input_v1 import AudienceSegmentComputeSizesInputV1
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_size_entity_v1_list_response import AudienceSegmentSizeEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_compute_sizes_input_v1 = AudienceSegmentComputeSizesInputV1(
        data=[
            AudienceSegmentComputeSizeEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # AudienceSegmentComputeSizesInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.compute_audience_segments_sizes(audience_segment_compute_sizes_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->compute_audience_segments_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_compute_sizes_input_v1** | [**AudienceSegmentComputeSizesInputV1**](AudienceSegmentComputeSizesInputV1.md)|  |

### Return type

[**AudienceSegmentSizeEntityV1ListResponse**](AudienceSegmentSizeEntityV1ListResponse.md)

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

# **compute_audiences_sizes**
> AudienceSizeEntityV1ListResponse compute_audiences_sizes(audience_compute_sizes_input_v1)



Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_size_entity_v1_list_response import AudienceSizeEntityV1ListResponse
from criteo_api_marketingsolutions_v2025_04.model.audience_compute_sizes_input_v1 import AudienceComputeSizesInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_compute_sizes_input_v1 = AudienceComputeSizesInputV1(
        data=[
            AudienceComputeSizeEntityV1Resource(
                attributes={},
                id="id_example",
                type="type_example",
            ),
        ],
    ) # AudienceComputeSizesInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.compute_audiences_sizes(audience_compute_sizes_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->compute_audiences_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_compute_sizes_input_v1** | [**AudienceComputeSizesInputV1**](AudienceComputeSizesInputV1.md)|  |

### Return type

[**AudienceSizeEntityV1ListResponse**](AudienceSizeEntityV1ListResponse.md)

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

# **estimate_audience_segment_size**
> AudienceSegmentSizeEstimationV1Response estimate_audience_segment_size(audience_segment_estimate_size_input_v1)



Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_estimate_size_input_v1 import AudienceSegmentEstimateSizeInputV1
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_size_estimation_v1_response import AudienceSegmentSizeEstimationV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_estimate_size_input_v1 = AudienceSegmentEstimateSizeInputV1(
        data=AudienceSegmentSizeEstimationEntityV1Resource(
            attributes=AudienceSegmentSizeEstimationEntityV1(
                advertiser_id="advertiser_id_example",
                in_market=InMarketSizeEstimationV1(
                    brand_ids=[
                        "brand_ids_example",
                    ],
                    buying_power=[
                        "Low",
                    ],
                    country="country_example",
                    gender="Male",
                    interest_ids=[
                        "interest_ids_example",
                    ],
                    price_range=[
                        "Low",
                    ],
                ),
                location=LocationSizeEstimationV1(
                    points_of_interest=[
                        PointOfInterestV1(
                            latitude=3.14,
                            longitude=3.14,
                            name="name_example",
                        ),
                    ],
                    radius_in_km=1,
                ),
            ),
            type="type_example",
        ),
    ) # AudienceSegmentEstimateSizeInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.estimate_audience_segment_size(audience_segment_estimate_size_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->estimate_audience_segment_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_estimate_size_input_v1** | [**AudienceSegmentEstimateSizeInputV1**](AudienceSegmentEstimateSizeInputV1.md)|  |

### Return type

[**AudienceSegmentSizeEstimationV1Response**](AudienceSegmentSizeEstimationV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_audience_size**
> AudienceSizeEstimationV1Response estimate_audience_size(audience_estimate_size_input_v1)



Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_size_estimation_v1_response import AudienceSizeEstimationV1Response
from criteo_api_marketingsolutions_v2025_04.model.audience_estimate_size_input_v1 import AudienceEstimateSizeInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_estimate_size_input_v1 = AudienceEstimateSizeInputV1(
        data=AudienceEstimateSizeEntityV1Resource(
            attributes=AudienceEstimateSizeEntityV1(
                advertiser_id="advertiser_id_example",
                algebra=AlgebraNodeV1(
                    _and=[
                        AlgebraNodeV1(),
                    ],
                    audience_segment_id="audience_segment_id_example",
                    _not=AlgebraNodeV1(),
                    _or=[
                        AlgebraNodeV1(),
                    ],
                ),
            ),
            type="type_example",
        ),
    ) # AudienceEstimateSizeInputV1 | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.estimate_audience_size(audience_estimate_size_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->estimate_audience_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_estimate_size_input_v1** | [**AudienceEstimateSizeInputV1**](AudienceEstimateSizeInputV1.md)|  |

### Return type

[**AudienceSizeEstimationV1Response**](AudienceSizeEstimationV1Response.md)

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

# **get_audience_segment_contact_list_statistics**
> ContactListStatisticsEntityV1Response get_audience_segment_contact_list_statistics(audience_segment_id)



Returns the statistics of a contact list segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.contact_list_statistics_entity_v1_response import ContactListStatisticsEntityV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_id = 1 # int | The segment ID.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audience_segment_contact_list_statistics(audience_segment_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->get_audience_segment_contact_list_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_id** | **int**| The segment ID. |

### Return type

[**ContactListStatisticsEntityV1Response**](ContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audience_segments_in_market_brands**
> InMarketAudienceSegmentBrandEntityV1ListResponse get_audience_segments_in_market_brands(advertiser_id, country)



Returns a list with all available in-market brands that can be used to define an in-market segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.in_market_audience_segment_brand_entity_v1_list_response import InMarketAudienceSegmentBrandEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser ID.
    country = "country_example" # str | The ISO 3166-1 alpha-2 country code.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audience_segments_in_market_brands(advertiser_id, country)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->get_audience_segments_in_market_brands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser ID. |
 **country** | **str**| The ISO 3166-1 alpha-2 country code. |

### Return type

[**InMarketAudienceSegmentBrandEntityV1ListResponse**](InMarketAudienceSegmentBrandEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audience_segments_in_market_interests**
> InMarketAudienceSegmentInterestEntityV1ListResponse get_audience_segments_in_market_interests(advertiser_id, country)



Returns a list with all available in-market interests that can be used to define an in-market segment. These in-market interests correspond to the Google product taxonomy.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.in_market_audience_segment_interest_entity_v1_list_response import InMarketAudienceSegmentInterestEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser ID.
    country = "country_example" # str | The ISO 3166-1 alpha-2 country code.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audience_segments_in_market_interests(advertiser_id, country)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->get_audience_segments_in_market_interests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser ID. |
 **country** | **str**| The ISO 3166-1 alpha-2 country code. |

### Return type

[**InMarketAudienceSegmentInterestEntityV1ListResponse**](InMarketAudienceSegmentInterestEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_audience_segments**
> AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse search_audience_segments(audience_segment_search_input_v1)



Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_entity_v1_audience_segment_search_metadata_v1_list_response import AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse
from criteo_api_marketingsolutions_v2025_04.model.audience_segment_search_input_v1 import AudienceSegmentSearchInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_segment_search_input_v1 = AudienceSegmentSearchInputV1(
        data=AudienceSegmentSearchEntityV1Resource(
            attributes=AudienceSegmentSearchEntityV1(
                advertiser_ids=[
                    "advertiser_ids_example",
                ],
                audience_segment_ids=[
                    "audience_segment_ids_example",
                ],
                audience_segment_types=[
                    "Unknown",
                ],
            ),
            type="type_example",
        ),
    ) # AudienceSegmentSearchInputV1 | Segment search filters.
    limit = 50 # int | The number of elements to be returned. The default is 50 and the maximum is 100. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The (zero-based) offset into the collection. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_audience_segments(audience_segment_search_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->search_audience_segments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audience_segments(audience_segment_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->search_audience_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_segment_search_input_v1** | [**AudienceSegmentSearchInputV1**](AudienceSegmentSearchInputV1.md)| Segment search filters. |
 **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse**](AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_audiences**
> AudienceEntityV1AudienceSearchMetadataV1ListResponse search_audiences(audience_search_input_v1)



Returns a list of audiences that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2025_04
from criteo_api_marketingsolutions_v2025_04.api import audience_api
from criteo_api_marketingsolutions_v2025_04.model.audience_search_input_v1 import AudienceSearchInputV1
from criteo_api_marketingsolutions_v2025_04.model.audience_entity_v1_audience_search_metadata_v1_list_response import AudienceEntityV1AudienceSearchMetadataV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2025_04.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2025_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_search_input_v1 = AudienceSearchInputV1(
        data=AudienceSearchEntityV1Resource(
            attributes=AudienceSearchEntityV1(
                ad_set_ids=[
                    "ad_set_ids_example",
                ],
                advertiser_ids=[
                    "advertiser_ids_example",
                ],
                audience_ids=[
                    "audience_ids_example",
                ],
                audience_segment_ids=[
                    "audience_segment_ids_example",
                ],
            ),
            type="type_example",
        ),
    ) # AudienceSearchInputV1 | Audience search filters.
    limit = 50 # int | The number of elements to be returned. The default is 50 and the maximum is 100. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The (zero-based) offset into the collection. The default is 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_audiences(audience_search_input_v1)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->search_audiences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_audiences(audience_search_input_v1, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2025_04.ApiException as e:
        print("Exception when calling AudienceApi->search_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_search_input_v1** | [**AudienceSearchInputV1**](AudienceSearchInputV1.md)| Audience search filters. |
 **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**AudienceEntityV1AudienceSearchMetadataV1ListResponse**](AudienceEntityV1AudienceSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

