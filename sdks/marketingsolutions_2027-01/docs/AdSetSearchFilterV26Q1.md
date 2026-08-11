# AdSetSearchFilterV26Q1

Filter on ad set ids.                Multiple filters are combined with an implicit AND operation.  Identifiers are string-encoded integers; invalid values are ignored.  If no filter is provided (both arrays are null or empty), the search returns all accessible campaigns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_ids** | **[str], none_type** | Ad set ids to filter on. Ids are string-encoded integers. | [optional] 
**advertiser_ids** | **[str], none_type** | Advertiser ids which ad sets belongs to (indirectly via their marketing campaign).  Ids are string-encoded integers. | [optional] 
**campaign_ids** | **[str], none_type** | Campaign ids to filter on. Ids are string-encoded integers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


