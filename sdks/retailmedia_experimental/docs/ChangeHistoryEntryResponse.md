# ChangeHistoryEntryResponse

A single configuration change.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_role** | [**ActorRole**](ActorRole.md) |  | 
**changes** | [**[ChangedField]**](ChangedField.md) | Old and new values for each field changed as part of this event. | 
**entity** | [**ChangeHistoryEntryResponseEntity**](ChangeHistoryEntryResponseEntity.md) |  | 
**event_type** | **str** | Semantic type of the configuration change, &#x60;&lt;entityType&gt;&lt;Action&gt;&#x60; style — for example &#x60;campaignCreated&#x60;, &#x60;lineItemUpdated&#x60;, &#x60;balanceUpdated&#x60;. Additional values may be returned.  | 
**occurred_at** | **datetime** | UTC timestamp when the change occurred (ISO-8601). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


