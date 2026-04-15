# AuctionDisplayLineItemSearchModel

Model for searching auction display line items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str, none_type** | search for line items within a specific campaign | [optional] 
**is_proposal** | **bool** | Indicating whether to filter for proposal line items.  Default is false, which means only active line items will be returned. | [optional]  if omitted the server will use the default value of False
**line_item_ids** | **[str], none_type** | The list of line item IDs to filter by. | [optional] 
**retailer_id** | **str, none_type** | search for line items for a specific retailer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


