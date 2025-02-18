# CreateAdSet

ad set create model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the ad set | 
**dataset_id** | **str, none_type** | Dataset id of this ad set | 
**campaign_id** | **str, none_type** | Campaign id this ad set belongs to | 
**objective** | **str** | Objective of the ad set | 
**schedule** | [**CreateAdSetSchedule**](CreateAdSetSchedule.md) |  | 
**bidding** | [**CreateAdSetBidding**](CreateAdSetBidding.md) |  | 
**targeting** | [**CreateAdSetTargeting**](CreateAdSetTargeting.md) |  | 
**tracking_code** | **str, none_type** | The click tracking code associated to this Ad Set. | 
**media_type** | **str** | Media type for the ad set | 
**budget** | [**CreateAdSetBudget**](CreateAdSetBudget.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


