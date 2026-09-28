# AdWrite

Entity to create an ad

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_id** | **str** | The id of the Ad Set bound to this Ad | 
**creative_id** | **str** | The id of the Creative bound to this Ad | 
**name** | **str** | The name of the ad | 
**start_date** | **str** | The date when the ad will be launched. It must be a date in the future.  String must be in ISO8601 format, more precisely \&quot;yyyy-MM-ddTHH:mm:ss.fffZ\&quot;: a UTC timestamp whose  three millisecond digits and trailing \&quot;Z\&quot; are both required, for example \&quot;2026-10-01T09:30:00.000Z\&quot;.  No other ISO8601 layout is accepted, neither a UTC offset such as \&quot;2026-10-01T11:30:00+02:00\&quot; nor a  second-precision \&quot;2026-10-01T09:30:00Z\&quot;. | 
**ad_click_tracking** | [**[ExamAdClickTracking], none_type**](ExamAdClickTracking.md) | Optional ad-level click tracking configuration. | [optional] 
**ad_impression_tracking** | [**[ExamAdImpressionTracking], none_type**](ExamAdImpressionTracking.md) | Optional ad-level impression tracking configuration. | [optional] 
**description** | **str, none_type** | The description of the ad | [optional] 
**end_date** | **str, none_type** | The date when we will stop showing this ad, which must come after the start date. If the end  date is not specified (i.e. null) then the ad will go on forever.  String must be in ISO8601 format, more precisely \&quot;yyyy-MM-ddTHH:mm:ss.fffZ\&quot;: a UTC timestamp whose  three millisecond digits and trailing \&quot;Z\&quot; are both required, for example \&quot;2026-10-01T09:30:00.000Z\&quot;.  No other ISO8601 layout is accepted, neither a UTC offset such as \&quot;2026-10-01T11:30:00+02:00\&quot; nor a  second-precision \&quot;2026-10-01T09:30:00Z\&quot;. | [optional] 
**id** | **str, none_type** |  | [optional] 
**inventory_type** | **str, none_type** | The inventory the Ad to be created or updated belongs to. Possible values are \&quot;Display\&quot;, \&quot;Native\&quot;,  \&quot;Video\&quot; and \&quot;Meta\&quot;. This is optional since it doesn&#39;t make sense for every creative type: it is inferred  from the creative for a video creative, and an error is returned if it is not set for a dynamic creative.  \&quot;Meta\&quot; additionally requires the target ad set to be linked to Meta. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


