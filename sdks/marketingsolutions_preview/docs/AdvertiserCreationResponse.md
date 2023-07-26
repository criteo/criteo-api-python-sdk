# AdvertiserCreationResponse

Advertiser Creation Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EntityV2OfObject**](EntityV2OfObject.md) |  | [optional] 
**errors** | [**[CommonProblem]**](CommonProblem.md) | Error list returned by the Criteo API  For successful requests it is empty | [optional] 
**warnings** | [**[CriteoApiWarningV2]**](CriteoApiWarningV2.md) | Warnings list returned by the Criteo API  In some situations the operations are successful but it may be useful to issue warnings to the API consumer.  For example the endpoint, entity or field is deprecated. Warnings are like compiler warnings, they indicate that problems may occur in the future. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


