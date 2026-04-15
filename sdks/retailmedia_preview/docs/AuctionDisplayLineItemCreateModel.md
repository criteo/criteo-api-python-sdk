# AuctionDisplayLineItemCreateModel

Model for creating an auction display line item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidding** | [**BiddingRequest**](BiddingRequest.md) |  | 
**budget** | **float** | The budget for the line item | 
**creative_ids** | **[str]** | The list of creative ids associated with the line item. | 
**is_active** | **bool** | Indicates whether the line item is active. | 
**media_type** | **str** | The media type of the line item. | 
**name** | **str** | The name of the line item. | 
**pacing** | [**LineItemPacingRequest**](LineItemPacingRequest.md) |  | 
**page_types** | **[str]** | The list of page types configured for the line item. | 
**product_ids** | **[str]** | The list of product ids associated with the line item. | 
**retailer_id** | **str** | The retailer id of the associated retailer. | 
**start_date** | **datetime** | The start date of the line item. | 
**end_date** | **datetime, none_type** | The end date of the line item. | [optional] 
**frequency_capping** | [**LineItemCappingTargetRequest**](LineItemCappingTargetRequest.md) |  | [optional] 
**targets** | [**TargetsRequest**](TargetsRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


