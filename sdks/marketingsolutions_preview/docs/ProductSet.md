# ProductSet

Encapsulate a group of product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | The partner to which the product set belong | [optional] 
**name** | **str** | The name of the product set | [optional] 
**status** | **str** | The status of the product set | [optional] 
**is_enabled** | **bool** | True if the product set is active | [optional] 
**number_of_products** | **int** | The number of product matching the product set | [optional] 
**creation_date** | **str** | Optional: The creation date of the product set (UTC time in ISO8601 format). Example: \&quot;02/25/2022 14:51:26\&quot;  Can be null if the value doesn&#39;t exist. | [optional] 
**rules** | [**[ProductSetRule]**](ProductSetRule.md) | The rules identifying the product belonging to the set | [optional] 
**id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


