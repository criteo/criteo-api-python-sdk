# PatchCampaignScheduledSpendLimit

Scheduled spend-limit operations for a marketing campaign (patch).  Create, update, and delete operations are applied together by the backend.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_spend_limit_creations** | [**[PatchCampaignScheduledSpendLimitCreation], none_type**](PatchCampaignScheduledSpendLimitCreation.md) | Scheduled spend limits to create. | [optional] 
**scheduled_spend_limit_deletions** | [**[PatchCampaignScheduledSpendLimitDeletion], none_type**](PatchCampaignScheduledSpendLimitDeletion.md) | Scheduled spend limits to delete. | [optional] 
**scheduled_spend_limit_updates** | [**[PatchCampaignScheduledSpendLimitUpdate], none_type**](PatchCampaignScheduledSpendLimitUpdate.md) | Scheduled spend limits to update. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


