# ScheduleDetailsUpdateModel

New flight dates for a campaign that owns them: a SponsoredProducts or OnsiteDisplay Auction  campaign. Omit the whole node to leave the schedule unchanged; when present, both dates are  required together. Any other OnsiteDisplay campaign derives its dates from its line items and  rejects this node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | New campaign end date. Pass exactly {9999-12-30T00:00:00Z} to make a SponsoredProducts  campaign run indefinitely; any other value is a real end date. An OnsiteDisplay Auction  campaign cannot run indefinitely and rejects that date. | 
**start_date** | **datetime** | New campaign start date. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


