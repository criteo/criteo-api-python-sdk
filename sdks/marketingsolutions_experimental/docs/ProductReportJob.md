# ProductReportJob

This is the message defining the query for the MPO product report (async export).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | The list of advertiser account IDs. Maximum 5, numeric. | 
**start_date** | **datetime** | Start of the reporting interval. ISO 8601 date-time (UTC). | 
**ad_set_ids** | **[str], none_type** | The list of ad set ids. Maximum 10. | [optional] 
**campaign_ids** | **[str], none_type** | The list of marketing campaign ids. Maximum 10. | [optional] 
**dimensions** | **[str], none_type** | The dimensions of the report. If not included, the default list of dimensions will be used. | [optional]  if omitted the server will use the default value of ["advertiserId","adSetId","sellerId","productId"]
**end_date** | **datetime** | End of the reporting interval. ISO 8601 date-time (UTC). Defaults to the last complete day. | [optional] 
**file_format** | **str, none_type** | The output file format. Supported: csv, json. | [optional]  if omitted the server will use the default value of "csv"
**metrics** | **[str], none_type** | The list of metrics to report. If not included, the default list of metrics will be used. | [optional]  if omitted the server will use the default value of ["clicks","impressions","cost"]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


