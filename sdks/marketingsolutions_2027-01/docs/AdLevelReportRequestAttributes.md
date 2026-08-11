# AdLevelReportRequestAttributes

Query parameters for the Ad-Level Report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str]** | List of advertiser IDs to report on. Between 1 and 5 advertiser IDs can be provided. | 
**dimensions** | **[str]** | List of breakdown dimensions for the report. At least one dimension must be provided; nothing is added to the response unless explicitly requested here. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. | 
**metrics** | **[str]** | List of metrics to return. At least one metric must be provided. AdGroupContextHint and AdGroupDescription require AdGroupName in dimensions; ProductName requires ProductId; AdTitle and AdCopy require AdId. | 
**start_date** | **datetime** | Start date of the report. Date component of ISO 8601 format, any time or timezone component is ignored. Must be less than or equal to endDate. | 
**adset_ids** | **[str], none_type** | Optional filter on ad set IDs. Also satisfies the ad-set-scope requirement for the AdGroupName, ProductId, and AdId breakdown dimensions: if any of those are requested, either adsetIds must be non-empty or AdsetId must also be included in dimensions. | [optional] 
**format** | **str** | Optional file format of the generated report. Only csv and json are currently supported by this endpoint — excel and xml requests are rejected with a 400 error. | [optional]  if omitted the server will use the default value of "json"
**timezone** | **str, none_type** | Optional timezone used for the report. Timezone Database (Tz) format. | [optional]  if omitted the server will use the default value of "UTC"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


