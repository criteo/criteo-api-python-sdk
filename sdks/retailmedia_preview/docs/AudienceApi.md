# criteo_api_retailmedia_preview.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legacy_get_audience_v1**](AudienceApi.md#legacy_get_audience_v1) | **GET** /preview/retail-media/accounts/{accountId}/audiences | 
[**legacy_get_audience_v2**](AudienceApi.md#legacy_get_audience_v2) | **GET** /preview/retail-media/v2/accounts/{accountId}/audiences | 


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

