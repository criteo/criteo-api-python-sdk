# TransactionsReportQueryMessage

This is the message defining the query for Transaction report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **str** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. | 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. | 
**event_type** | **str, none_type** | Optional event type to filter on. If empty, all event types will be included. | [optional] 
**format** | **str** | Optional file format of the generated report. | [optional]  if omitted the server will use the default value of "json"
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


