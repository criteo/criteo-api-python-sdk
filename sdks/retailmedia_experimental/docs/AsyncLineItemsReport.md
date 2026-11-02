# AsyncLineItemsReport

Async Line Items report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | End date | 
**start_date** | **datetime** | Start date | 
**activation_platforms** | **[str]** | Filter on the activation platform: CommerceMax, PrivateMarket | [optional] 
**budget_models** | **[str]** | Filter on the budget model: CriteoBudget, RetailerBudget | [optional] 
**buy_types** | **[str]** | Filter on the buy type: auction, preferredDeals, sponsorship | [optional] 
**campaign_type** | **str** | Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays | [optional]  if omitted the server will use the default value of "all"
**click_attribution_window** | **str, none_type** | Click attribution window | [optional]  if omitted the server will use the default value of "none"
**dimensions** | **[str]** | List of dimensions to report on | [optional] 
**format** | **str** | Format of the output | [optional]  if omitted the server will use the default value of "json-compact"
**id** | **str, none_type** | Line Item id to report on | [optional] 
**ids** | **[str]** | Line Item ids to report on | [optional] 
**media_type** | **str** | Filter on the type of media: unknown, display, video | [optional]  if omitted the server will use the default value of "all"
**metrics** | **[str]** | List of metrics to report on | [optional] 
**report_type** | **str, none_type** | Type of report, if no dimensions and metrics are provided, falls back to summary reportType | [optional]  if omitted the server will use the default value of "summary"
**sales_channel** | **str** | Filter on specific sales channel: offline or online | [optional]  if omitted the server will use the default value of "all"
**search_term_targetings** | **[str]** | Filter on the type of search term targeting: unknown, automatic, manual | [optional] 
**search_term_types** | **[str]** | Filter on the type of search term type: unknown, searched, entered | [optional] 
**targeted_keyword_types** | **[str]** | Filter on targeted keyword type: unknown, generic, branded, conquesting | [optional] 
**timezone** | **str, none_type** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**view_attribution_window** | **str, none_type** | View attribution window | [optional]  if omitted the server will use the default value of "none"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


