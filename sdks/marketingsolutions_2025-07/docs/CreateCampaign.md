# CreateCampaign

Campaign create model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str, none_type** | Advertiser ID this campaign belongs to (string-encoded integer). | 
**goal** | **str** | Goal of the campaign                Serialized values are {Unspecified}, {Acquisition} and {Retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. | 
**name** | **str, none_type** | Name of the campaign | 
**spend_limit** | [**CreateCampaignSpendLimit**](CreateCampaignSpendLimit.md) |  | 
**budget_automation** | [**BudgetAutomation**](BudgetAutomation.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


