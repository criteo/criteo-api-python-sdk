# SkuSearchRequestPreview

A request for sku by sellers or brands.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** | Query string to search for across SKU&#39;s properties (gtin, mpn, feed ID, Title, and Description) | 
**retailer_id** | **str** | Retailer Id | 
**sellers** | **[str]** | A list of seller names and/or seller Id&#39;s | [optional] 
**brand_ids** | **[str]** | A list of brand Id&#39;s | [optional] 
**sku_type** | **str** | Enum to set isSellerSku field | [optional]  if omitted the server will use the default value of "brand"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


