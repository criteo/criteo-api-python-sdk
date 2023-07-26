# GenerateAudiencePerformanceReportRequestAttributes

Request attributes for async audience performance report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**advertiser_id** | **str** | The advertiser id | 
**dimension** | **str** | The dimension for the report. | 
**metrics** | **[str]** | The list of metrics to report. | 
**timezone** | **str** | The timezone used for the report. Timezone Database format (Tz). | [optional] 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional] 
**ad_set_ids** | **[str]** | The list of adSets ids. If empty, all the adSets will be fetched. | [optional] 
**audience_ids** | **[str]** | The list of Audiences ids. If empty, all the Audiences will be fetched. | [optional] 
**segments_ids** | **[str]** | The list of Segments ids. If empty, all the segments will be fetched. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


