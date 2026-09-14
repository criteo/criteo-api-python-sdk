# criteo_api_retailmedia_experimental.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_audience**](AudienceApi.md#bulk_create_audience) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/create | /experimental/retail-media/accounts/{account-id}/audiences/create
[**bulk_delete_audiences**](AudienceApi.md#bulk_delete_audiences) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/delete | /experimental/retail-media/accounts/{account-id}/audiences/delete
[**bulk_update_audience**](AudienceApi.md#bulk_update_audience) | **PATCH** /experimental/retail-media/accounts/{account-id}/audiences | /experimental/retail-media/accounts/{account-id}/audiences
[**compute_audience_segments_sizes**](AudienceApi.md#compute_audience_segments_sizes) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes | /experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes
[**compute_audiences_sizes**](AudienceApi.md#compute_audiences_sizes) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/compute-sizes | /experimental/retail-media/accounts/{account-id}/audiences/compute-sizes
[**estimate_audience_segment_size**](AudienceApi.md#estimate_audience_segment_size) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size | /experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size
[**estimate_audience_size**](AudienceApi.md#estimate_audience_size) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/estimate-size | /experimental/retail-media/accounts/{account-id}/audiences/estimate-size


# **bulk_create_audience**
> RmAudienceEntityV1ListResponse bulk_create_audience(account_id, rm_audience_bulk_create_input_v1)

/experimental/retail-media/accounts/{account-id}/audiences/create

Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_entity_v1_list_response import RmAudienceEntityV1ListResponse
from criteo_api_retailmedia_experimental.model.rm_audience_bulk_create_input_v1 import RmAudienceBulkCreateInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audiences/create
        api_response = api_instance.bulk_create_audience(account_id, rm_audience_bulk_create_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **bulk_delete_audiences**
> RmAudienceSegmentIdEntityV1ListResponse bulk_delete_audiences(account_id, rm_audience_bulk_delete_input_v1)

/experimental/retail-media/accounts/{account-id}/audiences/delete

Deletes the audiences associated to the given IDs.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_segment_id_entity_v1_list_response import RmAudienceSegmentIdEntityV1ListResponse
from criteo_api_retailmedia_experimental.model.rm_audience_bulk_delete_input_v1 import RmAudienceBulkDeleteInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audiences/delete
        api_response = api_instance.bulk_delete_audiences(account_id, rm_audience_bulk_delete_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/accounts/{account-id}/audiences

Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_bulk_update_input_v1 import RmAudienceBulkUpdateInputV1
from criteo_api_retailmedia_experimental.model.rm_audience_entity_v1_list_response import RmAudienceEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audiences
        api_response = api_instance.bulk_update_audience(account_id, rm_audience_bulk_update_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **compute_audience_segments_sizes**
> RmAudienceSegmentSizeEntityV1ListResponse compute_audience_segments_sizes(account_id, rm_audience_segment_compute_sizes_input_v1)

/experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes

Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_segment_size_entity_v1_list_response import RmAudienceSegmentSizeEntityV1ListResponse
from criteo_api_retailmedia_experimental.model.rm_audience_segment_compute_sizes_input_v1 import RmAudienceSegmentComputeSizesInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes
        api_response = api_instance.compute_audience_segments_sizes(account_id, rm_audience_segment_compute_sizes_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/accounts/{account-id}/audiences/compute-sizes

Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_size_entity_v1_list_response import RmAudienceSizeEntityV1ListResponse
from criteo_api_retailmedia_experimental.model.rm_audience_compute_sizes_input_v1 import RmAudienceComputeSizesInputV1
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audiences/compute-sizes
        api_response = api_instance.compute_audiences_sizes(account_id, rm_audience_compute_sizes_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size

Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_segment_estimate_size_input_v1 import RmAudienceSegmentEstimateSizeInputV1
from criteo_api_retailmedia_experimental.model.rm_audience_segment_size_estimation_v1_response import RmAudienceSegmentSizeEstimationV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size
        api_response = api_instance.estimate_audience_segment_size(account_id, rm_audience_segment_estimate_size_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

/experimental/retail-media/accounts/{account-id}/audiences/estimate-size

Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import audience_api
from criteo_api_retailmedia_experimental.model.rm_audience_estimate_size_input_v1 import RmAudienceEstimateSizeInputV1
from criteo_api_retailmedia_experimental.model.rm_audience_size_estimation_v1_response import RmAudienceSizeEstimationV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/accounts/{account-id}/audiences/estimate-size
        api_response = api_instance.estimate_audience_size(account_id, rm_audience_estimate_size_input_v1)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

