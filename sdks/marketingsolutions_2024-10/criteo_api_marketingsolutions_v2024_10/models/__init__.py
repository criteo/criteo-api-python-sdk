# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from criteo_api_marketingsolutions_v2024_10.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_marketingsolutions_v2024_10.model.ad import Ad
from criteo_api_marketingsolutions_v2024_10.model.ad_set_audience_link_entity_v1 import AdSetAudienceLinkEntityV1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_audience_link_entity_v1_resource import AdSetAudienceLinkEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.ad_set_audience_link_entity_v1_response import AdSetAudienceLinkEntityV1Response
from criteo_api_marketingsolutions_v2024_10.model.ad_set_audience_link_input_entity_v1 import AdSetAudienceLinkInputEntityV1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_category_bid import AdSetCategoryBid
from criteo_api_marketingsolutions_v2024_10.model.ad_set_category_bid_list_response import AdSetCategoryBidListResponse
from criteo_api_marketingsolutions_v2024_10.model.ad_set_category_bid_resource import AdSetCategoryBidResource
from criteo_api_marketingsolutions_v2024_10.model.ad_set_delivery_limitations_v24_q1 import AdSetDeliveryLimitationsV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_display_multiplier import AdSetDisplayMultiplier
from criteo_api_marketingsolutions_v2024_10.model.ad_set_display_multiplier_list_response import AdSetDisplayMultiplierListResponse
from criteo_api_marketingsolutions_v2024_10.model.ad_set_display_multiplier_resource import AdSetDisplayMultiplierResource
from criteo_api_marketingsolutions_v2024_10.model.ad_set_frequency_capping_v24_q1 import AdSetFrequencyCappingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_geo_location_v24_q1 import AdSetGeoLocationV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_search_filter_v24_q1 import AdSetSearchFilterV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_search_request_v24_q1 import AdSetSearchRequestV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_targeting_rule_v24_q1 import AdSetTargetingRuleV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_set_targeting_v24_q1 import AdSetTargetingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.ad_write import AdWrite
from criteo_api_marketingsolutions_v2024_10.model.adaptive_attributes import AdaptiveAttributes
from criteo_api_marketingsolutions_v2024_10.model.adaptive_colors import AdaptiveColors
from criteo_api_marketingsolutions_v2024_10.model.adaptive_write_attributes import AdaptiveWriteAttributes
from criteo_api_marketingsolutions_v2024_10.model.algebra_node_v1 import AlgebraNodeV1
from criteo_api_marketingsolutions_v2024_10.model.application_summary_model import ApplicationSummaryModel
from criteo_api_marketingsolutions_v2024_10.model.application_summary_model_resource import ApplicationSummaryModelResource
from criteo_api_marketingsolutions_v2024_10.model.application_summary_model_response import ApplicationSummaryModelResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_bulk_create_input_v1 import AudienceBulkCreateInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_bulk_delete_input_v1 import AudienceBulkDeleteInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_bulk_update_input_v1 import AudienceBulkUpdateInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_compute_size_entity_v1_resource import AudienceComputeSizeEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_compute_sizes_input_v1 import AudienceComputeSizesInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_create_entity_v1 import AudienceCreateEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_create_entity_v1_resource import AudienceCreateEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_delete_entity_v1_resource import AudienceDeleteEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_entity_v1 import AudienceEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_entity_v1_audience_search_metadata_v1_list_response import AudienceEntityV1AudienceSearchMetadataV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_entity_v1_list_response import AudienceEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_entity_v1_resource import AudienceEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_error import AudienceError
from criteo_api_marketingsolutions_v2024_10.model.audience_estimate_size_entity_v1 import AudienceEstimateSizeEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_estimate_size_entity_v1_resource import AudienceEstimateSizeEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_estimate_size_input_v1 import AudienceEstimateSizeInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_id_entity_v1_list_response import AudienceIdEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_id_entity_v1_resource import AudienceIdEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_name_description import AudienceNameDescription
from criteo_api_marketingsolutions_v2024_10.model.audience_search_entity_v1 import AudienceSearchEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_search_entity_v1_resource import AudienceSearchEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_search_input_v1 import AudienceSearchInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_search_metadata_v1 import AudienceSearchMetadataV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_bulk_create_input_v1 import AudienceSegmentBulkCreateInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_bulk_delete_input_v1 import AudienceSegmentBulkDeleteInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_bulk_update_input_v1 import AudienceSegmentBulkUpdateInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_compute_size_entity_v1_resource import AudienceSegmentComputeSizeEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_compute_sizes_input_v1 import AudienceSegmentComputeSizesInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_create_entity_v1 import AudienceSegmentCreateEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_create_entity_v1_resource import AudienceSegmentCreateEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_delete_entity_v1_resource import AudienceSegmentDeleteEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_entity_v1 import AudienceSegmentEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_entity_v1_audience_segment_search_metadata_v1_list_response import AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_entity_v1_list_response import AudienceSegmentEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_entity_v1_resource import AudienceSegmentEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_estimate_size_input_v1 import AudienceSegmentEstimateSizeInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_id_entity_v1_list_response import AudienceSegmentIdEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_id_entity_v1_resource import AudienceSegmentIdEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_search_entity_v1 import AudienceSegmentSearchEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_search_entity_v1_resource import AudienceSegmentSearchEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_search_input_v1 import AudienceSegmentSearchInputV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_search_metadata_v1 import AudienceSegmentSearchMetadataV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_entity_v1 import AudienceSegmentSizeEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_entity_v1_list_response import AudienceSegmentSizeEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_entity_v1_resource import AudienceSegmentSizeEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_estimation_entity_v1 import AudienceSegmentSizeEstimationEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_estimation_entity_v1_resource import AudienceSegmentSizeEstimationEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_estimation_v1 import AudienceSegmentSizeEstimationV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_estimation_v1_resource import AudienceSegmentSizeEstimationV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_size_estimation_v1_response import AudienceSegmentSizeEstimationV1Response
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_update_entity_v1 import AudienceSegmentUpdateEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_segment_update_entity_v1_resource import AudienceSegmentUpdateEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_size_entity_v1 import AudienceSizeEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_size_entity_v1_list_response import AudienceSizeEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.audience_size_entity_v1_resource import AudienceSizeEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_size_estimation_v1 import AudienceSizeEstimationV1
from criteo_api_marketingsolutions_v2024_10.model.audience_size_estimation_v1_resource import AudienceSizeEstimationV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_size_estimation_v1_response import AudienceSizeEstimationV1Response
from criteo_api_marketingsolutions_v2024_10.model.audience_update_entity_v1 import AudienceUpdateEntityV1
from criteo_api_marketingsolutions_v2024_10.model.audience_update_entity_v1_resource import AudienceUpdateEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.audience_warning import AudienceWarning
from criteo_api_marketingsolutions_v2024_10.model.automated_budget_configuration import AutomatedBudgetConfiguration
from criteo_api_marketingsolutions_v2024_10.model.automated_budget_configuration_v23_q1 import AutomatedBudgetConfigurationV23Q1
from criteo_api_marketingsolutions_v2024_10.model.basic_audience_definition import BasicAudienceDefinition
from criteo_api_marketingsolutions_v2024_10.model.behavioral_v1 import BehavioralV1
from criteo_api_marketingsolutions_v2024_10.model.budget_automation import BudgetAutomation
from criteo_api_marketingsolutions_v2024_10.model.budget_automation_configuration import BudgetAutomationConfiguration
from criteo_api_marketingsolutions_v2024_10.model.campaign_budget_automation_v23_q1 import CampaignBudgetAutomationV23Q1
from criteo_api_marketingsolutions_v2024_10.model.campaign_search_filters_v23_q1 import CampaignSearchFiltersV23Q1
from criteo_api_marketingsolutions_v2024_10.model.campaign_search_request_v23_q1 import CampaignSearchRequestV23Q1
from criteo_api_marketingsolutions_v2024_10.model.campaign_spend_limit_v23_q1 import CampaignSpendLimitV23Q1
from criteo_api_marketingsolutions_v2024_10.model.campaign_v23_q1 import CampaignV23Q1
from criteo_api_marketingsolutions_v2024_10.model.campaign_v23_q1_list_response import CampaignV23Q1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.campaign_v23_q1_resource import CampaignV23Q1Resource
from criteo_api_marketingsolutions_v2024_10.model.campaign_v23_q1_response import CampaignV23Q1Response
from criteo_api_marketingsolutions_v2024_10.model.common_problem import CommonProblem
from criteo_api_marketingsolutions_v2024_10.model.contact_list_statistics_entity_v1 import ContactListStatisticsEntityV1
from criteo_api_marketingsolutions_v2024_10.model.contact_list_statistics_entity_v1_resource import ContactListStatisticsEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.contact_list_statistics_entity_v1_response import ContactListStatisticsEntityV1Response
from criteo_api_marketingsolutions_v2024_10.model.contact_list_v1 import ContactListV1
from criteo_api_marketingsolutions_v2024_10.model.contactlist_amendment import ContactlistAmendment
from criteo_api_marketingsolutions_v2024_10.model.contactlist_amendment_attributes import ContactlistAmendmentAttributes
from criteo_api_marketingsolutions_v2024_10.model.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_api_marketingsolutions_v2024_10.model.contactlist_operation import ContactlistOperation
from criteo_api_marketingsolutions_v2024_10.model.contactlist_operation_attributes import ContactlistOperationAttributes
from criteo_api_marketingsolutions_v2024_10.model.coupon import Coupon
from criteo_api_marketingsolutions_v2024_10.model.coupon_supported_sizes import CouponSupportedSizes
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_bidding_v24_q1 import CreateAdSetBiddingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_budget_v24_q1 import CreateAdSetBudgetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_geo_location_v24_q1 import CreateAdSetGeoLocationV24Q1
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_schedule_v24_q1 import CreateAdSetScheduleV24Q1
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_targeting_v24_q1 import CreateAdSetTargetingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_v24_q1 import CreateAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_v24_q1_request import CreateAdSetV24Q1Request
from criteo_api_marketingsolutions_v2024_10.model.create_ad_set_v24_q1_resource import CreateAdSetV24Q1Resource
from criteo_api_marketingsolutions_v2024_10.model.create_campaign import CreateCampaign
from criteo_api_marketingsolutions_v2024_10.model.create_campaign_request import CreateCampaignRequest
from criteo_api_marketingsolutions_v2024_10.model.create_campaign_resource import CreateCampaignResource
from criteo_api_marketingsolutions_v2024_10.model.create_campaign_spend_limit import CreateCampaignSpendLimit
from criteo_api_marketingsolutions_v2024_10.model.create_coupon import CreateCoupon
from criteo_api_marketingsolutions_v2024_10.model.create_image_slide import CreateImageSlide
from criteo_api_marketingsolutions_v2024_10.model.creative import Creative
from criteo_api_marketingsolutions_v2024_10.model.creative_write import CreativeWrite
from criteo_api_marketingsolutions_v2024_10.model.criteo_api_error import CriteoApiError
from criteo_api_marketingsolutions_v2024_10.model.criteo_api_warning import CriteoApiWarning
from criteo_api_marketingsolutions_v2024_10.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_api_marketingsolutions_v2024_10.model.dynamic_attributes import DynamicAttributes
from criteo_api_marketingsolutions_v2024_10.model.dynamic_write_attributes import DynamicWriteAttributes
from criteo_api_marketingsolutions_v2024_10.model.entity_of_portfolio_message import EntityOfPortfolioMessage
from criteo_api_marketingsolutions_v2024_10.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2024_10.model.get_portfolio_response import GetPortfolioResponse
from criteo_api_marketingsolutions_v2024_10.model.html_tag_attributes import HtmlTagAttributes
from criteo_api_marketingsolutions_v2024_10.model.html_tag_write_attributes import HtmlTagWriteAttributes
from criteo_api_marketingsolutions_v2024_10.model.image_attributes import ImageAttributes
from criteo_api_marketingsolutions_v2024_10.model.image_set import ImageSet
from criteo_api_marketingsolutions_v2024_10.model.image_set_base64 import ImageSetBase64
from criteo_api_marketingsolutions_v2024_10.model.image_shape import ImageShape
from criteo_api_marketingsolutions_v2024_10.model.image_slide import ImageSlide
from criteo_api_marketingsolutions_v2024_10.model.image_write_attributes import ImageWriteAttributes
from criteo_api_marketingsolutions_v2024_10.model.in_market_audience_segment_brand_entity_v1 import InMarketAudienceSegmentBrandEntityV1
from criteo_api_marketingsolutions_v2024_10.model.in_market_audience_segment_brand_entity_v1_list_response import InMarketAudienceSegmentBrandEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.in_market_audience_segment_brand_entity_v1_resource import InMarketAudienceSegmentBrandEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.in_market_audience_segment_interest_entity_v1 import InMarketAudienceSegmentInterestEntityV1
from criteo_api_marketingsolutions_v2024_10.model.in_market_audience_segment_interest_entity_v1_list_response import InMarketAudienceSegmentInterestEntityV1ListResponse
from criteo_api_marketingsolutions_v2024_10.model.in_market_audience_segment_interest_entity_v1_resource import InMarketAudienceSegmentInterestEntityV1Resource
from criteo_api_marketingsolutions_v2024_10.model.in_market_create_v1 import InMarketCreateV1
from criteo_api_marketingsolutions_v2024_10.model.in_market_size_estimation_v1 import InMarketSizeEstimationV1
from criteo_api_marketingsolutions_v2024_10.model.in_market_update_v1 import InMarketUpdateV1
from criteo_api_marketingsolutions_v2024_10.model.in_market_v1 import InMarketV1
from criteo_api_marketingsolutions_v2024_10.model.location_create_v1 import LocationCreateV1
from criteo_api_marketingsolutions_v2024_10.model.location_size_estimation_v1 import LocationSizeEstimationV1
from criteo_api_marketingsolutions_v2024_10.model.location_update_v1 import LocationUpdateV1
from criteo_api_marketingsolutions_v2024_10.model.location_v1 import LocationV1
from criteo_api_marketingsolutions_v2024_10.model.lookalike_create_v1 import LookalikeCreateV1
from criteo_api_marketingsolutions_v2024_10.model.lookalike_update_v1 import LookalikeUpdateV1
from criteo_api_marketingsolutions_v2024_10.model.lookalike_v1 import LookalikeV1
from criteo_api_marketingsolutions_v2024_10.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_v2024_10.model.nillable_ad_set_targeting_rule_v24_q1 import NillableAdSetTargetingRuleV24Q1
from criteo_api_marketingsolutions_v2024_10.model.nillable_ad_set_targeting_rule_v24_q1_value import NillableAdSetTargetingRuleV24Q1Value
from criteo_api_marketingsolutions_v2024_10.model.nillable_date_time import NillableDateTime
from criteo_api_marketingsolutions_v2024_10.model.nillable_decimal import NillableDecimal
from criteo_api_marketingsolutions_v2024_10.model.nillable_gender_v1 import NillableGenderV1
from criteo_api_marketingsolutions_v2024_10.model.nillable_int32 import NillableInt32
from criteo_api_marketingsolutions_v2024_10.model.nillable_string import NillableString
from criteo_api_marketingsolutions_v2024_10.model.outcome import Outcome
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_bidding_v24_q1 import PatchAdSetBiddingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_budget_v24_q1 import PatchAdSetBudgetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_category_bid import PatchAdSetCategoryBid
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_category_bid_list_request import PatchAdSetCategoryBidListRequest
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_category_bid_resource import PatchAdSetCategoryBidResource
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_category_bid_result_list_response import PatchAdSetCategoryBidResultListResponse
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_category_bid_result_resource import PatchAdSetCategoryBidResultResource
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_display_multiplier import PatchAdSetDisplayMultiplier
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_display_multiplier_list_request import PatchAdSetDisplayMultiplierListRequest
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_display_multiplier_resource import PatchAdSetDisplayMultiplierResource
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_display_multiplier_result_list_response import PatchAdSetDisplayMultiplierResultListResponse
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_display_multiplier_result_resource import PatchAdSetDisplayMultiplierResultResource
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_scheduling_v24_q1 import PatchAdSetSchedulingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.patch_ad_set_v24_q1 import PatchAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.patch_campaign import PatchCampaign
from criteo_api_marketingsolutions_v2024_10.model.patch_campaign_list_request import PatchCampaignListRequest
from criteo_api_marketingsolutions_v2024_10.model.patch_campaign_spend_limit import PatchCampaignSpendLimit
from criteo_api_marketingsolutions_v2024_10.model.patch_campaign_write_resource import PatchCampaignWriteResource
from criteo_api_marketingsolutions_v2024_10.model.patch_marketing_campaign_budget_automation import PatchMarketingCampaignBudgetAutomation
from criteo_api_marketingsolutions_v2024_10.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from criteo_api_marketingsolutions_v2024_10.model.patch_result_campaign_read_resource import PatchResultCampaignReadResource
from criteo_api_marketingsolutions_v2024_10.model.placements_report_query_message import PlacementsReportQueryMessage
from criteo_api_marketingsolutions_v2024_10.model.placements_report_query_message_list_request import PlacementsReportQueryMessageListRequest
from criteo_api_marketingsolutions_v2024_10.model.placements_report_query_message_resource import PlacementsReportQueryMessageResource
from criteo_api_marketingsolutions_v2024_10.model.point_of_interest_v1 import PointOfInterestV1
from criteo_api_marketingsolutions_v2024_10.model.portfolio_message import PortfolioMessage
from criteo_api_marketingsolutions_v2024_10.model.prospecting_create_v1 import ProspectingCreateV1
from criteo_api_marketingsolutions_v2024_10.model.prospecting_update_v1 import ProspectingUpdateV1
from criteo_api_marketingsolutions_v2024_10.model.prospecting_v1 import ProspectingV1
from criteo_api_marketingsolutions_v2024_10.model.read_ad_set_bidding_v24_q1 import ReadAdSetBiddingV24Q1
from criteo_api_marketingsolutions_v2024_10.model.read_ad_set_budget_v24_q1 import ReadAdSetBudgetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.read_ad_set_schedule_v24_q1 import ReadAdSetScheduleV24Q1
from criteo_api_marketingsolutions_v2024_10.model.read_ad_set_v24_q1 import ReadAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.read_model_ad_set_id import ReadModelAdSetId
from criteo_api_marketingsolutions_v2024_10.model.read_model_ad_set_id_v24_q1 import ReadModelAdSetIdV24Q1
from criteo_api_marketingsolutions_v2024_10.model.read_model_read_ad_set_v24_q1 import ReadModelReadAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.requests_ad_set_id import RequestsAdSetId
from criteo_api_marketingsolutions_v2024_10.model.requests_patch_ad_set_v24_q1 import RequestsPatchAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.resource_collection_outcome_of_ad import ResourceCollectionOutcomeOfAd
from criteo_api_marketingsolutions_v2024_10.model.resource_collection_outcome_of_coupon import ResourceCollectionOutcomeOfCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_collection_outcome_of_creative import ResourceCollectionOutcomeOfCreative
from criteo_api_marketingsolutions_v2024_10.model.resource_input_of_ad_write import ResourceInputOfAdWrite
from criteo_api_marketingsolutions_v2024_10.model.resource_input_of_create_coupon import ResourceInputOfCreateCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_input_of_creative_write import ResourceInputOfCreativeWrite
from criteo_api_marketingsolutions_v2024_10.model.resource_input_of_update_coupon import ResourceInputOfUpdateCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_of_ad import ResourceOfAd
from criteo_api_marketingsolutions_v2024_10.model.resource_of_ad_write import ResourceOfAdWrite
from criteo_api_marketingsolutions_v2024_10.model.resource_of_coupon import ResourceOfCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_of_coupon_supported_sizes import ResourceOfCouponSupportedSizes
from criteo_api_marketingsolutions_v2024_10.model.resource_of_create_coupon import ResourceOfCreateCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_of_creative import ResourceOfCreative
from criteo_api_marketingsolutions_v2024_10.model.resource_of_creative_write import ResourceOfCreativeWrite
from criteo_api_marketingsolutions_v2024_10.model.resource_of_update_coupon import ResourceOfUpdateCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_outcome_of_ad import ResourceOutcomeOfAd
from criteo_api_marketingsolutions_v2024_10.model.resource_outcome_of_coupon import ResourceOutcomeOfCoupon
from criteo_api_marketingsolutions_v2024_10.model.resource_outcome_of_coupon_supported_sizes import ResourceOutcomeOfCouponSupportedSizes
from criteo_api_marketingsolutions_v2024_10.model.resource_outcome_of_creative import ResourceOutcomeOfCreative
from criteo_api_marketingsolutions_v2024_10.model.response_read_ad_set_v24_q1 import ResponseReadAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2024_10.model.responses_ad_set_id_v24_q1 import ResponsesAdSetIdV24Q1
from criteo_api_marketingsolutions_v2024_10.model.responses_read_ad_set_v24_q1 import ResponsesReadAdSetV24Q1
from criteo_api_marketingsolutions_v2024_10.model.retargeting_create_v1 import RetargetingCreateV1
from criteo_api_marketingsolutions_v2024_10.model.retargeting_update_v1 import RetargetingUpdateV1
from criteo_api_marketingsolutions_v2024_10.model.retargeting_v1 import RetargetingV1
from criteo_api_marketingsolutions_v2024_10.model.size import Size
from criteo_api_marketingsolutions_v2024_10.model.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_api_marketingsolutions_v2024_10.model.tag import Tag
from criteo_api_marketingsolutions_v2024_10.model.transactions_report_query_message import TransactionsReportQueryMessage
from criteo_api_marketingsolutions_v2024_10.model.transactions_report_query_message_list_request import TransactionsReportQueryMessageListRequest
from criteo_api_marketingsolutions_v2024_10.model.transactions_report_query_message_resource import TransactionsReportQueryMessageResource
from criteo_api_marketingsolutions_v2024_10.model.transparency_query_message import TransparencyQueryMessage
from criteo_api_marketingsolutions_v2024_10.model.transparency_report import TransparencyReport
from criteo_api_marketingsolutions_v2024_10.model.transparency_report_file import TransparencyReportFile
from criteo_api_marketingsolutions_v2024_10.model.transparency_report_list_response import TransparencyReportListResponse
from criteo_api_marketingsolutions_v2024_10.model.transparency_report_resource import TransparencyReportResource
from criteo_api_marketingsolutions_v2024_10.model.update_coupon import UpdateCoupon
from criteo_api_marketingsolutions_v2024_10.model.video_detail import VideoDetail
from criteo_api_marketingsolutions_v2024_10.model.write_model_ad_set_id import WriteModelAdSetId
from criteo_api_marketingsolutions_v2024_10.model.write_model_patch_ad_set_v24_q1 import WriteModelPatchAdSetV24Q1
