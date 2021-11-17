# criteo_api_marketingsolutions_v2020_10.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audience**](AudienceApi.md#create_audience) | **POST** /2021-04/audiences | 
[**delete_identifiers**](AudienceApi.md#delete_identifiers) | **DELETE** /2021-04/audiences/{audience-id}/contactlist | 
[**get_audiences**](AudienceApi.md#get_audiences) | **GET** /2021-04/audiences | 
[**modify_audience**](AudienceApi.md#modify_audience) | **PATCH** /2021-04/audiences/{audience-id} | 
[**modify_audience_users**](AudienceApi.md#modify_audience_users) | **PATCH** /2021-04/audiences/{audience-id}/contactlist | 
[**remove_audience**](AudienceApi.md#remove_audience) | **DELETE** /2021-04/audiences/{audience-id} | 


# **create_audience**
> NewAudienceResponse create_audience(new_audience_request)



Create an Audience for an Advertiser

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import audience_api
from criteo_api_marketingsolutions_v2020_10.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2020_10.model.new_audience_response import NewAudienceResponse
from criteo_api_marketingsolutions_v2020_10.model.new_audience_request import NewAudienceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    new_audience_request = NewAudienceRequest(
        data=NewAudience(
            type="Audience",
            attributes=NewAudienceAttributes(
                advertiser_id="advertiser_id_example",
                name="name_example",
                description="description_example",
            ),
        ),
    ) # NewAudienceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_audience(new_audience_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AudienceApi->create_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_audience_request** | [**NewAudienceRequest**](NewAudienceRequest.md)|  |

### Return type

[**NewAudienceResponse**](NewAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience was created |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identifiers**
> DeleteAudienceContactListResponse delete_identifiers(audience_id)



delete all identifiers from an Audience

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import audience_api
from criteo_api_marketingsolutions_v2020_10.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2020_10.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_id = "audience-id_example" # str | The id of the audience to amend

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_identifiers(audience_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AudienceApi->delete_identifiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend |

### Return type

[**DeleteAudienceContactListResponse**](DeleteAudienceContactListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contactlist was deleted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences**
> GetAudiencesResponse get_audiences()



Get a list of all the audiences for the user or for the given advertiser_id

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import audience_api
from criteo_api_marketingsolutions_v2020_10.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2020_10.model.get_audiences_response import GetAudiencesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don't provide it, we will take into account the advertisers from your portfolio (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_audiences(advertiser_id=advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AudienceApi->get_audiences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don&#39;t provide it, we will take into account the advertisers from your portfolio | [optional]

### Return type

[**GetAudiencesResponse**](GetAudiencesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list was retrieved. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_audience**
> ReplaceAudienceResponse modify_audience(audience_id, replace_audience_request)



Update user audience specified by the audience id

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import audience_api
from criteo_api_marketingsolutions_v2020_10.model.replace_audience_response import ReplaceAudienceResponse
from criteo_api_marketingsolutions_v2020_10.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2020_10.model.replace_audience_request import ReplaceAudienceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_id = "audience-id_example" # str | The id of the audience to amend
    replace_audience_request = ReplaceAudienceRequest(
        data=ReplaceAudience(
            type="Audience",
            attributes=AudienceNameDescription(
                name="name_example",
                description="description_example",
            ),
        ),
    ) # ReplaceAudienceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.modify_audience(audience_id, replace_audience_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AudienceApi->modify_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend |
 **replace_audience_request** | [**ReplaceAudienceRequest**](ReplaceAudienceRequest.md)|  |

### Return type

[**ReplaceAudienceResponse**](ReplaceAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience was updated |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_audience_users**
> ModifyAudienceResponse modify_audience_users(audience_id, contactlist_amendment_request)



Add/remove users to or from an audience

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import audience_api
from criteo_api_marketingsolutions_v2020_10.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2020_10.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_v2020_10.model.contactlist_amendment_request import ContactlistAmendmentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_id = "audience-id_example" # str | The id of the audience to amend
    contactlist_amendment_request = ContactlistAmendmentRequest(
        data=ContactlistAmendment(
            type="ContactlistAmendment",
            attributes=ContactlistAmendmentAttributes(
                operation="add",
                identifier_type="email",
                identifiers=[
                    "identifiers_example",
                ],
                gum_caller_id=1,
                internal_identifiers=True,
            ),
        ),
    ) # ContactlistAmendmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.modify_audience_users(audience_id, contactlist_amendment_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AudienceApi->modify_audience_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend |
 **contactlist_amendment_request** | [**ContactlistAmendmentRequest**](ContactlistAmendmentRequest.md)|  |

### Return type

[**ModifyAudienceResponse**](ModifyAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

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

# **remove_audience**
> DeleteAudienceResponse remove_audience(audience_id)



Delete an audience by id

### Example

* OAuth Authentication (Authorization):
```python
import time
import criteo_api_marketingsolutions_v2020_10
from criteo_api_marketingsolutions_v2020_10.api import audience_api
from criteo_api_marketingsolutions_v2020_10.model.delete_audience_response import DeleteAudienceResponse
from criteo_api_marketingsolutions_v2020_10.model.error_code_response import ErrorCodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = criteo_api_marketingsolutions_v2020_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2020_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audience_api.AudienceApi(api_client)
    audience_id = "audience-id_example" # str | The id of the audience to amend

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_audience(audience_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2020_10.ApiException as e:
        print("Exception when calling AudienceApi->remove_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend |

### Return type

[**DeleteAudienceResponse**](DeleteAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience was deleted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

