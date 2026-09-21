# ShowcaseWriteAttributes

The attributes specific to create or update a Showcase creative (write).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls_to_action** | **[str]** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as \&quot;Buy now\&quot; or \&quot;Go!\&quot;. | 
**colors** | [**ShowcaseColors**](ShowcaseColors.md) |  | 
**layouts** | **[str]** | The layouts to enable for this Showcase creative.  Possible values include \&quot;Showcase\&quot;. | 
**logo_base64_strings** | [**[LogoInput]**](LogoInput.md) | Logo images as base-64 encoded strings with their shape.  At least one logo is required. | 
**product_image_display** | **str** | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your product catalog images should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether they should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. | 
**android_deeplink_url** | **str, none_type** | Android deep-link URL. | [optional] 
**app_link_url** | **str, none_type** | App link URL (Android fallback). | [optional] 
**branding_image_base64_strings** | [**[BrandingImageInput], none_type**](BrandingImageInput.md) | Branding images as base-64 encoded strings with their shape. | [optional] 
**branding_image_click_url** | **str, none_type** | Click URL associated with the branding images. | [optional] 
**ios_deeplink_url** | **str, none_type** | iOS deep-link URL. | [optional] 
**landing_page_url** | **str, none_type** | Web redirection of the landing page URL. | [optional] 
**meta_setting** | [**ShowcaseMetaSetting**](ShowcaseMetaSetting.md) |  | [optional] 
**price_settings** | [**ShowcasePriceSettings**](ShowcasePriceSettings.md) |  | [optional] 
**primary_font** | **str, none_type** | Font of the primary font.  Valid supported font like \&quot;Arial\&quot; | [optional] 
**secondary_font** | **str, none_type** | Font of the secondary font.  Valid supported font like \&quot;Arial\&quot; | [optional] 
**universal_link_url** | **str, none_type** | Universal link URL (iOS fallback). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


