# Error

Error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | (REQUIRED) A machine-readable unique error code, expressed as a string value. The format used must be kabab-case. | 
**instance** | **str** | (REQUIRED) A URI reference that identifies the specific occurrence of the problem. | 
**trace_id** | **str** | (REQUIRED) The Correlation ID provided by the Gateway. It is also a unique identifier for this particular occurrence of the problem. | 
**type** | **str** | Type should be: \&quot;validation\&quot;, \&quot;unavailable, \&quot;violation\&quot;, \&quot;permission\&quot;, ... | 
**detail** | **str** | (RECOMMENDED) A human-readable explanation specific to this occurrence of the problem. | [optional] 
**source** | [**MapString**](MapString.md) |  | [optional] 
**stack_trace** | **[str]** | (NEVER IN PRODUCTION) A human-readable stacktrace produced by the implementation technology e.g. .Net, Scala, etc | [optional] 
**title** | **str** | (RECOMMENDED) A short, human-readable summary of the problem type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


