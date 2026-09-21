# ScheduleDetailsCreateModel

Flight dates the campaign holds itself. A SponsoredProducts or OnsiteDisplay Auction campaign  owns its dates and requires this node; any other OnsiteDisplay campaign derives its dates from  its line items and rejects it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | Campaign end date. Pass exactly {9999-12-30T00:00:00Z} for a SponsoredProducts campaign that  runs indefinitely; any other value, including a neighbouring far-future date, is a real end date.  An OnsiteDisplay Auction campaign cannot run indefinitely and rejects that date. | 
**start_date** | **datetime** | Campaign start date. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


