# PreferredLineItemUpdateModelV2

Model used to update a preferred line item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**name** | **str** |  | 
**start_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**status** | **str** | Line Item Status Enum | 
**budget** | **float** |  | [optional] 
**capping** | [**LineItemCappingV2**](LineItemCappingV2.md) |  | [optional] 
**creative_id** | **str** |  | [optional] 
**pacing** | **str** |  | [optional]  if omitted the server will use the default value of "accelerated"
**page** | [**LineItemPageV2**](LineItemPageV2.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


