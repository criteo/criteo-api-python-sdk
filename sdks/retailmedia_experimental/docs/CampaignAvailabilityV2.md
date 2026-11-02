# CampaignAvailabilityV2

Information about the budget model availability for a specific campaign type and buy type combination, and page types and environments supported for that combination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_model_availabilities** | **[str], none_type** | The budget models available for this campaign type and buy type combination. Presence of a value indicates that budget model is available. | [optional] 
**buy_type** | **str, none_type** | The buy type this object represents availability for | [optional] 
**campaign_type** | **str, none_type** | The type of campaign this object represents availability for | [optional] 
**valid_combinations** | [**[PageTypeCombinationV2], none_type**](PageTypeCombinationV2.md) | PageType-PageEnvironmentType pairs which are supported for this campaign-buy type combination | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


