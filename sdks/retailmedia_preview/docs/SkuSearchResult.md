# SkuSearchResult

Data model for response resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The product name | [optional] 
**category_id** | **str, none_type** | The cateogry Id | [optional] 
**category** | **str, none_type** | The full retailer category taken from the retailers catalog | [optional] 
**global_brand_id** | **str, none_type** | The global brand id associated to the product | [optional] 
**global_brand_name** | **str, none_type** | The name of the global brand | [optional] 
**retailer_brand_id** | **str, none_type** | The retailer brand id associated to the product | [optional] 
**retailer_brand_name** | **str, none_type** | The name of the retailer brand | [optional] 
**global_category_id** | **str, none_type** | the Global Category Id | [optional] 
**price** | **float, none_type** | The product price pulled from the retailer&#39;s catalog | [optional] 
**model_number** | **str, none_type** | The model number for the product | [optional] 
**is_in_stock** | **bool, none_type** | Indicates if the retailer product is in stock | [optional] 
**gtin** | **str, none_type** | A GTIN identifier for the product if available.  TIt covers variations such as EANs and UPCs | [optional] 
**mpn** | **str, none_type** | The MPN identifier for the product if available | [optional] 
**image_url** | **str, none_type** | An http image resource provided by the retailer catalog | [optional] 
**updated_at** | **datetime, none_type** | The last time this product was updated in the Retail Media Catalog.  The date value is represented as an UTC ISO8601 string | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


