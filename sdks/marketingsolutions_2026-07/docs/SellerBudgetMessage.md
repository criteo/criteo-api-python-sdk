# SellerBudgetMessage

A budget defines spending constraints for a seller across one or more campaigns. Each seller can have one active budget per time period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float, none_type** | Budget amount in the advertiser&#39;s currency | [optional] 
**budget_type** | **str** | Type of budget: &#39;Daily&#39; (daily cap), &#39;Capped&#39; (lifetime with fixed amount), or &#39;Uncapped&#39; (lifetime with no limit) | [optional] 
**campaign_ids** | **[int]** | List of campaign IDs this budget applies to | [optional] 
**end_date** | **str** | End date of the budget period (format: YYYY-MM-DD), or empty string if open-ended | [optional] 
**id** | **str** | Unique budget identifier | [optional] 
**is_suspended** | **bool** | Whether the budget has been manually suspended by the partner | [optional] 
**seller_id** | **str** | Identifier of the seller this budget belongs to | [optional] 
**spend** | **float, none_type** | Amount spent against this budget so far, or null if not available | [optional] 
**start_date** | **date** | Start date of the budget period (format: YYYY-MM-DD) | [optional] 
**status** | [**SellerBudgetStatusV2**](SellerBudgetStatusV2.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


