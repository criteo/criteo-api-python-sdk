# Coupon

Coupons are static images applied on ad set which can be displayed within an ad and link to a landing page.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The name of the Coupon | [optional] 
**description** | **str, none_type** | The description of the Coupon | [optional] 
**author** | **str, none_type** | The login of the person who created this Coupon | [optional] 
**advertiser_id** | **str, none_type** | Advertiser linked to the Coupon | [optional] 
**ad_set_id** | **str, none_type** | The id of the Ad Set on which the Coupon is applied to | [optional] 
**landing_page_url** | **str, none_type** | Web redirection of the landing page url | [optional] 
**start_date** | **str, none_type** | The date when the Coupon will be launched  String must be in ISO8601 format | [optional] 
**end_date** | **str, none_type** | The date when when we will stop to show this Coupon. If the end date is not specified (i.e. null) then the Coupon will go on forever  String must be in ISO8601 format | [optional] 
**format** | **str, none_type** | Format of the Coupon, it can have two values: \&quot;FullFrame\&quot; or \&quot;LogoZone\&quot; | [optional] 
**status** | **str, none_type** | The status of the Coupon | [optional] 
**images** | [**[ImageSlide], none_type**](ImageSlide.md) | List of slides containing the image URLs | [optional] 
**show_every** | **int, none_type** | Show the Coupon every N seconds (between 1 and 10) | [optional] 
**show_duration** | **int, none_type** | Show Coupon for a duration of N seconds (between 1 and 5) | [optional] 
**rotations_number** | **int, none_type** | Number of rotations for the Coupons (from 1 to 10 times) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


