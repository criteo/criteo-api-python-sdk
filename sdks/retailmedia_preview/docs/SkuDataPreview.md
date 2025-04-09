# SkuDataPreview

Metadata and usage info of a sku search

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **str** | The global brand id associated to the product. | 
**brand_name** | **str** | The name of the global brand. | 
**category_id** | **str** | The category Id. | 
**is_in_stock** | **bool** | An indication of if the retailer currently has the product in stock. | 
**price** | **float** | The price of the product on the retailer site. | 
**retailer_id** | **str** | The identifier for the retailer the product is listed by. | 
**retailer_name** | **str** | The retailer name. | 
**sku_key** | **str** | The product SKU Key. | 
**updated_at** | **datetime** | The last time this product was updated in the Retail Media Catalog. Represented as a UTC ISO8601 string. | 
**category** | **str, none_type** | The full category breadcrumb in the retailers catalog. | [optional] 
**description** | **str, none_type** | A product description. | [optional] 
**gtin** | **str, none_type** | A GTIN identifier for the product if available. Covers variations such as EANs and UPCs. | [optional] 
**image_url** | **str** | An http image resource provided by the retailer. | [optional] 
**is_buybox** | **bool** | Whether the Sku is a Buybox Winner. | [optional] 
**is_seller_sku** | **bool** | An indication of if the sku is seller sku. | [optional] 
**model_number** | **str, none_type** | The Model Number for the product if available. | [optional] 
**mpn** | **str, none_type** | The MPN for the product if available. | [optional] 
**name** | **str** | A short product name. | [optional] 
**parent_id** | **str, none_type** | The ParentId for the product if available. | [optional] 
**product_page** | **str, none_type** | The product page URL | [optional] 
**seller_id** | **str, none_type** | The id of the seller. | [optional] 
**seller_name** | **str, none_type** | The name of the seller. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


