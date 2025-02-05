# criteo_api_retailmedia_preview.OnSiteRecommendationApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chatbot_product_recommendations**](OnSiteRecommendationApi.md#chatbot_product_recommendations) | **POST** /preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations | 


# **chatbot_product_recommendations**
> MessageBodyModel chatbot_product_recommendations(catalogid, inbot_discussion_body_model)



Ask a chatbot for a product recommendation

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import on_site_recommendation_api
from criteo_api_retailmedia_preview.model.message_body_model import MessageBodyModel
from criteo_api_retailmedia_preview.model.inbot_discussion_body_model import InbotDiscussionBodyModel
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
    api_instance = on_site_recommendation_api.OnSiteRecommendationApi(api_client)
    catalogid = 1 # int | the identifier of the catalog to query
    inbot_discussion_body_model = InbotDiscussionBodyModel(
        data=InbotDiscussionDataInstanceModel(
            type="InbotDiscussion",
            attributes=InbotDiscussion(
                messages=[
                    Message(
                        user_message="user_message_example",
                        bot_message=BotMessage(
                            opening="opening_example",
                            product_recos=[
                                ProductRecommendation(
                                    rationale="rationale_example",
                                    name="name_example",
                                    description="description_example",
                                    image_url="image_url_example",
                                    url="url_example",
                                    brand="brand_example",
                                    price=3.14,
                                    currency="currency_example",
                                ),
                            ],
                            closing="closing_example",
                        ),
                    ),
                ],
            ),
        ),
    ) # InbotDiscussionBodyModel | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chatbot_product_recommendations(catalogid, inbot_discussion_body_model)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling OnSiteRecommendationApi->chatbot_product_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogid** | **int**| the identifier of the catalog to query |
 **inbot_discussion_body_model** | [**InbotDiscussionBodyModel**](InbotDiscussionBodyModel.md)|  |

### Return type

[**MessageBodyModel**](MessageBodyModel.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

