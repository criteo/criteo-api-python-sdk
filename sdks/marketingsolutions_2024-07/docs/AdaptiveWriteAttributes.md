# AdaptiveWriteAttributes

The attributes specific to create or update an Adaptive creative

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layouts** | **[str]** | The Adaptive layouts that are enabled.  It can contain any of the following values: \&quot;Editorial\&quot;, “Montage“, \&quot;InBannerVideo\&quot;. | 
**logo_base64_string** | **str** | Logo image as a base-64 encoded string | 
**headline_text** | **str** | The headline text of the banner | 
**headline_font** | **str** | Font of the headline  Valid supported font like \&quot;Arial\&quot; | 
**description_text** | **str** | The description text of the banner | 
**description_font** | **str** | Font of the description  Valid supported font like \&quot;Arial\&quot; | 
**calls_to_action** | **[str]** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. | 
**colors** | [**AdaptiveColors**](AdaptiveColors.md) |  | 
**landing_page_url** | **str** | Web redirection of the landing page url. | 
**image_sets_base64** | [**[ImageSetBase64], none_type**](ImageSetBase64.md) | Multiple image sets, each image set consists of multiple images as a base-64 encoded string and a headline text. | [optional] 
**image_display** | **str, none_type** | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your image set should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether it should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. | [optional] 
**video_base64_strings** | **[str], none_type** | Multiple videos potentially in different shapes, each video is a base-64 encoded string. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


