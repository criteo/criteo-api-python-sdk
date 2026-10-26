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
**bid_strategy** | **str, none_type** | Bid strategy for the line item. | [optional] 
**budget** | **float, none_type** | The total budget allocated for this line item. | [optional] 
**budget_spent** | **float, none_type** | The amount of the budget that has been spent so far. | [optional] 
**daily_pacing** | **float, none_type** | The daily pacing limit for budget spending. | [optional] 
**end_date** | **datetime, none_type** | The date and time when the line item stops running. | [optional] 
**flight_schedule** | [**FlightSchedule**](FlightSchedule.md) |  | [optional] 
**is_auto_daily_pacing** | **bool, none_type** | Indicates whether automatic daily pacing is enabled. | [optional] 
**keyword_strategy** | **str, none_type** | The keyword targeting strategy for this line item. | [optional] 
**max_bid** | **float, none_type** | The maximum bid amount allowed for this line item. | [optional] 
**monthly_pacing** | **float, none_type** | The monthly pacing limit for budget spending. | [optional] 
**optimization_strategy** | **str, none_type** | The optimization strategy for this line item. | [optional] 
**status** | **str, none_type** | The current status of the line item.                unknown: could not be determined (data issue, not a line item state).  draft: never fully configured, has never served.  scheduled: configured, start date is in the future.  active: in flight, funded, under no budget cap.  paused: previously active, manually deactivated.                ended: end date passed, within the last 90 days.  archived: end date passed more than 90 days ago - same as ended, just older, not reversible.                noFunds: no currently-active funding source (no Active mapped Insertion Order, no active  Make-Good credit IO) - a missing-funding problem, separate from any budget cap.  budgetHit: a budget cap (daily, hourly, monthly, or total) is capped with zero or below  remaining. Doesn&#39;t distinguish line item vs. campaign budget, or which cap type.                draft/scheduled/ended/archived short-circuit before the funding/budget check runs, so  those states never report noFunds or budgetHit regardless of underlying financial data.  Where both would apply, noFunds takes precedence over budgetHit. | [optional] 
**target_bid** | **float, none_type** | The target bid amount for the line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


