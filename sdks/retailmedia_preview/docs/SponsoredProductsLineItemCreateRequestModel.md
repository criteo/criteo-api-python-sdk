# SponsoredProductsLineItemCreateRequestModel

Model to create a retail media auction line item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**start_date** | **datetime** |  | 
**target_retailer_id** | **str** |  | 
**bid_strategy** | **str** |  | [optional]  if omitted the server will use the default value of "Conversion"
**budget** | **float, none_type** |  | [optional] 
**conquesting_adstrategy_enabled** | **bool, none_type** |  | [optional] 
**daily_pacing** | **float, none_type** |  | [optional] 
**defensive_adstrategy_enabled** | **bool, none_type** |  | [optional] 
**end_date** | **datetime, none_type** |  | [optional] 
**flight_schedule** | [**FlightSchedule**](FlightSchedule.md) |  | [optional] 
**is_auto_daily_pacing** | **bool** |  | [optional]  if omitted the server will use the default value of False
**max_bid** | **float, none_type** |  | [optional] 
**monthly_pacing** | **float, none_type** |  | [optional] 
**neutral_adstrategy_enabled** | **bool, none_type** |  | [optional] 
**target_bid** | **float, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


