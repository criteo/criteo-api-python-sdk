# PatchCampaignV27Q1

Campaign patch model.  The campaign identifier is provided in the resource {id} field (string-encoded integer) and is required.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_automation** | [**PatchMarketingCampaignBudgetAutomationV27Q1**](PatchMarketingCampaignBudgetAutomationV27Q1.md) |  | [optional] 
**name** | **str, none_type** | New name of the campaign. Omit to leave unchanged. Must not be empty when provided. | [optional] 
**scheduled_spend_limit** | [**PatchCampaignScheduledSpendLimitV27Q1**](PatchCampaignScheduledSpendLimitV27Q1.md) |  | [optional] 
**spend_limit** | [**PatchCampaignSpendLimitV27Q1**](PatchCampaignSpendLimitV27Q1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


