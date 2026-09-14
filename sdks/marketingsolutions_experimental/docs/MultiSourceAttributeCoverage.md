# MultiSourceAttributeCoverage

Number of products whose attribute was filled from the source, and number of products whose attribute was overridden.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filled_from_source** | **int** | Products that kept this attribute from the primary catalog: the number of products in the ingestion, less the products where the attribute was overridden. The same value as valueOrigin.primaryComponent. Products whose attribute is absent from every source are counted here too. | [optional] 
**overridden** | **int** | Products where an existing value was replaced. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


