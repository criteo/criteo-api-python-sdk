# CampaignCreateModel

An object that represents the available options to set when creating a Retail Media Campaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**DynamicBudgetCreateModel**](DynamicBudgetCreateModel.md) |  | 
**campaign_type** | **str** | Type of campaign, set only on creation. | 
**name** | **str** |  | 
**objective** | **str** | Objective the campaign is optimized for. The platform derives the line item budgets from the  campaign budget to serve it. SponsoredProducts accepts clicks, conversion and revenue;  OnsiteDisplay accepts impressions. | 
**schedule_details** | [**ScheduleDetailsCreateModel**](ScheduleDetailsCreateModel.md) |  | 
**buy_type** | **str** | Buy type of campaign, set only on creation. Auction is the only buy type currently supported. | defaults to "Auction"
**attribution_settings** | [**AttributionSettingsCreateModel**](AttributionSettingsCreateModel.md) |  | [optional] 
**bill_by_retailer_id** | **str, none_type** |  | [optional] 
**company_name** | **str, none_type** |  | [optional] 
**drawable_balance_ids** | **[str], none_type** |  | [optional] 
**on_behalf_company_name** | **str, none_type** |  | [optional] 
**regulated_category** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


