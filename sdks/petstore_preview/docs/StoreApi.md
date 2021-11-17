# criteo_api_petstore_preview.StoreApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order**](StoreApi.md#delete_order) | **DELETE** /store/order/{orderId} | Delete purchase order by ID
[**get_inventory**](StoreApi.md#get_inventory) | **GET** /store/inventory | Returns pet inventories by status
[**get_order_by_id**](StoreApi.md#get_order_by_id) | **GET** /store/order/{orderId} | Find purchase order by ID
[**place_order**](StoreApi.md#place_order) | **POST** /store/order | Place an order for a pet


# **delete_order**
> delete_order(order_id)

Delete purchase order by ID

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import store_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = store_api.StoreApi(api_client)
    order_id = 1 # int | ID of the order that needs to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Delete purchase order by ID
        api_instance.delete_order(order_id)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling StoreApi->delete_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of the order that needs to be deleted |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid ID supplied |  -  |
**404** | Order not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory**
> {str: (int,)} get_inventory()

Returns pet inventories by status

Returns a map of status codes to quantities

### Example

* Api Key Authentication (api_key):
```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import store_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = store_api.StoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns pet inventories by status
        api_response = api_instance.get_inventory()
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling StoreApi->get_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (int,)}**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> Order get_order_by_id(order_id)

Find purchase order by ID

For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import store_api
from criteo_api_petstore_preview.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = store_api.StoreApi(api_client)
    order_id = 1 # int | ID of order that needs to be fetched

    # example passing only required values which don't have defaults set
    try:
        # Find purchase order by ID
        api_response = api_instance.get_order_by_id(order_id)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling StoreApi->get_order_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order that needs to be fetched |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Order not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> Order place_order()

Place an order for a pet

Place a new order in the store

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import store_api
from criteo_api_petstore_preview.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = store_api.StoreApi(api_client)
    order = Order(
        id=10,
        pet_id=198772,
        quantity=7,
        ship_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        status="approved",
        complete=True,
    ) # Order |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Place an order for a pet
        api_response = api_instance.place_order(order=order)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling StoreApi->place_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)|  | [optional]

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

