# AudienceSegmentCreateEntityV1

Set of rules that defines specific people to target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the segment | [optional] 
**description** | **str** | Description of the segment | [optional] 
**advertiser_id** | **str** | Advertiser associated to the segment | [optional] 
**commerce** | [**CommerceCreateV1**](CommerceCreateV1.md) |  | [optional] 
**similar** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Settings to target similar users to website visitors. | [optional] 
**contact_list** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Settings to target users with your contact lists. | [optional] 
**location** | [**LocationCreateV1**](LocationCreateV1.md) |  | [optional] 
**retargeting** | [**RetargetingCreateV1**](RetargetingCreateV1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


