# OnsiteDisplayForecast

The forecast for one page type, returned as an item of the response `data` array.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_impressions** | **int** | Estimated available impressions over the whole forecast period. | 
**budget** | [**OnsiteDisplayForecastBudget**](OnsiteDisplayForecastBudget.md) |  | 
**details** | [**[InventoryForecastDetail]**](InventoryForecastDetail.md) | Daily breakdown, one entry per row of the grain described on  &#x60;InventoryForecastDetail&#x60;. | 
**page_type** | **str** | Page type this forecast applies to. | 
**reservation_rate** | **float** | Proportion of inventory already reserved, from 0.0 to 1.0. | 
**average_cpm** | [**OnsiteDisplayForecastAverageCpm**](OnsiteDisplayForecastAverageCpm.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


