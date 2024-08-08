# RmAudienceSegmentEntityV1

Set of rules that defines specific people to target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | Account associated to the segment | [optional] 
**name** | **str, none_type** | Name of the segment | [optional] 
**description** | **str, none_type** | Description of the segment | [optional] 
**retailer_id** | **str, none_type** | Retailer  associated to the segment | [optional] 
**type** | **str, none_type** | Type of segment (read-only) | [optional] 
**created_at** | **datetime, none_type** | ISO-8601 timestamp in UTC of segment creation (read-only) | [optional] 
**updated_at** | **datetime, none_type** | ISO-8601 timestamp in UTC of segment update (read-only) | [optional] 
**created_by_id** | **str, none_type** | User that created the segment | [optional] 
**contact_list** | [**RmContactListV1**](RmContactListV1.md) |  | [optional] 
**user_behavior** | [**RmUserBehaviorV1**](RmUserBehaviorV1.md) |  | [optional] 
**channels** | **[str], none_type** | Channels associated to the segment (read-only) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


