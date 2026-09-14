# MultiSourceAttributeDetails

Multi-Source enrichment details of a single attribute: source field, source priority, coverage and resolution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coverage** | [**MultiSourceAttributeCoverage**](MultiSourceAttributeCoverage.md) |  | [optional] 
**resolution** | [**MultiSourceAttributeResolution**](MultiSourceAttributeResolution.md) |  | [optional] 
**source_field** | **str, none_type** | Source field used for this attribute. | [optional] 
**source_priority** | **int** | Priority of the additional source that wins for this attribute, which is the lowest priority configured for it. Zero when no additional source overrides the attribute, and also when the winning source is itself configured with priority zero; the two cases cannot be told apart. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


