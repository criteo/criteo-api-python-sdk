# AuctionDisplayLineItem

Represents the response model for an auction display line item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidding** | [**Bidding**](Bidding.md) |  | 
**budget** | **float** | The budget for the line item | 
**campaign_id** | **str** | The identifier of the campaign to which the line item belongs. | 
**creative_ids** | **[str]** | The list of creative IDs associated with the line item. | 
**is_proposal** | **bool** | Indicates whether the line item is a proposal. | 
**media_type** | **str** | The media type of the line item (e.g., display or video). | 
**name** | **str** | The name of the line item. | 
**pacing** | [**LineItemPacing**](LineItemPacing.md) |  | 
**page_types** | **[str]** | The list of page types where the line item can be displayed. | 
**product_ids** | **[str]** | The list of product IDs targeted by the line item. | 
**retailer_id** | **str** | The identifier of the retailer associated with the line item. | 
**start_date** | **datetime** | The start date of the line item. | 
**status** | **str** | The current status of the line item. | 
**end_date** | **datetime, none_type** | The end date of the line item. | [optional] 
**frequency_capping** | [**LineItemCappingTarget**](LineItemCappingTarget.md) |  | [optional] 
**targets** | [**Targets**](Targets.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


