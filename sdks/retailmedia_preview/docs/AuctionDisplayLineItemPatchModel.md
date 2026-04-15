# AuctionDisplayLineItemPatchModel

Represents a patch model for updating an auction display line item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidding** | [**BiddingRequest**](BiddingRequest.md) |  | [optional] 
**budget** | **float, none_type** | The budget for the line item | [optional] 
**campaign_id** | **str, none_type** | The identifier of the campaign to which the line item belongs. | [optional] 
**creative_ids** | **[str], none_type** | The list of creative IDs associated with the line item. | [optional] 
**end_date** | **datetime, none_type** | The end date of the line item. | [optional] 
**frequency_capping** | [**NillableOfLineItemCappingTargetRequest**](NillableOfLineItemCappingTargetRequest.md) |  | [optional] 
**is_active** | **bool, none_type** | Indicates whether the line item is active. | [optional] 
**media_type** | **str, none_type** | The media type of the line item (e.g., display or video). | [optional] 
**name** | **str, none_type** | The name of the line item. | [optional] 
**pacing** | [**LineItemPacingRequest**](LineItemPacingRequest.md) |  | [optional] 
**page_types** | **[str], none_type** | The list of page types configured for the line item. | [optional] 
**product_ids** | **[str], none_type** | The list of product IDs targeted by the line item. | [optional] 
**retailer_id** | **str, none_type** | The identifier of the retailer associated with the line item. | [optional] 
**start_date** | **datetime, none_type** | The start date of the line item. | [optional] 
**targets** | [**TargetsRequest**](TargetsRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


