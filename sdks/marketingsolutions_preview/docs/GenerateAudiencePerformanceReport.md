# GenerateAudiencePerformanceReport

Request attributes for async audience performance report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str** | The advertiser id | 
**dimension** | **str** | The dimension for the report. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**metrics** | **[str]** | The list of metrics to report. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**ad_set_ids** | **[str], none_type** | The list of adSets ids. If empty, all the adSets will be fetched. | [optional] 
**audience_ids** | **[str], none_type** | The list of Audiences ids. If empty, all the Audiences will be fetched. | [optional] 
**currency** | **str, none_type** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional] 
**segments_ids** | **[str], none_type** | The list of Segments ids. If empty, all the segments will be fetched. | [optional] 
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


