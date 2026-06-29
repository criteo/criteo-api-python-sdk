# AsyncPerformanceReport

Create payload attributes for a performance DSP analytics async report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | **[str]** | Required output grouping fields. Empty array means no grouping fields. At least one of dimensions or metrics must be non-empty. | 
**end_date** | **date** | Required inclusive report end date in YYYY-MM-DD format. Must be greater than or equal to startDate. | 
**filters** | [**PerformanceReportFilters**](PerformanceReportFilters.md) |  | 
**metrics** | **[str]** | Required output measure fields. Empty array means no measure fields. At least one of dimensions or metrics must be non-empty. | 
**start_date** | **date** | Required inclusive report start date in YYYY-MM-DD format. | 
**click_attribution_window** | **str** | Optional click attribution window. | [optional]  if omitted the server will use the default value of "none"
**format** | **str** | Output format. If omitted, json-compact is used. | [optional]  if omitted the server will use the default value of "json-compact"
**timezone** | **str** | Optional time zone identifier. If omitted, UTC is used. If provided, it must be valid. | [optional]  if omitted the server will use the default value of "UTC"
**view_attribution_window** | **str** | Optional view attribution window. | [optional]  if omitted the server will use the default value of "none"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


