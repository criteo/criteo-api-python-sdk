# StatisticsReportQueryMessage

This is the message defining the query for Adset report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | **[str]** | The dimensions for the report. | 
**metrics** | **[str]** | The list of metrics to report. | 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**format** | **str** | The file format of the generated report: csv, xml, excel or json. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**advertiser_ids** | **str, none_type** | The comma-separated list of advertiser ids. If empty, all the advertisers in the portfolio will be used | [optional] 
**ad_set_ids** | **[str], none_type** | list of adSets ids. If empty, all the adSets will be fetched | [optional] 
**ad_set_names** | **[str], none_type** | list of adSets names. If empty, all the adSets will be fetched | [optional] 
**ad_set_status** | **[str], none_type** | list of adSets status. If empty, all the adSets will be fetched | [optional] 
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


