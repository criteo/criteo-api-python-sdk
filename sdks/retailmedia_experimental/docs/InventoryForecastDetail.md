# InventoryForecastDetail

One row of a page type's daily breakdown.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_impressions** | **int** | Estimated available impressions for this day. | 
**average_cpm** | [**InventoryForecastDetailAverageCpm**](InventoryForecastDetailAverageCpm.md) |  | 
**budget** | [**InventoryForecastDetailBudget**](InventoryForecastDetailBudget.md) |  | 
**creative_formats** | **[str]** | Every creative format available on this placement configuration, restricted to the formats  the request asked for. The row aggregates them - impressions are not split per format. | 
**date** | **date** | The forecast day, as &#x60;YYYY-MM-DD&#x60;. | 
**placement_config_id** | **str** | Placement configuration this row is for. | 
**keyword** | **str** | The keyword this row is for. Present only for search and search bar pages. | [optional] 
**taxonomy_id** | **str** | The taxonomy id this row is for. Present only for category, product detail, category menu  and merchandising pages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


