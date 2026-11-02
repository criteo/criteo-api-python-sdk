# PageSetting

One page type to include in the forecast, and how to filter its inventory.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_type** | **str** | Page type to forecast. | 
**keywords** | **[str]** | Keywords to filter inventory by, up to 100. Required when &#x60;pageType&#x60; is  &#x60;search&#x60; or &#x60;searchBar&#x60;. Recommended  keywords come from &#x60;POST /retail-media/retailers/{retailerId}/recommend-keywords&#x60;. | [optional] 
**page_cpm** | [**PageSettingPageCpm**](PageSettingPageCpm.md) |  | [optional] 
**taxonomy_ids** | **[str]** | Retail Media category IDs to filter inventory by, up to 100. Required when  &#x60;pageType&#x60; is &#x60;category&#x60;,  &#x60;productDetail&#x60;, &#x60;categoryMenu&#x60; or  &#x60;merchandising&#x60;. The ids come from the returned category &#x60;id&#x60;  of &#x60;POST /retail-media/retailers/{retailerId}/categories/search&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


