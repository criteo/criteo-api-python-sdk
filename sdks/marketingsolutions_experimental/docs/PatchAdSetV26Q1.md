# PatchAdSetV26Q1

Model for patching an ad set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_configuration** | [**PatchAdSetAttributionConfigurationV26Q1**](PatchAdSetAttributionConfigurationV26Q1.md) |  | [optional] 
**bidding** | [**PatchAdSetBiddingV26Q1**](PatchAdSetBiddingV26Q1.md) |  | [optional] 
**budget** | [**PatchAdSetBudgetV26Q1**](PatchAdSetBudgetV26Q1.md) |  | [optional] 
**name** | **str, none_type** | Name of the ad set. | [optional] 
**scheduled_budget** | [**PatchAdSetScheduledBudgetV26Q1**](PatchAdSetScheduledBudgetV26Q1.md) |  | [optional] 
**scheduling** | [**PatchAdSetSchedulingV26Q1**](PatchAdSetSchedulingV26Q1.md) |  | [optional] 
**server_to_server_trackings** | [**[ServerToServerTrackingV26Q1], none_type**](ServerToServerTrackingV26Q1.md) | MMP server-to-server tracking URLs. Only allowed for app retargeting ad sets. Replaces the existing URLs when provided, clears them when empty, and leaves them unchanged when omitted | [optional] 
**targeting** | [**AdSetTargetingV26Q1**](AdSetTargetingV26Q1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


