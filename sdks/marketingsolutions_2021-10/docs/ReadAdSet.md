# ReadAdSet

ad set read model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the ad set | [optional] 
**advertiser_id** | **str** | Advertiser id of the campaign this ad set belongs to | [optional] 
**dataset_id** | **str** | Dataset id of this ad set | [optional] 
**campaign_id** | **str** | Campaign id this ad set belongs to | [optional] 
**destination_environment** | **str** | The environment that an ad click will lead a user to | [optional] 
**schedule** | [**ReadAdSetSchedule**](ReadAdSetSchedule.md) |  | [optional] 
**bidding** | [**ReadAdSetBidding**](ReadAdSetBidding.md) |  | [optional] 
**targeting** | [**AdSetTargeting**](AdSetTargeting.md) |  | [optional] 
**budget** | [**ReadAdSetBudget**](ReadAdSetBudget.md) |  | [optional] 
**media_type** | **str** | Media type for the ad set | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


