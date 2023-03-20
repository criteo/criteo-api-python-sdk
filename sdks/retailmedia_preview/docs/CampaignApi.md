# criteo_api_retailmedia_preview.CampaignApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_keywords**](CampaignApi.md#add_remove_keywords) | **POST** /preview/retail-media/line-items/{id}/keywords/add-remove | 
[**delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **DELETE** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**delete_api_v1_external_balance_campaigns_by_balance_id**](CampaignApi.md#delete_api_v1_external_balance_campaigns_by_balance_id) | **DELETE** /preview/retail-media/balances/{balanceId}/campaigns | 
[**delete_api_v1_external_line_item_products_by_line_item_id**](CampaignApi.md#delete_api_v1_external_line_item_products_by_line_item_id) | **DELETE** /preview/retail-media/line-items/{lineItemId}/products | 
[**fetch_keywords**](CampaignApi.md#fetch_keywords) | **GET** /preview/retail-media/line-items/{id}/keywords | 
[**fetch_proposal**](CampaignApi.md#fetch_proposal) | **GET** /preview/retail-media/preferred-deal-line-items/{id}/proposal | 
[**get_aip_v1_external_retailer_retailer_cpc_rates_by_retailer_id**](CampaignApi.md#get_aip_v1_external_retailer_retailer_cpc_rates_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/retailer-cpc-rates | 
[**get_api202210_external_account_by_account_id_creativescreative_id**](CampaignApi.md#get_api202210_external_account_by_account_id_creativescreative_id) | **GET** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**get_api202210_external_line_item_product_buttons_by_line_item_id**](CampaignApi.md#get_api202210_external_line_item_product_buttons_by_line_item_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons | 
[**get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **GET** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**get_api202301_external_line_item_bid_multipliers_by_line_item_id**](CampaignApi.md#get_api202301_external_line_item_bid_multipliers_by_line_item_id) | **GET** /preview/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**get_api_v0_external_catalog_output_by_catalog_id**](CampaignApi.md#get_api_v0_external_catalog_output_by_catalog_id) | **GET** /preview/retail-media/catalogs/{catalogId}/output | 
[**get_api_v0_external_catalog_status_by_catalog_id**](CampaignApi.md#get_api_v0_external_catalog_status_by_catalog_id) | **GET** /preview/retail-media/catalogs/{catalogId}/status | 
[**get_api_v1_external_account_balances_by_account_id**](CampaignApi.md#get_api_v1_external_account_balances_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/balances | 
[**get_api_v1_external_account_brands_by_account_id**](CampaignApi.md#get_api_v1_external_account_brands_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/brands | 
[**get_api_v1_external_account_campaigns_by_account_id**](CampaignApi.md#get_api_v1_external_account_campaigns_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/campaigns | 
[**get_api_v1_external_account_retailers_by_account_id**](CampaignApi.md#get_api_v1_external_account_retailers_by_account_id) | **GET** /preview/retail-media/accounts/{accountId}/retailers | 
[**get_api_v1_external_accounts**](CampaignApi.md#get_api_v1_external_accounts) | **GET** /preview/retail-media/accounts | 
[**get_api_v1_external_balance_campaigns_by_balance_id**](CampaignApi.md#get_api_v1_external_balance_campaigns_by_balance_id) | **GET** /preview/retail-media/balances/{balanceId}/campaigns | 
[**get_api_v1_external_campaign_by_campaign_id**](CampaignApi.md#get_api_v1_external_campaign_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaignId} | 
[**get_api_v1_external_campaign_line_items_by_campaign_id**](CampaignApi.md#get_api_v1_external_campaign_line_items_by_campaign_id) | **GET** /preview/retail-media/campaigns/{campaignId}/line-items | 
[**get_api_v1_external_line_item_by_line_item_id**](CampaignApi.md#get_api_v1_external_line_item_by_line_item_id) | **GET** /preview/retail-media/line-items/{lineItemId} | 
[**get_api_v1_external_line_item_products_by_line_item_id**](CampaignApi.md#get_api_v1_external_line_item_products_by_line_item_id) | **GET** /preview/retail-media/line-items/{lineItemId}/products | 
[**get_api_v1_external_retailer_brands_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_brands_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailerId}/brands | 
[**get_api_v1_external_retailer_by_retailer_id_seller_by_seller**](CampaignApi.md#get_api_v1_external_retailer_by_retailer_id_seller_by_seller) | **GET** /preview/retail-media/retailers/{retailerId}/sellers/{seller} | 
[**get_api_v1_external_retailer_category_cpc_rates_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_category_cpc_rates_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/category-cpc-rates | 
[**get_api_v1_external_retailer_placements_by_retailer_id**](CampaignApi.md#get_api_v1_external_retailer_placements_by_retailer_id) | **GET** /preview/retail-media/retailers/{retailer-id}/placements | 
[**post_api202210_external_account_creatives_by_account_id**](CampaignApi.md#post_api202210_external_account_creatives_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/creatives | 
[**post_api202210_external_account_creatives_search_by_account_id**](CampaignApi.md#post_api202210_external_account_creatives_search_by_account_id) | **POST** /preview/retail-media/accounts/{account-id}/creatives/search | 
[**post_api202210_external_line_item_product_buttons_create_by_line_item_id**](CampaignApi.md#post_api202210_external_line_item_product_buttons_create_by_line_item_id) | **POST** /preview/retail-media/line-items/{line-item-id}/product-buttons/create | 
[**post_api_v0_external_account_catalogs_by_account_id**](CampaignApi.md#post_api_v0_external_account_catalogs_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/catalogs | 
[**post_api_v1_external_account_campaigns_by_account_id**](CampaignApi.md#post_api_v1_external_account_campaigns_by_account_id) | **POST** /preview/retail-media/accounts/{accountId}/campaigns | 
[**post_api_v1_external_campaign_line_items_by_campaign_id**](CampaignApi.md#post_api_v1_external_campaign_line_items_by_campaign_id) | **POST** /preview/retail-media/campaigns/{campaignId}/line-items | 
[**post_api_v1_external_catalogs_sku_retrieval**](CampaignApi.md#post_api_v1_external_catalogs_sku_retrieval) | **POST** /preview/retail-media/catalogs/sku-retrieval | 
[**post_api_v1_external_catalogs_sku_search**](CampaignApi.md#post_api_v1_external_catalogs_sku_search) | **POST** /preview/retail-media/catalogs/sku-search | 
[**put_api202210_external_account_by_account_id_creativescreative_id**](CampaignApi.md#put_api202210_external_account_by_account_id_creativescreative_id) | **PUT** /preview/retail-media/accounts/{account-id}/creatives/{creative-id} | 
[**put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**](CampaignApi.md#put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id) | **PUT** /preview/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | 
[**put_api202301_external_line_item_bid_multipliers_by_line_item_id**](CampaignApi.md#put_api202301_external_line_item_bid_multipliers_by_line_item_id) | **PUT** /preview/retail-media/line-items/{line-item-id}/bid-multipliers | 
[**put_api_v1_external_balance_campaigns_by_balance_id**](CampaignApi.md#put_api_v1_external_balance_campaigns_by_balance_id) | **PUT** /preview/retail-media/balances/{balanceId}/campaigns | 
[**put_api_v1_external_campaign_by_campaign_id**](CampaignApi.md#put_api_v1_external_campaign_by_campaign_id) | **PUT** /preview/retail-media/campaigns/{campaignId} | 
[**put_api_v1_external_line_item_by_line_item_id**](CampaignApi.md#put_api_v1_external_line_item_by_line_item_id) | **PUT** /preview/retail-media/line-items/{lineItemId} | 
[**put_api_v1_external_line_item_products_by_line_item_id**](CampaignApi.md#put_api_v1_external_line_item_products_by_line_item_id) | **PUT** /preview/retail-media/line-items/{lineItemId}/products | 
[**set_keyword_bids**](CampaignApi.md#set_keyword_bids) | **POST** /preview/retail-media/line-items/{id}/keywords/set-bid | 
[**submit_proposal**](CampaignApi.md#submit_proposal) | **POST** /preview/retail-media/preferred-deal-line-items/{id}/proposal/submit | 


# **add_remove_keywords**
> RetailMediaExternalv1ResourceOutcome add_remove_keywords(id)



Add or Remove keywords from the associated line item in bulk

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.retail_media_externalv1_resource_outcome import RetailMediaExternalv1ResourceOutcome
from criteo_api_retailmedia_preview.model.retail_media_externalv1_add_remove_keywords_model_request import RetailMediaExternalv1AddRemoveKeywordsModelRequest
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | Long external id of the associated line item
    retail_media_externalv1_add_remove_keywords_model_request = RetailMediaExternalv1AddRemoveKeywordsModelRequest(
        data=RetailMediaExternalv1AddRemoveKeywordsModelResource(
            id="id_example",
            type="type_example",
            attributes=RetailMediaExternalv1AddRemoveKeywordsModel(
                keywords=[
                    RetailMediaExternalv1AddRemoveKeywordModel(
                        phrase="phrase_example",
                        match_type="PositiveExactMatch",
                        is_deleted=True,
                    ),
                ],
            ),
        ),
    ) # RetailMediaExternalv1AddRemoveKeywordsModelRequest | Object containing keywords to be added or removed (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_remove_keywords(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->add_remove_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_remove_keywords(id, retail_media_externalv1_add_remove_keywords_model_request=retail_media_externalv1_add_remove_keywords_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->add_remove_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Long external id of the associated line item |
 **retail_media_externalv1_add_remove_keywords_model_request** | [**RetailMediaExternalv1AddRemoveKeywordsModelRequest**](RetailMediaExternalv1AddRemoveKeywordsModelRequest.md)| Object containing keywords to be added or removed | [optional]

### Return type

[**RetailMediaExternalv1ResourceOutcome**](RetailMediaExternalv1ResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**
> delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)



Delete a product button

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_id = "product-button-id_example" # str | Sequential id of the product button

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_id** | **str**| Sequential id of the product button |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_v1_external_balance_campaigns_by_balance_id**
> PageOfBalanceCampaign delete_api_v1_external_balance_campaigns_by_balance_id(balance_id)



Removes one or more campaigns on the specified balance

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.page_of_balance_campaign import PageOfBalanceCampaign
from criteo_api_retailmedia_preview.model.json_api_data_request_of_delete_balance_campaign import JsonApiDataRequestOfDeleteBalanceCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balanceId_example" # str | The balance to remove campaigns from
    json_api_data_request_of_delete_balance_campaign = JsonApiDataRequestOfDeleteBalanceCampaign(
        data=[
            ExternalDeleteBalanceCampaign(
                type="type_example",
                id="id_example",
                attributes={},
            ),
        ],
    ) # JsonApiDataRequestOfDeleteBalanceCampaign | The campaigns to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_api_v1_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_api_v1_external_balance_campaigns_by_balance_id(balance_id, json_api_data_request_of_delete_balance_campaign=json_api_data_request_of_delete_balance_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to remove campaigns from |
 **json_api_data_request_of_delete_balance_campaign** | [**JsonApiDataRequestOfDeleteBalanceCampaign**](JsonApiDataRequestOfDeleteBalanceCampaign.md)| The campaigns to append | [optional]

### Return type

[**PageOfBalanceCampaign**](PageOfBalanceCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_v1_external_line_item_products_by_line_item_id**
> JsonApiPageResponseOfStringAndPromotedProduct delete_api_v1_external_line_item_products_by_line_item_id(line_item_id)



This endpoint removes one or more products from promotion on the specified line item.  The resulting state of the line item is returned.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_data_request_with_id_of_string_and_promoted_product import JsonApiDataRequestWithIdOfStringAndPromotedProduct
from criteo_api_retailmedia_preview.model.json_api_page_response_of_string_and_promoted_product import JsonApiPageResponseOfStringAndPromotedProduct
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item to interact with
    json_api_data_request_with_id_of_string_and_promoted_product = JsonApiDataRequestWithIdOfStringAndPromotedProduct(
        data=[
            JsonApiBodyWithIdOfStringAndPromotedProductAndPromotedProduct(
                id="id_example",
                type="type_example",
                attributes=ExternalPromotedProduct(
                    bid_override=3.14,
                ),
            ),
        ],
    ) # JsonApiDataRequestWithIdOfStringAndPromotedProduct |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_api_v1_external_line_item_products_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_api_v1_external_line_item_products_by_line_item_id(line_item_id, json_api_data_request_with_id_of_string_and_promoted_product=json_api_data_request_with_id_of_string_and_promoted_product)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->delete_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **json_api_data_request_with_id_of_string_and_promoted_product** | [**JsonApiDataRequestWithIdOfStringAndPromotedProduct**](JsonApiDataRequestWithIdOfStringAndPromotedProduct.md)|  | [optional]

### Return type

[**JsonApiPageResponseOfStringAndPromotedProduct**](JsonApiPageResponseOfStringAndPromotedProduct.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_keywords**
> RetailMediaExternalv1KeywordsModelResponse fetch_keywords(id)



Fetch keywords associated with the specified line item

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.retail_media_externalv1_keywords_model_response import RetailMediaExternalv1KeywordsModelResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | Long external id of the associated line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_keywords(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Long external id of the associated line item |

### Return type

[**RetailMediaExternalv1KeywordsModelResponse**](RetailMediaExternalv1KeywordsModelResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_proposal**
> RetailMediaExternalv1ProposalStatusModelResponse fetch_proposal(id)



Fetch the status of a proposal to modify a Preferred Deal Line Item.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.retail_media_externalv1_proposal_status_model_response import RetailMediaExternalv1ProposalStatusModelResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | The external id of a line item.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_proposal(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->fetch_proposal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The external id of a line item. |

### Return type

[**RetailMediaExternalv1ProposalStatusModelResponse**](RetailMediaExternalv1ProposalStatusModelResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aip_v1_external_retailer_retailer_cpc_rates_by_retailer_id**
> RetailerCpcRateCardPreviewResponse get_aip_v1_external_retailer_retailer_cpc_rates_by_retailer_id(retailer_id)



Gets the minimum cpc bid for a retailer

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.retailer_cpc_rate_card_preview_response import RetailerCpcRateCardPreviewResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aip_v1_external_retailer_retailer_cpc_rates_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_aip_v1_external_retailer_retailer_cpc_rates_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer id |

### Return type

[**RetailerCpcRateCardPreviewResponse**](RetailerCpcRateCardPreviewResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bids found |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202210_external_account_by_account_id_creativescreative_id**
> Creative202210Response get_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Get the specified creative

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative202210_response import Creative202210Response
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_id = "creative-id_example" # str | Creative to get

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api202210_external_account_by_account_id_creativescreative_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to retrieve creatives for |
 **creative_id** | **str**| Creative to get |

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202210_external_line_item_product_buttons_by_line_item_id**
> ProductButtonListResponse get_api202210_external_line_item_product_buttons_by_line_item_id(line_item_id)



Get all the product buttons associated with a line item

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202210_external_line_item_product_buttons_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api202210_external_line_item_product_buttons_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |

### Return type

[**ProductButtonListResponse**](ProductButtonListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**
> ProductButtonResponse get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)



Get a single product button

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_response import ProductButtonResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_id = "product-button-id_example" # str | Sequential id of the product button

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_id** | **str**| Sequential id of the product button |

### Return type

[**ProductButtonResponse**](ProductButtonResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api202301_external_line_item_bid_multipliers_by_line_item_id**
> JsonApiSingleResponseOfLineItemBidMultipliers get_api202301_external_line_item_bid_multipliers_by_line_item_id(line_item_id)



Get bid multipliers by line item

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item_bid_multipliers import JsonApiSingleResponseOfLineItemBidMultipliers
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api202301_external_line_item_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api202301_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |

### Return type

[**JsonApiSingleResponseOfLineItemBidMultipliers**](JsonApiSingleResponseOfLineItemBidMultipliers.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v0_external_catalog_output_by_catalog_id**
> get_api_v0_external_catalog_output_by_catalog_id(catalog_id)



Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream of CatalogProduct json objects.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_api_v0_external_catalog_output_by_catalog_id(catalog_id)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v0_external_catalog_output_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-json-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog download initiated. |  -  |
**400** | The indicated catalog is not available for retrieval, wait for a success status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v0_external_catalog_status_by_catalog_id**
> JsonApiSingleResponseOfCatalogStatus get_api_v0_external_catalog_status_by_catalog_id(catalog_id)



Check the status of a catalog request.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    catalog_id = "catalogId_example" # str | A catalog ID returned from an account catalog request.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v0_external_catalog_status_by_catalog_id(catalog_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v0_external_catalog_status_by_catalog_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| A catalog ID returned from an account catalog request. |

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_account_balances_by_account_id**
> JsonApiPageResponseOfBalance get_api_v1_external_account_balances_by_account_id(account_id)



Gets page of balance objects for the given account id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_balance import JsonApiPageResponseOfBalance
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to get balances for
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_balances_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_balances_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_balances_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_balances_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to get balances for |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfBalance**](JsonApiPageResponseOfBalance.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_account_brands_by_account_id**
> JsonApiPageResponseOfBrand get_api_v1_external_account_brands_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_brands_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_brands_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_brands_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_brands_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfBrand**](JsonApiPageResponseOfBrand.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_account_campaigns_by_account_id**
> JsonApiPageResponseOfCampaign get_api_v1_external_account_campaigns_by_account_id(account_id)



Gets page of campaign objects for the given account id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_campaign import JsonApiPageResponseOfCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_campaigns_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfCampaign**](JsonApiPageResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_account_retailers_by_account_id**
> JsonApiPageResponseOfRetailer get_api_v1_external_account_retailers_by_account_id(account_id)



Gets page of retailer objects that are associated with the given account

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_account_retailers_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_retailers_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_account_retailers_by_account_id(account_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_account_retailers_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfRetailer**](JsonApiPageResponseOfRetailer.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_accounts**
> JsonApiPageResponseOfAccount get_api_v1_external_accounts()



Gets page of account objects that the current user can access

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_accounts(limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfAccount**](JsonApiPageResponseOfAccount.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_balance_campaigns_by_balance_id**
> PageOfBalanceCampaign get_api_v1_external_balance_campaigns_by_balance_id(balance_id)



Gets page of campaigns for the given balanceId

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.page_of_balance_campaign import PageOfBalanceCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balanceId_example" # str | The balance to get campaigns from
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_balance_campaigns_by_balance_id(balance_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to get campaigns from |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**PageOfBalanceCampaign**](PageOfBalanceCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaign get_api_v1_external_campaign_by_campaign_id(campaign_id)



Gets the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |

### Return type

[**JsonApiSingleResponseOfCampaign**](JsonApiSingleResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_campaign_line_items_by_campaign_id**
> JsonApiPageResponseOfLineItem get_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)



Gets page of line item objects for the given campaign id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_line_item import JsonApiPageResponseOfLineItem
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_campaign_line_items_by_campaign_id(campaign_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfLineItem**](JsonApiPageResponseOfLineItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_line_item_by_line_item_id**
> JsonApiSingleResponseOfLineItem get_api_v1_external_line_item_by_line_item_id(line_item_id)



Gets the line item for the given line item id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item import JsonApiSingleResponseOfLineItem
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The given line item id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |

### Return type

[**JsonApiSingleResponseOfLineItem**](JsonApiSingleResponseOfLineItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_line_item_products_by_line_item_id**
> JsonApiPageResponseOfStringAndPromotedProduct get_api_v1_external_line_item_products_by_line_item_id(line_item_id)



This endpoint gets the promoted products on the specified line item.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_page_response_of_string_and_promoted_product import JsonApiPageResponseOfStringAndPromotedProduct
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item to interact with
    limit_to_id = [
        "limitToId_example",
    ] # [str] | The ids that you would like to limit your result set to (optional)
    page_index = 1 # int | The 0 indexed page index you would like to receive given the page size (optional)
    page_size = 1 # int | The maximum number of items you would like to receive in this request (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_line_item_products_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_line_item_products_by_line_item_id(line_item_id, limit_to_id=limit_to_id, page_index=page_index, page_size=page_size)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **limit_to_id** | **[str]**| The ids that you would like to limit your result set to | [optional]
 **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional]
 **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional]

### Return type

[**JsonApiPageResponseOfStringAndPromotedProduct**](JsonApiPageResponseOfStringAndPromotedProduct.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_brands_by_retailer_id**
> BrandPreviewListResponse get_api_v1_external_retailer_brands_by_retailer_id(retailer_id)



Gets the brands for the given retailer

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.brand_preview_list_response import BrandPreviewListResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | The retailer id for which brands should be fetched.
    sku_stock_type_filter = "first-party" # str | Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_api_v1_external_retailer_brands_by_retailer_id(retailer_id, sku_stock_type_filter=sku_stock_type_filter)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_brands_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which brands should be fetched. |
 **sku_stock_type_filter** | **str**| Filter to narrow down brands [first-party|third-party|first-and-third-party]. Defaults to first-and-third-party | [optional]

### Return type

[**BrandPreviewListResponse**](BrandPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Brands found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_by_retailer_id_seller_by_seller**
> SellerPreviewResponse get_api_v1_external_retailer_by_retailer_id_seller_by_seller(retailer_id, seller)



Endpoint to get market place seller id and name

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.seller_preview_response import SellerPreviewResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = 1 # int | The retailer id for which seller should be fetched.
    seller = "seller_example" # str | The seller id or seller name which should be validated.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_by_retailer_id_seller_by_seller(retailer_id, seller)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_by_retailer_id_seller_by_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **int**| The retailer id for which seller should be fetched. |
 **seller** | **str**| The seller id or seller name which should be validated. |

### Return type

[**SellerPreviewResponse**](SellerPreviewResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Seller found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_category_cpc_rates_by_retailer_id**
> CategoryCpcRateCardPreviewListResponse get_api_v1_external_retailer_category_cpc_rates_by_retailer_id(retailer_id)



Gets the minimum cpc bid for all categories for a retailer

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.category_cpc_rate_card_preview_list_response import CategoryCpcRateCardPreviewListResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_category_cpc_rates_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_category_cpc_rates_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer id |

### Return type

[**CategoryCpcRateCardPreviewListResponse**](CategoryCpcRateCardPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bids found |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_external_retailer_placements_by_retailer_id**
> PlacementPreviewListResponse get_api_v1_external_retailer_placements_by_retailer_id(retailer_id)



Gets all placement information for the given retailer

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.placement_preview_list_response import PlacementPreviewListResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    retailer_id = "retailer-id_example" # str | The retailer id for which placements should be fetched.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_v1_external_retailer_placements_by_retailer_id(retailer_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->get_api_v1_external_retailer_placements_by_retailer_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The retailer id for which placements should be fetched. |

### Return type

[**PlacementPreviewListResponse**](PlacementPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | placements records. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api202210_external_account_creatives_by_account_id**
> Creative202210Response post_api202210_external_account_creatives_by_account_id(account_id)



Create a creative for an account

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_preview.model.creative_create_model202207 import CreativeCreateModel202207
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to create a creative for
    creative_create_model202207 = CreativeCreateModel202207(
        name="name_example",
        brand_id=1,
        retailer_id=1,
        template_id=1,
        template_variable_values=[
            TemplateVariableValue(
                id="id_example",
                text_variable_value=TextVariableValue(
                    text="text_example",
                ),
                choice_variable_value=ChoiceVariableValue(
                    chosen_options=[
                        "chosen_options_example",
                    ],
                ),
                color_variable_value=ColorVariableValue(
                    color="#2EC",
                ),
                files_variable_value=FilesVariableValue(
                    asset_ids=[
                        "asset_ids_example",
                    ],
                ),
                hyperlink_variable_value=HyperlinkVariableValue(
                    url="url_example",
                ),
            ),
        ],
    ) # CreativeCreateModel202207 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202210_external_account_creatives_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_account_creatives_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202210_external_account_creatives_by_account_id(account_id, creative_create_model202207=creative_create_model202207)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_account_creatives_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to create a creative for |
 **creative_create_model202207** | [**CreativeCreateModel202207**](CreativeCreateModel202207.md)| The creative to create | [optional]

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creatives created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api202210_external_account_creatives_search_by_account_id**
> Creative202210ListResponse post_api202210_external_account_creatives_search_by_account_id(account_id)



Get account creatives

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative202210_list_response import Creative202210ListResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id to retrieve creatives for
    creative_ids = [
        "creative-ids_example",
    ] # [str] | Creatives to filter by (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202210_external_account_creatives_search_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_account_creatives_search_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202210_external_account_creatives_search_by_account_id(account_id, creative_ids=creative_ids)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_account_creatives_search_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id to retrieve creatives for |
 **creative_ids** | **[str]**| Creatives to filter by | [optional]

### Return type

[**Creative202210ListResponse**](Creative202210ListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api202210_external_line_item_product_buttons_create_by_line_item_id**
> ProductButtonListResponse post_api202210_external_line_item_product_buttons_create_by_line_item_id(line_item_id)



Append new product buttons to a line item

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
from criteo_api_retailmedia_preview.model.product_button_list_request import ProductButtonListRequest
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_list_request = ProductButtonListRequest(
        data=[
            ResourceOfProductButtonRequest(
                attributes=ExternalProductButtonRequest(
                    name="name_example",
                    background_image="background_image_example",
                    is_mandatory=1,
                    skus=[
                        "skus_example",
                    ],
                ),
                id="id_example",
                type="type_example",
            ),
        ],
    ) # ProductButtonListRequest | List of product buttons to append to the specified line item (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api202210_external_line_item_product_buttons_create_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_line_item_product_buttons_create_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api202210_external_line_item_product_buttons_create_by_line_item_id(line_item_id, product_button_list_request=product_button_list_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api202210_external_line_item_product_buttons_create_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_list_request** | [**ProductButtonListRequest**](ProductButtonListRequest.md)| List of product buttons to append to the specified line item | [optional]

### Return type

[**ProductButtonListResponse**](ProductButtonListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v0_external_account_catalogs_by_account_id**
> JsonApiSingleResponseOfCatalogStatus post_api_v0_external_account_catalogs_by_account_id(account_id)



Create a request for a Catalog available to the indicated account.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_request_of_catalog_request_preview import JsonApiRequestOfCatalogRequestPreview
from criteo_api_retailmedia_preview.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The account to request the catalog for.
    json_api_request_of_catalog_request_preview = JsonApiRequestOfCatalogRequestPreview(
        data=JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequestPreview(
            type="type_example",
            attributes=ExternalCatalogRequestPreview(
                format="json-newline",
            ),
        ),
    ) # JsonApiRequestOfCatalogRequestPreview |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v0_external_account_catalogs_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v0_external_account_catalogs_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v0_external_account_catalogs_by_account_id(account_id, json_api_request_of_catalog_request_preview=json_api_request_of_catalog_request_preview)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v0_external_account_catalogs_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account to request the catalog for. |
 **json_api_request_of_catalog_request_preview** | [**JsonApiRequestOfCatalogRequestPreview**](JsonApiRequestOfCatalogRequestPreview.md)|  | [optional]

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalog request successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_account_campaigns_by_account_id**
> JsonApiSingleResponseOfCampaign post_api_v1_external_account_campaigns_by_account_id(account_id)



Creates a new campaign with the specified settings

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from criteo_api_retailmedia_preview.model.external_post_campaign import ExternalPostCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "accountId_example" # str | The given account id
    external_post_campaign = ExternalPostCampaign(
        data=JsonApiBodyWithoutIdOfCampaignAttributesAndCampaign(
            type="type_example",
            attributes=ExternalCampaignAttributes(
                type="auction",
                drawable_balance_ids=[
                    "drawable_balance_ids_example",
                ],
                click_attribution_window="30D",
                view_attribution_window="none",
                name="name_example",
                budget=3.14,
                click_attribution_scope="unknown",
                view_attribution_scope="unknown",
            ),
        ),
    ) # ExternalPostCampaign | The campaign settings to create a campaign with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_account_campaigns_by_account_id(account_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_campaigns_by_account_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_account_campaigns_by_account_id(account_id, external_post_campaign=external_post_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_account_campaigns_by_account_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The given account id |
 **external_post_campaign** | [**ExternalPostCampaign**](ExternalPostCampaign.md)| The campaign settings to create a campaign with | [optional]

### Return type

[**JsonApiSingleResponseOfCampaign**](JsonApiSingleResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_campaign_line_items_by_campaign_id**
> JsonApiSingleResponseOfLineItem post_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)



Creates a new line item with the specified settings

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item import JsonApiSingleResponseOfLineItem
from criteo_api_retailmedia_preview.model.external_post_line_item import ExternalPostLineItem
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    external_post_line_item = ExternalPostLineItem(
        data=JsonApiBodyWithoutIdOfLineItemAttributesAndLineItem(
            type="type_example",
            attributes=ExternalLineItemAttributes(
                target_retailer_id="target_retailer_id_example",
                status="unknown",
                target_bid=3.14,
                is_auto_daily_pacing=False,
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                max_bid=3.14,
                budget=3.14,
                monthly_pacing=3.14,
                daily_pacing=3.14,
                bid_strategy="conversion",
            ),
        ),
    ) # ExternalPostLineItem | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_api_v1_external_campaign_line_items_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_campaign_line_items_by_campaign_id(campaign_id, external_post_line_item=external_post_line_item)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_campaign_line_items_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **external_post_line_item** | [**ExternalPostLineItem**](ExternalPostLineItem.md)| The line item settings to create a line item with | [optional]

### Return type

[**JsonApiSingleResponseOfLineItem**](JsonApiSingleResponseOfLineItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_catalogs_sku_retrieval**
> SkuDataPreviewListResponse post_api_v1_external_catalogs_sku_retrieval()



Endpoint to search skus by text, retailer and sellers/brands.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.sku_data_preview_list_response import SkuDataPreviewListResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    request_body = [
        "request_body_example",
    ] # [str] | The list of SKU keys to retrieve sku information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_retrieval(page_index=page_index, page_size=page_size, request_body=request_body)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_retrieval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
 **request_body** | **[str]**| The list of SKU keys to retrieve sku information | [optional]

### Return type

[**SkuDataPreviewListResponse**](SkuDataPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_external_catalogs_sku_search**
> SkuDataPreviewListResponse post_api_v1_external_catalogs_sku_search()



Endpoint to search skus by text, retailer and sellers/brands.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.sku_data_preview_list_response import SkuDataPreviewListResponse
from criteo_api_retailmedia_preview.model.sku_search_request_preview_request import SkuSearchRequestPreviewRequest
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    page_index = 0 # int | The start position in the overall list of matches. Must be zero or greater. (optional) if omitted the server will use the default value of 0
    page_size = 100 # int | The maximum number of results to return with each call. Must be greater than zero. (optional) if omitted the server will use the default value of 100
    sku_search_request_preview_request = SkuSearchRequestPreviewRequest(
        data=ResourceOfSkuSearchRequestPreview(
            id="id_example",
            type="type_example",
            attributes=SkuSearchRequestPreview(
                query_string="query_string_example",
                retailer_id="retailer_id_example",
                sellers=[
                    "sellers_example",
                ],
                brand_ids=[
                    "brand_ids_example",
                ],
                sku_type="brand",
            ),
        ),
    ) # SkuSearchRequestPreviewRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_api_v1_external_catalogs_sku_search(page_index=page_index, page_size=page_size, sku_search_request_preview_request=sku_search_request_preview_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->post_api_v1_external_catalogs_sku_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] if omitted the server will use the default value of 100
 **sku_search_request_preview_request** | [**SkuSearchRequestPreviewRequest**](SkuSearchRequestPreviewRequest.md)|  | [optional]

### Return type

[**SkuDataPreviewListResponse**](SkuDataPreviewListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Skus found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api202210_external_account_by_account_id_creativescreative_id**
> Creative202210Response put_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id)



Update a creative

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_preview.model.creative_update_model202207 import CreativeUpdateModel202207
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    account_id = "account-id_example" # str | External account id containing the creative
    creative_id = "creative-id_example" # str | Creative to update
    creative_update_model202207 = CreativeUpdateModel202207(
        name="name_example",
        brand_id=1,
        retailer_id=1,
        template_id=1,
        template_variable_values=[
            TemplateVariableValue(
                id="id_example",
                text_variable_value=TextVariableValue(
                    text="text_example",
                ),
                choice_variable_value=ChoiceVariableValue(
                    chosen_options=[
                        "chosen_options_example",
                    ],
                ),
                color_variable_value=ColorVariableValue(
                    color="#2EC",
                ),
                files_variable_value=FilesVariableValue(
                    asset_ids=[
                        "asset_ids_example",
                    ],
                ),
                hyperlink_variable_value=HyperlinkVariableValue(
                    url="url_example",
                ),
            ),
        ],
    ) # CreativeUpdateModel202207 | The creative to create (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_account_by_account_id_creativescreative_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202210_external_account_by_account_id_creativescreative_id(account_id, creative_id, creative_update_model202207=creative_update_model202207)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_account_by_account_id_creativescreative_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| External account id containing the creative |
 **creative_id** | **str**| Creative to update |
 **creative_update_model202207** | [**CreativeUpdateModel202207**](CreativeUpdateModel202207.md)| The creative to create | [optional]

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Creative updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id**
> ProductButtonResponse put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)



Update a product button

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.product_button_request import ProductButtonRequest
from criteo_api_retailmedia_preview.model.product_button_response import ProductButtonResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    product_button_id = "product-button-id_example" # str | Sequential id of the product button
    product_button_request = ProductButtonRequest(
        data=ResourceOfProductButtonRequest(
            attributes=ExternalProductButtonRequest(
                name="name_example",
                background_image="background_image_example",
                is_mandatory=1,
                skus=[
                    "skus_example",
                ],
            ),
            id="id_example",
            type="type_example",
        ),
    ) # ProductButtonRequest | Details of the updated product button (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id(line_item_id, product_button_id, product_button_request=product_button_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202210_external_line_item_product_buttons_by_line_item_id_product_button_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **product_button_id** | **str**| Sequential id of the product button |
 **product_button_request** | [**ProductButtonRequest**](ProductButtonRequest.md)| Details of the updated product button | [optional]

### Return type

[**ProductButtonResponse**](ProductButtonResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api202301_external_line_item_bid_multipliers_by_line_item_id**
> LineItemBidMultipliersResponse put_api202301_external_line_item_bid_multipliers_by_line_item_id(line_item_id)



Replace bid multipliers on a line item

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers_response import LineItemBidMultipliersResponse
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers_request import LineItemBidMultipliersRequest
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "line-item-id_example" # str | Long external id of the associated line item
    line_item_bid_multipliers_request = LineItemBidMultipliersRequest(
        data=ResourceOfLineItemBidMultipliers(
            attributes=LineItemBidMultipliers(
                search=3.14,
                homepage=3.14,
                categories=3.14,
                product_detail=3.14,
                confirmation=3.14,
                merchandising=3.14,
                deals=3.14,
                checkout=3.14,
            ),
            id="id_example",
            type="type_example",
        ),
    ) # LineItemBidMultipliersRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api202301_external_line_item_bid_multipliers_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202301_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api202301_external_line_item_bid_multipliers_by_line_item_id(line_item_id, line_item_bid_multipliers_request=line_item_bid_multipliers_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api202301_external_line_item_bid_multipliers_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| Long external id of the associated line item |
 **line_item_bid_multipliers_request** | [**LineItemBidMultipliersRequest**](LineItemBidMultipliersRequest.md)|  | [optional]

### Return type

[**LineItemBidMultipliersResponse**](LineItemBidMultipliersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_external_balance_campaigns_by_balance_id**
> PageOfBalanceCampaign put_api_v1_external_balance_campaigns_by_balance_id(balance_id)



appends one or more campaigns to the specified balance

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_data_request_of_put_balance_campaign import JsonApiDataRequestOfPutBalanceCampaign
from criteo_api_retailmedia_preview.model.page_of_balance_campaign import PageOfBalanceCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    balance_id = "balanceId_example" # str | The balance to add campaigns from
    json_api_data_request_of_put_balance_campaign = JsonApiDataRequestOfPutBalanceCampaign(
        data=[
            ExternalPutBalanceCampaign(
                type="type_example",
                id="id_example",
                attributes={},
            ),
        ],
    ) # JsonApiDataRequestOfPutBalanceCampaign | The campaigns to append (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_balance_campaigns_by_balance_id(balance_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_balance_campaigns_by_balance_id(balance_id, json_api_data_request_of_put_balance_campaign=json_api_data_request_of_put_balance_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_balance_campaigns_by_balance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**| The balance to add campaigns from |
 **json_api_data_request_of_put_balance_campaign** | [**JsonApiDataRequestOfPutBalanceCampaign**](JsonApiDataRequestOfPutBalanceCampaign.md)| The campaigns to append | [optional]

### Return type

[**PageOfBalanceCampaign**](PageOfBalanceCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_external_campaign_by_campaign_id**
> JsonApiSingleResponseOfCampaign put_api_v1_external_campaign_by_campaign_id(campaign_id)



Updates the campaign for the given campaign id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_single_response_of_campaign import JsonApiSingleResponseOfCampaign
from criteo_api_retailmedia_preview.model.external_put_campaign import ExternalPutCampaign
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    campaign_id = "campaignId_example" # str | The given campaign id
    external_put_campaign = ExternalPutCampaign(
        data=JsonApiBodyWithExternalIdOfEditableCampaignAttributesAndCampaign(
            id="id_example",
            type="type_example",
            attributes=ExternalEditableCampaignAttributes(
                name="name_example",
                budget=3.14,
                click_attribution_window="7D",
                view_attribution_window="none",
                click_attribution_scope="unknown",
                view_attribution_scope="unknown",
            ),
        ),
    ) # ExternalPutCampaign | The campaign settings to update that campaign with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_campaign_by_campaign_id(campaign_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_campaign_by_campaign_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_campaign_by_campaign_id(campaign_id, external_put_campaign=external_put_campaign)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_campaign_by_campaign_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The given campaign id |
 **external_put_campaign** | [**ExternalPutCampaign**](ExternalPutCampaign.md)| The campaign settings to update that campaign with | [optional]

### Return type

[**JsonApiSingleResponseOfCampaign**](JsonApiSingleResponseOfCampaign.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_external_line_item_by_line_item_id**
> JsonApiSingleResponseOfLineItem put_api_v1_external_line_item_by_line_item_id(line_item_id)



Updates the line item for the given line item id

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.external_put_line_item import ExternalPutLineItem
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item import JsonApiSingleResponseOfLineItem
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The given line item id
    external_put_line_item = ExternalPutLineItem(
        data=JsonApiBodyWithExternalIdOfEditableLineItemAttributesAndLineItem(
            id="id_example",
            type="type_example",
            attributes=ExternalEditableLineItemAttributes(
                name="name_example",
                start_date=dateutil_parser('1970-01-01').date(),
                end_date=dateutil_parser('1970-01-01').date(),
                target_bid=3.14,
                max_bid=3.14,
                budget=3.14,
                monthly_pacing=3.14,
                daily_pacing=3.14,
                is_auto_daily_pacing=True,
                bid_strategy="conversion",
                status="unknown",
            ),
        ),
    ) # ExternalPutLineItem | The line item settings to create a line item with (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_line_item_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_line_item_by_line_item_id(line_item_id, external_put_line_item=external_put_line_item)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The given line item id |
 **external_put_line_item** | [**ExternalPutLineItem**](ExternalPutLineItem.md)| The line item settings to create a line item with | [optional]

### Return type

[**JsonApiSingleResponseOfLineItem**](JsonApiSingleResponseOfLineItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_external_line_item_products_by_line_item_id**
> JsonApiPageResponseOfStringAndPromotedProduct put_api_v1_external_line_item_products_by_line_item_id(line_item_id)



This endpoint appends one or more products to promote on the specified line item.  The resulting state of the line item is returned.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.json_api_data_request_with_id_of_string_and_promoted_product import JsonApiDataRequestWithIdOfStringAndPromotedProduct
from criteo_api_retailmedia_preview.model.json_api_page_response_of_string_and_promoted_product import JsonApiPageResponseOfStringAndPromotedProduct
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    line_item_id = "lineItemId_example" # str | The line item to interact with
    json_api_data_request_with_id_of_string_and_promoted_product = JsonApiDataRequestWithIdOfStringAndPromotedProduct(
        data=[
            JsonApiBodyWithIdOfStringAndPromotedProductAndPromotedProduct(
                id="id_example",
                type="type_example",
                attributes=ExternalPromotedProduct(
                    bid_override=3.14,
                ),
            ),
        ],
    ) # JsonApiDataRequestWithIdOfStringAndPromotedProduct | the products to append to this line item (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_api_v1_external_line_item_products_by_line_item_id(line_item_id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_api_v1_external_line_item_products_by_line_item_id(line_item_id, json_api_data_request_with_id_of_string_and_promoted_product=json_api_data_request_with_id_of_string_and_promoted_product)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->put_api_v1_external_line_item_products_by_line_item_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | **str**| The line item to interact with |
 **json_api_data_request_with_id_of_string_and_promoted_product** | [**JsonApiDataRequestWithIdOfStringAndPromotedProduct**](JsonApiDataRequestWithIdOfStringAndPromotedProduct.md)| the products to append to this line item | [optional]

### Return type

[**JsonApiPageResponseOfStringAndPromotedProduct**](JsonApiPageResponseOfStringAndPromotedProduct.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_keyword_bids**
> RetailMediaExternalv1ResourceOutcome set_keyword_bids(id)



Set bid overrides for associated keywords to the given line item in bulk

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.retail_media_externalv1_resource_outcome import RetailMediaExternalv1ResourceOutcome
from criteo_api_retailmedia_preview.model.retail_media_externalv1_set_bids_model_request import RetailMediaExternalv1SetBidsModelRequest
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | Long external id of the associated line item
    retail_media_externalv1_set_bids_model_request = RetailMediaExternalv1SetBidsModelRequest(
        data=RetailMediaExternalv1SetBidsModelResource(
            id="id_example",
            type="type_example",
            attributes=RetailMediaExternalv1SetBidsModel(
                keywords=[
                    RetailMediaExternalv1SetBidModel(
                        phrase="phrase_example",
                        bid=3.14,
                    ),
                ],
            ),
        ),
    ) # RetailMediaExternalv1SetBidsModelRequest | Object containing a list of bid overrides for associated keywords (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_keyword_bids(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_keyword_bids: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_keyword_bids(id, retail_media_externalv1_set_bids_model_request=retail_media_externalv1_set_bids_model_request)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->set_keyword_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Long external id of the associated line item |
 **retail_media_externalv1_set_bids_model_request** | [**RetailMediaExternalv1SetBidsModelRequest**](RetailMediaExternalv1SetBidsModelRequest.md)| Object containing a list of bid overrides for associated keywords | [optional]

### Return type

[**RetailMediaExternalv1ResourceOutcome**](RetailMediaExternalv1ResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_proposal**
> RetailMediaExternalv1ProposalStatusModelResponse submit_proposal(id)



Submit a proposal to modify a Preferred Deal Line Item for review.

### Example

* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_preview
from criteo_api_retailmedia_preview.api import campaign_api
from criteo_api_retailmedia_preview.model.retail_media_externalv1_proposal_status_model_response import RetailMediaExternalv1ProposalStatusModelResponse
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

# Enter a context with an instance of the API client
with criteo_api_retailmedia_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaign_api.CampaignApi(api_client)
    id = "id_example" # str | The external id of a line item.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submit_proposal(id)
        pprint(api_response)
    except criteo_api_retailmedia_preview.ApiException as e:
        print("Exception when calling CampaignApi->submit_proposal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The external id of a line item. |

### Return type

[**RetailMediaExternalv1ProposalStatusModelResponse**](RetailMediaExternalv1ProposalStatusModelResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

