# GenerateTopProductsReportRequestAttributes

This is the message defining the query for TopProducts report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str** | The advertiser ID to report on. The advertiser must already exist. At least one advertiser ID should be provided | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. | 
**rank_products_by** | **str** | Optional metric used to rank the top products. Allowed values: &#39;Clicks&#39;, &#39;Displays&#39;, &#39;Sales&#39;. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. | 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | defaults to "EUR"
**ad_set_ids** | **[str], none_type** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be included. | [optional] 
**ad_set_status** | **[str], none_type** | Optional list of ad set statuses to filter on. If empty, all ad sets will be included. | [optional] 
**brands** | **[str], none_type** | Optional list of brand names to filter on. If empty, all brands will be included. | [optional] 
**campaign_ids** | **[str], none_type** | Optional list of campaign IDs to filter on. The campaigns must already exist. If empty, all campaigns will be included. | [optional] 
**category_ids** | **[str], none_type** | Optional list of product catalog category IDs to filter on. If empty, all categories will be included. | [optional] 
**dimensions** | **[str], none_type** | Optional list of dimensions for the report. If not provided, defaults to [ProductId, Product, ProductUrl]. When an ID dimension is requested (e.g., CampaignId), the corresponding name dimension (e.g., Campaign) is automatically included, and vice versa. This applies to the following pairs: CampaignId/Campaign, AdSetId/AdSet, ProductId/Product, CategoryId/Category, AdvertiserId/Advertiser. | [optional] 
**limit** | **int** | Optional maximum number of top products returned. Must be between 1 and 200. | [optional]  if omitted the server will use the default value of 200
**metrics** | **[str], none_type** | Optional list of metrics to report. If not provided, defaults to the metric specified in rankProductsBy. | [optional] 
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


