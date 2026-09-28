# LineItemMinBids

Represents minimum bidding guidance calculated for a line item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adaptive_min_bid** | **float** | The lowest strictly positive page-type minimum in the line item&#39;s currency, or zero when no positive minimum exists. | 
**page_type_min_bids** | [**[PageTypeMinBid]**](PageTypeMinBid.md) | The minimum bidding guidance for every page type configured on the line item. | 
**adaptive_recommended_min_bid** | **float, none_type** | The bid below which Adaptive bidding validation emits a low-bid warning in the line item&#39;s currency. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


