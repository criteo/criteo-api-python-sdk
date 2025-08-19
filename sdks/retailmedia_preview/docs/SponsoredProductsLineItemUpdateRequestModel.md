# SponsoredProductsLineItemUpdateRequestModel

A request to update a Sponsored Products Line Item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_daily_pacing** | **bool** |  | 
**name** | **str** |  | 
**start_date** | **datetime** |  | 
**status** | **str** | Status of a line item. | 
**target_bid** | **float** |  | 
**bid_strategy** | **str** |  | [optional]  if omitted the server will use the default value of "conversion"
**budget** | **float, none_type** |  | [optional] 
**daily_pacing** | **float, none_type** |  | [optional] 
**end_date** | **datetime, none_type** |  | [optional] 
**flight_schedule** | [**FlightSchedule**](FlightSchedule.md) |  | [optional] 
**max_bid** | **float, none_type** |  | [optional] 
**monthly_pacing** | **float, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


