# InsightStatusResponse

Status of an asynchronous insight report request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str, none_type** | When the insight report was created. | [optional] 
**expires_at** | **str, none_type** | When the insight report expires and can no longer be downloaded. | [optional] 
**file_size_bytes** | **int, none_type** | Size of the generated report file in bytes, when available. | [optional] 
**md5_check_sum** | **str, none_type** | MD5 checksum of the generated report file, when available. | [optional] 
**message** | **str, none_type** | Additional information about the report status, when available. | [optional] 
**row_count** | **int, none_type** | Number of rows in the generated report, when available. | [optional] 
**status** | **str, none_type** | Current status of the insight report. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


