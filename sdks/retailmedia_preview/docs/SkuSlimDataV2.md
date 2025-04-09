# SkuSlimDataV2

Slim  version of Sku Data model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_in_stock** | **bool** | An indication of if the retailer currently has the product in stock. | 
**price** | **float, none_type** | The price of the product on the retailer site. Can be omitted in certain circumstances | 
**updated_at** | **datetime** | The last time this product was updated in the Retail Media Catalog. Represented as a UTC ISO8601 string. | 
**brand** | [**Brand**](Brand.md) |  | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**description** | **str, none_type** | A short description of the product. | [optional] 
**gtin** | **str, none_type** | A GTIN identifier for the product if available. Covers variations such as EANs and UPCs. | [optional] 
**image_url** | **str** | An http image resource provided by the retailer. | [optional] 
**mpn** | **str, none_type** | The MPN for the product if available. | [optional] 
**name** | **str** | A short product name. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


