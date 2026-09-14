# MultiSourceImpact

Number of products evaluated, matched, enriched, modified and left unmatched by the Multi-Source enrichment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products_enriched** | **int** | Products where at least one missing attribute was filled. Not exclusive with productsModified: a product can be both enriched and modified. | [optional] 
**products_evaluated** | **int** | Total products considered for Multi-Source enrichment. | [optional] 
**products_matched** | **int** | Products matched with at least one additional source using the matching keys. | [optional] 
**products_modified** | **int** | Products where an existing value was overridden. | [optional] 
**products_unmatched** | **int** | Products not matched with any additional source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


