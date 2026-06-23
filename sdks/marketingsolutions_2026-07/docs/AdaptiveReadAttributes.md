# AdaptiveReadAttributes

The attributes specific to Adaptive creatives read

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls_to_action** | **[str], none_type** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. | [optional] 
**colors** | [**AdaptiveColors**](AdaptiveColors.md) |  | [optional] 
**description_font** | **str, none_type** | Font of the description  Valid supported font like \&quot;Arial\&quot; | [optional] 
**description_text** | **str, none_type** | The description text of the banner | [optional] 
**headline_font** | **str, none_type** | Font of the headline  Valid supported font like \&quot;Arial\&quot; | [optional] 
**headline_text** | **str, none_type** | The headline text of the banner | [optional] 
**image_display** | **str, none_type** | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your image set should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether it should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. | [optional] 
**image_sets** | [**[ImageSet], none_type**](ImageSet.md) | Multiple image sets, each image set consists of multiple images and a headline text. | [optional] 
**landing_page_url** | **str, none_type** | Web redirection of the landing page url | [optional] 
**layouts** | **[str], none_type** | The Adaptive layouts that are enabled.  It can contain any of the following values: \&quot;Editorial\&quot;, “Montage“, \&quot;InBannerVideo\&quot;. | [optional] 
**logos** | [**[ImageShape], none_type**](ImageShape.md) | Logo images uploaded on demostatic.criteo.com when deploying and then static.criteo.net | [optional] 
**videos** | [**[VideoDetail], none_type**](VideoDetail.md) | Multiple videos potentially in different shapes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


