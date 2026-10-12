# LineItemProductInput

One product to add to a line item's product pool. The product identifier is the resource id;  type-specific fields are grouped under the detail object selected by Criteo.RetailMedia.LineItem.AdContent.Contract.V2.Models.Products.LineItemProductInputModel.ProductType.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **str** | The type of the product, selecting which detail object is read. | 
**display_product_details** | **dict** | Onsite Display-specific product details supplied when adding a product. A display product is  identified entirely by its resource id, so this object carries no fields of its own today; it  exists so display can gain request-only fields without reshaping the request. | [optional] 
**sponsored_product_details** | [**SponsoredProductDetails**](SponsoredProductDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


