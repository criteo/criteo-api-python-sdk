# Criteo API SDK for Python

## Introduction

API Client Libraries can facilitate your use of the Criteo API allowing you to build unique and customized solutions to serve your businesses and clients.
These libraries can reduce the amount of code you need to write in order to start accessing Criteo programmatically. They also can help expedite troubleshooting, should you encounter any issues.

More information: [https://developers.criteo.com/marketing-solutions/docs/python-api-client-library](https://developers.criteo.com/marketing-solutions/docs/python-api-client-library)

[![](https://img.shields.io/pypi/pyversions/criteo-marketing.svg)](https://pypi.org/project/criteo-marketing-transition/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- Package version: 2021.10.0.211209

## Requirements

Python 2.7 and 3.5+

## Installation & Usage
### pip install

```sh
pip install criteo_api_retailmedia_v2021_10
```
(you may need to run `pip` with root permission: `sudo pip install criteo_api_retailmedia_v2021_10`)

Then import the package:
```python
import criteo_api_retailmedia_v2021_10 
```

### Manual Installation using [Setuptools](http://pypi.python.org/pypi/setuptools)

Download the code or clone the repository locally, then execute the following command:

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import criteo_api_retailmedia_v2021_10
```

## Example
Please see [examples/](examples/) for full examples to get a valid token and make a call to the API.

```sh
python ./examples/portfolio.py [client_id] [client_secret]
```

## Documentation for API Endpoints

The developers documentation is available at: *https://developers.criteo.com*.

All URIs are relative to *https://api.criteo.com*.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------


## Documentation For Models

 - [AddToBasketIdsUpdateModel202110Request](docs/AddToBasketIdsUpdateModel202110Request.md)
 - [AddToBasketTarget202110Request](docs/AddToBasketTarget202110Request.md)
 - [AddToBasketTarget202110Response](docs/AddToBasketTarget202110Response.md)
 - [AuctionLineItemCreateModelRequest](docs/AuctionLineItemCreateModelRequest.md)
 - [AuctionLineItemPagedListResponse](docs/AuctionLineItemPagedListResponse.md)
 - [AuctionLineItemResponse](docs/AuctionLineItemResponse.md)
 - [AuctionLineItemUpdateModelRequest](docs/AuctionLineItemUpdateModelRequest.md)
 - [AudienceIdsUpdateModel202110Request](docs/AudienceIdsUpdateModel202110Request.md)
 - [AudienceTarget202110Request](docs/AudienceTarget202110Request.md)
 - [AudienceTarget202110Response](docs/AudienceTarget202110Response.md)
 - [BadRequest](docs/BadRequest.md)
 - [Balance202110PagedListResponse](docs/Balance202110PagedListResponse.md)
 - [BalanceCampaign202110ListRequest](docs/BalanceCampaign202110ListRequest.md)
 - [BalanceCampaign202110PagedListResponse](docs/BalanceCampaign202110PagedListResponse.md)
 - [CommonError](docs/CommonError.md)
 - [CommonLineItemPagedListResponse](docs/CommonLineItemPagedListResponse.md)
 - [CommonLineItemResponse](docs/CommonLineItemResponse.md)
 - [CommonWarning](docs/CommonWarning.md)
 - [CreateAudienceBody](docs/CreateAudienceBody.md)
 - [CreateAudienceRequest](docs/CreateAudienceRequest.md)
 - [CreateRetailMediaAudienceResponse](docs/CreateRetailMediaAudienceResponse.md)
 - [Creative202110](docs/Creative202110.md)
 - [Creative202110ListResponse](docs/Creative202110ListResponse.md)
 - [EnvelopeReportRequest](docs/EnvelopeReportRequest.md)
 - [EnvelopeReportStatus](docs/EnvelopeReportStatus.md)
 - [Error](docs/Error.md)
 - [ExternalAccount](docs/ExternalAccount.md)
 - [ExternalAddToBasketIdsUpdateModel202110](docs/ExternalAddToBasketIdsUpdateModel202110.md)
 - [ExternalAddToBasketTarget202110](docs/ExternalAddToBasketTarget202110.md)
 - [ExternalAuctionLineItem](docs/ExternalAuctionLineItem.md)
 - [ExternalAuctionLineItemCreateModel](docs/ExternalAuctionLineItemCreateModel.md)
 - [ExternalAuctionLineItemUpdateModel](docs/ExternalAuctionLineItemUpdateModel.md)
 - [ExternalAudienceIdsUpdateModel202110](docs/ExternalAudienceIdsUpdateModel202110.md)
 - [ExternalAudienceTarget202110](docs/ExternalAudienceTarget202110.md)
 - [ExternalBalance202110](docs/ExternalBalance202110.md)
 - [ExternalBrand](docs/ExternalBrand.md)
 - [ExternalCampaign](docs/ExternalCampaign.md)
 - [ExternalCampaignAttributes](docs/ExternalCampaignAttributes.md)
 - [ExternalCatalogRequest](docs/ExternalCatalogRequest.md)
 - [ExternalCatalogStatus](docs/ExternalCatalogStatus.md)
 - [ExternalCommonLineItem](docs/ExternalCommonLineItem.md)
 - [ExternalEditableCampaignAttributes](docs/ExternalEditableCampaignAttributes.md)
 - [ExternalKeywordTarget202110](docs/ExternalKeywordTarget202110.md)
 - [ExternalLineItemCapping202110](docs/ExternalLineItemCapping202110.md)
 - [ExternalLineItemPage202110](docs/ExternalLineItemPage202110.md)
 - [ExternalLineItemPageCategory202110](docs/ExternalLineItemPageCategory202110.md)
 - [ExternalPostCampaign](docs/ExternalPostCampaign.md)
 - [ExternalPreferredLineItem202110](docs/ExternalPreferredLineItem202110.md)
 - [ExternalPreferredLineItemCreateModel202110](docs/ExternalPreferredLineItemCreateModel202110.md)
 - [ExternalPreferredLineItemUpdateModel202110](docs/ExternalPreferredLineItemUpdateModel202110.md)
 - [ExternalPromotedProduct202110](docs/ExternalPromotedProduct202110.md)
 - [ExternalPutCampaign](docs/ExternalPutCampaign.md)
 - [ExternalRetailer](docs/ExternalRetailer.md)
 - [ExternalRetailerPages202110](docs/ExternalRetailerPages202110.md)
 - [ExternalStoreIdsUpdateModel202110](docs/ExternalStoreIdsUpdateModel202110.md)
 - [ExternalStoreTarget202110](docs/ExternalStoreTarget202110.md)
 - [GetPageOfAudiencesByAccountIdResponse](docs/GetPageOfAudiencesByAccountIdResponse.md)
 - [InputResourceOfAuctionLineItemCreateModel](docs/InputResourceOfAuctionLineItemCreateModel.md)
 - [InputResourceOfPreferredLineItemCreateModel202110](docs/InputResourceOfPreferredLineItemCreateModel202110.md)
 - [JsonApiBodyWithExternalIdOfEditableCampaignAttributesAndCampaign](docs/JsonApiBodyWithExternalIdOfEditableCampaignAttributesAndCampaign.md)
 - [JsonApiBodyWithIdOfInt64AndAccountAndAccount](docs/JsonApiBodyWithIdOfInt64AndAccountAndAccount.md)
 - [JsonApiBodyWithIdOfInt64AndBrandAndBrand](docs/JsonApiBodyWithIdOfInt64AndBrandAndBrand.md)
 - [JsonApiBodyWithIdOfInt64AndCampaignAndCampaign](docs/JsonApiBodyWithIdOfInt64AndCampaignAndCampaign.md)
 - [JsonApiBodyWithIdOfInt64AndCatalogStatusAndCatalogStatus](docs/JsonApiBodyWithIdOfInt64AndCatalogStatusAndCatalogStatus.md)
 - [JsonApiBodyWithIdOfInt64AndRetailerAndRetailer](docs/JsonApiBodyWithIdOfInt64AndRetailerAndRetailer.md)
 - [JsonApiBodyWithoutIdOfCampaignAttributesAndCampaign](docs/JsonApiBodyWithoutIdOfCampaignAttributesAndCampaign.md)
 - [JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequest](docs/JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequest.md)
 - [JsonApiPageResponseOfAccount](docs/JsonApiPageResponseOfAccount.md)
 - [JsonApiPageResponseOfBrand](docs/JsonApiPageResponseOfBrand.md)
 - [JsonApiPageResponseOfCampaign](docs/JsonApiPageResponseOfCampaign.md)
 - [JsonApiPageResponseOfRetailer](docs/JsonApiPageResponseOfRetailer.md)
 - [JsonApiRequestOfCatalogRequest](docs/JsonApiRequestOfCatalogRequest.md)
 - [JsonApiSingleResponseOfCampaign](docs/JsonApiSingleResponseOfCampaign.md)
 - [JsonApiSingleResponseOfCatalogStatus](docs/JsonApiSingleResponseOfCatalogStatus.md)
 - [JwtModel](docs/JwtModel.md)
 - [KeywordTarget202110Request](docs/KeywordTarget202110Request.md)
 - [KeywordTarget202110Response](docs/KeywordTarget202110Response.md)
 - [MapString](docs/MapString.md)
 - [OAuth2Error](docs/OAuth2Error.md)
 - [PageMetadata](docs/PageMetadata.md)
 - [PreferredLineItem202110PagedListResponse](docs/PreferredLineItem202110PagedListResponse.md)
 - [PreferredLineItem202110Response](docs/PreferredLineItem202110Response.md)
 - [PreferredLineItemCreateModel202110Request](docs/PreferredLineItemCreateModel202110Request.md)
 - [PreferredLineItemUpdateModel202110Request](docs/PreferredLineItemUpdateModel202110Request.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [PromotedProduct202110ListRequest](docs/PromotedProduct202110ListRequest.md)
 - [PromotedProduct202110PagedListResponse](docs/PromotedProduct202110PagedListResponse.md)
 - [ReportRequest](docs/ReportRequest.md)
 - [ReportRequestAttributes](docs/ReportRequestAttributes.md)
 - [ReportStatus](docs/ReportStatus.md)
 - [ReportStatusAttributes](docs/ReportStatusAttributes.md)
 - [ResourceOfAuctionLineItem](docs/ResourceOfAuctionLineItem.md)
 - [ResourceOfAuctionLineItemUpdateModel](docs/ResourceOfAuctionLineItemUpdateModel.md)
 - [ResourceOfBalance202110](docs/ResourceOfBalance202110.md)
 - [ResourceOfBalanceCampaign202110](docs/ResourceOfBalanceCampaign202110.md)
 - [ResourceOfCommonLineItem](docs/ResourceOfCommonLineItem.md)
 - [ResourceOfCreative202110](docs/ResourceOfCreative202110.md)
 - [ResourceOfPreferredLineItem202110](docs/ResourceOfPreferredLineItem202110.md)
 - [ResourceOfPreferredLineItemUpdateModel202110](docs/ResourceOfPreferredLineItemUpdateModel202110.md)
 - [ResourceOfPromotedProduct202110](docs/ResourceOfPromotedProduct202110.md)
 - [RetailMediaAudience](docs/RetailMediaAudience.md)
 - [RetailMediaAudienceAttributes](docs/RetailMediaAudienceAttributes.md)
 - [StoreIdsUpdateModel202110Request](docs/StoreIdsUpdateModel202110Request.md)
 - [StoreTarget202110Request](docs/StoreTarget202110Request.md)
 - [StoreTarget202110Response](docs/StoreTarget202110Response.md)
 - [ValueTypeResourceOfAddToBasketIdsUpdateModel202110](docs/ValueTypeResourceOfAddToBasketIdsUpdateModel202110.md)
 - [ValueTypeResourceOfAddToBasketTarget202110](docs/ValueTypeResourceOfAddToBasketTarget202110.md)
 - [ValueTypeResourceOfAudienceIdsUpdateModel202110](docs/ValueTypeResourceOfAudienceIdsUpdateModel202110.md)
 - [ValueTypeResourceOfAudienceTarget202110](docs/ValueTypeResourceOfAudienceTarget202110.md)
 - [ValueTypeResourceOfKeywordTarget202110](docs/ValueTypeResourceOfKeywordTarget202110.md)
 - [ValueTypeResourceOfStoreIdsUpdateModel202110](docs/ValueTypeResourceOfStoreIdsUpdateModel202110.md)
 - [ValueTypeResourceOfStoreTarget202110](docs/ValueTypeResourceOfStoreTarget202110.md)


## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.