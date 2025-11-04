# SponsoredProductsLineItemCreateRequestModel

Model to create a retail media auction line item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the line item. | 
**start_date** | **datetime** | The date and time when the line item starts running. | 
**target_retailer_id** | **str** | The ID of the retailer to target for this line item. | 
**bid_strategy** | **str** | The bidding strategy for this line item.  Default value is manual. | [optional]  if omitted the server will use the default value of "manual"
**budget** | **float, none_type** | The total budget allocated for this line item. | [optional] 
**daily_pacing** | **float, none_type** | The daily pacing limit for budget spending. | [optional] 
**end_date** | **datetime, none_type** | The date and time when the line item stops running. | [optional] 
**flight_schedule** | [**FlightSchedule**](FlightSchedule.md) |  | [optional] 
**is_auto_daily_pacing** | **bool** | Indicates whether automatic daily pacing is enabled.  Default value is false. | [optional]  if omitted the server will use the default value of False
**keyword_strategy** | **str, none_type** | The keyword targeting strategy for this line item. | [optional] 
**max_bid** | **float, none_type** | The maximum bid amount allowed for this line item. | [optional] 
**monthly_pacing** | **float, none_type** | The monthly pacing limit for budget spending. | [optional] 
**optimization_strategy** | **str** | The optimization strategy to use for this line item.  Default value is Conversion. | [optional]  if omitted the server will use the default value of "conversion"
**target_bid** | **float, none_type** | The target bid amount for the line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


