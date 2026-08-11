# CampaignSearchFiltersV23Q1

Filters for searching campaigns.                Multiple filters are combined with an implicit AND operation.  Identifiers are string-encoded integers; invalid values are ignored.  If no filter is provided (both arrays are null or empty), the search returns all accessible campaigns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **[str], none_type** | Advertiser IDs to filter on (string-encoded integers). | [optional] 
**campaign_ids** | **[str], none_type** | Campaign IDs to filter on (string-encoded integers). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


