# ReportStatusAttributes

Report Status Attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | One of \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;failure\&quot;, or \&quot;expired\&quot; | 
**created_at** | **datetime** | Timestamp when the report started to execute | [optional] 
**expires_at** | **datetime** | Timestamp when the cached report will expire | [optional] 
**file_size_bytes** | **int, none_type** | Total size of file, only populated on success | [optional] 
**md5_checksum** | **str, none_type** | The MD5 checksum of the content, only populated on success | [optional] 
**message** | **str, none_type** | Failure message, only populated on failure | [optional] 
**row_count** | **int, none_type** | Rows of data in report, only populated on success | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


