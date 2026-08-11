# CampaignScheduledSpendLimitV23Q1

A campaign spend limit scheduled to become active on the specified \"startDate\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Identifier of the scheduled spend limit, for example \&quot;12345\&quot;. | [optional] 
**spend_limit_amount** | [**NillableDecimal**](NillableDecimal.md) |  | [optional] 
**spend_limit_renewal** | **str, none_type** | The period over which the campaign spend limit is applied.  - \&quot;daily\&quot;, \&quot;monthly\&quot;, and \&quot;lifetime\&quot; are valid when spendLimitType is \&quot;capped\&quot;.  - \&quot;undefined\&quot; is returned when spendLimitType is \&quot;uncapped\&quot;. | [optional] 
**spend_limit_type** | **str, none_type** | Controls whether the campaign has a spend limit.  - \&quot;capped\&quot;: a spend limit applies, spendLimitAmount.value is non-null, and spendLimitRenewal is \&quot;daily\&quot;, \&quot;monthly\&quot;, or \&quot;lifetime\&quot;.  - \&quot;uncapped\&quot;: no spend limit applies, spendLimitAmount.value is null, and spendLimitRenewal is \&quot;undefined\&quot;. | [optional] 
**start_date** | **date, none_type** | Advertiser-local calendar date when the scheduled spend limit becomes active, for example \&quot;2026-08-01\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


