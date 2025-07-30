# ExternalPreferredLineItemCreateModelV2

Model used to create a preferred line item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | **float** |  | 
**end_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**name** | **str** |  | 
**pacing** | **str** | Line Item Pacing Enum | 
**page** | [**ExternalLineItemPageV2**](ExternalLineItemPageV2.md) |  | 
**start_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**target_retailer_id** | **str** |  | 
**capping** | [**ExternalLineItemCappingV2**](ExternalLineItemCappingV2.md) |  | [optional] 
**creative_id** | **str, none_type** |  | [optional] 
**status** | **str** | Line Item Status Enum | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


