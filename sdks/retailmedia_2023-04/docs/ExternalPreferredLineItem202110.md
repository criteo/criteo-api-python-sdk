# ExternalPreferredLineItem202110

A Retail Media Preferred Line Item used to hold bid settings for one or many promoted products on a single retailer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**start_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**end_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**status** | **str** |  | 
**pacing** | **str** |  | 
**page** | [**ExternalLineItemPage202110**](ExternalLineItemPage202110.md) |  | 
**target_retailer_id** | **str** |  | 
**budget** | **float** |  | 
**campaign_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**capping** | [**ExternalLineItemCapping202110**](ExternalLineItemCapping202110.md) |  | [optional] 
**budget_spent** | **float** |  | [optional] 
**budget_remaining** | **float** |  | [optional] 
**creative_id** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


