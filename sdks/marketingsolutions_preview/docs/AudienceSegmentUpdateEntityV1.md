# AudienceSegmentUpdateEntityV1

Set of rules that defines specific people to target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | [**NillableString**](NillableString.md) |  | [optional] 
**commerce** | [**CommerceUpdateV1**](CommerceUpdateV1.md) |  | [optional] 
**contact_list** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Settings to target users with your contact lists. | [optional] 
**location** | [**LocationUpdateV1**](LocationUpdateV1.md) |  | [optional] 
**retargeting** | [**RetargetingUpdateV1**](RetargetingUpdateV1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


