# LocationUpdateV1

Settings to target users based on their location.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_of_interest** | [**[PointOfInterestV1]**](PointOfInterestV1.md) | Reach users which have been historically located in the given coordinates | [optional] 
**radius_in_km** | **int** | Radius in kilometers | [optional] 
**registry_type** | **str** | The kind of Location audience | [optional]  if omitted the server will use the default value of "PointOfInterest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


