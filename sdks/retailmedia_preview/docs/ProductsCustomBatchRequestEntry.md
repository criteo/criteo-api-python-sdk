# ProductsCustomBatchRequestEntry

A product event for a batch request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** | The ID of the managing account. Criteo: the partnerId. | 
**method** | **str** | The method of the batch entry. | 
**batch_id** | **int, none_type** | An entry ID, unique within the batch request. | [optional] 
**product_id** | **str, none_type** | The Product ID to delete. Only defined if the method is delete. | [optional] 
**item_group_id** | **str, none_type** | Deprecated (providing this information is no more needed, this field will be removed in next release). The itemGroupId of the product to delete. To be defined when the method is delete and the product is a variant. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**feed_id** | **str, none_type** | Not used by Criteo. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


