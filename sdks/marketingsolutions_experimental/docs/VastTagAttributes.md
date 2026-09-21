# VastTagAttributes

The attributes specific to VastTag creatives (read model).  Most fields are derived by parsing the VAST tag and are read-only.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_vpaid** | **bool, none_type** | Whether the tag contains a VPAID unit (vpaid y/n). Derived from the tag. VPAID is a deprecated  interactivity standard; this flag is recorded for information but interactive playback is not guaranteed. | [optional] 
**is_skippable** | **bool, none_type** | Whether the video is skippable. Derived from the tag. | [optional] 
**mime_types** | **[str], none_type** | The supported media-file mime types (e.g. \&quot;video/mp4\&quot;). Derived from the tag. | [optional] 
**vast_tag_url** | **str, none_type** | The VAST tag URL (a hosted VAST XML endpoint). | [optional] 
**vast_version** | **str, none_type** | The VAST version declared by the tag (e.g. \&quot;4.2\&quot;). Derived from the tag. | [optional] 
**video_duration_ms** | **float, none_type** | The video duration in milliseconds. Derived from the tag. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


