# MultiSourceAttributeMapping

Mapping of one catalog attribute to the source component field it is filled from.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str, none_type** | Target attribute in the catalog schema. | [optional] 
**source_component_id** | **int** | Identifies the additional source component this attribute is overridden from. Several mappings share it when one component overrides more than one attribute, which is why sourcesCount counts only the distinct ones. | [optional] 
**source_field** | **str, none_type** | Field name from the additional source mapped to this attribute. | [optional] 
**source_priority** | **int** | Priority of this source for this attribute: lower wins (1 overrides 2). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


