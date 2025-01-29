# CreateCoupon

Entity to create a Coupon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Coupon | 
**ad_set_id** | **str** | The id of the Ad Set on which the Coupon is applied to | 
**landing_page_url** | **str** | Web redirection of the landing page url | 
**start_date** | **str** | The date when the coupon will be launched  String must be in ISO8601 format | 
**format** | **str** | Format of the Coupon, it can have two values: \&quot;FullFrame\&quot; or \&quot;LogoZone\&quot; | 
**images** | [**[CreateImageSlide]**](CreateImageSlide.md) | List of slides containing the images as a base-64 encoded string | 
**show_every** | **int** | Show the Coupon every N seconds (between 1 and 10) | 
**show_duration** | **int** | Show Coupon for a duration of N seconds (between 1 and 5) | 
**rotations_number** | **int** | Number of rotations for the Coupons (from 1 to 10 times) | 
**description** | **str, none_type** | The description of the Coupon | [optional] 
**end_date** | **str, none_type** | The date when when we will stop to show this Coupon. If the end date is not specified (i.e. null) then the Coupon will go on forever  String must be in ISO8601 format | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


