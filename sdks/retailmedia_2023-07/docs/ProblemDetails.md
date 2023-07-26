# ProblemDetails

Data model for common error or warning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | The request correlation ID this problem comes from. | [optional] 
**trace_identifier** | **str** | The request correlation ID this problem comes from. (deprecated, use traceId instead) | [optional] 
**type** | **str** | The problem&#39;s category. | [optional] 
**code** | **str** | A machine-readable  error code, expressed as a string value. | [optional] 
**instance** | **str** | A URI that identifies the specific occurrence of the problem. | [optional] 
**title** | **str** | A short human-readable description of the problem type | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem | [optional] 
**source** | **{str: (str,)}** | A machine-readable structure to reference to the exact location(s) causing the error(s) | [optional] 
**stack_trace** | **str** | Technical information, only used in non-prod environments | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


