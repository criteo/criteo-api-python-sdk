# criteo_api_retailmedia_v2027_01.CatalogApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_store_inventory_per_merchant_id**](CatalogApi.md#delete_store_inventory_per_merchant_id) | **POST** /2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/delete | /2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/delete
[**upsert_store_inventory_per_merchant_id**](CatalogApi.md#upsert_store_inventory_per_merchant_id) | **POST** /2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert | /2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert


# **delete_store_inventory_per_merchant_id**
> delete_store_inventory_per_merchant_id(merchant_id, batch_store_inventory_delete_request)

/2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/delete

Used to publish a batch of store inventories to delete. The batch is processed asynchronously.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import catalog_api
from criteo_api_retailmedia_v2027_01.model.batch_store_inventory_delete_request import BatchStoreInventoryDeleteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    merchant_id = "merchantId_example" # str | Identifies the merchant, can also be called partnerId
    batch_store_inventory_delete_request = BatchStoreInventoryDeleteRequest(
        data=[
            DeleteEntry(
                attributes=StoreInventoryDelete(
                    batch_id="batch_id_example",
                    product_id="product_id_example",
                    store_id="store_id_example",
                ),
                type="Delete",
            ),
        ],
    ) # BatchStoreInventoryDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/delete
        api_instance.delete_store_inventory_per_merchant_id(merchant_id, batch_store_inventory_delete_request)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling CatalogApi->delete_store_inventory_per_merchant_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Identifies the merchant, can also be called partnerId |
 **batch_store_inventory_delete_request** | [**BatchStoreInventoryDeleteRequest**](BatchStoreInventoryDeleteRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Batch accepted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_store_inventory_per_merchant_id**
> upsert_store_inventory_per_merchant_id(merchant_id, batch_store_inventory_request)

/2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert

Used to publish a batch of store inventories to upsert. The batch is processed asynchronously.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_v2027_01
from criteo_api_retailmedia_v2027_01.api import catalog_api
from criteo_api_retailmedia_v2027_01.model.batch_store_inventory_request import BatchStoreInventoryRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_v2027_01.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_v2027_01.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_api.CatalogApi(api_client)
    merchant_id = "merchantId_example" # str | Identifies the merchant, can also be called partnerId
    batch_store_inventory_request = BatchStoreInventoryRequest(
        data=[
            InsertEntry(
                attributes=StoreInventoryUpsert(
                    availability="backorder",
                    batch_id="batch_id_example",
                    price="price_example",
                    product_id="product_id_example",
                    sale_price="sale_price_example",
                    store_id="store_id_example",
                ),
                type="Upsert",
            ),
        ],
    ) # BatchStoreInventoryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # /2027-01/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert
        api_instance.upsert_store_inventory_per_merchant_id(merchant_id, batch_store_inventory_request)
    except criteo_api_retailmedia_v2027_01.ApiException as e:
        print("Exception when calling CatalogApi->upsert_store_inventory_per_merchant_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Identifies the merchant, can also be called partnerId |
 **batch_store_inventory_request** | [**BatchStoreInventoryRequest**](BatchStoreInventoryRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Batch accepted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

