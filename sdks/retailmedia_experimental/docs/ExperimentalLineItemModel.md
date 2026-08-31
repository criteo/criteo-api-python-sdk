# ExperimentalLineItemModel

A unit of ad delivery configuration within a campaign. It defines how a specific subset of ads  is targeted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str, none_type** | The campaign id of the associated campaign. | [optional] 
**conquesting_settings** | [**ExperimentalConquestingSettingsModel**](ExperimentalConquestingSettingsModel.md) |  | [optional] 
**effective_flight_dates** | [**ExperimentalFlightDatesModel**](ExperimentalFlightDatesModel.md) |  | [optional] 
**funding_status** | **str, none_type** | Indicates whether the line item is funded. | [optional] 
**is_paused** | **bool, none_type** | Indicates whether the line item is paused. | [optional] 
**line_item_id** | **str, none_type** | The unique identifier of the line item. | [optional] 
**name** | **str, none_type** | The name of the line item. | [optional] 
**onsite_display_details** | [**ExperimentalOnsiteDisplayLineItemDetails**](ExperimentalOnsiteDisplayLineItemDetails.md) |  | [optional] 
**retailer_id** | **str, none_type** | The retailer id of the associated retailer. | [optional] 
**serve_to_opt_out_user** | **bool, none_type** | Whether ads are served to users who have opted out of personalization. | [optional] 
**type** | **str, none_type** | The type of the line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


