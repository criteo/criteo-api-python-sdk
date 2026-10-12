# CreativeSearchEnrichedResponse

Creative search-enriched response model. Same attributes as Criteo.RetailMedia.Creatives.Api.ExternalApi.Models.Creatives.V3.CreativeSearchResponse  plus the product collection constraints of the creative's template (retailer overrides applied).  The resource id is the first parent external id of the creative.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | Time search is created | [optional] 
**creative_type** | **str, none_type** | Creative type | [optional] 
**displayable_products_max** | **int, none_type** | Maximum number of displayable products allowed by the template | [optional] 
**modified_at** | **datetime, none_type** | Time it&#39;s modified | [optional] 
**name** | **str, none_type** | Name of the creative | [optional] 
**page_type** | **[str], none_type** | Page type | [optional] 
**preview** | **str, none_type** | Preview url of the creative | [optional] 
**product_collections_have_images** | **bool, none_type** | Whether the template&#39;s product collections carry an image | [optional] 
**product_collections_have_text** | **bool, none_type** | Whether the template&#39;s product collections carry a text | [optional] 
**product_collections_max** | **int, none_type** | Maximum number of product collections allowed by the template | [optional] 
**product_collections_min** | **int, none_type** | Minimum number of product collections required by the template | [optional] 
**products_per_collection_max** | **int, none_type** | Maximum number of products per collection allowed by the template | [optional] 
**products_per_collection_min** | **int, none_type** | Minimum number of products per collection required by the template | [optional] 
**retailer_id** | **str, none_type** | RetailerId of the search filter | [optional] 
**status** | **str, none_type** | The search status | [optional] 
**template_id** | **str, none_type** | Template Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


