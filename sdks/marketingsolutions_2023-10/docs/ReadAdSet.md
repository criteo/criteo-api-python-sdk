# ReadAdSet

ad set read model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the ad set | [optional] 
**advertiser_id** | **str, none_type** | Advertiser id of the campaign this ad set belongs to | [optional] 
**dataset_id** | **str, none_type** | Dataset id of this ad set | [optional] 
**campaign_id** | **str, none_type** | Campaign id this ad set belongs to | [optional] 
**destination_environment** | **str, none_type** | The environment that an ad click will lead a user to | [optional] 
**schedule** | [**ReadAdSetSchedule**](ReadAdSetSchedule.md) |  | [optional] 
**bidding** | [**ReadAdSetBidding**](ReadAdSetBidding.md) |  | [optional] 
**targeting** | [**AdSetTargeting**](AdSetTargeting.md) |  | [optional] 
**budget** | [**ReadAdSetBudget**](ReadAdSetBudget.md) |  | [optional] 
**media_type** | **str, none_type** | Media type for the ad set | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


