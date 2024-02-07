# ExternalPreferredLineItemUpdateModel202110

Model used to update a preferred line item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**start_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**end_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**status** | **str** |  | 
**pacing** | **str** |  | [optional]  if omitted the server will use the default value of "accelerated"
**capping** | [**ExternalLineItemCapping202110**](ExternalLineItemCapping202110.md) |  | [optional] 
**page** | [**ExternalLineItemPage202110**](ExternalLineItemPage202110.md) |  | [optional] 
**budget** | **float** |  | [optional] 
**creative_id** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


