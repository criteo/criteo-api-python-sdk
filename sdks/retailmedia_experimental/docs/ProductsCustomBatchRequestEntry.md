# ProductsCustomBatchRequestEntry

A product event for a batch request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** | The ID of the managing account. Criteo: the partnerId. | 
**method** | **str** | The method of the batch entry. | 
**batch_id** | **int** | An entry ID, unique within the batch request. | [optional] 
**feed_id** | **str** | Not used by Criteo. | [optional] 
**item_group_id** | **str** | Deprecated (providing this information is no more needed, this field will be removed in next release). The itemGroupId of the product to delete. To be defined when the method is delete and the product is a variant. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**product_id** | **str** | The Product ID to delete. Only defined if the method is delete. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


