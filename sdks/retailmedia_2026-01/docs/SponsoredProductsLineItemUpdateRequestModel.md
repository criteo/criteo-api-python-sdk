# SponsoredProductsLineItemUpdateRequestModel

A request to update a Sponsored Products Line Item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_daily_pacing** | **bool** | True if daily pacing is automatic, false if manual. | 
**name** | **str** | The name of this line item. | 
**start_date** | **datetime** | The date and time when the line item starts running. | 
**status** | **str** | The current status of the line item. | 
**bid_strategy** | **str** | The bid strategy for the line item. | [optional]  if omitted the server will use the default value of "manual"
**budget** | **float, none_type** | The total budget allocated for this line item. | [optional] 
**daily_pacing** | **float, none_type** | The daily pacing amount for the line item. | [optional] 
**end_date** | **datetime, none_type** | The date and time when the line item stops running. | [optional] 
**flight_schedule** | [**FlightSchedule**](FlightSchedule.md) |  | [optional] 
**max_bid** | **float, none_type** | The maximum bid amount for the line item. | [optional] 
**monthly_pacing** | **float, none_type** | The monthly pacing amount for the line item. | [optional] 
**optimization_strategy** | **str** | The optimization strategy for the line item. | [optional]  if omitted the server will use the default value of "conversion"
**target_bid** | **float, none_type** | The target bid amount for the line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


