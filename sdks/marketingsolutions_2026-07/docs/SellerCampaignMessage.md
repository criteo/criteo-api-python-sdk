# SellerCampaignMessage

A seller-campaign links a seller to a campaign, defining the CPC bid. A seller can participate in multiple campaigns, and a campaign can have multiple sellers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid** | **float, none_type** | Cost-per-click bid in the advertiser&#39;s currency. Null means no CPC is defined (seller-campaign will be suspended with NoCpcDefined). Set to 0 to stop delivery. | [optional] 
**campaign_id** | **int** | Identifier of the campaign this seller participates in | [optional] 
**id** | **str** | Composite identifier in format {sellerId}.{campaignId} | [optional] [readonly] 
**product_set** | [**SellerCampaignProductSet**](SellerCampaignProductSet.md) |  | [optional] 
**seller_id** | **str** | Unique identifier of the seller (merchant) | [optional] 
**suspended_since** | **datetime, none_type** | Timestamp when the seller-campaign was suspended. Null means the seller-campaign is active. | [optional] 
**suspension_reasons** | [**[SellerCampaignSuspensionReason], none_type**](SellerCampaignSuspensionReason.md) | List of reasons why the seller-campaign is suspended. Null means the seller-campaign is active. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


