# GenerateStatisticsReport

Request attributes for async statistics report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | The list of advertiser ids | 
**dimensions** | **[str]** | The dimensions for the report. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**metrics** | **[str]** | The list of metrics to report. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**ad_set_ids** | **[str], none_type** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. | [optional] 
**ad_set_names** | **[str], none_type** | The list of ad sets names. If empty, all the adSets will be fetched. | [optional] 
**ad_set_status** | **[str], none_type** | The list of ad sets status. If empty, all the adSets will be fetched. | [optional] 
**currency** | **str, none_type** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional] 
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database format (Tz). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


