# LineItemReport

Line item report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account id to report on | 
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End Date | 
**line_item_ids** | **[str]** | Line item ids to report on | [optional] 
**metrics** | **[str]** | List of metrics to report on | [optional] 
**dimensions** | **[str]** | List of dimensions to report on | [optional] 
**report_type** | **str** | Type of report, if no Dimensions / Metrics are provided fall back to summary reportType | [optional] 
**timezone** | **str** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**click_attribution_window** | **str** | Click Attribution Window | [optional]  if omitted the server will use the default value of "7D"
**view_attribution_window** | **str** | View Attribution window | [optional]  if omitted the server will use the default value of "none"
**campaign_type** | **str** | Filter the type of campaign to report on | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


