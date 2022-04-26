# SkuDataPreview

Metadata and usage info of a sku search

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku_key** | **str** | The product SKU Key. | 
**brand_id** | **str** | The global brand id associated to the product. | 
**brand_name** | **str** | The name of the global brand. | 
**retailer_id** | **str** | The identifier for the retailer the product is listed by. | 
**retailer_name** | **str** | The retailer name. | 
**price** | **float** | The price of the product on the retailer site. | 
**is_in_stock** | **bool** | An indication of if the retailer currently has the product in stock. | 
**updated_at** | **datetime** | The last time this product was updated in the Retail Media Catalog. Represented as a UTC ISO8601 string. | 
**name** | **str** | A short product name. | [optional] 
**description** | **str** | A product description. | [optional] 
**category_id** | **str** | The category Id. | [optional] 
**category** | **str** | The full category breadcrumb in the retailers catalog. | [optional] 
**is_seller_sku** | **bool** | An indication of if the sku is seller sku. | [optional] 
**seller_id** | **str** | The id of the seller. | [optional] 
**seller_name** | **str** | The name of the seller. | [optional] 
**gtin** | **str** | A GTIN identifier for the product if available. Covers variations such as EANs and UPCs. | [optional] 
**mpn** | **str** | The MPN for the product if available. | [optional] 
**image_url** | **str** | An http image resource provided by the retailer. | [optional] 
**product_page** | **str** | An The product page URL | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


