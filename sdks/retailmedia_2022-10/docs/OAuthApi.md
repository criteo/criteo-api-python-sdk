# criteo_api_retailmedia_v2022_10.OAuthApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](OAuthApi.md#get_token) | **POST** /oauth2/token | Creates a token based either on supplied client credentials or on single use authorization code


# **get_token**
> AccessTokenModel get_token(grant_type, client_id, client_secret)

Creates a token based either on supplied client credentials or on single use authorization code

Creates a token when the supplied client credentials are valid

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2022_10
from criteo_api_retailmedia_v2022_10.api import o_auth_api
from criteo_api_retailmedia_v2022_10.model.access_token_model import AccessTokenModel
from criteo_api_retailmedia_v2022_10.model.o_auth_error_model import OAuthErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2022_10.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2022_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = o_auth_api.OAuthApi(api_client)
    grant_type = "grant_type_example" # str | 
    client_id = "client_id_example" # str | 
    client_secret = "client_secret_example" # str | 
    redirect_uri = "redirect_uri_example" # str |  (optional)
    code = "code_example" # str |  (optional)
    refresh_token = "refresh_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a token based either on supplied client credentials or on single use authorization code
        api_response = api_instance.get_token(grant_type, client_id, client_secret)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_10.ApiException as e:
        print("Exception when calling OAuthApi->get_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a token based either on supplied client credentials or on single use authorization code
        api_response = api_instance.get_token(grant_type, client_id, client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
        pprint(api_response)
    except criteo_api_retailmedia_v2022_10.ApiException as e:
        print("Exception when calling OAuthApi->get_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  |
 **client_id** | **str**|  |
 **client_secret** | **str**|  |
 **redirect_uri** | **str**|  | [optional]
 **code** | **str**|  | [optional]
 **refresh_token** | **str**|  | [optional]

### Return type

[**AccessTokenModel**](AccessTokenModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

