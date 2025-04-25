# AdWrite

Entity to create or update an ad

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_id** | **str** | The id of the Ad Set bound to this Ad | 
**creative_id** | **str** | The id of the Creative bound to this Ad | 
**name** | **str** | The name of the ad | 
**start_date** | **str** | The date when the ad will be launched  String must be in ISO8601 format | 
**description** | **str, none_type** | The description of the ad | [optional] 
**end_date** | **str, none_type** | The date when when we will stop to show this ad. If the end date is not specified (i.e. null) then the ad will go on forever  String must be in ISO8601 format | [optional] 
**inventory_type** | **str, none_type** | The inventory the Ad to be created or updated belongs to. Possible values are \&quot;Display\&quot; and \&quot;Native\&quot;. This is optional since this doesn&#39;t make sense for every creative type but will throw an error if not set for a dynamic creative. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


