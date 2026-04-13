# CreateCampaignSpendLimit

Spend limit configuration for a marketing campaign. Controls how much can be spent and the renewal cadence.  When spendLimitType is \"capped\": spendLimitAmount and spendLimitRenewal are required.  When spendLimitType is \"uncapped\": spendLimitAmount is null and spendLimitRenewal is \"undefined\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_limit_type** | **str** | Controls whether the campaign has a spending limit.  - \&quot;capped\&quot;: spending is limited to spendLimitAmount. Requires spendLimitAmount (non-null) and spendLimitRenewal (not \&quot;undefined\&quot;).  - \&quot;uncapped\&quot;: no spending limit. spendLimitAmount is null and spendLimitRenewal is \&quot;undefined\&quot;. | 
**spend_limit_amount** | **float, none_type** | Maximum spend amount in the advertiser&#39;s currency per renewal period. Non-null when capped. null when uncapped. | [optional] 
**spend_limit_renewal** | **str** | The period over which the spend limit is consumed.  - \&quot;daily\&quot;, \&quot;monthly\&quot;: spend limit resets at the start of each period.  - \&quot;lifetime\&quot;: spend limit covers the entire campaign duration without resetting.  - \&quot;undefined\&quot;: only used when spendLimitType is \&quot;uncapped\&quot; (no renewal applies). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


