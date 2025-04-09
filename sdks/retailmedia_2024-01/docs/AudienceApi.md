# criteo_api_retailmedia_v2024_01.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legacy_create_audience_v1**](AudienceApi.md#legacy_create_audience_v1) | **POST** /2024-01/retail-media/accounts/{accountId}/audiences | 
[**legacy_get_audience_v1**](AudienceApi.md#legacy_get_audience_v1) | **GET** /2024-01/retail-media/accounts/{accountId}/audiences | 
[**legacy_get_audience_v2**](AudienceApi.md#legacy_get_audience_v2) | **GET** /2024-01/retail-media/v2/accounts/{accountId}/audiences | 
[**legacy_update_audience_v2**](AudienceApi.md#legacy_update_audience_v2) | **POST** /2024-01/retail-media/v2/accounts/{accountId}/audiences | 


# **legacy_create_audience_v1**
> RmLegacyAudienceCreateEntityV1Response legacy_create_audience_v1(account_id, rm_legacy_audience_create_input_entity_v1)



Create an Audience (deprecated Public API)

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_01
from criteo_api_retailmedia_v2024_01.api import audience_api
from criteo_api_retailmedia_v2024_01.model.rm_legacy_audience_create_input_entity_v1 import RmLegacyAudienceCreateInputEntityV1
from criteo_api_retailmedia_v2024_01.model.rm_legacy_audience_create_entity_v1_response import RmLegacyAudienceCreateEntityV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = 1 # int | ID of the account to which this audience belongs.
    rm_legacy_audience_create_input_entity_v1 = RmLegacyAudienceCreateInputEntityV1(
        data=RmLegacyAudienceCreateEntityV1Resource(
            attributes=RmLegacyAudienceCreateEntityV1(
                brand_ids=[
                    1,
                ],
                category_ids=[
                    1,
                ],
                lookback_window="P7D",
                name="name_example",
                retailer_id=1,
                user_type="viewer",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # RmLegacyAudienceCreateInputEntityV1 | Audience creation request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legacy_create_audience_v1(account_id, rm_legacy_audience_create_input_entity_v1)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_01.ApiException as e:
        print("Exception when calling AudienceApi->legacy_create_audience_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| ID of the account to which this audience belongs. |
 **rm_legacy_audience_create_input_entity_v1** | [**RmLegacyAudienceCreateInputEntityV1**](RmLegacyAudienceCreateInputEntityV1.md)| Audience creation request. |

### Return type

[**RmLegacyAudienceCreateEntityV1Response**](RmLegacyAudienceCreateEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | The audience that was just created. |  -  |
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
import criteo_api_retailmedia_v2024_01
from criteo_api_retailmedia_v2024_01.api import audience_api
from criteo_api_retailmedia_v2024_01.model.rm_legacy_audience_get_entity_v1_list_response import RmLegacyAudienceGetEntityV1ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = 1 # int | ID of the account to which this audience belongs.
    limit_to_id = [
        1,
    ] # [int] | Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2 (optional)
    page_index = 1 # int | Returns the specified page of results given a pageSize; pages are 0-indexed. (optional)
    page_size = 1 # int | Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legacy_get_audience_v1(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_01.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.legacy_get_audience_v1(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_01.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| ID of the account to which this audience belongs. |
 **limit_to_id** | **[int]**| Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId&#x3D;1&amp;limitToId&#x3D;2 | [optional]
 **page_index** | **int**| Returns the specified page of results given a pageSize; pages are 0-indexed. | [optional]
 **page_size** | **int**| Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. | [optional]

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
import criteo_api_retailmedia_v2024_01
from criteo_api_retailmedia_v2024_01.api import audience_api
from criteo_api_retailmedia_v2024_01.model.rm_legacy_audience_get_entity_v2_list_response import RmLegacyAudienceGetEntityV2ListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = 1 # int | ID of the account to which this audience belongs.
    limit_to_id = [
        1,
    ] # [int] | Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2 (optional)
    page_index = 1 # int | Returns the specified page of results given a pageSize; pages are 0-indexed. (optional)
    page_size = 1 # int | Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legacy_get_audience_v2(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_01.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.legacy_get_audience_v2(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_01.ApiException as e:
        print("Exception when calling AudienceApi->legacy_get_audience_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| ID of the account to which this audience belongs. |
 **limit_to_id** | **[int]**| Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId&#x3D;1&amp;limitToId&#x3D;2 | [optional]
 **page_index** | **int**| Returns the specified page of results given a pageSize; pages are 0-indexed. | [optional]
 **page_size** | **int**| Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. | [optional]

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

# **legacy_update_audience_v2**
> RmLegacyAudienceCreateEntityV2Response legacy_update_audience_v2(account_id, rm_legacy_audience_create_input_entity_v2)



Create an Audience (deprecated Public API)

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2024_01
from criteo_api_retailmedia_v2024_01.api import audience_api
from criteo_api_retailmedia_v2024_01.model.rm_legacy_audience_create_input_entity_v2 import RmLegacyAudienceCreateInputEntityV2
from criteo_api_retailmedia_v2024_01.model.rm_legacy_audience_create_entity_v2_response import RmLegacyAudienceCreateEntityV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2024_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2024_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = 1 # int | ID of the account to which this audience belongs.
    rm_legacy_audience_create_input_entity_v2 = RmLegacyAudienceCreateInputEntityV2(
        data=RmLegacyAudienceCreateEntityV2Resource(
            attributes=RmLegacyAudienceCreateEntityV2(
                name="name_example",
                retailer_id=1,
                user_behavior_details=RmLegacyAudienceUserBehaviorCreateV2(
                    exclusive_segment=RmLegacySegmentUserBehaviorCreateV2(
                        brand_ids=[
                            1,
                        ],
                        category_ids=[
                            1,
                        ],
                        lookback_window="P7D",
                        user_action="buy",
                    ),
                    inclusive_segment=RmLegacySegmentUserBehaviorCreateV2(
                        brand_ids=[
                            1,
                        ],
                        category_ids=[
                            1,
                        ],
                        lookback_window="P7D",
                        user_action="buy",
                    ),
                ),
            ),
            id="id_example",
            type="type_example",
        ),
    ) # RmLegacyAudienceCreateInputEntityV2 | Audience creation request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legacy_update_audience_v2(account_id, rm_legacy_audience_create_input_entity_v2)
        pprint(api_response)
    except criteo_api_retailmedia_v2024_01.ApiException as e:
        print("Exception when calling AudienceApi->legacy_update_audience_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| ID of the account to which this audience belongs. |
 **rm_legacy_audience_create_input_entity_v2** | [**RmLegacyAudienceCreateInputEntityV2**](RmLegacyAudienceCreateInputEntityV2.md)| Audience creation request. |

### Return type

[**RmLegacyAudienceCreateEntityV2Response**](RmLegacyAudienceCreateEntityV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | The audience that was just created. |  -  |
**400** | Bad request |  -  |
**401** | The API client is not properly authenticated. |  -  |
**403** | The API client is not authorized to access this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

