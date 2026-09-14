# ScheduleDetailsCreateModel

Flight dates of the campaign. Applies to SponsoredProducts only; OnsiteDisplay campaigns  derive their dates from their line items and reject this node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | Campaign end date. Pass exactly {9999-12-30T00:00:00Z} for a SponsoredProducts campaign that  runs indefinitely; any other value, including a neighbouring far-future date, is a real end date. | 
**start_date** | **datetime** | Campaign start date. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


