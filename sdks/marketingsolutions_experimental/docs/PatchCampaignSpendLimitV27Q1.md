# PatchCampaignSpendLimitV27Q1

Spend limit configuration for a marketing campaign (patch).  Only provided fields are updated; omitted fields are left unchanged.  When spendLimitType is \"capped\": spendLimitAmount and spendLimitRenewal are required.  When spendLimitType is \"uncapped\": spendLimitAmount is null and spendLimitRenewal is \"undefined\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_limit_amount** | [**NillableDecimal**](NillableDecimal.md) |  | [optional] 
**spend_limit_renewal** | **str, none_type** |  | [optional] 
**spend_limit_type** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


