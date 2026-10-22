# CampaignBudgetModel

Financial intent of a campaign.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float, none_type** | Total the campaign may spend over its flight. Null when the campaign is uncapped. | [optional] 
**cappings** | [**[BudgetCappingModel], none_type**](BudgetCappingModel.md) | Per-period ceilings. Only capped periods are reported. | [optional] 
**memo** | **str, none_type** | Note recorded with the latest budget change. | [optional] 
**pacing** | [**PacingModel**](PacingModel.md) |  | [optional] 
**remaining** | **float, none_type** | Amount left under the cap. Null when the campaign is uncapped. | [optional] 
**spent** | **float, none_type** | Amount spent so far. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


