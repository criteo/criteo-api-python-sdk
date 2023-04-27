# SkuSlimDataV2

Slim  version of Sku Data model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | The price of the product on the retailer site. | 
**is_in_stock** | **bool** | An indication of if the retailer currently has the product in stock. | 
**updated_at** | **datetime** | The last time this product was updated in the Retail Media Catalog. Represented as a UTC ISO8601 string. | 
**name** | **str** | A short product name. | [optional] 
**description** | **str** | A short description of the product. | [optional] 
**retailer_category** | [**RetailerCategory**](RetailerCategory.md) |  | [optional] 
**global_category_id** | **str** | The global category Id. | [optional] 
**global_brand** | [**GlobalBrand**](GlobalBrand.md) |  | [optional] 
**retailer_brand** | [**RetailerBrand**](RetailerBrand.md) |  | [optional] 
**gtin** | **str** | A GTIN identifier for the product if available. Covers variations such as EANs and UPCs. | [optional] 
**mpn** | **str** | The MPN for the product if available. | [optional] 
**image_url** | **str** | An http image resource provided by the retailer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


