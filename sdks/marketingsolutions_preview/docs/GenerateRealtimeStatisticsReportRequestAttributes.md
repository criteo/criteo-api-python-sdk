# GenerateRealtimeStatisticsReportRequestAttributes

This is the message defining the query for Realtime report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | List of advertiser ids to report on. | 
**adset_ids** | **[str], none_type** | List of adset ids to filter. | [optional] 
**campaign_ids** | **[str], none_type** | List of campaign ids to filter. | [optional] 
**currency** | **str, none_type** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional]  if omitted the server will use the default value of "EUR"
**dimensions** | **[str], none_type** | List of dimensions for the report. | [optional]  if omitted the server will use the default value of ["AdvertiserId","Advertiser","CampaignId","Campaign","AdsetId","Adset","Day","Hour"]
**lookback_window** | **int** | The number of hours to consider in the past. | [optional]  if omitted the server will use the default value of 12
**metrics** | **[str], none_type** | List of metrics for the report. | [optional]  if omitted the server will use the default value of ["Displays","Clicks","Cost"]
**timezone** | **str, none_type** | The timezone used for the report. | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


