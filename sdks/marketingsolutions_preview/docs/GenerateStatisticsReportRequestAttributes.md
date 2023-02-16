# GenerateStatisticsReportRequestAttributes

Request attributes for async statistics report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**dimensions** | **[str]** | The dimensions for the report. | 
**metrics** | **[str]** | The list of metrics to report. | 
**advertiser_ids** | **[str]** | The of advertiser ids | [optional] 
**timezone** | **str** | The timezone used for the report. Timezone Database format (Tz). | [optional] 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional] 
**ad_set_ids** | **[str]** | The list of adSets ids. If empty, all the adSets will be fetched | [optional] 
**ad_set_names** | **[str]** | The list of adSets names. If empty, all the adSets will be fetched | [optional] 
**ad_set_status** | **[str]** | The list of adSets status. If empty, all the adSets will be fetched | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


