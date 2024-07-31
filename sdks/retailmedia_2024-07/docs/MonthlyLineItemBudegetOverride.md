# MonthlyLineItemBudegetOverride

The details for a monthly budget override

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The number of MONTHs that the override is active from StartMonth, e.g. \&quot;1M\&quot;. Must end with &#39;M&#39; or &#39;m&#39;. | 
**max_monthly_spend** | **float** | Monthly budget override maximum monthly spend amount. | 
**start_month** | **datetime, none_type** | Monthly budget override start month, format \&quot;yyyy-MM\&quot;. If it is null, the StartMonth would be the following month of the last item in the override sequence. | [optional] 
**status** | **str, none_type** | Monthly budget override computed status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


