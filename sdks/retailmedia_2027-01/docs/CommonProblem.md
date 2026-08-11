# CommonProblem

Common problem object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str, none_type** | A machine-readable error code, expressed as a string value. | [optional] 
**detail** | **str, none_type** | A human-readable explanation specific to this occurrence of the problem | [optional] 
**instance** | **str, none_type** | A URI that identifies the specific occurrence of the problem. | [optional] 
**source** | **{str: (str,)}, none_type** | A machine-readable structure to reference to the exact location(s) causing the error(s) | [optional] 
**stack_trace** | **str, none_type** |  | [optional] 
**title** | **str, none_type** | A short human-readable description of the problem type | [optional] 
**trace_id** | **str, none_type** | The request correlation ID this problem comes from. | [optional] 
**trace_identifier** | **str, none_type** | The request correlation ID this problem comes from. (deprecated, use traceId instead) | [optional] 
**type** | **str, none_type** | The problem&#39;s category. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


