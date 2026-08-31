# ShareOfVoiceInsight

Parameters of a Share of Voice insight.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account ID the insight report is generated for. | 
**dimensions** | **[str]** | Dimensions to report on. | 
**end_date** | **str** | End date of the report, in ISO 8601 format (YYYY-MM-DD). | 
**metrics** | **[str]** | Metrics to report on. | 
**start_date** | **str** | Start date of the report, in ISO 8601 format (YYYY-MM-DD). | 
**aggregation_level** | **str** | Aggregation level of the report. Allowed values: &#x60;category&#x60;, &#x60;keyword&#x60;. Defaults to &#x60;category&#x60;. | [optional]  if omitted the server will use the default value of "category"
**filters** | [**ShareOfVoiceFilters**](ShareOfVoiceFilters.md) |  | [optional] 
**format** | **str** | Output format of the report. Allowed values: &#x60;json&#x60;, &#x60;json-compact&#x60;, &#x60;json-newline&#x60;, &#x60;csv&#x60;. Defaults to &#x60;json-compact&#x60;. | [optional]  if omitted the server will use the default value of "json-compact"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


