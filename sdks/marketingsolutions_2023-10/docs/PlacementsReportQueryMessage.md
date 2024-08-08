# PlacementsReportQueryMessage

This is the message defining the query for Placements report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **str** | The comma-separated list of advertiser ids. | 
**dimensions** | **[str]** | The dimensions for the report. | 
**metrics** | **[str]** | The list of metrics to report. | 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**format** | **str** | The file format of the generated report: csv, xml, excel or json. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**campaign_ids** | **str, none_type** | The comma-separated list of campaign ids. | [optional] 
**adset_ids** | **str, none_type** | The comma-separated list of adSet ids. | [optional] 
**environment** | **str, none_type** | Type of environment: Web, Android or iOS. | [optional] 
**placement** | **str, none_type** | Filter the value of the placement | [optional] 
**disclosed** | **bool, none_type** | Returns disclosed or undisclosed placements. | [optional]  if omitted the server will use the default value of True
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


