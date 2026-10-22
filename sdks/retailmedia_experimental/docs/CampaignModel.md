# CampaignModel

A campaign. A campaign groups line items that share attribution settings, flight dates and  budget.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | Account ID associated with the campaign, generated internally by Criteo. | [optional] 
**attribution_settings** | [**AttributionSettingsModel**](AttributionSettingsModel.md) |  | [optional] 
**bill_by_retailer_id** | **str, none_type** | The retailer this campaign is associated with, set only on creation. Required when using a  retailer budget balance. | [optional] 
**budget** | [**CampaignBudgetModel**](CampaignBudgetModel.md) |  | [optional] 
**buy_type** | **str, none_type** | Buy type of campaign, set only on creation. | [optional] 
**campaign_type** | **str, none_type** | Type of campaign, set only on creation. | [optional] 
**company_name** | **str, none_type** | This optional field, exclusively accessible to marketplaces within the European Union (in  compliance with the Digital Service Act - DSA), will display the name of the company  associated with the advertisement. | [optional] 
**created_at** | **datetime, none_type** | Timestamp of campaign creation, in UTC. | [optional] 
**id** | **str, none_type** | Campaign ID, generated internally by Criteo. | [optional] 
**name** | **str, none_type** | Campaign name; must be unique within an Account. | [optional] 
**objective** | **str, none_type** | Objective of a campaign. | [optional] 
**on_behalf_company_name** | **str, none_type** | This optional field, exclusively accessible to marketplaces within the European Union (in  compliance with the Digital Service Act - DSA), will display the name of the company (on  behalf of companyName) associated with the advertisement. | [optional] 
**regulated_category** | **str, none_type** | Regulated category the campaign advertises in, set only on creation. | [optional] 
**schedule_details** | [**ScheduleDetailsModel**](ScheduleDetailsModel.md) |  | [optional] 
**status** | **str, none_type** | Campaign status, derived from the status of Line Items it holds; active if at least  one line item is active. | [optional] 
**updated_at** | **datetime, none_type** | Timestamp of last campaign update, in UTC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


