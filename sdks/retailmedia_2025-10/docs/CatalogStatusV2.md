# CatalogStatusV2

The status of an asynchronous request to generate a catalog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time this catalog was created. Represented as a UTC ISO8601 string. | 
**status** | **str** | An enumeration of the status of the catalog. | 
**file_size_bytes** | **int, none_type** | The size of this catalog in bytes. Available when this catalog reaches a success status. | [optional] 
**md5_checksum** | **str, none_type** | An MD5 checksum of the catalog for use in confirming complete and uncorrupted retrieval.  Available when this catalog reaches a success status. | [optional] 
**message** | **str, none_type** | An optional information message intended for developer consumption. | [optional] 
**row_count** | **int, none_type** | An indication of the number of products contained in this catalog. Available when  this catalog reaches a success status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


