# AsyncAttributedTransactionsReport

Create payload attributes for an attributed-transactions async report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | **[str]** |  | 
**end_date** | **datetime** |  | 
**filters** | [**AttributedTransactionsReportFilters**](AttributedTransactionsReportFilters.md) |  | 
**metrics** | **[str]** |  | 
**start_date** | **datetime** |  | 
**click_attribution_window** | **str** |  | [optional] 
**click_match_level** | **str** |  | [optional]  if omitted the server will use the default value of "campaign"
**format** | **str** |  | [optional] 
**timezone** | **str** |  | [optional]  if omitted the server will use the default value of "UTC"
**view_attribution_window** | **str** |  | [optional] 
**view_match_level** | **str** |  | [optional]  if omitted the server will use the default value of "campaign"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


