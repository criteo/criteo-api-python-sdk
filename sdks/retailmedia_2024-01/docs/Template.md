# Template

A template for creating creatives.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_format** | **str** | The kind of creative this template can be used to build. | 
**name** | **str** | The name of the template | 
**sku_collection_min** | **int** | TODO: what is it ? | 
**sku_per_collection_min** | **int** | TODO: what is it ? | 
**all_collections_mandatory** | **bool** | TODO: what is it ? | 
**created_at** | **datetime** | The time at which the template was created | 
**updated_at** | **datetime** | The time at which the template was updated | 
**sections** | [**[Section]**](Section.md) | The sections holding various template variables | 
**retailer_id** | **int** | The retailer associated to the template | [optional] 
**sku_collection_max** | **int, none_type** | TODO: what is it ? | [optional] 
**sku_per_collection_max** | **int, none_type** | TODO: what is it ? | [optional] 
**displayable_skus_max** | **int, none_type** | TODO: what is it ? | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


