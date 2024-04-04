# ProductShipping

Defines the shipping information of a product.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**Price**](Price.md) |  | [optional] 
**country** | **str, none_type** | The CLDR territory code of the country to which an item will ship. | [optional] 
**region** | **str, none_type** | The geographic region to which a shipping rate applies. | [optional] 
**service** | **str, none_type** | A free-form description of the service class or delivery speed. | [optional] 
**location_id** | **int, none_type** | The numeric ID of a location that the shipping rate applies to as defined in the AdWords API. | [optional] 
**location_group_name** | **str, none_type** | The location where the shipping is applicable, represented by a location group name. | [optional] 
**postal_code** | **str, none_type** | The postal code range that the shipping rate applies to, represented by a postal code, a postal code prefix followed by a * wildcard, a range between two postal codes or two postal code prefixes of equal length. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


