# CreateSellerBudgetMapiMessage

Data used to create a seller's budget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Budget amount as a string (e.g. &#39;100.50&#39;) | [optional] 
**budget_type** | **str** | Type of budget: &#39;Daily&#39; (daily cap), &#39;Capped&#39; (lifetime with fixed amount), or &#39;Uncapped&#39; (lifetime with no limit) | [optional] 
**campaign_ids** | **[int]** | List of campaign IDs this budget applies to | [optional] 
**end_date** | **str** | Budget end date as a string (format: YYYY-MM-DD), or empty string for open-ended | [optional] 
**seller_id** | **str** | Identifier of the seller this budget is for | [optional] 
**start_date** | **datetime** | Budget start date. Time component is ignored. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


