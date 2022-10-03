# criteo_api_retailmedia_v2022_04.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audience**](AudienceApi.md#create_audience) | **POST** /2022-04/retail-media/accounts/{accountId}/audiences | 
[**get_audiences_by_account_id**](AudienceApi.md#get_audiences_by_account_id) | **GET** /2022-04/retail-media/accounts/{accountId}/audiences | 


# **create_audience**
> CreateRetailMediaAudienceResponse create_audience(account_id, create_retail_media_audience_request)



Create an audience for a given account ID

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2022_04
from criteo_api_retailmedia_v2022_04.api import audience_api
from criteo_api_retailmedia_v2022_04.model.create_retail_media_audience_response import CreateRetailMediaAudienceResponse
from criteo_api_retailmedia_v2022_04.model.create_retail_media_audience_request import CreateRetailMediaAudienceRequest
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_04.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "68004146450571264" # str | ID of the account to which this audience belongs.
    create_retail_media_audience_request = CreateRetailMediaAudienceRequest(
        data=CreateRetailMediaAudienceBody(
            type="RetailMediaAudience",
            attributes=CreateRetailMediaAudienceAttributes(
                user_type="viewer",
                lookback_window="P7D",
                brand_ids=[
                    "brand_ids_example",
                ],
                category_ids=[
                    "category_ids_example",
                ],
                retailer_id="68004146450571264",
                name="Test audience",
            ),
        ),
    ) # CreateRetailMediaAudienceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_audience(account_id, create_retail_media_audience_request)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_04.ApiException as e:
        print("Exception when calling AudienceApi->create_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account to which this audience belongs. |
 **create_retail_media_audience_request** | [**CreateRetailMediaAudienceRequest**](CreateRetailMediaAudienceRequest.md)|  |

### Return type

[**CreateRetailMediaAudienceResponse**](CreateRetailMediaAudienceResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The audience that was just created. |  -  |
**400** | Missing or invalid account ID. - OR - Missing or invalid retailerID field. - OR - Missing or invalid name field. Name should be less than 255 characters. - OR - Missing or invalid userType field. Valid values are: &#39;buy&#39;, &#39;view&#39;. - OR - The retailerTaxonomyIds is not a valid list of IDs or may contain more than 100 elements. - OR - Missing or invalid lookbackDays field.  Valid values are: 7, 14,  30, 45, 60, 90, 120, 150 or 180. - OR - Exactly one of retailerTaxonomyIds or globalBrandIds must be specified, but not both. - OR - The retailer is invalid because it is not live - OR - The globalBrandIds is not a valid list of IDs or may contain more than 100 elements. |  -  |
**404** | The audience was not found. - OR - You do not have permission to access these global brands. |  -  |
**406** | The Accept header must contain application/json. |  -  |
**409** | An audience name should be unique per account. |  -  |
**415** | The Content-Type header must be application/json if present. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences_by_account_id**
> GetPageOfAudiencesByAccountIdResponse get_audiences_by_account_id(account_id)



Get a page of audiences for a given account ID

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_retailmedia_v2022_04
from criteo_api_retailmedia_v2022_04.api import audience_api
from criteo_api_retailmedia_v2022_04.model.get_page_of_audiences_by_account_id_response import GetPageOfAudiencesByAccountIdResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_04.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_04.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    account_id = "68004146450571264" # str | External account ID which owns audience.
    limit_to_id = [
        "limitToId_example",
    ] # [str] | Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2 (optional)
    page_size = 25 # int | Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page (optional)
    page_index = 0 # int | Returns the specified page of results given a pageSize; pages are 0-indexed (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_audiences_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_04.ApiException as e:
        print("Exception when calling AudienceApi->get_audiences_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_audiences_by_account_id(account_id, limit_to_id=limit_to_id, page_size=page_size, page_index=page_index)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_04.ApiException as e:
        print("Exception when calling AudienceApi->get_audiences_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account ID which owns audience. |
 **limit_to_id** | **[str]**| Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId&#x3D;1&amp;limitToId&#x3D;2 | [optional]
 **page_size** | **int**| Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page | [optional]
 **page_index** | **int**| Returns the specified page of results given a pageSize; pages are 0-indexed | [optional]

### Return type

[**GetPageOfAudiencesByAccountIdResponse**](GetPageOfAudiencesByAccountIdResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of audiences for the supplied account. |  -  |
**400** | Missing or invalid account ID. |  -  |
**404** | The audience was not found. |  -  |
**406** | The Accept header must contain application/json. |  -  |
**415** | The Content-Type header must be application/json if present. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

