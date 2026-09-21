# ShowcaseAttributes

The attributes specific to Showcase creatives (read).  On read, URLs are returned instead of base64.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_deeplink_url** | **str, none_type** | Android deep-link URL. | [optional] 
**app_link_url** | **str, none_type** | App link URL (Android fallback). | [optional] 
**branding_image_click_url** | **str, none_type** | Click URL associated with the branding images. | [optional] 
**branding_images** | [**[ShowcaseBrandingImage], none_type**](ShowcaseBrandingImage.md) | Branding images per shape (horizontal, vertical, square) displayed in the creative. | [optional] 
**calls_to_action** | **[str], none_type** | A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as \&quot;Buy now\&quot; or \&quot;Go!\&quot;. | [optional] 
**colors** | [**ShowcaseColors**](ShowcaseColors.md) |  | [optional] 
**ios_deeplink_url** | **str, none_type** | iOS deep-link URL. | [optional] 
**landing_page_url** | **str, none_type** | Web redirection of the landing page URL. | [optional] 
**layouts** | **[str], none_type** | The layouts enabled for this Showcase creative.  Possible values include \&quot;Showcase\&quot;. | [optional] 
**logos** | [**[ShowcaseLogo], none_type**](ShowcaseLogo.md) | Logo images with their shape and URL. | [optional] 
**meta_setting** | [**ShowcaseMetaSetting**](ShowcaseMetaSetting.md) |  | [optional] 
**price_settings** | [**ShowcasePriceSettings**](ShowcasePriceSettings.md) |  | [optional] 
**primary_font** | **str, none_type** | Font of the primary font.  Valid supported font like \&quot;Arial\&quot; | [optional] 
**product_image_display** | **str, none_type** | Value can be \&quot;ShowFullImage\&quot; or \&quot;ZoomOnImage\&quot;. Choose whether your product catalog images should fit inside the allocated  space (\&quot;ShowFullImage\&quot;) or whether they should fill that space (\&quot;ZoomOnImage\&quot;). If you choose ZoomOnImage, there may be some  image cropping. | [optional] 
**secondary_font** | **str, none_type** | Font of the secondary font.  Valid supported font like \&quot;Arial\&quot; | [optional] 
**universal_link_url** | **str, none_type** | Universal link URL (iOS fallback). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


