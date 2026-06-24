# PatchProductSetRequest

Entity to update a product set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_draft** | **bool, none_type** | [optional] New value of product set segment status (draft or active) | [optional] 
**minimum_number_of_products** | **int, none_type** | [optional] New minimum number of products of the product set to be patched. This is used to determine if the rules are valid! | [optional] 
**name** | **str** | [optional]  New name that will be associated to the product set | [optional] 
**rules** | [**[ProductSetRule]**](ProductSetRule.md) | [optional] New rules that will be associated to the product set | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


