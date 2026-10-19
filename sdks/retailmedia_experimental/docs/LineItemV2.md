# LineItemV2

A unit of ad delivery configuration within a campaign. It defines how a specific subset of ads  is targeted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_status** | **str** | Indicates whether the line item has budget headroom to serve ads. | 
**campaign_id** | **str, none_type** | The campaign id of the associated campaign. | 
**is_paused** | **bool** | Indicates whether the line item is paused. | 
**line_item_id** | **str, none_type** | The unique identifier of the line item. | 
**name** | **str, none_type** | The name of the line item. | 
**retailer_id** | **str, none_type** | The retailer id of the associated retailer. | 
**serve_to_opt_out_user** | **bool** | Whether ads are served to users who have opted out of personalization. | 
**type** | **str** | The type of the line item. | 
**effective_flight_dates** | [**ExternalFlightDatesModelV2**](ExternalFlightDatesModelV2.md) |  | [optional] 
**onsite_display_details** | [**OnsiteDisplayLineItemDetailsV2**](OnsiteDisplayLineItemDetailsV2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


