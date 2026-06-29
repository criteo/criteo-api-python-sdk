# GenerateAllProductsReportRequestAttributes

This is the message defining the query for AllProducts report (async export)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | The list of advertiser account IDs. | 
**start_date** | **datetime** | Start date of the report. ISO 8601 date-time (UTC). | 
**ad_set_ids** | **[str], none_type** | The list of ad set ids. | [optional] 
**campaign_ids** | **[str], none_type** | The list of campaign ids. | [optional] 
**currency** | **str, none_type** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional]  if omitted the server will use the default value of "EUR"
**dimensions** | **[str], none_type** | The dimensions for the report. | [optional] 
**end_date** | **datetime, none_type** | End date of the report. ISO 8601 date-time (UTC). Defaults to Now if not provided. | [optional] 
**file_format** | **str, none_type** | The output file format. Supported: csv, json. | [optional]  if omitted the server will use the default value of "csv"
**metrics** | **[str], none_type** | The list of metrics to report. | [optional] 
**seller_ids** | **[str], none_type** | The list of seller ids. | [optional] 
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


