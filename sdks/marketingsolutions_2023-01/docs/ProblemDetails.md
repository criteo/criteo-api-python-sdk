# ProblemDetails

Data model for common error or warning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str, none_type** | The request correlation ID this problem comes from. | [optional] 
**trace_identifier** | **str, none_type** | The request correlation ID this problem comes from. (deprecated, use traceId instead) | [optional] 
**type** | **str, none_type** |  | [optional] 
**code** | **str, none_type** |  | [optional] 
**instance** | **str, none_type** |  | [optional] 
**title** | **str, none_type** |  | [optional] 
**detail** | **str, none_type** |  | [optional] 
**source** | **{str: (str,)}, none_type** |  | [optional] 
**stack_trace** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


