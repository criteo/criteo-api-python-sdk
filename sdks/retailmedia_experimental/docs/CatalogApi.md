# criteo_api_retailmedia_experimental.CatalogApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_ingestion_report_summary**](CatalogApi.md#get_catalog_ingestion_report_summary) | **GET** /experimental/retail-media/catalog/ingestion/{ingestion-id}/reports/summary | /experimental/retail-media/catalog/ingestion/{ingestion-id}/reports/summary
[**get_catalog_ingestion_reports**](CatalogApi.md#get_catalog_ingestion_reports) | **GET** /experimental/retail-media/catalog/merchants/{merchant-id}/ingestion/reports | /experimental/retail-media/catalog/merchants/{merchant-id}/ingestion/reports
[**get_catalog_products_batch_report**](CatalogApi.md#get_catalog_products_batch_report) | **GET** /experimental/retail-media/catalog/products/batch/report/{operation-token} | /experimental/retail-media/catalog/products/batch/report/{operation-token}
[**offer_set_bbw_v1**](CatalogApi.md#offer_set_bbw_v1) | **POST** /experimental/retail-media/retailers/{retailer-id}/products/set-buy-box-winners | /experimental/retail-media/retailers/{retailer-id}/products/set-buy-box-winners
[**offer_update_v1**](CatalogApi.md#offer_update_v1) | **POST** /experimental/retail-media/retailers/{retailer-id}/offers/update | /experimental/retail-media/retailers/{retailer-id}/offers/update
[**submit_catalog_products_batch**](CatalogApi.md#submit_catalog_products_batch) | **POST** /experimental/retail-media/catalog/products/batch | /experimental/retail-media/catalog/products/batch


# **get_catalog_ingestion_report_summary**
> CatalogIngestionSummaryResponse get_catalog_ingestion_report_summary(ingestion_id)

/experimental/retail-media/catalog/ingestion/{ingestion-id}/reports/summary

Get the summary report of a catalog ingestion: what triggered it, how long it ran, how many offers it held, what it changed and how clean the data was.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import catalog_api
from criteo_api_retailmedia_experimental.model.catalog_ingestion_summary_response import CatalogIngestionSummaryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    ingestion_id = "ingestion-id_example" # str | Identifies the catalog ingestion to report on.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/catalog/ingestion/{ingestion-id}/reports/summary
        api_response = api_instance.get_catalog_ingestion_report_summary(ingestion_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_ingestion_report_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestion_id** | **str**| Identifies the catalog ingestion to report on. |

### Return type

[**CatalogIngestionSummaryResponse**](CatalogIngestionSummaryResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The summary report of the ingestion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_ingestion_reports**
> CatalogIngestionReportListResponse get_catalog_ingestion_reports(merchant_id)

/experimental/retail-media/catalog/merchants/{merchant-id}/ingestion/reports

List the catalog ingestions of a merchant, most recent first, with their type, status and timing.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import catalog_api
from criteo_api_retailmedia_experimental.model.catalog_ingestion_report_list_response import CatalogIngestionReportListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    merchant_id = "merchant-id_example" # str | Identifies the merchant whose catalog ingestions are reported.
    limit = 25 # int | Maximum number of ingestion reports returned in the page. (optional) if omitted the server will use the default value of 25
    offset = 0 # int | Index of the first ingestion report of the page, used to page through the collection. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/catalog/merchants/{merchant-id}/ingestion/reports
        api_response = api_instance.get_catalog_ingestion_reports(merchant_id)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_ingestion_reports: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/retail-media/catalog/merchants/{merchant-id}/ingestion/reports
        api_response = api_instance.get_catalog_ingestion_reports(merchant_id, limit=limit, offset=offset)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_ingestion_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Identifies the merchant whose catalog ingestions are reported. |
 **limit** | **int**| Maximum number of ingestion reports returned in the page. | [optional] if omitted the server will use the default value of 25
 **offset** | **int**| Index of the first ingestion report of the page, used to page through the collection. | [optional] if omitted the server will use the default value of 0

### Return type

[**CatalogIngestionReportListResponse**](CatalogIngestionReportListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The page of catalog ingestion reports. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_products_batch_report**
> ReportOkResponse get_catalog_products_batch_report(operation_token)

/experimental/retail-media/catalog/products/batch/report/{operation-token}

Get the report of an asynchronous batch operation previously requested

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import catalog_api
from criteo_api_retailmedia_experimental.model.report_ok_response import ReportOkResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    operation_token = "operation-token_example" # str | The token returned by the batch endpoint.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/catalog/products/batch/report/{operation-token}
        api_response = api_instance.get_catalog_products_batch_report(operation_token)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

# **offer_set_bbw_v1**
> Outcome offer_set_bbw_v1(retailer_id, value_resource_input_set_product_buy_box_winners_request)

/experimental/retail-media/retailers/{retailer-id}/products/set-buy-box-winners

Update the buy box winner for one or more products

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import catalog_api
from criteo_api_retailmedia_experimental.model.value_resource_input_set_product_buy_box_winners_request import ValueResourceInputSetProductBuyBoxWinnersRequest
from criteo_api_retailmedia_experimental.model.outcome import Outcome
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer for which these buy box winners will be set
    value_resource_input_set_product_buy_box_winners_request = ValueResourceInputSetProductBuyBoxWinnersRequest(
        data=ValueResourceSetProductBuyBoxWinnersRequest(
            attributes=SetProductBuyBoxWinnersRequest(
                product_buy_box_winners=[
                    ProductBuyBoxWinner(
                        offer_id="offer_id_example",
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputSetProductBuyBoxWinnersRequest | Updated buy box winners for one or more products

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/retailers/{retailer-id}/products/set-buy-box-winners
        api_response = api_instance.offer_set_bbw_v1(retailer_id, value_resource_input_set_product_buy_box_winners_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CatalogApi->offer_set_bbw_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer for which these buy box winners will be set |
 **value_resource_input_set_product_buy_box_winners_request** | [**ValueResourceInputSetProductBuyBoxWinnersRequest**](ValueResourceInputSetProductBuyBoxWinnersRequest.md)| Updated buy box winners for one or more products |

### Return type

[**Outcome**](Outcome.md)

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
> Outcome offer_update_v1(retailer_id, value_resource_input_update_offers_request)

/experimental/retail-media/retailers/{retailer-id}/offers/update

Update one or more offers by replacing each offer's price and availability with the given values

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import catalog_api
from criteo_api_retailmedia_experimental.model.outcome import Outcome
from criteo_api_retailmedia_experimental.model.value_resource_input_update_offers_request import ValueResourceInputUpdateOffersRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer for which these offers will be updated
    value_resource_input_update_offers_request = ValueResourceInputUpdateOffersRequest(
        data=ValueResourceUpdateOffersRequest(
            attributes=UpdateOffersRequest(
                offer_updates=[
                    OfferUpdate(
                        availability="outOfStock",
                        offer_id="offer_id_example",
                        price=3.14,
                    ),
                ],
            ),
            type="type_example",
        ),
    ) # ValueResourceInputUpdateOffersRequest | Collection of offer price and availability updates to be applied.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/retailers/{retailer-id}/offers/update
        api_response = api_instance.offer_update_v1(retailer_id, value_resource_input_update_offers_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling CatalogApi->offer_update_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer for which these offers will be updated |
 **value_resource_input_update_offers_request** | [**ValueResourceInputUpdateOffersRequest**](ValueResourceInputUpdateOffersRequest.md)| Collection of offer price and availability updates to be applied. |

### Return type

[**Outcome**](Outcome.md)

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

# **submit_catalog_products_batch**
> BatchAcceptedResponse submit_catalog_products_batch(products_custom_batch_request)

/experimental/retail-media/catalog/products/batch

Used to publish a batch of operations to insert, update and deletes products.  The batch is processed asynchronously.The response provides an operationToken which can be used to track  the status of the report of the operation.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import catalog_api
from criteo_api_retailmedia_experimental.model.products_custom_batch_request import ProductsCustomBatchRequest
from criteo_api_retailmedia_experimental.model.batch_accepted_response import BatchAcceptedResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
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
        # /experimental/retail-media/catalog/products/batch
        api_response = api_instance.submit_catalog_products_batch(products_custom_batch_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
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

