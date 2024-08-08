# GenerateCreativesReportRequestAttributes

This is the message defining the query for Creatives report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**advertiser_ids** | **[str]** | The list of client ids. | 
**metrics** | **[str]** | The list of metrics to report. | 
**dimensions** | **[str]** | The list of dimensions to report. | 
**timezone** | **str, none_type** | The timezone used for the report. Timezone Database format (Tz). | [optional] 
**ad_formats** | **[str], none_type** | The list of adFormats. | [optional] 
**display_sizes** | **[str], none_type** | The list of displaySizes. | [optional] 
**coupon_names** | **[str], none_type** | The list of coupon names. | [optional] 
**coupon_ids** | **[str], none_type** | The list of coupon ids. | [optional] 
**ad_names** | **[str], none_type** | The list of ad names. | [optional] 
**ad_ids** | **[str], none_type** | The list of ad ids. | [optional] 
**campaign_ids** | **[str], none_type** | The list of campaign ids (marketing campaign ids). | [optional] 
**ad_set_ids** | **[str], none_type** | The list of adSet ids (campaign ids). | [optional] 
**ad_set_status** | **[str], none_type** | The list of adSet status (ex: &#39;Active&#39;,&#39;NotRunning&#39;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


