# AsyncOffsiteReport

Async Offsite report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | Account ids to report on | 
**dimensions** | **[str]** | List of dimensions to report on | 
**end_date** | **datetime** | End date | 
**metrics** | **[str]** | List of metrics to report on | 
**start_date** | **datetime** | Start date | 
**buy_type** | **str, none_type** | Filter on buy type: Auction, Preferred Deals or Sponsorship | [optional] 
**campaign_ids** | **[str]** | Campaign ids to filter | [optional] 
**campaign_type** | **str** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**click_attribution_window** | **str, none_type** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**creative_ids** | **[str]** | Creative ids to filter | [optional] 
**format** | **str** | Format of the output | [optional]  if omitted the server will use the default value of "json-compact"
**line_item_ids** | **[str]** | Line item ids to filter | [optional] 
**media_type** | **str** | Filter on the type of media: unknown, display, video | [optional]  if omitted the server will use the default value of "all"
**retailer_ids** | **[str]** | Retailer ids to filter | [optional] 
**sales_channel** | **str** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**timezone** | **str, none_type** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**view_attribution_window** | **str, none_type** | View attribution window | [optional]  if omitted the server will use the default value of "none"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


