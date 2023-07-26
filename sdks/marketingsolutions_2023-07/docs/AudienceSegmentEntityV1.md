# AudienceSegmentEntityV1

Set of rules that defines specific people to target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the segment | [optional] 
**description** | **str** | Description of the segment | [optional] 
**type** | **str** | Type of segment (read-only) | [optional] 
**created_at** | **datetime** | ISO-8601 timestamp in UTC of segment creation (read-only) | [optional] 
**updated_at** | **datetime** | ISO-8601 timestamp in UTC of segment update (read-only) | [optional] 
**advertiser_id** | **str** | Advertiser associated to the segment | [optional] 
**in_market** | [**InMarketV1**](InMarketV1.md) |  | [optional] 
**prospecting** | [**ProspectingV1**](ProspectingV1.md) |  | [optional] 
**contact_list** | [**ContactListV1**](ContactListV1.md) |  | [optional] 
**location** | [**LocationV1**](LocationV1.md) |  | [optional] 
**behavioral** | [**BehavioralV1**](BehavioralV1.md) |  | [optional] 
**retargeting** | [**RetargetingV1**](RetargetingV1.md) |  | [optional] 
**lookalike** | [**LookalikeV1**](LookalikeV1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


