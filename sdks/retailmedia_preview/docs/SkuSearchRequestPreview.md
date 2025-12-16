# SkuSearchRequestPreview

A request for sku by sellers or brands.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** | Query string to search for across SKU&#39;s properties (gtin, mpn, feed ID, Title, and Description) | 
**retailer_id** | **str** | Retailer Id | 
**brand_ids** | **[str], none_type** | A list of brand Id&#39;s | [optional] 
**brand_type** | **str** | Enum to set type of brand id&#39;s to filter by | [optional]  if omitted the server will use the default value of "uC"
**id** | **str, none_type** |  | [optional] 
**product_ids** | **[str], none_type** | A list of product Id&#39;s, if not passed ignore and search by QueryString | [optional] 
**product_id_type** | **str** | Type of Product Ids to search for. | [optional]  if omitted the server will use the default value of "skuKey"
**sellers** | **[str], none_type** | A list of seller names and/or seller Id&#39;s | [optional] 
**sku_type** | **str** | Enum to set isSellerSku field | [optional]  if omitted the server will use the default value of "brand"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


