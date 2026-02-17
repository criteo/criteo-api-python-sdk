# criteo_api_marketingsolutions_preview.OnSiteRecommendationApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_recommended_products**](OnSiteRecommendationApi.md#search_recommended_products) | **POST** /preview/recommendation/search | 
[**search_recommended_products_conversational**](OnSiteRecommendationApi.md#search_recommended_products_conversational) | **POST** /preview/recommendation/search-conversational | 


# **search_recommended_products**
> OnSiteRecoResponse search_recommended_products()



Retrieves a list of products recommended for the given user. This end point can either rely on a Criteo UserId, or a list of user events to perform the recommendation

### Example

* OAuth Authentication (oauth):
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
        ad_id=1,
        ad_set_id=1,
        identity_type="CtoBundle",
        nb_requested_products=1,
        partner_id=1,
        user_id="user_id_example",
    ) # OnSiteRecoRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_recommended_products(on_site_reco_request=on_site_reco_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling OnSiteRecommendationApi->search_recommended_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_site_reco_request** | [**OnSiteRecoRequest**](OnSiteRecoRequest.md)|  | [optional]

### Return type

[**OnSiteRecoResponse**](OnSiteRecoResponse.md)

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

# **search_recommended_products_conversational**
> OnSiteRecoResponse search_recommended_products_conversational()



Retrieves a list of products recommended for the given user based on a conversation between a user and a partner's agent

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import on_site_recommendation_api
from criteo_api_marketingsolutions_preview.model.on_site_reco_response import OnSiteRecoResponse
from criteo_api_marketingsolutions_preview.model.on_site_reco_request_conversational import OnSiteRecoRequestConversational
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

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_preview.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = on_site_recommendation_api.OnSiteRecommendationApi(api_client)
    on_site_reco_request_conversational = OnSiteRecoRequestConversational(
        ad_id=1,
        ad_set_id=1,
        conversation=[
            OnSiteRecoChatMessage(
                content="content_example",
                role="role_example",
            ),
        ],
        nb_requested_products=1,
        partner_id=1,
        product=OnSiteRecoProductContext(
            brand="brand_example",
            category="category_example",
            color="color_example",
            description="description_example",
            name="name_example",
            price=OnSiteRecoPrice(
                amount=3.14,
                currency="currency_example",
            ),
            product_id="product_id_example",
            size="size_example",
        ),
        user_id="user_id_example",
    ) # OnSiteRecoRequestConversational |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_recommended_products_conversational(on_site_reco_request_conversational=on_site_reco_request_conversational)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling OnSiteRecommendationApi->search_recommended_products_conversational: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_site_reco_request_conversational** | [**OnSiteRecoRequestConversational**](OnSiteRecoRequestConversational.md)|  | [optional]

### Return type

[**OnSiteRecoResponse**](OnSiteRecoResponse.md)

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

