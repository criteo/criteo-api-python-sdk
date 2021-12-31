# ProductsCustomBatchRequestEntry

A batch entry encoding a single non-batch products request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** | The ID of the managing account. Criteo: the partnerId. | 
**method** | **str** | The method of the batch entry. | 
**batch_id** | **int** | An entry ID, unique within the batch request. | [optional] 
**product_id** | **str** | The Product ID to delete. Only defined if the method is delete. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**feed_id** | **str** | Not used by Criteo. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


