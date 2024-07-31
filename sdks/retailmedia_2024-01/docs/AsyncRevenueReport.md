# AsyncRevenueReport

Async Revenue report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End date | 
**ids** | **[str], none_type** | Supply account ids to report on | [optional] 
**id** | **str, none_type** | Supply account id to report on | [optional] 
**report_type** | **str, none_type** | Type of report | [optional] 
**revenue_type** | **str, none_type** | Type of revenue | [optional] 
**sold_by** | **str, none_type** | Filter on the seller: Indirect Sold, Direct Sold or Private Market | [optional] 
**buy_type** | **str, none_type** | Filter on buy type: Auction, Preferred Deals or Sponsorship | [optional] 
**advertiser_types** | **[str], none_type** | Filter on the type of advertiser: retailer, brand, seller | [optional] 
**sku_relations** | **[str], none_type** | Filter on sku relations: Same SKU, Same Parent SKU, Same Category, Same Brand or Same Seller | [optional] 
**format** | **str, none_type** | Format of the output | [optional] 
**campaign_type** | **str, none_type** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**sales_channel** | **str, none_type** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**click_attribution_window** | **str, none_type** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**view_attribution_window** | **str, none_type** | View attribution window | [optional]  if omitted the server will use the default value of "none"
**dimensions** | **[str], none_type** | List of dimensions to report on | [optional] 
**metrics** | **[str], none_type** | List of metrics to report on | [optional] 
**timezone** | **str, none_type** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


