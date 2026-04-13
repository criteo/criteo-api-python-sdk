# BudgetAutomation

Budget automation, lets users configure budgets once at the campaign level while Criteo dynamically routes spend toward the best-performing ad sets.  If \"enabled\" is omitted and only \"budgetConfiguration\" is provided, \"enabled\" defaults to false — budget automation will not be activated.  To activate budget automation at creation, \"enabled\" must be explicitly set to true along with a valid \"budgetConfiguration\".  If the entire \"budgetAutomation\" object is omitted from the create request, the campaign is created with budget automation disabled.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_configuration** | [**BudgetAutomationConfiguration**](BudgetAutomationConfiguration.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


