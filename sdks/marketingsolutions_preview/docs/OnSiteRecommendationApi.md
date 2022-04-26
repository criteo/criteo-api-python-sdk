# criteo_api_marketingsolutions_preview.OnSiteRecommendationApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_reco_post**](OnSiteRecommendationApi.md#api_v1_reco_post) | **POST** /preview/recommendation/search | 


# **api_v1_reco_post**
> OnSiteRecoResponse api_v1_reco_post()



Retrieves a list of products recommended for the given user. This end point can either rely on a Criteo UserId, or a list of user events to perform the recommendation.

### Example

* OAuth Authentication (oauth):
```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import on_site_recommendation_api
from criteo_api_marketingsolutions_preview.model.on_site_reco_request import OnSiteRecoRequest
from criteo_api_marketingsolutions_preview.model.on_site_reco_response import OnSiteRecoResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = on_site_recommendation_api.OnSiteRecommendationApi(api_client)
    on_site_reco_request = OnSiteRecoRequest(
        nb_requested_products=1,
        user_id="user_id_example",
        user_events=[
            UserEvent(
                product_external_id="product_external_id_example",
                type=0,
                date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
    ) # OnSiteRecoRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v1_reco_post(on_site_reco_request=on_site_reco_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling OnSiteRecommendationApi->api_v1_reco_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_site_reco_request** | [**OnSiteRecoRequest**](OnSiteRecoRequest.md)|  | [optional]

### Return type

[**OnSiteRecoResponse**](OnSiteRecoResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

