# MultiSourceConfiguration

Multi-Source Catalog configuration applied to the ingestion: main component, number of sources, matching keys and attribute mappings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_mappings** | [**[MultiSourceAttributeMapping], none_type**](MultiSourceAttributeMapping.md) | Attribute-level mapping rules applied during enrichment. | [optional] 
**enabled** | **bool** | Whether Multi-Source Catalog was enabled for this ingestion. | [optional] 
**main_component_id** | **int** | Identifier of the primary catalog component. | [optional] 
**matching_keys** | **[str, none_type], none_type** | Keys used to match products between the primary catalog and the additional sources. | [optional] 
**sources_count** | **int** | Number of additional sources configured, excluding the primary catalog. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


