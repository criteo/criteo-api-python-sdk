# BalanceHistoryChangeDataCaptureV1

Data model represents the data change capture of balance history.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_modification** | **datetime** | Date when data change has occured. | 
**modified_by_user** | **str** | Username who modified the insertion order. | 
**change_type** | **str** | Represent the type of change states of the history. | 
**change_details** | [**ChangeDetailsV1**](ChangeDetailsV1.md) |  | 
**memo** | **str, none_type** | Memo associate with the insertion order modification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


