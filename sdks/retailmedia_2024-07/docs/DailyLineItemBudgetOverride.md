# DailyLineItemBudgetOverride

The details for a daily budget override

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The number of DAYs that the override is active from StartDate, e.g. \&quot;1D\&quot;. Must end with &#39;D&#39; or &#39;d&#39;. | 
**start_date** | **datetime, none_type** | Daily budget override start date, format \&quot;yyyy-MM-dd\&quot;. If it is null, the StartDate would be the following date of the last item in the override sequence. | [optional] 
**max_daily_spend** | **float, none_type** | Daily budget override maximum daily spend amount. | [optional] 
**status** | **str, none_type** | Daily budget override computed status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


