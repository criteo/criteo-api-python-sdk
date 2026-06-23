# CommonError

A JSON:API Common error structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str, none_type** | (REQUIRED) A machine-readable unique error code, expressed as a string value. The format used must be kebab-case. | [optional] 
**detail** | **str, none_type** | (RECOMMENDED) A human-readable explanation specific to this occurrence of the problem. | [optional] 
**instance** | **str, none_type** | (REQUIRED) A URI reference that identifies the specific occurrence of the problem. | [optional] 
**source** | **{str: (str,)}, none_type** | (OPTIONAL) A machine-readable structure to reference to the exact location(s) causing the error(s) | [optional] 
**stack_trace** | **str, none_type** | (NEVER IN PRODUCTION) A human-readable stacktrace produced by the implementation technology | [optional] 
**title** | **str, none_type** | (RECOMMENDED) A short, human-readable summary of the problem type. | [optional] 
**trace_id** | **str, none_type** | (REQUIRED) The Correlation ID provided by the Gateway. It is also a unique identifier for this particular occurrence of the problem. | [optional] 
**type** | **str, none_type** | (REQUIRED) The classification of the error. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


