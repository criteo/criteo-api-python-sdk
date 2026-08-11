# PatchCampaignScheduledSpendLimitUpdate

Scheduled spend-limit update.  Updates are full replacements: id, startDate, spendLimitType, and the capped or uncapped spend-limit values must describe the complete desired state.  The startDate is an advertiser-local calendar date, for example 2026-09-01.  All scheduled spend limits for the campaign must use the same spendLimitRenewal as the active spend limit.  When spendLimitRenewal is \"monthly\", startDate must be the first day of the month.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Identifier of the scheduled spend limit to update. | 
**spend_limit_type** | **str, none_type** | Controls whether the campaign has a spend limit.  \&quot;capped\&quot; returns a non-null spendLimitAmount.value and a spendLimitRenewal of \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  \&quot;uncapped\&quot; returns spendLimitAmount.value as null and spendLimitRenewal as \&quot;undefined\&quot;. | 
**start_date** | **date, none_type** | Advertiser-local calendar date when the scheduled spend limit becomes active, for example \&quot;2026-09-01\&quot;. | 
**spend_limit_amount** | [**NillableDecimal**](NillableDecimal.md) |  | [optional] 
**spend_limit_renewal** | **str, none_type** | The period over which the campaign spend limit is applied.  When spendLimitType is \&quot;capped\&quot;, this is \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  When spendLimitType is \&quot;uncapped\&quot;, this is \&quot;undefined\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


