# GenerateTopProductsReportRequestAttributes

This is the message defining the query for TopProducts report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**advertiser_id** | **str** | The client id. | 
**rank_products_by** | **str** | The metric used to filter the top products. | 
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"
**limit** | **int** | The maximum number of top products returned. | [optional] 
**dimensions** | **[str], none_type** | The dimensions for the report. | [optional] 
**metrics** | **[str], none_type** | The list of metrics to report. | [optional] 
**currency** | **str, none_type** | The currency used for the report. ISO 4217 code (three-letter capitals). | [optional]  if omitted the server will use the default value of "EUR"
**brands** | **[str], none_type** | The list of brands names. | [optional] 
**category_ids** | **[str], none_type** | The list of category ids. | [optional] 
**campaign_ids** | **[str], none_type** | The list of campaign ids. | [optional] 
**ad_set_ids** | **[str], none_type** | The list of adSet ids. | [optional] 
**ad_set_status** | **[str], none_type** | The list of adSet status (ex: &#39;Active&#39;,&#39;NotRunning&#39;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


