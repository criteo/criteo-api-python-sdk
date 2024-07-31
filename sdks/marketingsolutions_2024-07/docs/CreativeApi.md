# criteo_api_marketingsolutions_v2024_07.CreativeApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_advertiser_ad**](CreativeApi.md#create_advertiser_ad) | **POST** /2024-07/marketing-solutions/advertisers/{advertiser-id}/ads | 
[**create_advertiser_coupon**](CreativeApi.md#create_advertiser_coupon) | **POST** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons | 
[**create_advertiser_creative**](CreativeApi.md#create_advertiser_creative) | **POST** /2024-07/marketing-solutions/advertisers/{advertiser-id}/creatives | 
[**delete_ad**](CreativeApi.md#delete_ad) | **DELETE** /2024-07/marketing-solutions/ads/{id} | 
[**delete_advertiser_coupon**](CreativeApi.md#delete_advertiser_coupon) | **DELETE** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} | 
[**delete_creative**](CreativeApi.md#delete_creative) | **DELETE** /2024-07/marketing-solutions/creatives/{id} | 
[**edit_advertiser_coupon**](CreativeApi.md#edit_advertiser_coupon) | **PUT** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} | 
[**edit_creative**](CreativeApi.md#edit_creative) | **PUT** /2024-07/marketing-solutions/creatives/{id} | 
[**generate_creative_preview**](CreativeApi.md#generate_creative_preview) | **POST** /2024-07/marketing-solutions/creatives/{id}/preview | 
[**get_ad**](CreativeApi.md#get_ad) | **GET** /2024-07/marketing-solutions/ads/{id} | 
[**get_advertiser_ads**](CreativeApi.md#get_advertiser_ads) | **GET** /2024-07/marketing-solutions/advertisers/{advertiser-id}/ads | 
[**get_advertiser_coupon**](CreativeApi.md#get_advertiser_coupon) | **GET** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} | 
[**get_advertiser_coupon_preview**](CreativeApi.md#get_advertiser_coupon_preview) | **GET** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}/preview | 
[**get_advertiser_coupon_supported_sizes**](CreativeApi.md#get_advertiser_coupon_supported_sizes) | **GET** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons-supported-sizes | 
[**get_advertiser_coupons**](CreativeApi.md#get_advertiser_coupons) | **GET** /2024-07/marketing-solutions/advertisers/{advertiser-id}/coupons | 
[**get_advertiser_creatives**](CreativeApi.md#get_advertiser_creatives) | **GET** /2024-07/marketing-solutions/advertisers/{advertiser-id}/creatives | 
[**get_creative**](CreativeApi.md#get_creative) | **GET** /2024-07/marketing-solutions/creatives/{id} | 


# **create_advertiser_ad**
> AdResponse create_advertiser_ad(advertiser_id, ad_write_request)



Create an Ad

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.ad_write_request import AdWriteRequest
from criteo_api_marketingsolutions_v2024_07.model.ad_response import AdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    ad_write_request = AdWriteRequest(
        data=AdWriteResource(
            attributes=AdWrite(
                name="name_example",
                description="description_example",
                creative_id="creative_id_example",
                ad_set_id="ad_set_id_example",
                inventory_type="Display",
                start_date="start_date_example",
                end_date="end_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # AdWriteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_advertiser_ad(advertiser_id, ad_write_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->create_advertiser_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **ad_write_request** | [**AdWriteRequest**](AdWriteRequest.md)|  |

### Return type

[**AdResponse**](AdResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Ad is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advertiser_coupon**
> CouponResponse create_advertiser_coupon(advertiser_id, create_coupon_request)



Create a Coupon

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.create_coupon_request import CreateCouponRequest
from criteo_api_marketingsolutions_v2024_07.model.coupon_response import CouponResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    create_coupon_request = CreateCouponRequest(
        data=CreateCouponResource(
            attributes=CreateCoupon(
                name="name_example",
                description="description_example",
                ad_set_id="ad_set_id_example",
                landing_page_url="landing_page_url_example",
                start_date="start_date_example",
                end_date="end_date_example",
                format="FullFrame",
                images=[
                    CreateImageSlide(
                        width=1,
                        height=1,
                        slide_base64_strings=[
                            "slide_base64_strings_example",
                        ],
                    ),
                ],
                show_every=1,
                show_duration=1,
                rotations_number=1,
            ),
            id="id_example",
            type="type_example",
        ),
    ) # CreateCouponRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_advertiser_coupon(advertiser_id, create_coupon_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->create_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **create_coupon_request** | [**CreateCouponRequest**](CreateCouponRequest.md)|  |

### Return type

[**CouponResponse**](CouponResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Coupon is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advertiser_creative**
> CreativeResponse create_advertiser_creative(advertiser_id, creative_write_request)



Create a Creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.creative_response import CreativeResponse
from criteo_api_marketingsolutions_v2024_07.model.creative_write_request import CreativeWriteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    creative_write_request = CreativeWriteRequest(
        data=CreativeWriteResource(
            attributes=CreativeWrite(
                name="name_example",
                description="description_example",
                format="Image",
                dataset_id="dataset_id_example",
                image_write_attributes=ImageWriteAttributes(
                    base64_strings=[
                        "base64_strings_example",
                    ],
                    landing_page_url="landing_page_url_example",
                ),
                html_tag_write_attributes=HtmlTagWriteAttributes(
                    tags=[
                        Tag(
                            html_tag="html_tag_example",
                            size=Size(
                                width=1,
                                height=1,
                            ),
                        ),
                    ],
                ),
                dynamic_write_attributes=DynamicWriteAttributes(
                    logo_base64_string="logo_base64_string_example",
                    creative_background_color="creative_background_color_example",
                    body_text_color="body_text_color_example",
                    prices_color="prices_color_example",
                    primary_font="primary_font_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    product_image_display="ShowFullImage",
                ),
                adaptive_write_attributes=AdaptiveWriteAttributes(
                    layouts=[
                        "Editorial",
                    ],
                    logo_base64_string="logo_base64_string_example",
                    headline_text="headline_text_example",
                    headline_font="headline_font_example",
                    description_text="description_text_example",
                    description_font="description_font_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    colors=AdaptiveColors(
                        logo_area_and_title_color="logo_area_and_title_color_example",
                        background_color="background_color_example",
                        text1_color="text1_color_example",
                        text2_color="text2_color_example",
                        cta_background_color="cta_background_color_example",
                        cta_text_color="cta_text_color_example",
                    ),
                    image_sets_base64=[
                        ImageSetBase64(
                            image_base64_strings=[
                                "image_base64_strings_example",
                            ],
                            headline_text="headline_text_example",
                        ),
                    ],
                    image_display="ShowFullImage",
                    video_base64_strings=[
                        "video_base64_strings_example",
                    ],
                    landing_page_url="landing_page_url_example",
                ),
            ),
            id="id_example",
            type="type_example",
        ),
    ) # CreativeWriteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_advertiser_creative(advertiser_id, creative_write_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->create_advertiser_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **creative_write_request** | [**CreativeWriteRequest**](CreativeWriteRequest.md)|  |

### Return type

[**CreativeResponse**](CreativeResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created creative is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ad**
> delete_ad(id)



Delete an Ad

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    id = 1 # int | The ad identifier to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ad(id)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->delete_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad identifier to delete. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The ad was deleted. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_advertiser_coupon**
> delete_advertiser_coupon(advertiser_id, id)



Delete a Coupon

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_advertiser_coupon(advertiser_id, id)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->delete_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to delete. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Coupon was deleted. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_creative**
> delete_creative(id)



Delete a Creative if there are no ads binded to it

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The creative identifier to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_creative(id)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->delete_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The creative identifier to delete. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The creative was deleted. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_advertiser_coupon**
> CouponResponse edit_advertiser_coupon(advertiser_id, id, update_coupon_request)



Edit a specific Coupon

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.coupon_response import CouponResponse
from criteo_api_marketingsolutions_v2024_07.model.update_coupon_request import UpdateCouponRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to edit.
    update_coupon_request = UpdateCouponRequest(
        data=UpdateCouponResource(
            attributes=UpdateCoupon(
                start_date="start_date_example",
                end_date="end_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # UpdateCouponRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_advertiser_coupon(advertiser_id, id, update_coupon_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->edit_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to edit. |
 **update_coupon_request** | [**UpdateCouponRequest**](UpdateCouponRequest.md)|  |

### Return type

[**CouponResponse**](CouponResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edited Coupon is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_creative**
> CreativeResponse edit_creative(id, creative_write_request)



Edit a specific Creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.creative_response import CreativeResponse
from criteo_api_marketingsolutions_v2024_07.model.creative_write_request import CreativeWriteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The creative identifier to edit.
    creative_write_request = CreativeWriteRequest(
        data=CreativeWriteResource(
            attributes=CreativeWrite(
                name="name_example",
                description="description_example",
                format="Image",
                dataset_id="dataset_id_example",
                image_write_attributes=ImageWriteAttributes(
                    base64_strings=[
                        "base64_strings_example",
                    ],
                    landing_page_url="landing_page_url_example",
                ),
                html_tag_write_attributes=HtmlTagWriteAttributes(
                    tags=[
                        Tag(
                            html_tag="html_tag_example",
                            size=Size(
                                width=1,
                                height=1,
                            ),
                        ),
                    ],
                ),
                dynamic_write_attributes=DynamicWriteAttributes(
                    logo_base64_string="logo_base64_string_example",
                    creative_background_color="creative_background_color_example",
                    body_text_color="body_text_color_example",
                    prices_color="prices_color_example",
                    primary_font="primary_font_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    product_image_display="ShowFullImage",
                ),
                adaptive_write_attributes=AdaptiveWriteAttributes(
                    layouts=[
                        "Editorial",
                    ],
                    logo_base64_string="logo_base64_string_example",
                    headline_text="headline_text_example",
                    headline_font="headline_font_example",
                    description_text="description_text_example",
                    description_font="description_font_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    colors=AdaptiveColors(
                        logo_area_and_title_color="logo_area_and_title_color_example",
                        background_color="background_color_example",
                        text1_color="text1_color_example",
                        text2_color="text2_color_example",
                        cta_background_color="cta_background_color_example",
                        cta_text_color="cta_text_color_example",
                    ),
                    image_sets_base64=[
                        ImageSetBase64(
                            image_base64_strings=[
                                "image_base64_strings_example",
                            ],
                            headline_text="headline_text_example",
                        ),
                    ],
                    image_display="ShowFullImage",
                    video_base64_strings=[
                        "video_base64_strings_example",
                    ],
                    landing_page_url="landing_page_url_example",
                ),
            ),
            id="id_example",
            type="type_example",
        ),
    ) # CreativeWriteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_creative(id, creative_write_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->edit_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The creative identifier to edit. |
 **creative_write_request** | [**CreativeWriteRequest**](CreativeWriteRequest.md)|  |

### Return type

[**CreativeResponse**](CreativeResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edited creative is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_creative_preview**
> str generate_creative_preview(id)



Generate a preview of a specific Creative

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The Creative identifier to preview.
    width = 1 # int | The width of the Creative to preview. (optional)
    height = 1 # int | The height of the Creative to preview. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_creative_preview(id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->generate_creative_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_creative_preview(id, width=width, height=height)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->generate_creative_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Creative identifier to preview. |
 **width** | **int**| The width of the Creative to preview. | [optional]
 **height** | **int**| The height of the Creative to preview. | [optional]

### Return type

**str**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The preview HTML of a specific Creative is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad**
> AdResponse get_ad(id)



Get an Ad from its id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.ad_response import AdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    id = 1 # int | The ad identifier to retrieve.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ad(id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad identifier to retrieve. |

### Return type

[**AdResponse**](AdResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found ad is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_ads**
> AdListResponse get_advertiser_ads(advertiser_id)



Get the list of self-services Ads for a given advertiser

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.ad_list_response import AdListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    limit = 1 # int | The number of ads to be returned. The default is 50. (optional)
    offset = 1 # int | The (zero-based) offset into the collection of ads. The default is 0. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_ads(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_ads: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_advertiser_ads(advertiser_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_ads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **limit** | **int**| The number of ads to be returned. The default is 50. | [optional]
 **offset** | **int**| The (zero-based) offset into the collection of ads. The default is 0. | [optional]

### Return type

[**AdListResponse**](AdListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of self-services Ads is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupon**
> CouponResponse get_advertiser_coupon(advertiser_id, id)



Get a Coupon from its id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.coupon_response import CouponResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to retrieve.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_coupon(advertiser_id, id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to retrieve. |

### Return type

[**CouponResponse**](CouponResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found Coupon is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupon_preview**
> str get_advertiser_coupon_preview(advertiser_id, id)



Get the preview of a specific Coupon

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to preview.
    width = 1 # int | The width of the coupon to preview. (optional)
    height = 1 # int | The height of the coupon to preview. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_coupon_preview(advertiser_id, id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_advertiser_coupon_preview(advertiser_id, id, width=width, height=height)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to preview. |
 **width** | **int**| The width of the coupon to preview. | [optional]
 **height** | **int**| The height of the coupon to preview. | [optional]

### Return type

**str**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The preview HTML of a specific Coupon is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupon_supported_sizes**
> CouponSupportedSizesResponse get_advertiser_coupon_supported_sizes(advertiser_id)



Get the list of Coupon supported sizes

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.coupon_supported_sizes_response import CouponSupportedSizesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    ad_set_id = "ad-set-id_example" # str | The ad set id on which you want to check the Coupon supported sizes. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_coupon_supported_sizes(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_supported_sizes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_advertiser_coupon_supported_sizes(advertiser_id, ad_set_id=ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_supported_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **ad_set_id** | **str**| The ad set id on which you want to check the Coupon supported sizes. | [optional]

### Return type

[**CouponSupportedSizesResponse**](CouponSupportedSizesResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Coupon supported sizes is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupons**
> CouponListResponse get_advertiser_coupons(advertiser_id)



Get the list of self-services Coupons for a given advertiser

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.coupon_list_response import CouponListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    limit = 1 # int | The number of coupons to be returned. The default is 50. (optional)
    offset = 1 # int | The (zero-based) offset into the collection of coupons. The default is 0. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_coupons(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupons: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_advertiser_coupons(advertiser_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **limit** | **int**| The number of coupons to be returned. The default is 50. | [optional]
 **offset** | **int**| The (zero-based) offset into the collection of coupons. The default is 0. | [optional]

### Return type

[**CouponListResponse**](CouponListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of self-services Coupons is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**403** | The request was not properly authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_creatives**
> CreativeListResponse get_advertiser_creatives(advertiser_id)



Get the list of self-services Creatives for a given advertiser

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.creative_list_response import CreativeListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    limit = 1 # int | The number of creatives to be returned. The default is 50. (optional)
    offset = 1 # int | The (zero-based) offset into the collection of creatives. The default is 0. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_advertiser_creatives(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_creatives: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_advertiser_creatives(advertiser_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_creatives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **limit** | **int**| The number of creatives to be returned. The default is 50. | [optional]
 **offset** | **int**| The (zero-based) offset into the collection of creatives. The default is 0. | [optional]

### Return type

[**CreativeListResponse**](CreativeListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of self-services Creatives is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creative**
> CreativeResponse get_creative(id)



Get a Creative from its id

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_v2024_07
from criteo_api_marketingsolutions_v2024_07.api import creative_api
from criteo_api_marketingsolutions_v2024_07.model.creative_response import CreativeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_marketingsolutions_v2024_07.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2024_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The creative identifier to retrieve.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_creative(id)
        pprint(api_response)
    except criteo_api_marketingsolutions_v2024_07.ApiException as e:
        print("Exception when calling CreativeApi->get_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The creative identifier to retrieve. |

### Return type

[**CreativeResponse**](CreativeResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found creative is returned. |  -  |
**400** | The request contained invalid parameters. |  -  |
**401** | The request was not properly authorized. |  -  |
**500** | A non-request based error occurred on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

