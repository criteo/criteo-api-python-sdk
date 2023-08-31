# EntityV2OfObject

Generic Criteo API successful data model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A string containing the entity type | 
**id** | **str** | A opaque string containing the unique Id of the entity | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Generic Criteo API successful data model  While others may be computed e.g. lastChangedDate.  Computed attributes are only part of the read model and not part of the write model. | [optional] 
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | A meta object that contains application-specific metadata | [optional] 
**relationships** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Relationships with this entity | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


