# AdaptiveAttributes

The attributes specific to Adaptive creatives

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layouts** | **[str]** | The Adaptive layouts that are enabled.  It can contain any of the following values: \&quot;Editorial\&quot;, “Montage“, \&quot;InBannerVideo\&quot;. | 
**logos** | [**[ImageShape]**](ImageShape.md) | Logo images uploaded on demostatic.criteo.com when deploying and then static.criteo.net | 
**headline_text** | **str** | The headline text of the banner | 
**headline_font** | **str** | Font of the headline  Valid supported font like \&quot;Arial\&quot; | 
**description_text** | **str** | The description text of the banner | 
**description_font** | **str** | Font of the description  Valid supported font like \&quot;Arial\&quot; | 
**calls_to_action** | **[str]** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”. | 
**colors** | [**AdaptiveColors**](AdaptiveColors.md) |  | 
**landing_page_url** | **str** | Web redirection of the landing page url | 
**image_sets** | [**[ImageSet]**](ImageSet.md) | Multiple image sets, each image set consists of multiple images and a headline text. | [optional] 
**image_display** | **str** | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your image set should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether it should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. | [optional] 
**videos** | [**[VideoDetail]**](VideoDetail.md) | Multiple videos potentially in different shapes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


