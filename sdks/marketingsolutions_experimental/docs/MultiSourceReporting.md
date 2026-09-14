# MultiSourceReporting

The Multi-Source Catalog enrichment of one ingestion, as reported under multiSource in the ingestion summary: the configuration that was applied, its impact on the products, and the per-attribute details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_details** | [**{str: (MultiSourceAttributeDetails,)}, none_type**](MultiSourceAttributeDetails.md) | Attribute-level reporting keyed by catalog attribute name (e.g. brand, color, gtin). | [optional] 
**configuration** | [**MultiSourceConfiguration**](MultiSourceConfiguration.md) |  | [optional] 
**impact** | [**MultiSourceImpact**](MultiSourceImpact.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


