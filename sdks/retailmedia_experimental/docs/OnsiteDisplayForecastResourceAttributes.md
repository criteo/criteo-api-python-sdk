# OnsiteDisplayForecastResourceAttributes

Attributes of the resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_impressions** | **int** | Estimated available impressions over the whole forecast period. | 
**budget** | [**OnsiteDisplayForecastBudget**](OnsiteDisplayForecastBudget.md) |  | 
**details** | [**[InventoryForecastDetail]**](InventoryForecastDetail.md) | Daily breakdown, one entry per row of the grain described on  &#x60;InventoryForecastDetail&#x60;. | 
**page_type** | **str** | Page type this forecast applies to. | 
**reservation_rate** | **float** | Proportion of inventory already reserved, from 0.0 to 1.0. | 
**average_cpm** | [**OnsiteDisplayForecastAverageCpm**](OnsiteDisplayForecastAverageCpm.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


