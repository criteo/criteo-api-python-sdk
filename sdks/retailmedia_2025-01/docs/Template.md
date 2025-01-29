# Template

A template for creating creatives.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_format** | **str** | The kind of creative this template can be used to build. | 
**name** | **str** | The name of the template | 
**sku_collection_min** | **int** | Minimum number of skus in the collection | 
**sku_per_collection_min** | **int** | Minimum number of skus per collection | 
**all_collections_mandatory** | **bool** | Marks whether or not all collections are mandatory | 
**created_at** | **datetime** | The time at which the template was created | 
**updated_at** | **datetime** | The time at which the template was updated | 
**sections** | [**[Section]**](Section.md) | The sections holding various template variables | 
**sku_collection_max** | **int, none_type** | Maximum number of skus in the collection | [optional] 
**sku_per_collection_max** | **int, none_type** | Maximum number of skus per collection | [optional] 
**displayable_skus_max** | **int, none_type** | Maximum number of displayable skus | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


