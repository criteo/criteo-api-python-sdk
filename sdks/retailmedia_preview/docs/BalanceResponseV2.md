# BalanceResponseV2

A Retail Media Balance used to determine the funds available for any or all campaigns in an account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the balance. | 
**start_date** | **str** | Start date of the balance in the format YYYY-MM-DD. | 
**balance_type** | **str** | Type of the balance. | 
**spend_type** | **str** | Spend Type of the balance. | 
**private_market_billing_type** | **str** | Billing type for Private Market of the balance. | 
**po_number** | **str, none_type** | Purchase Order number. | [optional] 
**memo** | **str, none_type** | Memo. | [optional] 
**deposited** | **float, none_type** | Amount of billable funds allotted to the balance. | [optional] 
**spent** | **float, none_type** | Amount of spent funds of the balance. | [optional] 
**remaining** | **float, none_type** | Amount of remaining funds of the balance. | [optional] 
**end_date** | **str, none_type** | End date of the balance in the format YYYY-MM-DD. | [optional] 
**status** | **str** | Status of the balance. | [optional] 
**created_at** | **datetime** | Creation time of the balance. | [optional] 
**updated_at** | **datetime** | Update time of the balance. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


