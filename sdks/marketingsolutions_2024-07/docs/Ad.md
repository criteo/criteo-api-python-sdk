# Ad

An ad is the binding that connects a creative with an ad set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The name of the ad | [optional] 
**description** | **str, none_type** | The description of the ad | [optional] 
**creative_id** | **str, none_type** | The id of the Creative binded to this Ad | [optional] 
**ad_set_id** | **str, none_type** | The id of the Ad Set binded to this Ad | [optional] 
**inventory_type** | **str, none_type** | The inventory the Ad belongs to. Possible values are \&quot;Display\&quot; and \&quot;Native\&quot;. This is optional since this doesn&#39;t make sense for every creative type but will throw an error if not set for a dynamic creative. | [optional] 
**start_date** | **str, none_type** | The date when the ad will be launched  String must be in ISO8601 format | [optional] 
**end_date** | **str, none_type** | The date when when we will stop to show this ad. If the end date is not specified (i.e. null) then the ad will go on forever  String must be in ISO8601 format | [optional] 
**id** | **str, none_type** | Unique identifier (duplicate of the parent id). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


