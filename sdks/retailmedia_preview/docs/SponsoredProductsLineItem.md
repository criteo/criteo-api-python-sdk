# SponsoredProductsLineItem

Model of a retail media auction line item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_remaining** | **float, none_type** | The amount of the budget that remains available. | 
**campaign_id** | **str** | The ID of the campaign this line item belongs to. | 
**created_at** | **datetime** | The date and time when the line item was created. | 
**name** | **str** | The name of the line item. | 
**start_date** | **datetime** | The date and time when the line item starts running. | 
**target_retailer_id** | **str** | The ID of the retailer targeted by this line item. | 
**updated_at** | **datetime** | The date and time when the line item was last updated. | 
**bid_strategy** | **str, none_type** | Optional field. | [optional] 
**budget** | **float, none_type** | The total budget allocated for this line item. | [optional] 
**budget_spent** | **float, none_type** | The amount of the budget that has been spent so far. | [optional] 
**daily_pacing** | **float, none_type** | The daily pacing limit for budget spending. | [optional] 
**end_date** | **datetime, none_type** | The date and time when the line item stops running. | [optional] 
**flight_schedule** | [**FlightSchedule**](FlightSchedule.md) |  | [optional] 
**is_auto_daily_pacing** | **bool, none_type** | Indicates whether automatic daily pacing is enabled. | [optional] 
**keyword_strategy** | **str, none_type** | The keyword targeting strategy for this line item. | [optional] 
**max_bid** | **float, none_type** | The maximum bid amount allowed for this line item. | [optional] 
**monthly_pacing** | **float, none_type** | The monthly pacing limit for budget spending. | [optional] 
**optimization_strategy** | **str, none_type** | Optimization strategy for the line item. | [optional] 
**status** | **str, none_type** | The current status of the line item. | [optional] 
**target_bid** | **float, none_type** | The target bid amount for the line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


