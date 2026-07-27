# StatisticsReportQueryMessage

This is the message defining the query for Adset report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **str** | List of advertiser IDs to report on, provided as a single comma-separated string (e.g., \&quot;123,456,789\&quot;). The advertisers must already exist. If empty, all advertisers will be used. | 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**dimensions** | **[str]** | List of dimensions for the report. At least one dimension should be provided. &lt;br/&gt;&lt;br/&gt; When an ID dimension is requested (e.g., AdsetId), the corresponding name dimension (e.g., Adset) is automatically included, and vice versa. This applies to the following pairs: AdsetId/Adset, AdId/Ad, AdvertiserId/Advertiser, CampaignId/Campaign, CategoryId/Category, CouponId/Coupon, MarketingObjectiveId/MarketingObjective, ChannelId/Channel. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. | 
**metrics** | **[str]** | List of metrics for the report. Provide at least one metric to return performance data; otherwise, the response will include only dimension-related information. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be ≤ endDate. | 
**ad_set_ids** | **[str], none_type** | Optional list of ad set IDs to filter on. The ad sets must already exist. If empty, all ad sets will be fetched. | [optional] 
**ad_set_names** | **[str], none_type** | Optional list of ad set names to filter on. If empty, all ad sets will be fetched. | [optional] 
**ad_set_status** | **[str], none_type** | Optional list of ad set statuses to filter on. If empty, all ad sets will be fetched. | [optional] 
**format** | **str** | Optional file format of the generated report. | [optional]  if omitted the server will use the default value of "json"
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database format (Tz). | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


