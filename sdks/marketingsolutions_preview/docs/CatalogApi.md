# criteo_api_marketingsolutions_preview.CatalogApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_merchant_stats**](CatalogApi.md#get_catalog_merchant_stats) | **GET** /preview/catalog/stats/merchants/{merchant-id} | 
[**get_catalog_products_batch_report**](CatalogApi.md#get_catalog_products_batch_report) | **GET** /preview/catalog/products/batch/report/{operation-token} | 
[**submit_catalog_products_batch**](CatalogApi.md#submit_catalog_products_batch) | **POST** /preview/catalog/products/batch | 


# **get_catalog_merchant_stats**
> StatisticsOkResponse get_catalog_merchant_stats(merchant_id)



get an stats request

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import catalog_api
from criteo_api_marketingsolutions_preview.model.statistics_ok_response import StatisticsOkResponse
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
    api_instance = catalog_api.CatalogApi(api_client)
    merchant_id = "merchant-id_example" # str | merchant-id to get
    last_num_hours = 1 # int | the last number of hours (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_catalog_merchant_stats(merchant_id)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_merchant_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_catalog_merchant_stats(merchant_id, last_num_hours=last_num_hours)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_merchant_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant-id to get |
 **last_num_hours** | **int**| the last number of hours | [optional]

### Return type

[**StatisticsOkResponse**](StatisticsOkResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successful response of GET stats request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_products_batch_report**
> ReportOkResponse get_catalog_products_batch_report(operation_token)



Get the report of an asynchronous batch operation previously requested

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import catalog_api
from criteo_api_marketingsolutions_preview.model.report_ok_response import ReportOkResponse
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
    api_instance = catalog_api.CatalogApi(api_client)
    operation_token = "operation-token_example" # str | The token returned by the batch endpoint.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_catalog_products_batch_report(operation_token)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_products_batch_report: %s\n" % e)
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

# **submit_catalog_products_batch**
> BatchAcceptedResponse submit_catalog_products_batch(products_custom_batch_request)



Used to publish a batch of operations to insert, update and deletes products.  The batch is processed asynchronously.The response provides an operationToken which can be used to track  the status of the report of the operation.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_marketingsolutions_preview
from criteo_api_marketingsolutions_preview.api import catalog_api
from criteo_api_marketingsolutions_preview.model.batch_accepted_response import BatchAcceptedResponse
from criteo_api_marketingsolutions_preview.model.products_custom_batch_request import ProductsCustomBatchRequest
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
                    filters={
                        "key": [
                            "key_example",
                        ],
                    },
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
        api_response = api_instance.submit_catalog_products_batch(products_custom_batch_request)
        pprint(api_response)
    except criteo_api_marketingsolutions_preview.ApiException as e:
        print("Exception when calling CatalogApi->submit_catalog_products_batch: %s\n" % e)
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

