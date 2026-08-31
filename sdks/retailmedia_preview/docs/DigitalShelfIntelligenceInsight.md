# DigitalShelfIntelligenceInsight

Parameters of a Digital Shelf Intelligence insight.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account ID the insight report is generated for. | 
**aggregation_level** | **str** | Aggregation level of the report. Allowed values: &#x60;brand&#x60;, &#x60;sku&#x60;. | 
**end_date** | **str** | End date of the report (inclusive), in ISO 8601 format (YYYY-MM-DD).  Adjusted to the Sunday of the week containing the provided date. | 
**metrics** | **[str]** | Metrics to report on. | 
**start_date** | **str** | Start date of the report (inclusive), in ISO 8601 format (YYYY-MM-DD).  Adjusted to the Monday of the week containing the provided date. | 
**filters** | [**DigitalShelfIntelligenceFilters**](DigitalShelfIntelligenceFilters.md) |  | [optional] 
**format** | **str** | Output format of the report. Allowed values: &#x60;json&#x60;, &#x60;json-compact&#x60;, &#x60;json-newline&#x60;, &#x60;csv&#x60;. Defaults to &#x60;json-compact&#x60;. | [optional]  if omitted the server will use the default value of "json-compact"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


