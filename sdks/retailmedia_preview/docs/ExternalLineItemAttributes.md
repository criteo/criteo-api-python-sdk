# ExternalLineItemAttributes

The attributes of a Retail Media Line Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_retailer_id** | **str** |  | 
**name** | **str** |  | 
**start_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**status** | **str** |  | [optional] 
**target_bid** | **float, none_type** |  | [optional] 
**is_auto_daily_pacing** | **bool** |  | [optional]  if omitted the server will use the default value of False
**end_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | [optional] 
**max_bid** | **float, none_type** |  | [optional] 
**budget** | **float, none_type** |  | [optional] 
**monthly_pacing** | **float, none_type** |  | [optional] 
**daily_pacing** | **float, none_type** |  | [optional] 
**bid_strategy** | **str** |  | [optional]  if omitted the server will use the default value of "conversion"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


