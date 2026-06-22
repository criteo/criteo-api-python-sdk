# PlacementsReportQueryMessage

This is the message defining the query for Placements report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **str** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. | 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**dimensions** | **[str]** | List of dimensions for the report. At least one dimension should be provided. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. | 
**metrics** | **[str]** | List of metrics for the report. At least one dimension should be provided. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. | 
**adset_ids** | **str, none_type** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. | [optional] 
**campaign_ids** | **str, none_type** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. | [optional] 
**disclosed** | **bool** | Optionally returns disclosed or undisclosed placements. | [optional]  if omitted the server will use the default value of True
**environment** | **str, none_type** | Optional type of environment to filter on. If empty, all environments will be included. | [optional] 
**format** | **str** | Optional file format of the generated report. | [optional]  if omitted the server will use the default value of "json"
**placement** | **str, none_type** | Optional filter on a specific placement domain name. If empty, all placements will be included. | [optional] 
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


