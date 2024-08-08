# GenerateCategoriesReportRequestAttributes

This is the message defining the query for Categories report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | List of Advertiser ids. | 
**format** | **str** | The file format of the generated report: csv, xml, excel or json. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**campaign_id** | **str, none_type** | Report only on the specified Campaign id. | [optional] 
**adset_id** | **str, none_type** | Report only on the specified AdSet id. | [optional] 
**domain** | **str, none_type** | Report only on the specified domain. | [optional] 
**category** | **str, none_type** | Report only on the specified category. | [optional] 
**should_display_domain_dimension** | **bool, none_type** | Specify if the domain dimension is displayed in the report. | [optional]  if omitted the server will use the default value of True
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


