# GenerateCategoriesReportRequestAttributes

This is the message defining the query for Categories report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | List of advertiser IDs to report on. The advertisers must already exist. At least one advertiser ID should be provided. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. | 
**adset_id** | **str, none_type** | Optional adset id to filter on. The adset must already exist. If empty, all adsets will be fetched. | [optional] 
**campaign_id** | **str, none_type** | Optional campaign id to filter on. The campaign must already exist. If empty, all campaign will be fetched. | [optional] 
**category** | **str, none_type** | Optional category to filter on. If empty, all categories will be fetched. | [optional] 
**domain** | **str, none_type** | Optional domain to filter on. If empty, all domains will be fetched. | [optional] 
**format** | **str** | Optional file format of the generated report. | [optional]  if omitted the server will use the default value of "json"
**should_display_domain_dimension** | **bool** | Optionally specify if the domain dimension is displayed in the report. | [optional]  if omitted the server will use the default value of True
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


