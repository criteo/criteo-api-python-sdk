# AsyncFillRateReport

Async FillRate report body request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | **[str]** | List of dimensions to report on | 
**end_date** | **datetime** | End date | 
**metrics** | **[str]** | List of metrics to report on | 
**start_date** | **datetime** | Start date | 
**supply_account_ids** | **[str]** | Supply account ids to report on | 
**ad_server_type** | **str** | Filter on the type of the ad server: criteo, gam, all | [optional]  if omitted the server will use the default value of "all"
**format** | **str** | Format of the output | [optional]  if omitted the server will use the default value of "json"
**timezone** | **str** | Time zone : see criteo developer portal for supported time zones | [optional]  if omitted the server will use the default value of "UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


