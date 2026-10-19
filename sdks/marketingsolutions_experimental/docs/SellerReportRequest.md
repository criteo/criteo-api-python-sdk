# SellerReportRequest

Filters and options used to generate a synchronous seller performance report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str** | Identifier of the advertiser for which the report is generated. | 
**dimensions** | **[str]** | Dimensions used to group the report. At least one dimension is required. | 
**end_date** | **date** | Inclusive end date of the reporting period, formatted as yyyy-MM-dd. | 
**metrics** | **[str]** | Metrics returned for each dimension combination. At least one metric is required. | 
**start_date** | **date** | Inclusive start date of the reporting period, formatted as yyyy-MM-dd. | 
**ad_set_ids** | **[str]** | Restricts the report to the specified ad sets. If omitted, all ad sets in scope are included.  Up to 10 ad set identifiers can be supplied. | [optional] 
**campaign_ids** | **[str]** | Restricts the report to the specified marketing campaigns. If omitted, all campaigns in scope are included.  Up to 10 campaign identifiers can be supplied. | [optional] 
**format** | **str** | Output format. Defaults to JSON. | [optional]  if omitted the server will use the default value of "json"
**seller_ids** | **[str]** | Restricts the report to the specified sellers. If omitted, all sellers in scope are included.  Up to 10 seller identifiers can be supplied. | [optional] 
**timezone** | **str** | IANA time zone used for time-based aggregation. Defaults to UTC. | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


