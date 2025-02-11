# CampaignAttributesV202301

An object that represents the available options to set when creating a Retail Media Campaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_auto_daily_pacing** | **bool** |  | 
**start_date** | **datetime, none_type** |  | 
**end_date** | **datetime, none_type** |  | 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "auction"
**drawable_balance_ids** | **[str]** |  | [optional] 
**click_attribution_window** | **str** |  | [optional]  if omitted the server will use the default value of "30D"
**view_attribution_window** | **str** |  | [optional]  if omitted the server will use the default value of "none"
**budget** | **float, none_type** |  | [optional] 
**monthly_pacing** | **float, none_type** |  | [optional] 
**daily_pacing** | **float, none_type** |  | [optional] 
**click_attribution_scope** | **str, none_type** |  | [optional] 
**view_attribution_scope** | **str, none_type** |  | [optional] 
**company_name** | **str, none_type** |  | [optional] 
**on_behalf_company_name** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


