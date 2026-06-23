# PatchMarketingCampaignBudgetAutomation

Budget automation, lets users configure budgets once at the campaign level while Criteo dynamically routes spend toward the best-performing ad sets.  Only provided fields are updated; omitted fields are left unchanged.  If \"enabled\" is omitted and only \"budgetConfiguration\" is provided, \"enabled\" defaults to false — budget automation will not be activated.  To activate budget automation, \"enabled\" must be explicitly set to true along with a valid \"budgetConfiguration\".  To deactivate, set \"enabled\" to false; \"budgetConfiguration\" can be omitted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_configuration** | [**BudgetAutomationConfiguration**](BudgetAutomationConfiguration.md) |  | [optional] 
**enabled** | **bool** | Whether budget automation is enabled for this campaign. This field is always present in the response. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


