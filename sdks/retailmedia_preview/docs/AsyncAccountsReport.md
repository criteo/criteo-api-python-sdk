# AsyncAccountsReport

Async Accounts report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | Account Ids to report on | 
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End date | 
**aggregation_level** | **str, none_type** | Level of aggregation, if no dimensions/metrics are provided, falls back to campaign aggregationLevel | [optional]  if omitted the server will use the default value of "campaign"
**search_term_types** | **[str], none_type** | Filter on the type of search term type: unknown, searched, entered | [optional] 
**search_term_targetings** | **[str], none_type** | Filter on the type of search term targeting: unknown, automatic, manual | [optional] 
**campaign_type** | **str, none_type** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**sales_channel** | **str, none_type** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**format** | **str, none_type** | Format of the output | [optional]  if omitted the server will use the default value of "json-compact"
**report_type** | **str, none_type** | Type of report, if no dimensions/metrics are provided, falls back to summary reportType | [optional]  if omitted the server will use the default value of "summary"
**click_attribution_window** | **str, none_type** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**view_attribution_window** | **str, none_type** | View attribution window | [optional]  if omitted the server will use the default value of "none"
**dimensions** | **[str], none_type** | List of dimensions to report on | [optional] 
**metrics** | **[str], none_type** | List of metrics to report on | [optional] 
**timezone** | **str, none_type** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


