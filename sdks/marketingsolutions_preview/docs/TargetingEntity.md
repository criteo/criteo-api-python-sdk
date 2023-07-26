# TargetingEntity

Represents either an allowlisting or a blocklisting rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Can be either DOMAIN or BUNDLE | [optional] 
**mode** | **str** | Can be either BLOCKLIST or ALLOWLIST | [optional] 
**data** | [**[EntityFilter]**](EntityFilter.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


