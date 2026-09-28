# UpdateCoupon

Entity to edit a Coupon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The date when the coupon will be launched. It must be a date in the future, and it must not  move earlier than the start date the coupon already has.  String must be in ISO8601 format, more precisely \&quot;yyyy-MM-ddTHH:mm:ss.fffZ\&quot;: a UTC timestamp whose  three millisecond digits and trailing \&quot;Z\&quot; are both required, for example \&quot;2026-10-01T09:00:00.000Z\&quot;.  No other ISO8601 layout is accepted, neither a UTC offset such as \&quot;2026-10-01T11:00:00+02:00\&quot; nor a  second-precision \&quot;2026-10-01T09:00:00Z\&quot;.  A date that does not fall on a whole hour is rounded up to the next one, so  \&quot;2026-10-01T09:30:00.000Z\&quot; is stored as \&quot;2026-10-01T10:00:00.000Z\&quot;. | 
**end_date** | **str, none_type** | The date when we will stop showing this coupon, which must come after the start date. If the  end date is not specified (i.e. null) then the coupon will go on forever.  String must be in ISO8601 format, more precisely \&quot;yyyy-MM-ddTHH:mm:ss.fffZ\&quot;: a UTC timestamp whose  three millisecond digits and trailing \&quot;Z\&quot; are both required, for example \&quot;2026-10-01T09:00:00.000Z\&quot;.  No other ISO8601 layout is accepted, neither a UTC offset such as \&quot;2026-10-01T11:00:00+02:00\&quot; nor a  second-precision \&quot;2026-10-01T09:00:00Z\&quot;.  A date that does not fall on a whole hour is rounded up to the next one, so  \&quot;2026-10-01T09:30:00.000Z\&quot; is stored as \&quot;2026-10-01T10:00:00.000Z\&quot;. | [optional] 
**id** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


