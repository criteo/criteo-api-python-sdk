# ProductTax

Defines the tax information of a product.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float, none_type** | The percentage of tax rate that applies to the item price. | [optional] 
**country** | **str, none_type** | The country within which the item is taxed, specified as a CLDR territory code. | [optional] 
**region** | **str, none_type** | The geographic region to which the tax rate applies. | [optional] 
**tax_ship** | **bool, none_type** | Set to true if tax is charged on shipping. | [optional] 
**location_id** | **int, none_type** | The numeric ID of a location that the tax rate applies to as defined in the AdWords API. | [optional] 
**postal_code** | **str, none_type** | The postal code range that the tax rate applies to, represented by a ZIP code, a ZIP code prefix using * wildcard, a range between two ZIP codes or two ZIP code prefixes of equal length. Examples: 94114, 94*, 94002-95460, 94*-95*. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


