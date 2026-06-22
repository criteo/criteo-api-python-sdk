# GenerateRealtimeStatisticsReportRequestAttributes

This is the message defining the query for Realtime report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | List of advertiser IDs to report on. The advertisers must already exist. Between 1 and 10 advertiser IDs can be provided. | 
**adset_ids** | **[str], none_type** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. | [optional] 
**campaign_ids** | **[str], none_type** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. | [optional] 
**currency** | **str, none_type** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional]  if omitted the server will use the default value of "EUR"
**dimensions** | **[str], none_type** | List of dimensions for the report. If not included, the default list of dimensions will be used. | [optional]  if omitted the server will use the default value of ["AdvertiserId","Advertiser","CampaignId","Campaign","AdsetId","Adset","Day","Hour"]
**lookback_window** | **int** | Optional number of hours to consider in the past. | [optional]  if omitted the server will use the default value of 12
**metrics** | **[str], none_type** | List of metrics for the report. If included, at least one metric should be provided. | [optional]  if omitted the server will use the default value of ["Displays","Clicks","Cost"]
**timezone** | **str, none_type** | Optional timezone used for the report. | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


