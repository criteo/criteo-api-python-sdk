# ContactlistWithAttributesAmendmentAttributes

the name of the entity type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Whether to add or remove users | 
**identifier_type** | **str** | What type of identifiers are used | 
**identifiers** | [**[UserDef]**](UserDef.md) | The users to add or remove, each in the schema specified, defined with attributes | 
**gum_caller_id** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The Gum caller id of the advertiser patching identifiers of type Gum | [optional] [readonly] 
**internal_identifiers** | **bool** | The flag to indicate if identifiers are external or internal | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


