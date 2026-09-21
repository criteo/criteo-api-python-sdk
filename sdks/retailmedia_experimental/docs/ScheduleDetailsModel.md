# ScheduleDetailsModel

Flight dates of the campaign. A SponsoredProducts campaign and an OnsiteDisplay Auction  campaign report the dates they hold themselves; any other OnsiteDisplay campaign reports the  dates derived from its line items, which it cannot set through this API. A SponsoredProducts  campaign that runs indefinitely reports the documented indefinite end date rather than  omitting it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime, none_type** | Campaign end date. A SponsoredProducts campaign that runs indefinitely reports  {9999-12-30T00:00:00Z}. An OnsiteDisplay campaign reports a real end date, and omits  it when neither the campaign nor its line items carry one. | [optional] 
**start_date** | **datetime, none_type** | Campaign start date. Defaults to the creation timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


