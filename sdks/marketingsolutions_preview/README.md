# Criteo API SDK for Python

## Introduction
API Client Libraries can facilitate your use of the Criteo API allowing you to build unique and customized solutions to serve your businesses and clients.
These libraries can reduce the amount of code you need to write in order to start accessing Criteo programmatically. They also can help expedite troubleshooting, should you encounter any issues.

More information on how to use Criteo API and these SDKs can be found at: [https://developers.criteo.com/](https://developers.criteo.com/).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- Package version: 0.0.241029

## Requirements

Python 2.7 and 3.5+

## Installation & Usage
### pip install

```sh
pip install criteo-api-marketingsolutions-sdk==0.0.241029
```
(you may need to run `pip` with root permission: `sudo pip install criteo-api-marketingsolutions-sdk==0.0.241029`)

Then import the package:
```python
import criteo_api_marketingsolutions_preview
```

### Manual Installation using [Setuptools](http://pypi.python.org/pypi/setuptools)

Download the code or clone the repository locally, then execute the following command:

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import criteo_api_marketingsolutions_preview
```

## Example
There are multiple examples for the different OAuth flows that the SDK supports.
- See [test/example_application_with_client_credentials.py](test/example_application_with_client_credentials.py) for an example with Client Credentials.
- See [test/example_application_with_auth_code.py](test/example_application_with_auth_code.py) for an example with Authorization Code.
Once you follow the authorization code flow, you will have a refresh token that has to be used to regenerate access token for future usage. 
    - See [test/example_application_with_refresh_token.py](test/example_application_with_refresh_token.py) for an example with Refresh Token .

## Documentation for API Endpoints

The developers documentation is available at: *https://developers.criteo.com*.

All URIs are relative to *https://api.criteo.com*.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------


## Documentation For Models

 - [Ad](docs/Ad.md)
 - [AdListResponse](docs/AdListResponse.md)
 - [AdResource](docs/AdResource.md)
 - [AdResponse](docs/AdResponse.md)
 - [AdSetAudienceLinkEntityV1](docs/AdSetAudienceLinkEntityV1.md)
 - [AdSetAudienceLinkEntityV1Resource](docs/AdSetAudienceLinkEntityV1Resource.md)
 - [AdSetAudienceLinkEntityV1Response](docs/AdSetAudienceLinkEntityV1Response.md)
 - [AdSetAudienceLinkInputEntityV1](docs/AdSetAudienceLinkInputEntityV1.md)
 - [AdSetCategoryBid](docs/AdSetCategoryBid.md)
 - [AdSetCategoryBidListResponse](docs/AdSetCategoryBidListResponse.md)
 - [AdSetCategoryBidResource](docs/AdSetCategoryBidResource.md)
 - [AdSetDeliveryLimitationsV24Q3](docs/AdSetDeliveryLimitationsV24Q3.md)
 - [AdSetDisplayMultiplier](docs/AdSetDisplayMultiplier.md)
 - [AdSetDisplayMultiplierListResponse](docs/AdSetDisplayMultiplierListResponse.md)
 - [AdSetDisplayMultiplierResource](docs/AdSetDisplayMultiplierResource.md)
 - [AdSetFrequencyCappingV24Q3](docs/AdSetFrequencyCappingV24Q3.md)
 - [AdSetGeoLocationV24Q3](docs/AdSetGeoLocationV24Q3.md)
 - [AdSetSearchFilterV24Q3](docs/AdSetSearchFilterV24Q3.md)
 - [AdSetSearchRequestV24Q3](docs/AdSetSearchRequestV24Q3.md)
 - [AdSetTargetingDealIds](docs/AdSetTargetingDealIds.md)
 - [AdSetTargetingDealIdsDisableResultResource](docs/AdSetTargetingDealIdsDisableResultResource.md)
 - [AdSetTargetingDealIdsDisableResultResponse](docs/AdSetTargetingDealIdsDisableResultResponse.md)
 - [AdSetTargetingDealIdsResource](docs/AdSetTargetingDealIdsResource.md)
 - [AdSetTargetingDealIdsResponse](docs/AdSetTargetingDealIdsResponse.md)
 - [AdSetTargetingDealIdsSetResultResource](docs/AdSetTargetingDealIdsSetResultResource.md)
 - [AdSetTargetingDealIdsSetResultResponse](docs/AdSetTargetingDealIdsSetResultResponse.md)
 - [AdSetTargetingRuleV24Q3](docs/AdSetTargetingRuleV24Q3.md)
 - [AdSetTargetingV24Q3](docs/AdSetTargetingV24Q3.md)
 - [AdSetTargetingVideoPositioning](docs/AdSetTargetingVideoPositioning.md)
 - [AdSetTargetingVideoPositioningDisableResultResource](docs/AdSetTargetingVideoPositioningDisableResultResource.md)
 - [AdSetTargetingVideoPositioningDisableResultResponse](docs/AdSetTargetingVideoPositioningDisableResultResponse.md)
 - [AdSetTargetingVideoPositioningResource](docs/AdSetTargetingVideoPositioningResource.md)
 - [AdSetTargetingVideoPositioningResponse](docs/AdSetTargetingVideoPositioningResponse.md)
 - [AdSetTargetingVideoPositioningSetResultResource](docs/AdSetTargetingVideoPositioningSetResultResource.md)
 - [AdSetTargetingVideoPositioningSetResultResponse](docs/AdSetTargetingVideoPositioningSetResultResponse.md)
 - [AdWrite](docs/AdWrite.md)
 - [AdWriteRequest](docs/AdWriteRequest.md)
 - [AdWriteResource](docs/AdWriteResource.md)
 - [AdaptiveAttributes](docs/AdaptiveAttributes.md)
 - [AdaptiveColors](docs/AdaptiveColors.md)
 - [AdaptiveWriteAttributes](docs/AdaptiveWriteAttributes.md)
 - [AdvertiserCreationInput](docs/AdvertiserCreationInput.md)
 - [AdvertiserCreationRequest](docs/AdvertiserCreationRequest.md)
 - [AdvertiserCreationResponse](docs/AdvertiserCreationResponse.md)
 - [AdvertiserDatasetListResponse](docs/AdvertiserDatasetListResponse.md)
 - [AlgebraNodeV1](docs/AlgebraNodeV1.md)
 - [ApiErrorResponse](docs/ApiErrorResponse.md)
 - [ApiRequestOfTargetingEntity](docs/ApiRequestOfTargetingEntity.md)
 - [ApiResponseOfTargetingEntity](docs/ApiResponseOfTargetingEntity.md)
 - [ApplicationSummaryModel](docs/ApplicationSummaryModel.md)
 - [ApplicationSummaryModelResource](docs/ApplicationSummaryModelResource.md)
 - [ApplicationSummaryModelResponse](docs/ApplicationSummaryModelResponse.md)
 - [Attribute](docs/Attribute.md)
 - [AudienceBulkCreateInputV1](docs/AudienceBulkCreateInputV1.md)
 - [AudienceBulkDeleteInputV1](docs/AudienceBulkDeleteInputV1.md)
 - [AudienceBulkUpdateInputV1](docs/AudienceBulkUpdateInputV1.md)
 - [AudienceComputeSizeEntityV1Resource](docs/AudienceComputeSizeEntityV1Resource.md)
 - [AudienceComputeSizesInputV1](docs/AudienceComputeSizesInputV1.md)
 - [AudienceCreateEntityV1](docs/AudienceCreateEntityV1.md)
 - [AudienceCreateEntityV1Resource](docs/AudienceCreateEntityV1Resource.md)
 - [AudienceDeleteEntityV1Resource](docs/AudienceDeleteEntityV1Resource.md)
 - [AudienceEntityV1](docs/AudienceEntityV1.md)
 - [AudienceEntityV1AudienceSearchMetadataV1ListResponse](docs/AudienceEntityV1AudienceSearchMetadataV1ListResponse.md)
 - [AudienceEntityV1ListResponse](docs/AudienceEntityV1ListResponse.md)
 - [AudienceEntityV1Resource](docs/AudienceEntityV1Resource.md)
 - [AudienceError](docs/AudienceError.md)
 - [AudienceEstimateSizeEntityV1](docs/AudienceEstimateSizeEntityV1.md)
 - [AudienceEstimateSizeEntityV1Resource](docs/AudienceEstimateSizeEntityV1Resource.md)
 - [AudienceEstimateSizeInputV1](docs/AudienceEstimateSizeInputV1.md)
 - [AudienceIdEntityV1ListResponse](docs/AudienceIdEntityV1ListResponse.md)
 - [AudienceIdEntityV1Resource](docs/AudienceIdEntityV1Resource.md)
 - [AudienceNameDescription](docs/AudienceNameDescription.md)
 - [AudienceSearchEntityV1](docs/AudienceSearchEntityV1.md)
 - [AudienceSearchEntityV1Resource](docs/AudienceSearchEntityV1Resource.md)
 - [AudienceSearchInputV1](docs/AudienceSearchInputV1.md)
 - [AudienceSearchMetadataV1](docs/AudienceSearchMetadataV1.md)
 - [AudienceSegmentBulkCreateInputV1](docs/AudienceSegmentBulkCreateInputV1.md)
 - [AudienceSegmentBulkDeleteInputV1](docs/AudienceSegmentBulkDeleteInputV1.md)
 - [AudienceSegmentBulkUpdateInputV1](docs/AudienceSegmentBulkUpdateInputV1.md)
 - [AudienceSegmentComputeSizeEntityV1Resource](docs/AudienceSegmentComputeSizeEntityV1Resource.md)
 - [AudienceSegmentComputeSizesInputV1](docs/AudienceSegmentComputeSizesInputV1.md)
 - [AudienceSegmentCreateEntityV1](docs/AudienceSegmentCreateEntityV1.md)
 - [AudienceSegmentCreateEntityV1Resource](docs/AudienceSegmentCreateEntityV1Resource.md)
 - [AudienceSegmentDeleteEntityV1Resource](docs/AudienceSegmentDeleteEntityV1Resource.md)
 - [AudienceSegmentEntityV1](docs/AudienceSegmentEntityV1.md)
 - [AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse](docs/AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse.md)
 - [AudienceSegmentEntityV1ListResponse](docs/AudienceSegmentEntityV1ListResponse.md)
 - [AudienceSegmentEntityV1Resource](docs/AudienceSegmentEntityV1Resource.md)
 - [AudienceSegmentEstimateSizeInputV1](docs/AudienceSegmentEstimateSizeInputV1.md)
 - [AudienceSegmentIdEntityV1ListResponse](docs/AudienceSegmentIdEntityV1ListResponse.md)
 - [AudienceSegmentIdEntityV1Resource](docs/AudienceSegmentIdEntityV1Resource.md)
 - [AudienceSegmentSearchEntityV1](docs/AudienceSegmentSearchEntityV1.md)
 - [AudienceSegmentSearchEntityV1Resource](docs/AudienceSegmentSearchEntityV1Resource.md)
 - [AudienceSegmentSearchInputV1](docs/AudienceSegmentSearchInputV1.md)
 - [AudienceSegmentSearchMetadataV1](docs/AudienceSegmentSearchMetadataV1.md)
 - [AudienceSegmentSizeEntityV1](docs/AudienceSegmentSizeEntityV1.md)
 - [AudienceSegmentSizeEntityV1ListResponse](docs/AudienceSegmentSizeEntityV1ListResponse.md)
 - [AudienceSegmentSizeEntityV1Resource](docs/AudienceSegmentSizeEntityV1Resource.md)
 - [AudienceSegmentSizeEstimationEntityV1](docs/AudienceSegmentSizeEstimationEntityV1.md)
 - [AudienceSegmentSizeEstimationEntityV1Resource](docs/AudienceSegmentSizeEstimationEntityV1Resource.md)
 - [AudienceSegmentSizeEstimationV1](docs/AudienceSegmentSizeEstimationV1.md)
 - [AudienceSegmentSizeEstimationV1Resource](docs/AudienceSegmentSizeEstimationV1Resource.md)
 - [AudienceSegmentSizeEstimationV1Response](docs/AudienceSegmentSizeEstimationV1Response.md)
 - [AudienceSegmentUpdateEntityV1](docs/AudienceSegmentUpdateEntityV1.md)
 - [AudienceSegmentUpdateEntityV1Resource](docs/AudienceSegmentUpdateEntityV1Resource.md)
 - [AudienceSizeEntityV1](docs/AudienceSizeEntityV1.md)
 - [AudienceSizeEntityV1ListResponse](docs/AudienceSizeEntityV1ListResponse.md)
 - [AudienceSizeEntityV1Resource](docs/AudienceSizeEntityV1Resource.md)
 - [AudienceSizeEstimationV1](docs/AudienceSizeEstimationV1.md)
 - [AudienceSizeEstimationV1Resource](docs/AudienceSizeEstimationV1Resource.md)
 - [AudienceSizeEstimationV1Response](docs/AudienceSizeEstimationV1Response.md)
 - [AudienceUpdateEntityV1](docs/AudienceUpdateEntityV1.md)
 - [AudienceUpdateEntityV1Resource](docs/AudienceUpdateEntityV1Resource.md)
 - [AudienceWarning](docs/AudienceWarning.md)
 - [BasicAudienceDefinition](docs/BasicAudienceDefinition.md)
 - [BatchAcceptedResponse](docs/BatchAcceptedResponse.md)
 - [BehavioralV1](docs/BehavioralV1.md)
 - [CampaignSearchFiltersV23Q1](docs/CampaignSearchFiltersV23Q1.md)
 - [CampaignSearchRequestV23Q1](docs/CampaignSearchRequestV23Q1.md)
 - [CampaignSpendLimitV23Q1](docs/CampaignSpendLimitV23Q1.md)
 - [CampaignV23Q1](docs/CampaignV23Q1.md)
 - [CampaignV23Q1ListResponse](docs/CampaignV23Q1ListResponse.md)
 - [CampaignV23Q1Resource](docs/CampaignV23Q1Resource.md)
 - [CampaignV23Q1Response](docs/CampaignV23Q1Response.md)
 - [CommonProblem](docs/CommonProblem.md)
 - [ContactListStatisticsEntityV1](docs/ContactListStatisticsEntityV1.md)
 - [ContactListStatisticsEntityV1Resource](docs/ContactListStatisticsEntityV1Resource.md)
 - [ContactListStatisticsEntityV1Response](docs/ContactListStatisticsEntityV1Response.md)
 - [ContactListV1](docs/ContactListV1.md)
 - [ContactlistAmendment](docs/ContactlistAmendment.md)
 - [ContactlistAmendmentAttributes](docs/ContactlistAmendmentAttributes.md)
 - [ContactlistAmendmentRequest](docs/ContactlistAmendmentRequest.md)
 - [ContactlistOperation](docs/ContactlistOperation.md)
 - [ContactlistOperationAttributes](docs/ContactlistOperationAttributes.md)
 - [ContactlistWithAttributesAmendment](docs/ContactlistWithAttributesAmendment.md)
 - [ContactlistWithAttributesAmendmentAttributes](docs/ContactlistWithAttributesAmendmentAttributes.md)
 - [ContactlistWithAttributesAmendmentRequest](docs/ContactlistWithAttributesAmendmentRequest.md)
 - [Coupon](docs/Coupon.md)
 - [CouponListResponse](docs/CouponListResponse.md)
 - [CouponResource](docs/CouponResource.md)
 - [CouponResponse](docs/CouponResponse.md)
 - [CouponSupportedSizes](docs/CouponSupportedSizes.md)
 - [CouponSupportedSizesResource](docs/CouponSupportedSizesResource.md)
 - [CouponSupportedSizesResponse](docs/CouponSupportedSizesResponse.md)
 - [CreateAdSetBiddingV24Q3](docs/CreateAdSetBiddingV24Q3.md)
 - [CreateAdSetBudgetV24Q3](docs/CreateAdSetBudgetV24Q3.md)
 - [CreateAdSetGeoLocationV24Q3](docs/CreateAdSetGeoLocationV24Q3.md)
 - [CreateAdSetScheduleV24Q3](docs/CreateAdSetScheduleV24Q3.md)
 - [CreateAdSetTargetingV24Q3](docs/CreateAdSetTargetingV24Q3.md)
 - [CreateAdSetV24Q3](docs/CreateAdSetV24Q3.md)
 - [CreateAdSetV24Q3Request](docs/CreateAdSetV24Q3Request.md)
 - [CreateAdSetV24Q3Resource](docs/CreateAdSetV24Q3Resource.md)
 - [CreateCampaign](docs/CreateCampaign.md)
 - [CreateCampaignRequest](docs/CreateCampaignRequest.md)
 - [CreateCampaignResource](docs/CreateCampaignResource.md)
 - [CreateCampaignSpendLimit](docs/CreateCampaignSpendLimit.md)
 - [CreateCoupon](docs/CreateCoupon.md)
 - [CreateCouponRequest](docs/CreateCouponRequest.md)
 - [CreateCouponResource](docs/CreateCouponResource.md)
 - [CreateImageSlide](docs/CreateImageSlide.md)
 - [CreateProductFilterRequest](docs/CreateProductFilterRequest.md)
 - [CreateProductSetRequest](docs/CreateProductSetRequest.md)
 - [Creative](docs/Creative.md)
 - [CreativeListResponse](docs/CreativeListResponse.md)
 - [CreativeResource](docs/CreativeResource.md)
 - [CreativeResponse](docs/CreativeResponse.md)
 - [CreativeWrite](docs/CreativeWrite.md)
 - [CreativeWriteRequest](docs/CreativeWriteRequest.md)
 - [CreativeWriteResource](docs/CreativeWriteResource.md)
 - [CriteoApiError](docs/CriteoApiError.md)
 - [CriteoApiWarning](docs/CriteoApiWarning.md)
 - [CriteoApiWarningV2](docs/CriteoApiWarningV2.md)
 - [CustomAttribute](docs/CustomAttribute.md)
 - [Dataset](docs/Dataset.md)
 - [DealId](docs/DealId.md)
 - [DeleteAudienceContactListResponse](docs/DeleteAudienceContactListResponse.md)
 - [DynamicAttributes](docs/DynamicAttributes.md)
 - [DynamicWriteAttributes](docs/DynamicWriteAttributes.md)
 - [EntityFilter](docs/EntityFilter.md)
 - [EntityOfPortfolioMessage](docs/EntityOfPortfolioMessage.md)
 - [EntityV2OfDataset](docs/EntityV2OfDataset.md)
 - [EntityV2OfObject](docs/EntityV2OfObject.md)
 - [EntityWrapperOfTargetingEntity](docs/EntityWrapperOfTargetingEntity.md)
 - [ErrorCodeResponse](docs/ErrorCodeResponse.md)
 - [ErrorDescription](docs/ErrorDescription.md)
 - [ExportColumn](docs/ExportColumn.md)
 - [ExportMetaData](docs/ExportMetaData.md)
 - [ExportResult](docs/ExportResult.md)
 - [ExportResultData](docs/ExportResultData.md)
 - [FailResponse](docs/FailResponse.md)
 - [GenerateAudiencePerformanceReport](docs/GenerateAudiencePerformanceReport.md)
 - [GenerateAudiencePerformanceReportRequest](docs/GenerateAudiencePerformanceReportRequest.md)
 - [GenerateAudiencePerformanceReportResource](docs/GenerateAudiencePerformanceReportResource.md)
 - [GenerateCategoriesReportRequestAttributes](docs/GenerateCategoriesReportRequestAttributes.md)
 - [GenerateCategoriesReportRequestAttributesRequest](docs/GenerateCategoriesReportRequestAttributesRequest.md)
 - [GenerateCategoriesReportRequestAttributesResource](docs/GenerateCategoriesReportRequestAttributesResource.md)
 - [GenerateCreativesReportRequestAttributes](docs/GenerateCreativesReportRequestAttributes.md)
 - [GenerateCreativesReportRequestAttributesRequest](docs/GenerateCreativesReportRequestAttributesRequest.md)
 - [GenerateCreativesReportRequestAttributesResource](docs/GenerateCreativesReportRequestAttributesResource.md)
 - [GenerateStatisticsReport](docs/GenerateStatisticsReport.md)
 - [GenerateStatisticsReportRequest](docs/GenerateStatisticsReportRequest.md)
 - [GenerateStatisticsReportResource](docs/GenerateStatisticsReportResource.md)
 - [GenerateTopProductsReportRequestAttributes](docs/GenerateTopProductsReportRequestAttributes.md)
 - [GenerateTopProductsReportRequestAttributesRequest](docs/GenerateTopProductsReportRequestAttributesRequest.md)
 - [GenerateTopProductsReportRequestAttributesResource](docs/GenerateTopProductsReportRequestAttributesResource.md)
 - [GetPortfolioResponse](docs/GetPortfolioResponse.md)
 - [HtmlTagAttributes](docs/HtmlTagAttributes.md)
 - [HtmlTagWriteAttributes](docs/HtmlTagWriteAttributes.md)
 - [ImageAttributes](docs/ImageAttributes.md)
 - [ImageSet](docs/ImageSet.md)
 - [ImageSetBase64](docs/ImageSetBase64.md)
 - [ImageShape](docs/ImageShape.md)
 - [ImageSlide](docs/ImageSlide.md)
 - [ImageWriteAttributes](docs/ImageWriteAttributes.md)
 - [InMarketAudienceSegmentBrandEntityV1](docs/InMarketAudienceSegmentBrandEntityV1.md)
 - [InMarketAudienceSegmentBrandEntityV1ListResponse](docs/InMarketAudienceSegmentBrandEntityV1ListResponse.md)
 - [InMarketAudienceSegmentBrandEntityV1Resource](docs/InMarketAudienceSegmentBrandEntityV1Resource.md)
 - [InMarketAudienceSegmentInterestEntityV1](docs/InMarketAudienceSegmentInterestEntityV1.md)
 - [InMarketAudienceSegmentInterestEntityV1ListResponse](docs/InMarketAudienceSegmentInterestEntityV1ListResponse.md)
 - [InMarketAudienceSegmentInterestEntityV1Resource](docs/InMarketAudienceSegmentInterestEntityV1Resource.md)
 - [InMarketCreateV1](docs/InMarketCreateV1.md)
 - [InMarketSizeEstimationV1](docs/InMarketSizeEstimationV1.md)
 - [InMarketUpdateV1](docs/InMarketUpdateV1.md)
 - [InMarketV1](docs/InMarketV1.md)
 - [Installment](docs/Installment.md)
 - [JsonReportRows](docs/JsonReportRows.md)
 - [JsonReportRowsListResponse](docs/JsonReportRowsListResponse.md)
 - [JsonReportRowsResource](docs/JsonReportRowsResource.md)
 - [ListAvailableIndustriesResponse](docs/ListAvailableIndustriesResponse.md)
 - [LocationCreateV1](docs/LocationCreateV1.md)
 - [LocationSizeEstimationV1](docs/LocationSizeEstimationV1.md)
 - [LocationUpdateV1](docs/LocationUpdateV1.md)
 - [LocationV1](docs/LocationV1.md)
 - [LookalikeCreateV1](docs/LookalikeCreateV1.md)
 - [LookalikeUpdateV1](docs/LookalikeUpdateV1.md)
 - [LookalikeV1](docs/LookalikeV1.md)
 - [LoyaltyPoints](docs/LoyaltyPoints.md)
 - [MarketingSolutionsReportStatus](docs/MarketingSolutionsReportStatus.md)
 - [MarketingSolutionsReportStatusResource](docs/MarketingSolutionsReportStatusResource.md)
 - [MarketingSolutionsReportStatusResponse](docs/MarketingSolutionsReportStatusResponse.md)
 - [ModifyAudienceResponse](docs/ModifyAudienceResponse.md)
 - [NillableAdSetTargetingRuleV24Q3](docs/NillableAdSetTargetingRuleV24Q3.md)
 - [NillableAdSetTargetingRuleV24Q3Value](docs/NillableAdSetTargetingRuleV24Q3Value.md)
 - [NillableDateTime](docs/NillableDateTime.md)
 - [NillableDecimal](docs/NillableDecimal.md)
 - [NillableGenderV1](docs/NillableGenderV1.md)
 - [NillableInt32](docs/NillableInt32.md)
 - [NillableString](docs/NillableString.md)
 - [OciBrandSafetyResponse](docs/OciBrandSafetyResponse.md)
 - [OciBrandSafetyResponseData](docs/OciBrandSafetyResponseData.md)
 - [OciBrandSafetyRule](docs/OciBrandSafetyRule.md)
 - [OciBrandSafetySegment](docs/OciBrandSafetySegment.md)
 - [OciTargetingNode](docs/OciTargetingNode.md)
 - [OciTargetingResponse](docs/OciTargetingResponse.md)
 - [OciTargetingResponseData](docs/OciTargetingResponseData.md)
 - [OciTargetingRule](docs/OciTargetingRule.md)
 - [OnSiteRecoRequest](docs/OnSiteRecoRequest.md)
 - [OnSiteRecoResponse](docs/OnSiteRecoResponse.md)
 - [Outcome](docs/Outcome.md)
 - [PatchAdSetBiddingV24Q3](docs/PatchAdSetBiddingV24Q3.md)
 - [PatchAdSetBudgetV24Q3](docs/PatchAdSetBudgetV24Q3.md)
 - [PatchAdSetCategoryBid](docs/PatchAdSetCategoryBid.md)
 - [PatchAdSetCategoryBidListRequest](docs/PatchAdSetCategoryBidListRequest.md)
 - [PatchAdSetCategoryBidResource](docs/PatchAdSetCategoryBidResource.md)
 - [PatchAdSetCategoryBidResultListResponse](docs/PatchAdSetCategoryBidResultListResponse.md)
 - [PatchAdSetCategoryBidResultResource](docs/PatchAdSetCategoryBidResultResource.md)
 - [PatchAdSetDisplayMultiplier](docs/PatchAdSetDisplayMultiplier.md)
 - [PatchAdSetDisplayMultiplierListRequest](docs/PatchAdSetDisplayMultiplierListRequest.md)
 - [PatchAdSetDisplayMultiplierResource](docs/PatchAdSetDisplayMultiplierResource.md)
 - [PatchAdSetDisplayMultiplierResultListResponse](docs/PatchAdSetDisplayMultiplierResultListResponse.md)
 - [PatchAdSetDisplayMultiplierResultResource](docs/PatchAdSetDisplayMultiplierResultResource.md)
 - [PatchAdSetSchedulingV24Q3](docs/PatchAdSetSchedulingV24Q3.md)
 - [PatchAdSetV24Q3](docs/PatchAdSetV24Q3.md)
 - [PatchCampaign](docs/PatchCampaign.md)
 - [PatchCampaignListRequest](docs/PatchCampaignListRequest.md)
 - [PatchCampaignSpendLimit](docs/PatchCampaignSpendLimit.md)
 - [PatchCampaignWriteResource](docs/PatchCampaignWriteResource.md)
 - [PatchResultCampaignListResponse](docs/PatchResultCampaignListResponse.md)
 - [PatchResultCampaignReadResource](docs/PatchResultCampaignReadResource.md)
 - [PlacementsReportQueryMessage](docs/PlacementsReportQueryMessage.md)
 - [PlacementsReportQueryMessageListRequest](docs/PlacementsReportQueryMessageListRequest.md)
 - [PlacementsReportQueryMessageResource](docs/PlacementsReportQueryMessageResource.md)
 - [PointOfInterestV1](docs/PointOfInterestV1.md)
 - [PortfolioMessage](docs/PortfolioMessage.md)
 - [Price](docs/Price.md)
 - [Product](docs/Product.md)
 - [ProductFilterConfig](docs/ProductFilterConfig.md)
 - [ProductImporterError](docs/ProductImporterError.md)
 - [ProductImporterWarning](docs/ProductImporterWarning.md)
 - [ProductSet](docs/ProductSet.md)
 - [ProductSetRule](docs/ProductSetRule.md)
 - [ProductShipping](docs/ProductShipping.md)
 - [ProductShippingDimension](docs/ProductShippingDimension.md)
 - [ProductShippingWeight](docs/ProductShippingWeight.md)
 - [ProductTax](docs/ProductTax.md)
 - [ProductUnitPricingBaseMeasure](docs/ProductUnitPricingBaseMeasure.md)
 - [ProductUnitPricingMeasure](docs/ProductUnitPricingMeasure.md)
 - [ProductsCustomBatchRequest](docs/ProductsCustomBatchRequest.md)
 - [ProductsCustomBatchRequestEntry](docs/ProductsCustomBatchRequestEntry.md)
 - [ProspectingCreateV1](docs/ProspectingCreateV1.md)
 - [ProspectingUpdateV1](docs/ProspectingUpdateV1.md)
 - [ProspectingV1](docs/ProspectingV1.md)
 - [ReadAdSetBiddingV24Q3](docs/ReadAdSetBiddingV24Q3.md)
 - [ReadAdSetBudgetV24Q3](docs/ReadAdSetBudgetV24Q3.md)
 - [ReadAdSetScheduleV24Q3](docs/ReadAdSetScheduleV24Q3.md)
 - [ReadAdSetV24Q3](docs/ReadAdSetV24Q3.md)
 - [ReadModelAdSetId](docs/ReadModelAdSetId.md)
 - [ReadModelAdSetIdV24Q3](docs/ReadModelAdSetIdV24Q3.md)
 - [ReadModelReadAdSetV24Q3](docs/ReadModelReadAdSetV24Q3.md)
 - [RecommendedProduct](docs/RecommendedProduct.md)
 - [ReportDetailError](docs/ReportDetailError.md)
 - [ReportDetailErrors](docs/ReportDetailErrors.md)
 - [ReportDetailWarning](docs/ReportDetailWarning.md)
 - [ReportDetailWarnings](docs/ReportDetailWarnings.md)
 - [ReportOkResponse](docs/ReportOkResponse.md)
 - [RequestsAdSetId](docs/RequestsAdSetId.md)
 - [RequestsPatchAdSetV24Q3](docs/RequestsPatchAdSetV24Q3.md)
 - [ResourceCollectionOutcomeOfProductSet](docs/ResourceCollectionOutcomeOfProductSet.md)
 - [ResourceOfProductSet](docs/ResourceOfProductSet.md)
 - [ResourceOutcomeOfProductSet](docs/ResourceOutcomeOfProductSet.md)
 - [ResponseReadAdSetV24Q3](docs/ResponseReadAdSetV24Q3.md)
 - [ResponsesAdSetId](docs/ResponsesAdSetId.md)
 - [ResponsesAdSetIdV24Q3](docs/ResponsesAdSetIdV24Q3.md)
 - [ResponsesReadAdSetV24Q3](docs/ResponsesReadAdSetV24Q3.md)
 - [RetargetingCreateV1](docs/RetargetingCreateV1.md)
 - [RetargetingUpdateV1](docs/RetargetingUpdateV1.md)
 - [RetargetingV1](docs/RetargetingV1.md)
 - [SetAdSetTargetingDealIds](docs/SetAdSetTargetingDealIds.md)
 - [SetAdSetTargetingDealIdsRequest](docs/SetAdSetTargetingDealIdsRequest.md)
 - [SetAdSetTargetingDealIdsResource](docs/SetAdSetTargetingDealIdsResource.md)
 - [SetAdSetTargetingVideoPositioning](docs/SetAdSetTargetingVideoPositioning.md)
 - [SetAdSetTargetingVideoPositioningRequest](docs/SetAdSetTargetingVideoPositioningRequest.md)
 - [SetAdSetTargetingVideoPositioningResource](docs/SetAdSetTargetingVideoPositioningResource.md)
 - [Size](docs/Size.md)
 - [StatisticsOkResponse](docs/StatisticsOkResponse.md)
 - [StatisticsRecord](docs/StatisticsRecord.md)
 - [StatisticsRecordList](docs/StatisticsRecordList.md)
 - [StatisticsReportQueryMessage](docs/StatisticsReportQueryMessage.md)
 - [SupplyVendor](docs/SupplyVendor.md)
 - [SupplyVendorListResponse](docs/SupplyVendorListResponse.md)
 - [SupplyVendorResource](docs/SupplyVendorResource.md)
 - [Tag](docs/Tag.md)
 - [Target](docs/Target.md)
 - [TargetType](docs/TargetType.md)
 - [TargetingEntity](docs/TargetingEntity.md)
 - [TargetingErrorModel](docs/TargetingErrorModel.md)
 - [TargetingOperator](docs/TargetingOperator.md)
 - [TransactionsReportQueryMessage](docs/TransactionsReportQueryMessage.md)
 - [TransactionsReportQueryMessageListRequest](docs/TransactionsReportQueryMessageListRequest.md)
 - [TransactionsReportQueryMessageResource](docs/TransactionsReportQueryMessageResource.md)
 - [TransparencyQueryMessage](docs/TransparencyQueryMessage.md)
 - [TransparencyReport](docs/TransparencyReport.md)
 - [TransparencyReportFile](docs/TransparencyReportFile.md)
 - [TransparencyReportListResponse](docs/TransparencyReportListResponse.md)
 - [TransparencyReportResource](docs/TransparencyReportResource.md)
 - [UnauthorizedResponseV2](docs/UnauthorizedResponseV2.md)
 - [UpdateCoupon](docs/UpdateCoupon.md)
 - [UpdateCouponRequest](docs/UpdateCouponRequest.md)
 - [UpdateCouponResource](docs/UpdateCouponResource.md)
 - [UserDef](docs/UserDef.md)
 - [ValueResourceCollectionOutcomeOfProductFilterConfig](docs/ValueResourceCollectionOutcomeOfProductFilterConfig.md)
 - [ValueResourceInputOfCreateProductFilterRequest](docs/ValueResourceInputOfCreateProductFilterRequest.md)
 - [ValueResourceInputOfCreateProductSetRequest](docs/ValueResourceInputOfCreateProductSetRequest.md)
 - [ValueResourceOfAdvertiserCreationInput](docs/ValueResourceOfAdvertiserCreationInput.md)
 - [ValueResourceOfCreateProductFilterRequest](docs/ValueResourceOfCreateProductFilterRequest.md)
 - [ValueResourceOfCreateProductSetRequest](docs/ValueResourceOfCreateProductSetRequest.md)
 - [ValueResourceOfProductFilterConfig](docs/ValueResourceOfProductFilterConfig.md)
 - [ValueResourceOutcomeOfProductFilterConfig](docs/ValueResourceOutcomeOfProductFilterConfig.md)
 - [VideoDetail](docs/VideoDetail.md)
 - [WriteModelAdSetId](docs/WriteModelAdSetId.md)
 - [WriteModelPatchAdSetV24Q3](docs/WriteModelPatchAdSetV24Q3.md)


## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.