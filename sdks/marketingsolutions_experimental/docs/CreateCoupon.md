# CreateCoupon

Entity to create a Coupon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_id** | **str** | The id of the Ad Set on which the Coupon is applied to | 
**format** | **str** | Format of the Coupon, it can have two values: \&quot;FullFrame\&quot; or \&quot;LogoZone\&quot; | 
**images** | [**[CreateImageSlide]**](CreateImageSlide.md) | List of slides containing the images as a base-64 encoded string | 
**landing_page_url** | **str** | Web redirection of the landing page url | 
**name** | **str** | The name of the Coupon | 
**rotations_number** | **int** | Number of rotations for the Coupons (from 1 to 10 times) | 
**show_duration** | **int** | Show Coupon for a duration of N seconds (between 1 and 5) | 
**show_every** | **int** | Show the Coupon every N seconds (between 1 and 10) | 
**start_date** | **str** | The date when the coupon will be launched. It must be a date in the future.  String must be in ISO8601 format, more precisely \&quot;yyyy-MM-ddTHH:mm:ss.fffZ\&quot;: a UTC timestamp whose  three millisecond digits and trailing \&quot;Z\&quot; are both required, for example \&quot;2026-10-01T09:00:00.000Z\&quot;.  No other ISO8601 layout is accepted, neither a UTC offset such as \&quot;2026-10-01T11:00:00+02:00\&quot; nor a  second-precision \&quot;2026-10-01T09:00:00Z\&quot;.  A date that does not fall on a whole hour is rounded up to the next one, so  \&quot;2026-10-01T09:30:00.000Z\&quot; is stored as \&quot;2026-10-01T10:00:00.000Z\&quot;. | 
**description** | **str, none_type** | The description of the Coupon | [optional] 
**end_date** | **str, none_type** | The date when we will stop showing this coupon, which must come after the start date. If the  end date is not specified (i.e. null) then the coupon will go on forever.  String must be in ISO8601 format, more precisely \&quot;yyyy-MM-ddTHH:mm:ss.fffZ\&quot;: a UTC timestamp whose  three millisecond digits and trailing \&quot;Z\&quot; are both required, for example \&quot;2026-10-01T09:00:00.000Z\&quot;.  No other ISO8601 layout is accepted, neither a UTC offset such as \&quot;2026-10-01T11:00:00+02:00\&quot; nor a  second-precision \&quot;2026-10-01T09:00:00Z\&quot;.  A date that does not fall on a whole hour is rounded up to the next one, so  \&quot;2026-10-01T09:30:00.000Z\&quot; is stored as \&quot;2026-10-01T10:00:00.000Z\&quot;. | [optional] 
**id** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


