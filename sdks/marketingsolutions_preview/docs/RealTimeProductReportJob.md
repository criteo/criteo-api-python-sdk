# RealTimeProductReportJob

Represents a request to create a real-time product export.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str], none_type** | List of advertiser IDs to include in the export. Required. | [optional] 
**campaign_ids** | **[str], none_type** | Optional list of campaign IDs to filter the export. | [optional] 
**currency** | **str, none_type** | Currency for the export. Default is \&quot;EUR\&quot;. | [optional] 
**dimensions** | **[str], none_type** | List of dimensions to include in the export. Default: [\&quot;advertiserId\&quot;, \&quot;campaignId\&quot;, \&quot;sellerId\&quot;, \&quot;productId\&quot;, \&quot;day\&quot;]. | [optional] 
**end_date** | **datetime, none_type** | End of the reporting interval, in ISOâ€‘8601 dateâ€‘time format (UTC). Mutually exclusive with lookbackWindow.  If omitted while startDate is provided, defaults to the current time. | [optional] 
**file_format** | **str** | The file format for the export. Allowed values: \&quot;csv\&quot;, \&quot;json\&quot;. Default is \&quot;csv\&quot;. | [optional] 
**lookback_window** | **int, none_type** | Lookback window in days. Default is 60. | [optional] 
**metrics** | **[str], none_type** | List of metrics to include in the export. Default: [\&quot;clicks\&quot;, \&quot;displays\&quot;, \&quot;cost\&quot;]. | [optional] 
**partner_ids** | **[str], none_type** | Optional list of partner IDs to filter the export. | [optional] 
**seller_ids** | **[str], none_type** | Optional list of seller IDs to filter the export. | [optional] 
**start_date** | **datetime, none_type** | Start of the reporting interval, in ISOâ€‘8601 dateâ€‘time format (UTC). Mutually exclusive with lookbackWindow. | [optional] 
**timezone** | **str, none_type** | Timezone for the export. Default is \&quot;UTC\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


