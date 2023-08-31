# AttributedTransactionsReport

Attributed transactions report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account id to report on | 
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End Date | 
**campaign_ids** | **[str], none_type** | Campaign ids to report on | [optional] 
**line_item_ids** | **[str], none_type** | Line item ids to report on | [optional] 
**dimensions** | **[str], none_type** | List of dimensions to report on | [optional] 
**metrics** | **[str], none_type** | List of metrics to report on | [optional] 
**timezone** | **str, none_type** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**click_attribution_window** | **str, none_type** | Click Attribution Window | [optional]  if omitted the server will use the default value of "7D"
**view_attribution_window** | **str, none_type** | View Attribution window | [optional]  if omitted the server will use the default value of "none"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


