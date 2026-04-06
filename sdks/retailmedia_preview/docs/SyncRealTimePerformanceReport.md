# SyncRealTimePerformanceReport

Real Time Performance report body request (one sheeter: startDate, endDate (optional), RetailerIds, accountIds, campaignIds, lineItemIds, dimensions, metrics, timezones).  Extends SyncReport only (no default filters); adds entry filter arrays.  Dimensions and metrics are restricted to Criteo.RetailMedia.Exam.Reporting.Resources.Models.Inputs.RealTimePerformance.SyncRealTimeDimension and Criteo.RetailMedia.Exam.Reporting.Resources.Models.Inputs.RealTimePerformance.SyncRealTimeMetric; invalid values cause deserialization to fail.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date (real-time: must be within the last 7 days). | 
**account_ids** | **[str]** | Account ids to filter (plural; base has AccountId for single account). | [optional] 
**campaign_ids** | **[str]** | Campaign ids to filter. | [optional] 
**dimensions** | **[str]** | List of dimensions to report on (real-time: at least one required). Only values from Criteo.RetailMedia.Exam.Reporting.Resources.Models.Inputs.RealTimePerformance.SyncRealTimeDimension are valid. | [optional] 
**end_date** | **datetime** | Optional end date/time (inclusive in the request timezone). If empty or not provided, no end date filter is applied.  When provided, used as the inclusive upper bound for the report range.  Hides base Report.EndDate so this report can treat end date as optional (no [Required]). | [optional] 
**line_item_ids** | **[str]** | Line item ids to filter. | [optional] 
**metrics** | **[str]** | List of metrics to report on (real-time: at least one required). Only values from Criteo.RetailMedia.Exam.Reporting.Resources.Models.Inputs.RealTimePerformance.SyncRealTimeMetric are valid (billableImpressions, billableClicks, spend). | [optional] 
**retailer_ids** | **[str]** | Retailer ids to filter. This is not used for security, so no need to check for &gt; 0 elements | [optional] 
**timezone** | **str** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


