# CampaignResponseModel

A Retail Media Campaign used to represent an advertiser's marketing objective

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**attribution_settings** | [**AttributionSettingsModel**](AttributionSettingsModel.md) |  | 
**buy_type** | **str** | Buy type of campaign, set only on creation. | 
**campaign_type** | **str** | Type of campaign, set only on creation. | 
**created_at** | **datetime** |  | 
**drawable_balance_ids** | **[str]** |  | 
**name** | **str** |  | 
**status** | **str** | Campaign status, derived from the status of Line Items it holds; active if at least  one line item is active. | 
**updated_at** | **datetime** |  | 
**bill_by_retailer_id** | **str, none_type** |  | [optional] 
**budget_details** | [**BudgetDetailsModel**](BudgetDetailsModel.md) |  | [optional] 
**company_name** | **str, none_type** |  | [optional] 
**id** | **str, none_type** |  | [optional] 
**objective** | **str, none_type** | Dynamic Campaign Budgets control: manual keeps today&#39;s behavior; clicks, conversion and  revenue activate campaign-level budget allocation. Impressions is the Onsite Display  objective. | [optional] 
**on_behalf_company_name** | **str, none_type** |  | [optional] 
**schedule_details** | [**ScheduleDetailsModel**](ScheduleDetailsModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


