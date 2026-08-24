# CampaignCreateModel

An object that represents the available options to set when creating a Retail Media Campaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_type** | **str** | Type of campaign, set only on creation. | 
**name** | **str** |  | 
**buy_type** | **str** | Buy type of campaign, set only on creation. Auction is the only buy type currently supported. | defaults to "Auction"
**attribution_settings** | [**AttributionSettingsCreateModel**](AttributionSettingsCreateModel.md) |  | [optional] 
**bill_by_retailer_id** | **str, none_type** |  | [optional] 
**budget_details** | [**BudgetDetailsCreateModel**](BudgetDetailsCreateModel.md) |  | [optional] 
**company_name** | **str, none_type** |  | [optional] 
**drawable_balance_ids** | **[str], none_type** |  | [optional] 
**objective** | **str, none_type** |  | [optional] 
**on_behalf_company_name** | **str, none_type** |  | [optional] 
**schedule_details** | [**ScheduleDetailsCreateModel**](ScheduleDetailsCreateModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


