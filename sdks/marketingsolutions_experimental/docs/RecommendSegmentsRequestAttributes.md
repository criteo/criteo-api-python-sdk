# RecommendSegmentsRequestAttributes

Brief and options of a segment recommendation request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brief** | **str** | A freeform audience description. | 
**advertiser_id** | **str** | [Optional] AdvertiserId this requestor has access to. | [optional] 
**country** | **str** | [Optional] Country code. Must be a supported country. When &#x60;advertiserId&#x60; is set, it must also match the country of the advertiser. | [optional] 
**nb_segments** | **int** | Number of segments to recommend, between 1 and 20 (default to 5). | [optional]  if omitted the server will use the default value of 5
**segment_status_to_recommend** | **str** | [Optional] Recommend only existing segments or suggest the new ones. Default to new. | [optional]  if omitted the server will use the default value of "new"
**segment_types_to_recommend** | **[str]** | [Optional] Restrict the recommended segment types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


