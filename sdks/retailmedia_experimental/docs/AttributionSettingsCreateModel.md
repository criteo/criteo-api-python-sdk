# AttributionSettingsCreateModel

Wrapper for attribution settings. Each setting may be omitted, in which case it is  populated with the default for the campaign type: OnsiteDisplay defaults to a 14D click  window, a 14D view window and sameSkuCategory for both scopes; SponsoredProducts defaults  to a 30D click window, a 1D view window, sameSkuCategory click scope and sameSku view  scope.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**click_attribution_scope** | **str, none_type** | Post-click attribution scope setting. | [optional] 
**click_attribution_window** | **str, none_type** | Post-click attribution window setting. | [optional] 
**view_attribution_scope** | **str, none_type** | Post-view attribution scope setting. Must not be broader than the click attribution scope. | [optional] 
**view_attribution_window** | **str, none_type** | Post-view attribution window setting. Must not exceed the click attribution window. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


