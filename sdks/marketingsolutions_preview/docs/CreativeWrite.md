# CreativeWrite

Entity to create or update a creative

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the creative | 
**type** | **str** | The type of the creative  You can use \&quot;Image\&quot;, \&quot; ThirdPartyHtml\&quot; or \&quot;Dynamic\&quot; | 
**advertiser_id** | **str** | Advertiser linked to the Creative | 
**partner_id** | **str** | Partner linked to the Creative | 
**ad_set_id** | **str** | Ad set on which Creative will be applied | [optional] 
**description** | **str** | The description of the creative | [optional] 
**image_write_attributes** | [**ImageWriteAttributes**](ImageWriteAttributes.md) |  | [optional] 
**third_party_html_write_attributes** | [**ThirdPartyHtmlWriteAttributes**](ThirdPartyHtmlWriteAttributes.md) |  | [optional] 
**dynamic_write_attributes** | [**DynamicWriteAttributes**](DynamicWriteAttributes.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


