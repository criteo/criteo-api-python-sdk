# ProductSet

Encapsulate a group of product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | The dataset to which the product set belong | 
**name** | **str** | The name of the product set | 
**minimum_number_of_products** | **int** | Minimum amount of products that should match the product set to consider it valid.  Greater or equal than one. | 
**status** | **str** | The status of the product set | 
**number_of_products** | **int, none_type** | The number of product matching the product set.  Can be null for newly created product set. | 
**creation_date** | **str** | The creation date of the product set (UTC time in ISO8601 format). Example: \&quot;02/25/2022 14:51:26\&quot;.  Can be null if the value isn&#39;t available. | 
**rules** | [**[ProductSetRule]**](ProductSetRule.md) | The rules identifying the product belonging to the set | 
**client_type** | **str** | The client type of the product set | 
**keep_variant_products** | **bool** |  | 
**id** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


