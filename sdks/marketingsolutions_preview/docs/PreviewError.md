# PreviewError

Error descriptor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | The MACHINE-READABLE correlation ID provided by the gateway | 
**type** | **str** | A MACHINE-READABLE code specifying error category. This information is used on client side to focus on certain type of error, to either retry some processing or display only certain type of errors. | 
**code** | **str** | A MACHINE-READABLE error code string in kebab-case. Unique across Criteo | 
**instance** | **str** | A MACHINE-READABLE URI reference that identifies the specific occurrence of the problem. This could be useful when we want to the return the API Endpoint identifying the exact resource related to the error. | 
**title** | **str** | A short, HUMAN-READABLE summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. | 
**detail** | **str** | A HUMAN-READABLE detailed explanation specific to this occurrence of the problem. This should not be more that 1 paragraph | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


