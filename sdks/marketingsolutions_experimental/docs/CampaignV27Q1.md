# CampaignV27Q1

Campaign read model                The {id} field is the campaign identifier (string-encoded integer).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str, none_type** | Advertiser id of the campaign (string-encoded integer) | [optional] 
**budget_automation** | [**CampaignBudgetAutomationV27Q1**](CampaignBudgetAutomationV27Q1.md) |  | [optional] 
**goal** | **str, none_type** | Goal of the campaign                Serialized values are {unspecified}, {acquisition} and {retention}.                Acquisition and retention are defined as follows:  - Acquisition: campaign with the goal of acquiring new customers. The success of an acquisition campaign is measured by the number of new customers it brings.  - Retention: campaign with the goal of retaining existing customers. The success of a retention campaign is measured by the number of existing customers it retains. | [optional] 
**name** | **str, none_type** | Name of the campaign | [optional] 
**scheduled_spend_limits** | [**[CampaignScheduledSpendLimitV27Q1], none_type**](CampaignScheduledSpendLimitV27Q1.md) | Spend limits scheduled to become active in the future. Empty when the campaign has no scheduled spend limits. | [optional] 
**seller_id** | **str, none_type** | Optional marketplace seller id of the campaign (string-encoded long) | [optional] 
**spend_limit** | [**CampaignSpendLimitV27Q1**](CampaignSpendLimitV27Q1.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


