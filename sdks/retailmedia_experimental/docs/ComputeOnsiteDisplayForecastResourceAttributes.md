# ComputeOnsiteDisplayForecastResourceAttributes

Attributes of the resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | Last day of the forecast period, inclusive, as &#x60;YYYY-MM-DD&#x60;. May equal  &#x60;startDate&#x60; for a single-day forecast. | 
**page_settings** | [**[PageSetting]**](PageSetting.md) | Page types to include, at least one, and at most one entry per page type. | 
**retailer_id** | **str** | Identifies the retailer whose inventory is being forecast. | 
**start_date** | **date** | First day of the forecast period, as &#x60;YYYY-MM-DD&#x60;. | 
**buy_type** | **str** | How the inventory is bought. | [optional]  if omitted the server will use the default value of "auction"
**creative_formats** | **[str]** | Restricts the forecast to these creative formats. Defaults to all formats. | [optional] 
**frequency_capping** | [**ComputeOnsiteDisplayForecastFrequencyCapping**](ComputeOnsiteDisplayForecastFrequencyCapping.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


