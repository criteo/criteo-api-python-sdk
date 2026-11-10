# LineItemMinBidResponse

Represents the minimum bid guidance of a line item using Adaptive bidding.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidding_type** | **str** | The type of bidding the guidance applies to. It matches the populated details:  Criteo.RetailMedia.LineItem.Bid.Contract.V1.Models.BiddingType.CpmBidding for CPM details and Criteo.RetailMedia.LineItem.Bid.Contract.V1.Models.BiddingType.CpcBidding for CPC details. | 
**cpc_min_bid_details** | [**CpcMinBidDetails**](CpcMinBidDetails.md) |  | [optional] 
**cpm_min_bid_details** | [**CpmMinBidDetails**](CpmMinBidDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


