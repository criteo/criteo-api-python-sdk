# ExternalPreferredLineItemV2

A Retail Media Preferred Line Item used to hold bid settings for one or many promoted products on a single retailer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** |  | 
**created_at** | **datetime** |  | 
**end_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**name** | **str** |  | 
**start_date** | **date** | Represents the Date as a year, month, and day in the format YYYY-MM-DD | 
**status** | **str** | Line Item Status Enum | 
**target_retailer_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**budget** | **float, none_type** |  | [optional] 
**budget_remaining** | **float, none_type** |  | [optional] 
**budget_spent** | **float, none_type** |  | [optional] 
**capping** | [**ExternalLineItemCappingV2**](ExternalLineItemCappingV2.md) |  | [optional] 
**creative_id** | **str, none_type** | External creative Id | [optional] 
**id** | **str, none_type** | Id of the entity | [optional] 
**pacing** | **str, none_type** |  | [optional] 
**page** | [**ExternalLineItemPageV2**](ExternalLineItemPageV2.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


