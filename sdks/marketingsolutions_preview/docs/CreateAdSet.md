# CreateAdSet

ad set create model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the ad set | [optional] 
**dataset_id** | **str** | Dataset id of this ad set | [optional] 
**campaign_id** | **str** | Campaign id this ad set belongs to | [optional] 
**objective** | **str** | Objective of the ad set | [optional] 
**schedule** | [**CreateAdSetSchedule**](CreateAdSetSchedule.md) |  | [optional] 
**bidding** | [**CreateAdSetBidding**](CreateAdSetBidding.md) |  | [optional] 
**targeting** | [**CreateAdSetTargeting**](CreateAdSetTargeting.md) |  | [optional] 
**budget** | [**CreateAdSetBudget**](CreateAdSetBudget.md) |  | [optional] 
**tracking_code** | **str** | The click tracking code associated to this Ad Set. | [optional] 
**media_type** | **str** | Media type for the ad set | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


