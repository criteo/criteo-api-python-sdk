# SellerCatalogRequestV2

Used to request a catalog of seller SKUs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_fields** | **[str], none_type** | Out of the optional fields, only the ones specified will be included in the catalog generated. | [optional] 
**modified_after** | **datetime, none_type** | Only products modified after this time will be returned. | [optional] 
**sellers** | [**[SellerIdentifierV2], none_type**](SellerIdentifierV2.md) | A list of sellers to restrict the catalog to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


