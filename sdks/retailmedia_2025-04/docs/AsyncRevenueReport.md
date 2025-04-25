# AsyncRevenueReport

Async Revenue report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | End date | 
**start_date** | **datetime** | Start date | 
**account_ids** | **[str]** | Account ids to filter | [optional] 
**advertiser_types** | **[str]** | Filter on the type of advertiser: retailer, brand, seller | [optional] 
**buy_type** | **str** | Filter on buy type: Auction, Preferred Deals or Sponsorship | [optional] 
**campaign_ids** | **[str]** | Campaign ids to filter | [optional] 
**campaign_type** | **str** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**click_attribution_window** | **str** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**dimensions** | **[str]** | List of dimensions to report on | [optional] 
**format** | **str** | Format of the output | [optional]  if omitted the server will use the default value of "json"
**id** | **str** | Supply account id to report on | [optional] 
**ids** | **[str]** | Supply account ids to report on | [optional] 
**line_item_ids** | **[str]** | Line item ids to filter | [optional] 
**metrics** | **[str]** | List of metrics to report on | [optional] 
**report_type** | **str** | Type of report, if no dimensions and metrics are provided, falls back to advertiser reportType | [optional] 
**retailer_ids** | **[str]** | Retailer ids to filter | [optional] 
**revenue_type** | **str** | Type of revenue | [optional] 
**sales_channel** | **str** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**sku_relations** | **[str]** | Filter on sku relations: Same SKU, Same Parent SKU, Same Category, Same Brand or Same Seller | [optional] 
**sold_by** | **str** | Filter on the seller: Indirect Sold, Direct Sold or Private Market | [optional] 
**timezone** | **str** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**view_attribution_window** | **str** | View attribution window | [optional]  if omitted the server will use the default value of "none"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


