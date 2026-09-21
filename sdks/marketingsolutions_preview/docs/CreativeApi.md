# criteo_api_marketingsolutions_preview.CreativeApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_advertiser_ad**](CreativeApi.md#create_advertiser_ad) | **POST** /preview/advertisers/{advertiser-id}/ads | /preview/advertisers/{advertiser-id}/ads
[**create_advertiser_coupon**](CreativeApi.md#create_advertiser_coupon) | **POST** /preview/advertisers/{advertiser-id}/coupons | /preview/advertisers/{advertiser-id}/coupons
[**create_advertiser_creative**](CreativeApi.md#create_advertiser_creative) | **POST** /preview/advertisers/{advertiser-id}/creatives | /preview/advertisers/{advertiser-id}/creatives
[**delete_ad**](CreativeApi.md#delete_ad) | **DELETE** /preview/ads/{id} | /preview/ads/{id}
[**delete_ad_segment_link**](CreativeApi.md#delete_ad_segment_link) | **DELETE** /preview/marketing-solutions/ads/{ad-id}/audience-segment | /preview/marketing-solutions/ads/{ad-id}/audience-segment
[**delete_advertiser_coupon**](CreativeApi.md#delete_advertiser_coupon) | **DELETE** /preview/advertisers/{advertiser-id}/coupons/{id} | /preview/advertisers/{advertiser-id}/coupons/{id}
[**delete_creative**](CreativeApi.md#delete_creative) | **DELETE** /preview/creatives/{id} | /preview/creatives/{id}
[**edit_advertiser_coupon**](CreativeApi.md#edit_advertiser_coupon) | **PUT** /preview/advertisers/{advertiser-id}/coupons/{id} | /preview/advertisers/{advertiser-id}/coupons/{id}
[**edit_creative**](CreativeApi.md#edit_creative) | **PUT** /preview/creatives/{id} | /preview/creatives/{id}
[**generate_creative_preview**](CreativeApi.md#generate_creative_preview) | **POST** /preview/creatives/{id}/preview | /preview/creatives/{id}/preview
[**get_ad**](CreativeApi.md#get_ad) | **GET** /preview/ads/{id} | /preview/ads/{id}
[**get_ad_segment_link**](CreativeApi.md#get_ad_segment_link) | **GET** /preview/marketing-solutions/ads/{ad-id}/audience-segment | /preview/marketing-solutions/ads/{ad-id}/audience-segment
[**get_advertiser_ads**](CreativeApi.md#get_advertiser_ads) | **GET** /preview/advertisers/{advertiser-id}/ads | /preview/advertisers/{advertiser-id}/ads
[**get_advertiser_coupon**](CreativeApi.md#get_advertiser_coupon) | **GET** /preview/advertisers/{advertiser-id}/coupons/{id} | /preview/advertisers/{advertiser-id}/coupons/{id}
[**get_advertiser_coupon_preview**](CreativeApi.md#get_advertiser_coupon_preview) | **GET** /preview/advertisers/{advertiser-id}/coupons/{id}/preview | /preview/advertisers/{advertiser-id}/coupons/{id}/preview
[**get_advertiser_coupon_supported_sizes**](CreativeApi.md#get_advertiser_coupon_supported_sizes) | **GET** /preview/advertisers/{advertiser-id}/coupons-supported-sizes | /preview/advertisers/{advertiser-id}/coupons-supported-sizes
[**get_advertiser_coupons**](CreativeApi.md#get_advertiser_coupons) | **GET** /preview/advertisers/{advertiser-id}/coupons | /preview/advertisers/{advertiser-id}/coupons
[**get_advertiser_creatives**](CreativeApi.md#get_advertiser_creatives) | **GET** /preview/advertisers/{advertiser-id}/creatives | /preview/advertisers/{advertiser-id}/creatives
[**get_creative**](CreativeApi.md#get_creative) | **GET** /preview/creatives/{id} | /preview/creatives/{id}
[**link_ad_segment**](CreativeApi.md#link_ad_segment) | **PUT** /preview/marketing-solutions/ads/{ad-id}/audience-segment | /preview/marketing-solutions/ads/{ad-id}/audience-segment


# **create_advertiser_ad**
> ResourceOutcomeOfAd create_advertiser_ad(advertiser_id, resource_input_of_ad_write)

/preview/advertisers/{advertiser-id}/ads

Creates an ad by binding an existing creative to an existing ad set of the advertiser, delivering  from the start date given. The creative and the ad set must both belong to that advertiser. Returns  the new ad and its id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_input_of_ad_write import ResourceInputOfAdWrite
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_ad import ResourceOutcomeOfAd
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    resource_input_of_ad_write = ResourceInputOfAdWrite(
        data=ResourceOfAdWrite(
            attributes=AdWrite(
                ad_click_tracking=[
                    ExamAdClickTracking(
                        binding_id="binding_id_example",
                        click_zone="Unknown",
                        disable_for_coupons=True,
                        disable_landing_url_encode=True,
                        disable_macro_url_encode=True,
                        display_height=1,
                        display_width=1,
                        id="id_example",
                        url_prefix="url_prefix_example",
                        url_suffix="url_suffix_example",
                    ),
                ],
                ad_impression_tracking=[
                    ExamAdImpressionTracking(
                        binding_id="binding_id_example",
                        display_height=1,
                        display_width=1,
                        id="id_example",
                        url="url_example",
                        vendor_id="vendor_id_example",
                    ),
                ],
                ad_set_id="ad_set_id_example",
                creative_id="creative_id_example",
                description="description_example",
                end_date="end_date_example",
                id="id_example",
                inventory_type="Native",
                name="name_example",
                start_date="start_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ResourceInputOfAdWrite | The ad information.

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/ads
        api_response = api_instance.create_advertiser_ad(advertiser_id, resource_input_of_ad_write)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->create_advertiser_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **resource_input_of_ad_write** | [**ResourceInputOfAdWrite**](ResourceInputOfAdWrite.md)| The ad information. |

### Return type

[**ResourceOutcomeOfAd**](ResourceOutcomeOfAd.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Ad is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advertiser_coupon**
> ResourceOutcomeOfCoupon create_advertiser_coupon(advertiser_id, resource_input_of_create_coupon)

/preview/advertisers/{advertiser-id}/coupons

Creates a coupon on one ad set of the advertiser. The ad set must already carry dynamic display or  HTML ads, and each slide image must match a size that ad set supports, which the supported-sizes  operation lists. Returns the new coupon and its id.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_input_of_create_coupon import ResourceInputOfCreateCoupon
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_coupon import ResourceOutcomeOfCoupon
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    resource_input_of_create_coupon = ResourceInputOfCreateCoupon(
        data=ResourceOfCreateCoupon(
            attributes=CreateCoupon(
                ad_set_id="ad_set_id_example",
                description="description_example",
                end_date="end_date_example",
                format="FullFrame",
                id="id_example",
                images=[
                    CreateImageSlide(
                        height=1,
                        slide_base64_strings=[
                            "slide_base64_strings_example",
                        ],
                        width=1,
                    ),
                ],
                landing_page_url="landing_page_url_example",
                name="name_example",
                rotations_number=1,
                show_duration=1,
                show_every=1,
                start_date="start_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ResourceInputOfCreateCoupon | The coupon to create.

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons
        api_response = api_instance.create_advertiser_coupon(advertiser_id, resource_input_of_create_coupon)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->create_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **resource_input_of_create_coupon** | [**ResourceInputOfCreateCoupon**](ResourceInputOfCreateCoupon.md)| The coupon to create. |

### Return type

[**ResourceOutcomeOfCoupon**](ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Coupon is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advertiser_creative**
> ResourceOutcomeOfCreative create_advertiser_creative(advertiser_id, resource_input_of_creative_write)

/preview/advertisers/{advertiser-id}/creatives

Creates a creative in the library of one advertiser. The format decides which attributes block must  be filled in, and the dataset must be one of that advertiser's. Returns the new creative, whose id is  what an ad binds to.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_input_of_creative_write import ResourceInputOfCreativeWrite
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_creative import ResourceOutcomeOfCreative
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    resource_input_of_creative_write = ResourceInputOfCreativeWrite(
        data=ResourceOfCreativeWrite(
            attributes=CreativeWrite(
                adaptive_write_attributes=AdaptiveWriteAttributes(
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    colors=AdaptiveColors(
                        background_color="background_color_example",
                        cta_background_color="cta_background_color_example",
                        cta_text_color="cta_text_color_example",
                        logo_area_and_title_color="logo_area_and_title_color_example",
                        text1_color="text1_color_example",
                        text2_color="text2_color_example",
                    ),
                    description_font="description_font_example",
                    description_text="description_text_example",
                    headline_font="headline_font_example",
                    headline_text="headline_text_example",
                    image_display="ShowFullImage",
                    image_sets_base64=[
                        ImageSetBase64(
                            headline_text="headline_text_example",
                            image_base64_strings=[
                                "image_base64_strings_example",
                            ],
                        ),
                    ],
                    landing_page_url="landing_page_url_example",
                    layouts=[
                        "Editorial",
                    ],
                    logo_base64_string="logo_base64_string_example",
                    video_base64_strings=[
                        "video_base64_strings_example",
                    ],
                ),
                dataset_id="dataset_id_example",
                description="description_example",
                dynamic_write_attributes=DynamicWriteAttributes(
                    body_text_color="body_text_color_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    creative_background_color="creative_background_color_example",
                    logo_base64_string="logo_base64_string_example",
                    prices_color="prices_color_example",
                    primary_font="primary_font_example",
                    product_image_display="ShowFullImage",
                ),
                format="Dynamic",
                html_tag_write_attributes=HtmlTagWriteAttributes(
                    tags=[
                        Tag(
                            html_tag="html_tag_example",
                            size=Size(
                                height=1,
                                width=1,
                            ),
                        ),
                    ],
                ),
                id="id_example",
                image_write_attributes=ImageWriteAttributes(
                    base64_strings=[
                        "base64_strings_example",
                    ],
                    landing_page_url="landing_page_url_example",
                ),
                name="name_example",
                showcase_write_attributes=ShowcaseWriteAttributes(
                    android_deeplink_url="android_deeplink_url_example",
                    app_link_url="app_link_url_example",
                    branding_image_base64_strings=[
                        BrandingImageInput(
                            base64_string="base64_string_example",
                            shape="shape_example",
                        ),
                    ],
                    branding_image_click_url="branding_image_click_url_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    colors=ShowcaseColors(
                        body_text_color="body_text_color_example",
                        creative_background_color="creative_background_color_example",
                        prices_color="prices_color_example",
                    ),
                    ios_deeplink_url="ios_deeplink_url_example",
                    landing_page_url="landing_page_url_example",
                    layouts=[
                        "Showcase",
                    ],
                    logo_base64_strings=[
                        LogoInput(
                            base64_string="base64_string_example",
                            shape="shape_example",
                        ),
                    ],
                    meta_setting=ShowcaseMetaSetting(
                        call_to_action="call_to_action_example",
                        headline="headline_example",
                    ),
                    price_settings=ShowcasePriceSettings(
                        hide_decimals=True,
                        price_format="price_format_example",
                        price_format_body="price_format_body_example",
                        price_text_after="price_text_after_example",
                        price_text_before="price_text_before_example",
                    ),
                    primary_font="primary_font_example",
                    product_image_display="ShowFullImage",
                    secondary_font="secondary_font_example",
                    universal_link_url="universal_link_url_example",
                ),
                social_settings=SocialSettings(
                    meta=CreativeMetaSetting(
                        call_to_action="call_to_action_example",
                        headline="headline_example",
                    ),
                    tiktok=CreativeTikTokSetting(
                        call_to_action="call_to_action_example",
                        headline="headline_example",
                    ),
                ),
                vast_tag_write_attributes=VastTagWriteAttributes(
                    vast_tag_url="vast_tag_url_example",
                ),
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ResourceInputOfCreativeWrite | The creative information.

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/creatives
        api_response = api_instance.create_advertiser_creative(advertiser_id, resource_input_of_creative_write)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->create_advertiser_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **resource_input_of_creative_write** | [**ResourceInputOfCreativeWrite**](ResourceInputOfCreativeWrite.md)| The creative information. |

### Return type

[**ResourceOutcomeOfCreative**](ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created creative is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ad**
> delete_ad(id)

/preview/ads/{id}

Deletes one ad, which stops it delivering for good. The creative it was bound to is kept and can be  reused; to stop delivery without losing the ad, pause it instead.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
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
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The ad identifier to delete.

    # example passing only required values which don't have defaults set
    try:
        # /preview/ads/{id}
        api_instance.delete_ad(id)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->delete_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ad identifier to delete. |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ad_segment_link**
> delete_ad_segment_link(ad_id)

/preview/marketing-solutions/ads/{ad-id}/audience-segment

Delete the link between an Ad and an Audience Segment.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
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
    api_instance = creative_api.CreativeApi(api_client)
    ad_id = "ad-id_example" # str | The ad identifier.

    # example passing only required values which don't have defaults set
    try:
        # /preview/marketing-solutions/ads/{ad-id}/audience-segment
        api_instance.delete_ad_segment_link(ad_id)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->delete_ad_segment_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_id** | **str**| The ad identifier. |

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
**204** | The link between the ad and its audience segment has been deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_advertiser_coupon**
> delete_advertiser_coupon(advertiser_id, id)

/preview/advertisers/{advertiser-id}/coupons/{id}

Deletes one coupon of an advertiser. A coupon that is already deleted or under review cannot be  deleted.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to delete.

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons/{id}
        api_instance.delete_advertiser_coupon(advertiser_id, id)
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_creative**
> delete_creative(id)

/preview/creatives/{id}

Deletes one creative. Every ad bound to it must be deleted or rebound first, and a creative that is  already deleted or under review cannot be deleted.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
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
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The creative identifier to delete.

    # example passing only required values which don't have defaults set
    try:
        # /preview/creatives/{id}
        api_instance.delete_creative(id)
    except criteo_api_marketingsolutions_preview.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_advertiser_coupon**
> ResourceOutcomeOfCoupon edit_advertiser_coupon(advertiser_id, id, resource_input_of_update_coupon)

/preview/advertisers/{advertiser-id}/coupons/{id}

Changes when a coupon runs; only the start and end dates can be edited, and the start date must come  before the end date. The coupon must still be a draft or live coupon that is not yet delivering.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_input_of_update_coupon import ResourceInputOfUpdateCoupon
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_coupon import ResourceOutcomeOfCoupon
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to edit.
    resource_input_of_update_coupon = ResourceInputOfUpdateCoupon(
        data=ResourceOfUpdateCoupon(
            attributes=UpdateCoupon(
                end_date="end_date_example",
                id="id_example",
                start_date="start_date_example",
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ResourceInputOfUpdateCoupon | The new start and end dates of the coupon.

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons/{id}
        api_response = api_instance.edit_advertiser_coupon(advertiser_id, id, resource_input_of_update_coupon)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->edit_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to edit. |
 **resource_input_of_update_coupon** | [**ResourceInputOfUpdateCoupon**](ResourceInputOfUpdateCoupon.md)| The new start and end dates of the coupon. |

### Return type

[**ResourceOutcomeOfCoupon**](ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edited Coupon is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_creative**
> ResourceOutcomeOfCreative edit_creative(id, resource_input_of_creative_write)

/preview/creatives/{id}

Replaces the attributes of one creative: any attribute left out is cleared, so read the creative  first and send it back with your changes applied. The format must be the creative's existing format  and the dataset must stay the one it already belongs to; neither can be changed here. A creative  that is being deployed, archived or deleted cannot be edited.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_input_of_creative_write import ResourceInputOfCreativeWrite
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_creative import ResourceOutcomeOfCreative
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
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The creative identifier to edit.
    resource_input_of_creative_write = ResourceInputOfCreativeWrite(
        data=ResourceOfCreativeWrite(
            attributes=CreativeWrite(
                adaptive_write_attributes=AdaptiveWriteAttributes(
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    colors=AdaptiveColors(
                        background_color="background_color_example",
                        cta_background_color="cta_background_color_example",
                        cta_text_color="cta_text_color_example",
                        logo_area_and_title_color="logo_area_and_title_color_example",
                        text1_color="text1_color_example",
                        text2_color="text2_color_example",
                    ),
                    description_font="description_font_example",
                    description_text="description_text_example",
                    headline_font="headline_font_example",
                    headline_text="headline_text_example",
                    image_display="ShowFullImage",
                    image_sets_base64=[
                        ImageSetBase64(
                            headline_text="headline_text_example",
                            image_base64_strings=[
                                "image_base64_strings_example",
                            ],
                        ),
                    ],
                    landing_page_url="landing_page_url_example",
                    layouts=[
                        "Editorial",
                    ],
                    logo_base64_string="logo_base64_string_example",
                    video_base64_strings=[
                        "video_base64_strings_example",
                    ],
                ),
                dataset_id="dataset_id_example",
                description="description_example",
                dynamic_write_attributes=DynamicWriteAttributes(
                    body_text_color="body_text_color_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    creative_background_color="creative_background_color_example",
                    logo_base64_string="logo_base64_string_example",
                    prices_color="prices_color_example",
                    primary_font="primary_font_example",
                    product_image_display="ShowFullImage",
                ),
                format="Dynamic",
                html_tag_write_attributes=HtmlTagWriteAttributes(
                    tags=[
                        Tag(
                            html_tag="html_tag_example",
                            size=Size(
                                height=1,
                                width=1,
                            ),
                        ),
                    ],
                ),
                id="id_example",
                image_write_attributes=ImageWriteAttributes(
                    base64_strings=[
                        "base64_strings_example",
                    ],
                    landing_page_url="landing_page_url_example",
                ),
                name="name_example",
                showcase_write_attributes=ShowcaseWriteAttributes(
                    android_deeplink_url="android_deeplink_url_example",
                    app_link_url="app_link_url_example",
                    branding_image_base64_strings=[
                        BrandingImageInput(
                            base64_string="base64_string_example",
                            shape="shape_example",
                        ),
                    ],
                    branding_image_click_url="branding_image_click_url_example",
                    calls_to_action=[
                        "calls_to_action_example",
                    ],
                    colors=ShowcaseColors(
                        body_text_color="body_text_color_example",
                        creative_background_color="creative_background_color_example",
                        prices_color="prices_color_example",
                    ),
                    ios_deeplink_url="ios_deeplink_url_example",
                    landing_page_url="landing_page_url_example",
                    layouts=[
                        "Showcase",
                    ],
                    logo_base64_strings=[
                        LogoInput(
                            base64_string="base64_string_example",
                            shape="shape_example",
                        ),
                    ],
                    meta_setting=ShowcaseMetaSetting(
                        call_to_action="call_to_action_example",
                        headline="headline_example",
                    ),
                    price_settings=ShowcasePriceSettings(
                        hide_decimals=True,
                        price_format="price_format_example",
                        price_format_body="price_format_body_example",
                        price_text_after="price_text_after_example",
                        price_text_before="price_text_before_example",
                    ),
                    primary_font="primary_font_example",
                    product_image_display="ShowFullImage",
                    secondary_font="secondary_font_example",
                    universal_link_url="universal_link_url_example",
                ),
                social_settings=SocialSettings(
                    meta=CreativeMetaSetting(
                        call_to_action="call_to_action_example",
                        headline="headline_example",
                    ),
                    tiktok=CreativeTikTokSetting(
                        call_to_action="call_to_action_example",
                        headline="headline_example",
                    ),
                ),
                vast_tag_write_attributes=VastTagWriteAttributes(
                    vast_tag_url="vast_tag_url_example",
                ),
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ResourceInputOfCreativeWrite | The complete new attributes of the creative.

    # example passing only required values which don't have defaults set
    try:
        # /preview/creatives/{id}
        api_response = api_instance.edit_creative(id, resource_input_of_creative_write)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->edit_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The creative identifier to edit. |
 **resource_input_of_creative_write** | [**ResourceInputOfCreativeWrite**](ResourceInputOfCreativeWrite.md)| The complete new attributes of the creative. |

### Return type

[**ResourceOutcomeOfCreative**](ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edited creative is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_creative_preview**
> str generate_creative_preview(id)

/preview/creatives/{id}/preview

Renders one creative as preview HTML at the size asked for. Only the sizes the creative was built for  can be previewed; when the size does not match, the error lists the ones that can.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
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
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The Creative identifier to preview.
    height = 1 # int | The height of the Creative to preview. (optional)
    width = 1 # int | The width of the Creative to preview. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /preview/creatives/{id}/preview
        api_response = api_instance.generate_creative_preview(id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->generate_creative_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /preview/creatives/{id}/preview
        api_response = api_instance.generate_creative_preview(id, height=height, width=width)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->generate_creative_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Creative identifier to preview. |
 **height** | **int**| The height of the Creative to preview. | [optional]
 **width** | **int**| The width of the Creative to preview. | [optional]

### Return type

**str**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The preview HTML of a specific Creative is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad**
> ResourceOutcomeOfAd get_ad(id)

/preview/ads/{id}

Reads one ad by its id: the creative and ad set it binds, its schedule and its delivery status. The  id comes from the ad list of the advertiser.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_ad import ResourceOutcomeOfAd
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
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The ad identifier to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # /preview/ads/{id}
        api_response = api_instance.get_ad(id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ad identifier to retrieve. |

### Return type

[**ResourceOutcomeOfAd**](ResourceOutcomeOfAd.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found ad is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_segment_link**
> ValueResourceOutcomeOfExamAdAudienceSegmentLink get_ad_segment_link(ad_id)

/preview/marketing-solutions/ads/{ad-id}/audience-segment

Retrieve the Ad audience segment link.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.value_resource_outcome_of_exam_ad_audience_segment_link import ValueResourceOutcomeOfExamAdAudienceSegmentLink
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
    api_instance = creative_api.CreativeApi(api_client)
    ad_id = "ad-id_example" # str | The ad identifier.

    # example passing only required values which don't have defaults set
    try:
        # /preview/marketing-solutions/ads/{ad-id}/audience-segment
        api_response = api_instance.get_ad_segment_link(ad_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_ad_segment_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_id** | **str**| The ad identifier. |

### Return type

[**ValueResourceOutcomeOfExamAdAudienceSegmentLink**](ValueResourceOutcomeOfExamAdAudienceSegmentLink.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found ad audience segment link is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_ads**
> ResourceCollectionOutcomeOfAd get_advertiser_ads(advertiser_id)

/preview/advertisers/{advertiser-id}/ads

Lists the ads of one advertiser, each one binding a creative to an ad set. Use it to find an ad id  before reading, pausing, unpausing or deleting a single ad. Page through the ads with limit and  offset.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_collection_outcome_of_ad import ResourceCollectionOutcomeOfAd
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    limit = 1 # int, none_type | The number of ads to be returned. The default is 50. (optional)
    offset = 1 # int, none_type | The (zero-based) offset into the collection of ads. The default is 0. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/ads
        api_response = api_instance.get_advertiser_ads(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_ads: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /preview/advertisers/{advertiser-id}/ads
        api_response = api_instance.get_advertiser_ads(advertiser_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_ads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **limit** | **int, none_type**| The number of ads to be returned. The default is 50. | [optional]
 **offset** | **int, none_type**| The (zero-based) offset into the collection of ads. The default is 0. | [optional]

### Return type

[**ResourceCollectionOutcomeOfAd**](ResourceCollectionOutcomeOfAd.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of self-services Ads is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupon**
> ResourceOutcomeOfCoupon get_advertiser_coupon(advertiser_id, id)

/preview/advertisers/{advertiser-id}/coupons/{id}

Reads one coupon of an advertiser by its id: its schedule, its slides and the ad set it runs on. The  id comes from the coupon list of the advertiser.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_coupon import ResourceOutcomeOfCoupon
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons/{id}
        api_response = api_instance.get_advertiser_coupon(advertiser_id, id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to retrieve. |

### Return type

[**ResourceOutcomeOfCoupon**](ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found Coupon is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupon_preview**
> str get_advertiser_coupon_preview(advertiser_id, id)

/preview/advertisers/{advertiser-id}/coupons/{id}/preview

Renders one coupon as preview HTML at the size asked for. The size must be one the coupon's ad set  supports, as listed by the supported-sizes operation.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    id = "id_example" # str | The Coupon identifier to preview.
    height = 1 # int | The height of the coupon to preview. (optional)
    width = 1 # int | The width of the coupon to preview. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons/{id}/preview
        api_response = api_instance.get_advertiser_coupon_preview(advertiser_id, id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /preview/advertisers/{advertiser-id}/coupons/{id}/preview
        api_response = api_instance.get_advertiser_coupon_preview(advertiser_id, id, height=height, width=width)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **id** | **str**| The Coupon identifier to preview. |
 **height** | **int**| The height of the coupon to preview. | [optional]
 **width** | **int**| The width of the coupon to preview. | [optional]

### Return type

**str**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The preview HTML of a specific Coupon is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupon_supported_sizes**
> ResourceOutcomeOfCouponSupportedSizes get_advertiser_coupon_supported_sizes(advertiser_id)

/preview/advertisers/{advertiser-id}/coupons-supported-sizes

Lists, per coupon format, the sizes an ad set supports. Call it before creating a coupon to pick a  valid slide size; the ad set must already carry dynamic ads.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_coupon_supported_sizes import ResourceOutcomeOfCouponSupportedSizes
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    ad_set_id = "ad-set-id_example" # str | The ad set id on which you want to check the Coupon supported sizes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons-supported-sizes
        api_response = api_instance.get_advertiser_coupon_supported_sizes(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_supported_sizes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /preview/advertisers/{advertiser-id}/coupons-supported-sizes
        api_response = api_instance.get_advertiser_coupon_supported_sizes(advertiser_id, ad_set_id=ad_set_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupon_supported_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **ad_set_id** | **str**| The ad set id on which you want to check the Coupon supported sizes. | [optional]

### Return type

[**ResourceOutcomeOfCouponSupportedSizes**](ResourceOutcomeOfCouponSupportedSizes.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Coupon supported sizes is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_coupons**
> ResourceCollectionOutcomeOfCoupon get_advertiser_coupons(advertiser_id)

/preview/advertisers/{advertiser-id}/coupons

Lists the coupons of one advertiser. Use it to find a coupon id before reading, editing, previewing  or deleting a single coupon. Page through the coupons with limit and offset.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_collection_outcome_of_coupon import ResourceCollectionOutcomeOfCoupon
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    limit = 1 # int, none_type | The number of coupons to be returned. The default is 50. (optional)
    offset = 1 # int, none_type | The (zero-based) offset into the collection of coupons. The default is 0. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/coupons
        api_response = api_instance.get_advertiser_coupons(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupons: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /preview/advertisers/{advertiser-id}/coupons
        api_response = api_instance.get_advertiser_coupons(advertiser_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_coupons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **limit** | **int, none_type**| The number of coupons to be returned. The default is 50. | [optional]
 **offset** | **int, none_type**| The (zero-based) offset into the collection of coupons. The default is 0. | [optional]

### Return type

[**ResourceCollectionOutcomeOfCoupon**](ResourceCollectionOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of self-services Coupons is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advertiser_creatives**
> ResourceCollectionOutcomeOfCreativeRead get_advertiser_creatives(advertiser_id)

/preview/advertisers/{advertiser-id}/creatives

Lists the creatives in the library of one advertiser. Use it to find a creative id before reading,  editing or previewing a creative, or before binding one to an ad. Page through the library with  limit and offset.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_collection_outcome_of_creative_read import ResourceCollectionOutcomeOfCreativeRead
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
    api_instance = creative_api.CreativeApi(api_client)
    advertiser_id = "advertiser-id_example" # str | The advertiser identifier.
    limit = 1 # int, none_type | The number of creatives to be returned. The default is 50. (optional)
    offset = 1 # int, none_type | The (zero-based) offset into the collection of creatives. The default is 0. (optional)

    # example passing only required values which don't have defaults set
    try:
        # /preview/advertisers/{advertiser-id}/creatives
        api_response = api_instance.get_advertiser_creatives(advertiser_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_creatives: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /preview/advertisers/{advertiser-id}/creatives
        api_response = api_instance.get_advertiser_creatives(advertiser_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_advertiser_creatives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser identifier. |
 **limit** | **int, none_type**| The number of creatives to be returned. The default is 50. | [optional]
 **offset** | **int, none_type**| The (zero-based) offset into the collection of creatives. The default is 0. | [optional]

### Return type

[**ResourceCollectionOutcomeOfCreativeRead**](ResourceCollectionOutcomeOfCreativeRead.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of self-services Creatives is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creative**
> ResourceOutcomeOfCreative get_creative(id)

/preview/creatives/{id}

Reads one creative by its id, with the attributes of its format. Use it to check a creative before  editing it or binding it to an ad.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_creative import ResourceOutcomeOfCreative
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
    api_instance = creative_api.CreativeApi(api_client)
    id = "id_example" # str | The creative identifier to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # /preview/creatives/{id}
        api_response = api_instance.get_creative(id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->get_creative: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The creative identifier to retrieve. |

### Return type

[**ResourceOutcomeOfCreative**](ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found creative is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_ad_segment**
> ValueResourceOutcomeOfExamAdAudienceSegmentLink link_ad_segment(ad_id, exam_ad_audience_segment_link_input)

/preview/marketing-solutions/ads/{ad-id}/audience-segment

Link an Ad with an Audience Segment. If a link already exists, its segment ID will be updated.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import creative_api
from criteo_api_marketingsolutions_preview.model.value_resource_outcome_of_exam_ad_audience_segment_link import ValueResourceOutcomeOfExamAdAudienceSegmentLink
from criteo_api_marketingsolutions_preview.model.exam_ad_audience_segment_link_input import ExamAdAudienceSegmentLinkInput
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
    api_instance = creative_api.CreativeApi(api_client)
    ad_id = "ad-id_example" # str | The ad identifier.
    exam_ad_audience_segment_link_input = ExamAdAudienceSegmentLinkInput(
        data=ValueResourceOfExamAdAudienceSegmentLinkWrite(
            attributes=ExamAdAudienceSegmentLinkWrite(
                audience_segment_id="audience_segment_id_example",
            ),
            type="type_example",
        ),
    ) # ExamAdAudienceSegmentLinkInput | The audience segment link information.

    # example passing only required values which don't have defaults set
    try:
        # /preview/marketing-solutions/ads/{ad-id}/audience-segment
        api_response = api_instance.link_ad_segment(ad_id, exam_ad_audience_segment_link_input)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CreativeApi->link_ad_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_id** | **str**| The ad identifier. |
 **exam_ad_audience_segment_link_input** | [**ExamAdAudienceSegmentLinkInput**](ExamAdAudienceSegmentLinkInput.md)| The audience segment link information. |

### Return type

[**ValueResourceOutcomeOfExamAdAudienceSegmentLink**](ValueResourceOutcomeOfExamAdAudienceSegmentLink.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The link between the Ad and the Audience Segment is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

