# TransactionsReportQueryMessage

This is the message defining the query for Transaction report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**format** | **str** | The file format of the generated report: csv, xml, excel or json. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**advertiser_ids** | **str, none_type** | The comma-separated list of advertiser ids. If empty, all the advertisers in the portfolio will be used | [optional] 
**event_type** | **str, none_type** | Apply a filter on Event type . | [optional] 
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


