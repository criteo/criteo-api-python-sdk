# AsyncRevenueReport

Async Revenue report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End date | 
**ids** | **[str], none_type** | Campaign ids to report on | [optional] 
**id** | **str, none_type** | Campaign id to report on | [optional] 
**report_type** | **str, none_type** | Type of report | [optional] 
**revenue_type** | **str, none_type** | Type of revenue | [optional] 
**format** | **str, none_type** | Format of the output | [optional] 
**sold_by** | **str, none_type** | Filter on the seller: indirect, direct or private market | [optional] 
**campaign_sub_type** | **str, none_type** | Filter on campaign subType : Auction and Preferred Deals or Lockout campaign | [optional] 
**click_attribution_window** | **str, none_type** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**view_attribution_window** | **str, none_type** | View attribution window | [optional]  if omitted the server will use the default value of "none"
**campaign_type** | **str, none_type** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional] 
**sales_channel** | **str, none_type** | Filter on specific sales channel: offline or online | [optional] 
**dimensions** | **[str], none_type** | List of dimensions to report on | [optional] 
**metrics** | **[str], none_type** | List of metrics to report on | [optional] 
**timezone** | **str, none_type** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


