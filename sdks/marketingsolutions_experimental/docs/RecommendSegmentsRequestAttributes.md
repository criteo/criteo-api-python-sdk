# RecommendSegmentsRequestAttributes

Brief and options of a segment recommendation request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brief** | **str** | A freeform audience description. | 
**advertiser_id** | **str** | Advertiser ID the caller has access to. | [optional] 
**nb_segments** | **int** | Number of segments to recommend, between 1 and 20 (defaults to 5). | [optional]  if omitted the server will use the default value of 5
**segment_status_to_recommend** | **str** | Recommend existing segments or suggest new ones. | [optional]  if omitted the server will use the default value of "new"
**segment_types_to_recommend** | **[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


