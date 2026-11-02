# ReadAdSetBudgetV27Q1

Budget configuration for an ad set. Controls how much can be spent and how spending is paced.  When budgetStrategy is \"capped\": budgetAmount, budgetRenewal, and budgetDeliverySmoothing are all set.  When budgetStrategy is \"uncapped\": budgetAmount is null, budgetRenewal is \"undefined\", budgetDeliverySmoothing is null, and budgetDeliveryWeek is \"undefined\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_amount** | **float, none_type** | Maximum budget amount in the advertiser&#39;s currency per renewal period. Non-null when capped. null when uncapped. | [optional] 
**budget_delivery_smoothing** | **str, none_type** |  | [optional] 
**budget_delivery_week** | **str, none_type** | Defines which day-of-week boundaries are used for weekly budget renewal. Only applicable when budgetStrategy is \&quot;capped\&quot;, budgetRenewal is \&quot;weekly\&quot;, and budgetDeliverySmoothing is \&quot;standard\&quot;.  - \&quot;mondayToSunday\&quot;, \&quot;tuesdayToMonday\&quot;, etc.: the day range over which the weekly budget is paced. Changing this value on the active budget also propagates to all scheduled budgets of the same ad set.  - \&quot;undefined\&quot;: used when budgetStrategy is \&quot;uncapped\&quot;, when budgetRenewal is not \&quot;weekly\&quot;, or when budgetDeliverySmoothing is \&quot;accelerated\&quot;. | [optional] 
**budget_renewal** | **str, none_type** | The period over which the budget is spent.  - \&quot;daily\&quot;, \&quot;monthly\&quot;, \&quot;weekly\&quot;: budget resets at the start of each period.  - \&quot;lifetime\&quot;: budget covers the entire ad set duration without resetting.  - \&quot;undefined\&quot;: only used when budgetStrategy is \&quot;uncapped\&quot; (no renewal applies). Required for capped budgets (must not be \&quot;undefined\&quot;). | [optional] 
**budget_strategy** | **str, none_type** | Controls whether the ad set has a spending limit.  - \&quot;capped\&quot;: spending is limited to budgetAmount. Requires budgetAmount (non-null), budgetRenewal (not \&quot;undefined\&quot;), and budgetDeliverySmoothing (not null).  - \&quot;uncapped\&quot;: no spending limit. budgetAmount is null, budgetRenewal is \&quot;undefined\&quot;, and budgetDeliverySmoothing is null. | [optional] 
**pacing_behavior** | **str, none_type** | Controls how a standard capped budget is paced.  - \&quot;targetFullBudget\&quot;: spend toward the full budget amount within the renewal period.  - \&quot;targetAverageDailyBudget\&quot;: spend toward an average daily amount. Currently only returned for capped, standard, monthly budgets.  - \&quot;undefined\&quot;: no explicit pacing behavior. Returned for uncapped budgets and budgets without explicit pacing behavior. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


