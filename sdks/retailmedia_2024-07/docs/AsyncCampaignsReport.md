# AsyncCampaignsReport

Async Campaigns report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End date | 
**ids** | **[str]** | Campaign ids to report on | [optional] 
**id** | **str** | Campaign id to report on | [optional] 
**search_term_types** | **[str]** | Filter on the type of search term type: unknown, searched, entered | [optional] 
**search_term_targetings** | **[str]** | Filter on the type of search term targeting: unknown, automatic, manual | [optional] 
**campaign_type** | **str** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**sales_channel** | **str** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**format** | **str** | Format of the output | [optional]  if omitted the server will use the default value of "json-compact"
**report_type** | **str** | Type of report, if no dimensions/metrics are provided, falls back to summary reportType | [optional]  if omitted the server will use the default value of "summary"
**click_attribution_window** | **str** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**view_attribution_window** | **str** | View attribution window | [optional]  if omitted the server will use the default value of "none"
**dimensions** | **[str]** | List of dimensions to report on | [optional] 
**metrics** | **[str]** | List of metrics to report on | [optional] 
**timezone** | **str** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


