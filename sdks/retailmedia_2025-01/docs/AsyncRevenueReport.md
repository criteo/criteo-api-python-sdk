# AsyncRevenueReport

Async Revenue report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End date | 
**ids** | **[str]** | Supply account ids to report on | [optional] 
**id** | **str** | Supply account id to report on | [optional] 
**retailer_ids** | **[str]** | Retailer ids to filter | [optional] 
**account_ids** | **[str]** | Account ids to filter | [optional] 
**campaign_ids** | **[str]** | Campaign ids to filter | [optional] 
**line_item_ids** | **[str]** | Line item ids to filter | [optional] 
**report_type** | **str** | Type of report | [optional] 
**revenue_type** | **str** | Type of revenue | [optional] 
**sold_by** | **str** | Filter on the seller: Indirect Sold, Direct Sold or Private Market | [optional] 
**buy_type** | **str** | Filter on buy type: Auction, Preferred Deals or Sponsorship | [optional] 
**advertiser_types** | **[str]** | Filter on the type of advertiser: retailer, brand, seller | [optional] 
**sku_relations** | **[str]** | Filter on sku relations: Same SKU, Same Parent SKU, Same Category, Same Brand or Same Seller | [optional] 
**format** | **str** | Format of the output | [optional]  if omitted the server will use the default value of "json"
**campaign_type** | **str** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**sales_channel** | **str** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**click_attribution_window** | **str** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**view_attribution_window** | **str** | View attribution window | [optional]  if omitted the server will use the default value of "none"
**dimensions** | **[str]** | List of dimensions to report on | [optional] 
**metrics** | **[str]** | List of metrics to report on | [optional] 
**timezone** | **str** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


