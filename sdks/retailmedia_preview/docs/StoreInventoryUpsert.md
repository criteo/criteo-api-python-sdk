# StoreInventoryUpsert

Defines a store inventory to be upserted. Inspired from google spec.See https://developers.google.com/shopping-content/reference/rest/v2.1/localinventory/custombatch#LocalinventoryCustomBatchRequestEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | **str** | Might be: In stock, Out of stock, Preorder, Backorder | 
**batch_id** | **str** | Identifies this array entry | 
**price** | **str** | Product&#39;s price at this store | 
**product_id** | **str** |  Identifies a product | 
**store_id** | **str** | Identifies the store, for the customer | 
**sale_price** | **str** | The sale price of the product. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


