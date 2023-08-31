# TargetingErrorModel

A machine-readable format for specifying errors in Targeting.API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A machine-readable error code string. | 
**instance** | **str** | A machine-readable URI reference that identifies the specific occurrence of the problem. | 
**trace_id** | **str** | The machine-readable correlation Id provided by the gateway. | 
**type** | **str** | A machine-readable code specifying error category. This information is used on client side to focus on certain type of error,  to either retry some processing or display only certain type of errors. | 
**detail** | **str, none_type** | A human-readable detailed explanation specific to this occurrence of the problem. | [optional] 
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | A machine-readable structure to reference to the exact location(s) causing the error(s). | [optional] 
**title** | **str, none_type** | A short, human-readable summary of the problem type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


