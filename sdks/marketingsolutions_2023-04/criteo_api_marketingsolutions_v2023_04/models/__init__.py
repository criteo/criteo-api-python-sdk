# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from criteo_api_marketingsolutions_v2023_04.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_marketingsolutions_v2023_04.model.ad_set_category_bid import AdSetCategoryBid
from criteo_api_marketingsolutions_v2023_04.model.ad_set_category_bid_list_response import AdSetCategoryBidListResponse
from criteo_api_marketingsolutions_v2023_04.model.ad_set_category_bid_resource import AdSetCategoryBidResource
from criteo_api_marketingsolutions_v2023_04.model.ad_set_delivery_limitations import AdSetDeliveryLimitations
from criteo_api_marketingsolutions_v2023_04.model.ad_set_display_multiplier import AdSetDisplayMultiplier
from criteo_api_marketingsolutions_v2023_04.model.ad_set_display_multiplier_list_response import AdSetDisplayMultiplierListResponse
from criteo_api_marketingsolutions_v2023_04.model.ad_set_display_multiplier_resource import AdSetDisplayMultiplierResource
from criteo_api_marketingsolutions_v2023_04.model.ad_set_frequency_capping import AdSetFrequencyCapping
from criteo_api_marketingsolutions_v2023_04.model.ad_set_geo_location import AdSetGeoLocation
from criteo_api_marketingsolutions_v2023_04.model.ad_set_search_filter import AdSetSearchFilter
from criteo_api_marketingsolutions_v2023_04.model.ad_set_targeting import AdSetTargeting
from criteo_api_marketingsolutions_v2023_04.model.ad_set_targeting_rule import AdSetTargetingRule
from criteo_api_marketingsolutions_v2023_04.model.application_summary_model import ApplicationSummaryModel
from criteo_api_marketingsolutions_v2023_04.model.application_summary_model_resource import ApplicationSummaryModelResource
from criteo_api_marketingsolutions_v2023_04.model.application_summary_model_response import ApplicationSummaryModelResponse
from criteo_api_marketingsolutions_v2023_04.model.audience import Audience
from criteo_api_marketingsolutions_v2023_04.model.audience_attributes import AudienceAttributes
from criteo_api_marketingsolutions_v2023_04.model.audience_error import AudienceError
from criteo_api_marketingsolutions_v2023_04.model.audience_name_description import AudienceNameDescription
from criteo_api_marketingsolutions_v2023_04.model.audience_warning import AudienceWarning
from criteo_api_marketingsolutions_v2023_04.model.basic_audience_definition import BasicAudienceDefinition
from criteo_api_marketingsolutions_v2023_04.model.campaign import Campaign
from criteo_api_marketingsolutions_v2023_04.model.campaign_list_response import CampaignListResponse
from criteo_api_marketingsolutions_v2023_04.model.campaign_read_resource import CampaignReadResource
from criteo_api_marketingsolutions_v2023_04.model.campaign_response import CampaignResponse
from criteo_api_marketingsolutions_v2023_04.model.campaign_search_filters import CampaignSearchFilters
from criteo_api_marketingsolutions_v2023_04.model.campaign_search_request import CampaignSearchRequest
from criteo_api_marketingsolutions_v2023_04.model.campaign_spend_limit import CampaignSpendLimit
from criteo_api_marketingsolutions_v2023_04.model.common_problem import CommonProblem
from criteo_api_marketingsolutions_v2023_04.model.contactlist_amendment import ContactlistAmendment
from criteo_api_marketingsolutions_v2023_04.model.contactlist_amendment_attributes import ContactlistAmendmentAttributes
from criteo_api_marketingsolutions_v2023_04.model.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_api_marketingsolutions_v2023_04.model.contactlist_operation import ContactlistOperation
from criteo_api_marketingsolutions_v2023_04.model.contactlist_operation_attributes import ContactlistOperationAttributes
from criteo_api_marketingsolutions_v2023_04.model.criteo_api_error import CriteoApiError
from criteo_api_marketingsolutions_v2023_04.model.criteo_api_warning import CriteoApiWarning
from criteo_api_marketingsolutions_v2023_04.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_api_marketingsolutions_v2023_04.model.delete_audience_response import DeleteAudienceResponse
from criteo_api_marketingsolutions_v2023_04.model.entity_of_portfolio_message import EntityOfPortfolioMessage
from criteo_api_marketingsolutions_v2023_04.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2023_04.model.get_audiences_response import GetAudiencesResponse
from criteo_api_marketingsolutions_v2023_04.model.get_portfolio_response import GetPortfolioResponse
from criteo_api_marketingsolutions_v2023_04.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_v2023_04.model.new_audience import NewAudience
from criteo_api_marketingsolutions_v2023_04.model.new_audience_attributes import NewAudienceAttributes
from criteo_api_marketingsolutions_v2023_04.model.new_audience_request import NewAudienceRequest
from criteo_api_marketingsolutions_v2023_04.model.new_audience_response import NewAudienceResponse
from criteo_api_marketingsolutions_v2023_04.model.nillable_ad_set_targeting_rule import NillableAdSetTargetingRule
from criteo_api_marketingsolutions_v2023_04.model.nillable_ad_set_targeting_rule_value import NillableAdSetTargetingRuleValue
from criteo_api_marketingsolutions_v2023_04.model.nillable_date_time import NillableDateTime
from criteo_api_marketingsolutions_v2023_04.model.nillable_decimal import NillableDecimal
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set import PatchAdSet
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_bidding import PatchAdSetBidding
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_budget import PatchAdSetBudget
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_category_bid import PatchAdSetCategoryBid
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_category_bid_list_request import PatchAdSetCategoryBidListRequest
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_category_bid_resource import PatchAdSetCategoryBidResource
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_category_bid_result_list_response import PatchAdSetCategoryBidResultListResponse
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_category_bid_result_resource import PatchAdSetCategoryBidResultResource
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_display_multiplier import PatchAdSetDisplayMultiplier
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_display_multiplier_list_request import PatchAdSetDisplayMultiplierListRequest
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_display_multiplier_resource import PatchAdSetDisplayMultiplierResource
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_display_multiplier_result_list_response import PatchAdSetDisplayMultiplierResultListResponse
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_display_multiplier_result_resource import PatchAdSetDisplayMultiplierResultResource
from criteo_api_marketingsolutions_v2023_04.model.patch_ad_set_scheduling import PatchAdSetScheduling
from criteo_api_marketingsolutions_v2023_04.model.patch_campaign import PatchCampaign
from criteo_api_marketingsolutions_v2023_04.model.patch_campaign_list_request import PatchCampaignListRequest
from criteo_api_marketingsolutions_v2023_04.model.patch_campaign_spend_limit import PatchCampaignSpendLimit
from criteo_api_marketingsolutions_v2023_04.model.patch_campaign_write_resource import PatchCampaignWriteResource
from criteo_api_marketingsolutions_v2023_04.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from criteo_api_marketingsolutions_v2023_04.model.patch_result_campaign_read_resource import PatchResultCampaignReadResource
from criteo_api_marketingsolutions_v2023_04.model.placements_report_query_data_message import PlacementsReportQueryDataMessage
from criteo_api_marketingsolutions_v2023_04.model.placements_report_query_entity_message import PlacementsReportQueryEntityMessage
from criteo_api_marketingsolutions_v2023_04.model.placements_report_query_message import PlacementsReportQueryMessage
from criteo_api_marketingsolutions_v2023_04.model.portfolio_message import PortfolioMessage
from criteo_api_marketingsolutions_v2023_04.model.problem_details import ProblemDetails
from criteo_api_marketingsolutions_v2023_04.model.problems_details import ProblemsDetails
from criteo_api_marketingsolutions_v2023_04.model.read_ad_set import ReadAdSet
from criteo_api_marketingsolutions_v2023_04.model.read_ad_set_bidding import ReadAdSetBidding
from criteo_api_marketingsolutions_v2023_04.model.read_ad_set_budget import ReadAdSetBudget
from criteo_api_marketingsolutions_v2023_04.model.read_ad_set_schedule import ReadAdSetSchedule
from criteo_api_marketingsolutions_v2023_04.model.read_model_ad_set_id import ReadModelAdSetId
from criteo_api_marketingsolutions_v2023_04.model.read_model_read_ad_set import ReadModelReadAdSet
from criteo_api_marketingsolutions_v2023_04.model.replace_audience import ReplaceAudience
from criteo_api_marketingsolutions_v2023_04.model.replace_audience_request import ReplaceAudienceRequest
from criteo_api_marketingsolutions_v2023_04.model.replace_audience_response import ReplaceAudienceResponse
from criteo_api_marketingsolutions_v2023_04.model.request_ad_set_search import RequestAdSetSearch
from criteo_api_marketingsolutions_v2023_04.model.requests_ad_set_id import RequestsAdSetId
from criteo_api_marketingsolutions_v2023_04.model.requests_patch_ad_set import RequestsPatchAdSet
from criteo_api_marketingsolutions_v2023_04.model.response_ad_set_id import ResponseAdSetId
from criteo_api_marketingsolutions_v2023_04.model.response_read_ad_set import ResponseReadAdSet
from criteo_api_marketingsolutions_v2023_04.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2023_04.model.responses_read_ad_set import ResponsesReadAdSet
from criteo_api_marketingsolutions_v2023_04.model.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_api_marketingsolutions_v2023_04.model.transactions_report_query_data_message import TransactionsReportQueryDataMessage
from criteo_api_marketingsolutions_v2023_04.model.transactions_report_query_entity_message import TransactionsReportQueryEntityMessage
from criteo_api_marketingsolutions_v2023_04.model.transactions_report_query_message import TransactionsReportQueryMessage
from criteo_api_marketingsolutions_v2023_04.model.transparency_query_message import TransparencyQueryMessage
from criteo_api_marketingsolutions_v2023_04.model.transparency_report_attributes import TransparencyReportAttributes
from criteo_api_marketingsolutions_v2023_04.model.transparency_report_data_message import TransparencyReportDataMessage
from criteo_api_marketingsolutions_v2023_04.model.transparency_report_entity_message import TransparencyReportEntityMessage
from criteo_api_marketingsolutions_v2023_04.model.transparency_report_file import TransparencyReportFile
from criteo_api_marketingsolutions_v2023_04.model.write_model_ad_set_id import WriteModelAdSetId
from criteo_api_marketingsolutions_v2023_04.model.write_model_patch_ad_set import WriteModelPatchAdSet