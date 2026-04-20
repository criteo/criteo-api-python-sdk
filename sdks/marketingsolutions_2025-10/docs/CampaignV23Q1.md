# CampaignV23Q1

Campaign read model                The {id} field is the campaign identifier (string-encoded integer).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str, none_type** | Advertiser id of the campaign (string-encoded integer) | [optional] 
**budget_automation** | [**CampaignBudgetAutomationV23Q1**](CampaignBudgetAutomationV23Q1.md) |  | [optional] 
**goal** | **str, none_type** | Goal of the campaign                Serialized values are {unspecified}, {acquisition} and {retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. | [optional] 
**id** | **str, none_type** | Id of the entity (duplicate of the parent id). | [optional] 
**name** | **str, none_type** | Name of the campaign | [optional] 
**spend_limit** | [**CampaignSpendLimitV23Q1**](CampaignSpendLimitV23Q1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


