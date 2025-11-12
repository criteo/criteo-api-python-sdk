# criteo_api_retailmedia_preview.CatalogApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_load_v1**](CatalogApi.md#offer_load_v1) | **POST** /preview/retail-media/retailers/{retailerId}/offers/load | 
[**offer_set_bbw_v1**](CatalogApi.md#offer_set_bbw_v1) | **POST** /preview/retail-media/retailers/{retailerId}/offers/set-buy-box-winners | 
[**offer_update_v1**](CatalogApi.md#offer_update_v1) | **POST** /preview/retail-media/retailers/{retailerId}/offers/update | 
[**preview_retail_media_catalog_products_batch_post**](CatalogApi.md#preview_retail_media_catalog_products_batch_post) | **POST** /preview/retail-media/catalog/products/batch | 
[**preview_retail_media_catalog_products_batch_report_operation_token_get**](CatalogApi.md#preview_retail_media_catalog_products_batch_report_operation_token_get) | **GET** /preview/retail-media/catalog/products/batch/report/{operation-token} | 


# **offer_load_v1**
> ValueResourceOutcomeAsyncJobResponse offer_load_v1(retailer_id)



Replace the offers for one or more SKUs with a snapshot of the new offers for each respective SKU

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import catalog_api
from criteo_api_retailmedia_preview.model.value_resource_input_load_sku_offers_request import ValueResourceInputLoadSkuOffersRequest
from criteo_api_retailmedia_preview.model.value_resource_outcome_async_job_response import ValueResourceOutcomeAsyncJobResponse
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
    api_instance = catalog_api.CatalogApi(api_client)
    retailer_id = 1 # int | The retailer for which these offers will be loaded
    value_resource_input_load_sku_offers_request = ValueResourceInputLoadSkuOffersRequest(
        data=ValueResourceLoadSkuOffersRequest(
            attributes=LoadSkuOffersRequest(
                sku_offer_loads=[
                    SkuOfferLoad(
                        buy_box_winner="buy_box_winner_example",
                        offers=[
                            OfferLoad(
                                availability="OutOfStock",
                                offer_type="Seller",
                                price=3.14,
                                seller_id="seller_id_example",
                            ),
                        ],
                        sku_id="sku_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputLoadSkuOffersRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.offer_load_v1(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->offer_load_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.offer_load_v1(retailer_id, value_resource_input_load_sku_offers_request=value_resource_input_load_sku_offers_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->offer_load_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer for which these offers will be loaded |
 **value_resource_input_load_sku_offers_request** | [**ValueResourceInputLoadSkuOffersRequest**](ValueResourceInputLoadSkuOffersRequest.md)|  | [optional]

### Return type

[**ValueResourceOutcomeAsyncJobResponse**](ValueResourceOutcomeAsyncJobResponse.md)

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

# **offer_set_bbw_v1**
> ValueResourceOutcomeAsyncJobResponse offer_set_bbw_v1(retailer_id, value_resource_input_set_sku_buy_box_winners_request)



Update the buy box winner for one or more SKUs

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import catalog_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_async_job_response import ValueResourceOutcomeAsyncJobResponse
from criteo_api_retailmedia_preview.model.value_resource_input_set_sku_buy_box_winners_request import ValueResourceInputSetSkuBuyBoxWinnersRequest
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
    api_instance = catalog_api.CatalogApi(api_client)
    retailer_id = 1 # int | The retailer for which these buy box winners will be set
    value_resource_input_set_sku_buy_box_winners_request = ValueResourceInputSetSkuBuyBoxWinnersRequest(
        data=ValueResourceSetSkuBuyBoxWinnersRequest(
            attributes=SetSkuBuyBoxWinnersRequest(
                sku_buy_box_winners=[
                    SkuBuyBoxWinner(
                        seller_id="seller_id_example",
                        sku_id="sku_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputSetSkuBuyBoxWinnersRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.offer_set_bbw_v1(retailer_id, value_resource_input_set_sku_buy_box_winners_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->offer_set_bbw_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer for which these buy box winners will be set |
 **value_resource_input_set_sku_buy_box_winners_request** | [**ValueResourceInputSetSkuBuyBoxWinnersRequest**](ValueResourceInputSetSkuBuyBoxWinnersRequest.md)|  |

### Return type

[**ValueResourceOutcomeAsyncJobResponse**](ValueResourceOutcomeAsyncJobResponse.md)

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

# **offer_update_v1**
> ValueResourceOutcomeAsyncJobResponse offer_update_v1(retailer_id)



Update one or more offers by replacing each offer's price and availability with the given values

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import catalog_api
from criteo_api_retailmedia_preview.model.value_resource_outcome_async_job_response import ValueResourceOutcomeAsyncJobResponse
from criteo_api_retailmedia_preview.model.value_resource_input_update_offers_request import ValueResourceInputUpdateOffersRequest
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
    api_instance = catalog_api.CatalogApi(api_client)
    retailer_id = 1 # int | The retailer for which these offers will be updated
    value_resource_input_update_offers_request = ValueResourceInputUpdateOffersRequest(
        data=ValueResourceUpdateOffersRequest(
            attributes=UpdateOffersRequest(
                offer_updates=[
                    OfferUpdate(
                        availability="OutOfStock",
                        price=3.14,
                        seller_id="seller_id_example",
                        sku_id="sku_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputUpdateOffersRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.offer_update_v1(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->offer_update_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.offer_update_v1(retailer_id, value_resource_input_update_offers_request=value_resource_input_update_offers_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->offer_update_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer for which these offers will be updated |
 **value_resource_input_update_offers_request** | [**ValueResourceInputUpdateOffersRequest**](ValueResourceInputUpdateOffersRequest.md)|  | [optional]

### Return type

[**ValueResourceOutcomeAsyncJobResponse**](ValueResourceOutcomeAsyncJobResponse.md)

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

# **preview_retail_media_catalog_products_batch_post**
> BatchAcceptedResponse preview_retail_media_catalog_products_batch_post(products_custom_batch_request)



Used to publish a batch of operations to insert, update and deletes products.  The batch is processed asynchronously.The response provides an operationToken which can be used to track  the status of the report of the operation.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import catalog_api
from criteo_api_retailmedia_preview.model.batch_accepted_response import BatchAcceptedResponse
from criteo_api_retailmedia_preview.model.products_custom_batch_request import ProductsCustomBatchRequest
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
    api_instance = catalog_api.CatalogApi(api_client)
    products_custom_batch_request = ProductsCustomBatchRequest(
        entries=[
            ProductsCustomBatchRequestEntry(
                batch_id=1,
                feed_id="feed_id_example",
                item_group_id="item_group_id_example",
                merchant_id=1,
                method="delete",
                product=Product(
                    additional_image_links=[
                        "additional_image_links_example",
                    ],
                    ads_grouping="ads_grouping_example",
                    ads_labels=[
                        "ads_labels_example",
                    ],
                    ads_redirect="ads_redirect_example",
                    adult=True,
                    age_group="age_group_example",
                    availability="availability_example",
                    availability_date="availability_date_example",
                    badge="badge_example",
                    brand="brand_example",
                    channel="online",
                    color="color_example",
                    condition="condition_example",
                    content_language="content_language_example",
                    cost_of_goods_sold=Price(
                        currency="currency_example",
                        value="value_example",
                    ),
                    custom_attributes=[
                        CustomAttribute(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    custom_label0="custom_label0_example",
                    custom_label1="custom_label1_example",
                    custom_label2="custom_label2_example",
                    custom_label3="custom_label3_example",
                    custom_label4="custom_label4_example",
                    description="description_example",
                    display_ads_id="display_ads_id_example",
                    display_ads_link="display_ads_link_example",
                    display_ads_similar_ids=[
                        "display_ads_similar_ids_example",
                    ],
                    display_ads_title="display_ads_title_example",
                    display_ads_value=3.14,
                    energy_efficiency_class="energy_efficiency_class_example",
                    excluded_destinations=[
                        "excluded_destinations_example",
                    ],
                    expiration_date="expiration_date_example",
                    external_seller_id="external_seller_id_example",
                    external_seller_name="external_seller_name_example",
                    gender="gender_example",
                    google_product_category="google_product_category_example",
                    gtin="gtin_example",
                    id="id_example",
                    identifier_exists=True,
                    image_link="image_link_example",
                    included_destinations=[
                        "included_destinations_example",
                    ],
                    installment=Installment(
                        amount=Price(
                            currency="currency_example",
                            value="value_example",
                        ),
                        months=1,
                    ),
                    is_bundle=True,
                    item_group_id="item_group_id_example",
                    kind="kind_example",
                    link="link_example",
                    loyalty_points=LoyaltyPoints(
                        name="name_example",
                        points_value=1,
                        ratio=3.14,
                    ),
                    material="material_example",
                    max_energy_efficiency_class="max_energy_efficiency_class_example",
                    max_handling_time=1,
                    min_energy_efficiency_class="min_energy_efficiency_class_example",
                    min_handling_time=1,
                    mobile_link="mobile_link_example",
                    mpn="mpn_example",
                    multipack=1,
                    number_of_reviews=1,
                    offer_id="offer_id_example",
                    pattern="pattern_example",
                    price=Price(
                        currency="currency_example",
                        value="value_example",
                    ),
                    product_rating="product_rating_example",
                    product_type_keys=[
                        "product_type_keys_example",
                    ],
                    product_types=[
                        "product_types_example",
                    ],
                    promotion_ids=[
                        "promotion_ids_example",
                    ],
                    sale_price=Price(
                        currency="currency_example",
                        value="value_example",
                    ),
                    sale_price_effective_date="sale_price_effective_date_example",
                    seller_id="seller_id_example",
                    sell_on_google_quantity=1,
                    shipping=[
                        ProductShipping(
                            country="country_example",
                            location_group_name="location_group_name_example",
                            location_id=1,
                            postal_code="postal_code_example",
                            price=Price(
                                currency="currency_example",
                                value="value_example",
                            ),
                            region="region_example",
                            service="service_example",
                        ),
                    ],
                    shipping_height=ProductShippingDimension(
                        unit="unit_example",
                        value=3.14,
                    ),
                    shipping_label="shipping_label_example",
                    shipping_length=ProductShippingDimension(
                        unit="unit_example",
                        value=3.14,
                    ),
                    shipping_weight=ProductShippingWeight(
                        unit="unit_example",
                        value=3.14,
                    ),
                    shipping_width=ProductShippingDimension(
                        unit="unit_example",
                        value=3.14,
                    ),
                    sizes=[
                        "sizes_example",
                    ],
                    size_system="size_system_example",
                    size_type="size_type_example",
                    source="source_example",
                    target_country="target_country_example",
                    tax_category="tax_category_example",
                    taxes=[
                        ProductTax(
                            country="country_example",
                            location_id=1,
                            postal_code="postal_code_example",
                            rate=3.14,
                            region="region_example",
                            tax_ship=True,
                        ),
                    ],
                    title="title_example",
                    transit_time_label="transit_time_label_example",
                    unit_pricing_base_measure=ProductUnitPricingBaseMeasure(
                        unit="unit_example",
                        value=1,
                    ),
                    unit_pricing_measure=ProductUnitPricingMeasure(
                        unit="unit_example",
                        value=3.14,
                    ),
                ),
                product_id="product_id_example",
            ),
        ],
    ) # ProductsCustomBatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_catalog_products_batch_post(products_custom_batch_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->preview_retail_media_catalog_products_batch_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **products_custom_batch_request** | [**ProductsCustomBatchRequest**](ProductsCustomBatchRequest.md)|  |

### Return type

[**BatchAcceptedResponse**](BatchAcceptedResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch accepted. The status of the operation can be tracked using the report endpoint and the operationToken. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_retail_media_catalog_products_batch_report_operation_token_get**
> ReportOkResponse preview_retail_media_catalog_products_batch_report_operation_token_get(operation_token)



Get the report of an asynchronous batch operation previously requested

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import catalog_api
from criteo_api_retailmedia_preview.model.report_ok_response import ReportOkResponse
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
    api_instance = catalog_api.CatalogApi(api_client)
    operation_token = "operation-token_example" # str | The token returned by the batch endpoint.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_retail_media_catalog_products_batch_report_operation_token_get(operation_token)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CatalogApi->preview_retail_media_catalog_products_batch_report_operation_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_token** | **str**| The token returned by the batch endpoint. |

### Return type

[**ReportOkResponse**](ReportOkResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The report object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

