# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from criteo_api_retailmedia_v2023_10.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_retailmedia_v2023_10.model.add_funds_to_balance_request import AddFundsToBalanceRequest
from criteo_api_retailmedia_v2023_10.model.add_to_basket_ids_update_model202110_request import AddToBasketIdsUpdateModel202110Request
from criteo_api_retailmedia_v2023_10.model.add_to_basket_target202110_request import AddToBasketTarget202110Request
from criteo_api_retailmedia_v2023_10.model.add_to_basket_target202110_response import AddToBasketTarget202110Response
from criteo_api_retailmedia_v2023_10.model.application_summary_model import ApplicationSummaryModel
from criteo_api_retailmedia_v2023_10.model.application_summary_model_resource import ApplicationSummaryModelResource
from criteo_api_retailmedia_v2023_10.model.application_summary_model_response import ApplicationSummaryModelResponse
from criteo_api_retailmedia_v2023_10.model.asset import Asset
from criteo_api_retailmedia_v2023_10.model.asset_resource import AssetResource
from criteo_api_retailmedia_v2023_10.model.asset_response import AssetResponse
from criteo_api_retailmedia_v2023_10.model.async_campaigns_report import AsyncCampaignsReport
from criteo_api_retailmedia_v2023_10.model.async_campaigns_report_request import AsyncCampaignsReportRequest
from criteo_api_retailmedia_v2023_10.model.async_campaigns_report_resource import AsyncCampaignsReportResource
from criteo_api_retailmedia_v2023_10.model.async_line_items_report import AsyncLineItemsReport
from criteo_api_retailmedia_v2023_10.model.async_line_items_report_request import AsyncLineItemsReportRequest
from criteo_api_retailmedia_v2023_10.model.async_line_items_report_resource import AsyncLineItemsReportResource
from criteo_api_retailmedia_v2023_10.model.async_report_response import AsyncReportResponse
from criteo_api_retailmedia_v2023_10.model.async_revenue_report import AsyncRevenueReport
from criteo_api_retailmedia_v2023_10.model.async_revenue_report_request import AsyncRevenueReportRequest
from criteo_api_retailmedia_v2023_10.model.async_revenue_report_resource import AsyncRevenueReportResource
from criteo_api_retailmedia_v2023_10.model.auction_line_item_create_model_request import AuctionLineItemCreateModelRequest
from criteo_api_retailmedia_v2023_10.model.auction_line_item_paged_list_response import AuctionLineItemPagedListResponse
from criteo_api_retailmedia_v2023_10.model.auction_line_item_response import AuctionLineItemResponse
from criteo_api_retailmedia_v2023_10.model.auction_line_item_update_model_request import AuctionLineItemUpdateModelRequest
from criteo_api_retailmedia_v2023_10.model.audience_ids_update_model202110_request import AudienceIdsUpdateModel202110Request
from criteo_api_retailmedia_v2023_10.model.audience_target202110_request import AudienceTarget202110Request
from criteo_api_retailmedia_v2023_10.model.audience_target202110_response import AudienceTarget202110Response
from criteo_api_retailmedia_v2023_10.model.balance202110_paged_list_response import Balance202110PagedListResponse
from criteo_api_retailmedia_v2023_10.model.balance_campaign202110_list_request import BalanceCampaign202110ListRequest
from criteo_api_retailmedia_v2023_10.model.balance_campaign202110_paged_list_response import BalanceCampaign202110PagedListResponse
from criteo_api_retailmedia_v2023_10.model.balance_response import BalanceResponse
from criteo_api_retailmedia_v2023_10.model.balance_response_paged_list_response import BalanceResponsePagedListResponse
from criteo_api_retailmedia_v2023_10.model.campaign_attributes_v202301 import CampaignAttributesV202301
from criteo_api_retailmedia_v2023_10.model.campaign_v202301 import CampaignV202301
from criteo_api_retailmedia_v2023_10.model.category202204 import Category202204
from criteo_api_retailmedia_v2023_10.model.category202204_list_response import Category202204ListResponse
from criteo_api_retailmedia_v2023_10.model.change_dates_of_balance_request import ChangeDatesOfBalanceRequest
from criteo_api_retailmedia_v2023_10.model.choice_option import ChoiceOption
from criteo_api_retailmedia_v2023_10.model.choice_variable_specification import ChoiceVariableSpecification
from criteo_api_retailmedia_v2023_10.model.choice_variable_value import ChoiceVariableValue
from criteo_api_retailmedia_v2023_10.model.color_variable_value import ColorVariableValue
from criteo_api_retailmedia_v2023_10.model.common_error import CommonError
from criteo_api_retailmedia_v2023_10.model.common_line_item_paged_list_response import CommonLineItemPagedListResponse
from criteo_api_retailmedia_v2023_10.model.common_line_item_response import CommonLineItemResponse
from criteo_api_retailmedia_v2023_10.model.common_problem import CommonProblem
from criteo_api_retailmedia_v2023_10.model.common_status_code_response import CommonStatusCodeResponse
from criteo_api_retailmedia_v2023_10.model.common_warning import CommonWarning
from criteo_api_retailmedia_v2023_10.model.create_balance_request import CreateBalanceRequest
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience import CreateRetailMediaAudience
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_attributes import CreateRetailMediaAudienceAttributes
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_body import CreateRetailMediaAudienceBody
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_request import CreateRetailMediaAudienceRequest
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_response import CreateRetailMediaAudienceResponse
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_v2 import CreateRetailMediaAudienceV2
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_v2_attributes import CreateRetailMediaAudienceV2Attributes
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_v2_data import CreateRetailMediaAudienceV2Data
from criteo_api_retailmedia_v2023_10.model.create_retail_media_audience_v2_request import CreateRetailMediaAudienceV2Request
from criteo_api_retailmedia_v2023_10.model.create_user_behavior_segment_v2 import CreateUserBehaviorSegmentV2
from criteo_api_retailmedia_v2023_10.model.creative202110 import Creative202110
from criteo_api_retailmedia_v2023_10.model.creative202110_list_response import Creative202110ListResponse
from criteo_api_retailmedia_v2023_10.model.creative202210 import Creative202210
from criteo_api_retailmedia_v2023_10.model.creative202210_list_response import Creative202210ListResponse
from criteo_api_retailmedia_v2023_10.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_v2023_10.model.creative_create_model202207 import CreativeCreateModel202207
from criteo_api_retailmedia_v2023_10.model.creative_update_model202207 import CreativeUpdateModel202207
from criteo_api_retailmedia_v2023_10.model.customer_list_details import CustomerListDetails
from criteo_api_retailmedia_v2023_10.model.editable_campaign_attributes_v202301 import EditableCampaignAttributesV202301
from criteo_api_retailmedia_v2023_10.model.external_account import ExternalAccount
from criteo_api_retailmedia_v2023_10.model.external_add_funds_to_balance import ExternalAddFundsToBalance
from criteo_api_retailmedia_v2023_10.model.external_add_to_basket_ids_update_model202110 import ExternalAddToBasketIdsUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.external_add_to_basket_target202110 import ExternalAddToBasketTarget202110
from criteo_api_retailmedia_v2023_10.model.external_auction_line_item import ExternalAuctionLineItem
from criteo_api_retailmedia_v2023_10.model.external_auction_line_item_create_model import ExternalAuctionLineItemCreateModel
from criteo_api_retailmedia_v2023_10.model.external_auction_line_item_update_model import ExternalAuctionLineItemUpdateModel
from criteo_api_retailmedia_v2023_10.model.external_audience_ids_update_model202110 import ExternalAudienceIdsUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.external_audience_target202110 import ExternalAudienceTarget202110
from criteo_api_retailmedia_v2023_10.model.external_balance202110 import ExternalBalance202110
from criteo_api_retailmedia_v2023_10.model.external_balance_response import ExternalBalanceResponse
from criteo_api_retailmedia_v2023_10.model.external_brand import ExternalBrand
from criteo_api_retailmedia_v2023_10.model.external_catalog_request import ExternalCatalogRequest
from criteo_api_retailmedia_v2023_10.model.external_catalog_status import ExternalCatalogStatus
from criteo_api_retailmedia_v2023_10.model.external_change_dates_of_balance import ExternalChangeDatesOfBalance
from criteo_api_retailmedia_v2023_10.model.external_common_line_item import ExternalCommonLineItem
from criteo_api_retailmedia_v2023_10.model.external_create_balance import ExternalCreateBalance
from criteo_api_retailmedia_v2023_10.model.external_keyword_target202110 import ExternalKeywordTarget202110
from criteo_api_retailmedia_v2023_10.model.external_line_item_capping202110 import ExternalLineItemCapping202110
from criteo_api_retailmedia_v2023_10.model.external_line_item_page202110 import ExternalLineItemPage202110
from criteo_api_retailmedia_v2023_10.model.external_line_item_page_category202110 import ExternalLineItemPageCategory202110
from criteo_api_retailmedia_v2023_10.model.external_preferred_line_item202110 import ExternalPreferredLineItem202110
from criteo_api_retailmedia_v2023_10.model.external_preferred_line_item_create_model202110 import ExternalPreferredLineItemCreateModel202110
from criteo_api_retailmedia_v2023_10.model.external_preferred_line_item_update_model202110 import ExternalPreferredLineItemUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.external_promoted_product202110 import ExternalPromotedProduct202110
from criteo_api_retailmedia_v2023_10.model.external_retailer import ExternalRetailer
from criteo_api_retailmedia_v2023_10.model.external_retailer_pages202110 import ExternalRetailerPages202110
from criteo_api_retailmedia_v2023_10.model.external_store_ids_update_model202110 import ExternalStoreIdsUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.external_store_target202110 import ExternalStoreTarget202110
from criteo_api_retailmedia_v2023_10.model.external_update_balance_model import ExternalUpdateBalanceModel
from criteo_api_retailmedia_v2023_10.model.files_variable_value import FilesVariableValue
from criteo_api_retailmedia_v2023_10.model.files_variables_specification import FilesVariablesSpecification
from criteo_api_retailmedia_v2023_10.model.get_page_of_audiences_by_account_id_response import GetPageOfAudiencesByAccountIdResponse
from criteo_api_retailmedia_v2023_10.model.hyperlink_variable_value import HyperlinkVariableValue
from criteo_api_retailmedia_v2023_10.model.input_resource_of_auction_line_item_create_model import InputResourceOfAuctionLineItemCreateModel
from criteo_api_retailmedia_v2023_10.model.input_resource_of_preferred_line_item_create_model202110 import InputResourceOfPreferredLineItemCreateModel202110
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_external_id_of_editable_campaign_attributes_v202301_and_campaign_v202301 import JsonApiBodyWithExternalIdOfEditableCampaignAttributesV202301AndCampaignV202301
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_id_of_int64_and_account_and_account import JsonApiBodyWithIdOfInt64AndAccountAndAccount
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_id_of_int64_and_brand_and_brand import JsonApiBodyWithIdOfInt64AndBrandAndBrand
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_id_of_int64_and_campaign_v202301_and_campaign_v202301 import JsonApiBodyWithIdOfInt64AndCampaignV202301AndCampaignV202301
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_id_of_int64_and_catalog_status_and_catalog_status import JsonApiBodyWithIdOfInt64AndCatalogStatusAndCatalogStatus
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_id_of_int64_and_line_item_bid_multipliers_and_line_item_bid_multipliers import JsonApiBodyWithIdOfInt64AndLineItemBidMultipliersAndLineItemBidMultipliers
from criteo_api_retailmedia_v2023_10.model.json_api_body_with_id_of_int64_and_retailer_and_retailer import JsonApiBodyWithIdOfInt64AndRetailerAndRetailer
from criteo_api_retailmedia_v2023_10.model.json_api_body_without_id_of_campaign_attributes_v202301_and_campaign_v202301 import JsonApiBodyWithoutIdOfCampaignAttributesV202301AndCampaignV202301
from criteo_api_retailmedia_v2023_10.model.json_api_body_without_id_of_catalog_request_and_catalog_request import JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequest
from criteo_api_retailmedia_v2023_10.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
from criteo_api_retailmedia_v2023_10.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from criteo_api_retailmedia_v2023_10.model.json_api_page_response_of_campaign_v202301 import JsonApiPageResponseOfCampaignV202301
from criteo_api_retailmedia_v2023_10.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
from criteo_api_retailmedia_v2023_10.model.json_api_request_of_catalog_request import JsonApiRequestOfCatalogRequest
from criteo_api_retailmedia_v2023_10.model.json_api_single_response_of_campaign_v202301 import JsonApiSingleResponseOfCampaignV202301
from criteo_api_retailmedia_v2023_10.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_v2023_10.model.json_api_single_response_of_line_item_bid_multipliers import JsonApiSingleResponseOfLineItemBidMultipliers
from criteo_api_retailmedia_v2023_10.model.keyword_target202110_request import KeywordTarget202110Request
from criteo_api_retailmedia_v2023_10.model.keyword_target202110_response import KeywordTarget202110Response
from criteo_api_retailmedia_v2023_10.model.line_item_bid_multipliers import LineItemBidMultipliers
from criteo_api_retailmedia_v2023_10.model.line_item_bid_multipliers_request import LineItemBidMultipliersRequest
from criteo_api_retailmedia_v2023_10.model.line_item_bid_multipliers_response import LineItemBidMultipliersResponse
from criteo_api_retailmedia_v2023_10.model.page_metadata import PageMetadata
from criteo_api_retailmedia_v2023_10.model.page_type_environment import PageTypeEnvironment
from criteo_api_retailmedia_v2023_10.model.post_campaign_v202301 import PostCampaignV202301
from criteo_api_retailmedia_v2023_10.model.preferred_line_item202110_paged_list_response import PreferredLineItem202110PagedListResponse
from criteo_api_retailmedia_v2023_10.model.preferred_line_item202110_response import PreferredLineItem202110Response
from criteo_api_retailmedia_v2023_10.model.preferred_line_item_create_model202110_request import PreferredLineItemCreateModel202110Request
from criteo_api_retailmedia_v2023_10.model.preferred_line_item_update_model202110_request import PreferredLineItemUpdateModel202110Request
from criteo_api_retailmedia_v2023_10.model.problem_details import ProblemDetails
from criteo_api_retailmedia_v2023_10.model.promoted_product202110_list_request import PromotedProduct202110ListRequest
from criteo_api_retailmedia_v2023_10.model.promoted_product202110_paged_list_response import PromotedProduct202110PagedListResponse
from criteo_api_retailmedia_v2023_10.model.put_campaign_v202301 import PutCampaignV202301
from criteo_api_retailmedia_v2023_10.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_v2023_10.model.resource_of_add_funds_to_balance import ResourceOfAddFundsToBalance
from criteo_api_retailmedia_v2023_10.model.resource_of_auction_line_item import ResourceOfAuctionLineItem
from criteo_api_retailmedia_v2023_10.model.resource_of_auction_line_item_update_model import ResourceOfAuctionLineItemUpdateModel
from criteo_api_retailmedia_v2023_10.model.resource_of_balance202110 import ResourceOfBalance202110
from criteo_api_retailmedia_v2023_10.model.resource_of_balance_campaign202110 import ResourceOfBalanceCampaign202110
from criteo_api_retailmedia_v2023_10.model.resource_of_balance_response import ResourceOfBalanceResponse
from criteo_api_retailmedia_v2023_10.model.resource_of_category202204 import ResourceOfCategory202204
from criteo_api_retailmedia_v2023_10.model.resource_of_change_dates_of_balance import ResourceOfChangeDatesOfBalance
from criteo_api_retailmedia_v2023_10.model.resource_of_common_line_item import ResourceOfCommonLineItem
from criteo_api_retailmedia_v2023_10.model.resource_of_create_balance import ResourceOfCreateBalance
from criteo_api_retailmedia_v2023_10.model.resource_of_creative202110 import ResourceOfCreative202110
from criteo_api_retailmedia_v2023_10.model.resource_of_creative202210 import ResourceOfCreative202210
from criteo_api_retailmedia_v2023_10.model.resource_of_line_item_bid_multipliers import ResourceOfLineItemBidMultipliers
from criteo_api_retailmedia_v2023_10.model.resource_of_preferred_line_item202110 import ResourceOfPreferredLineItem202110
from criteo_api_retailmedia_v2023_10.model.resource_of_preferred_line_item_update_model202110 import ResourceOfPreferredLineItemUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.resource_of_promoted_product202110 import ResourceOfPromotedProduct202110
from criteo_api_retailmedia_v2023_10.model.resource_of_template import ResourceOfTemplate
from criteo_api_retailmedia_v2023_10.model.resource_of_update_balance_model import ResourceOfUpdateBalanceModel
from criteo_api_retailmedia_v2023_10.model.retail_media_audience import RetailMediaAudience
from criteo_api_retailmedia_v2023_10.model.retail_media_audience_attributes import RetailMediaAudienceAttributes
from criteo_api_retailmedia_v2023_10.model.retail_media_audience_v2 import RetailMediaAudienceV2
from criteo_api_retailmedia_v2023_10.model.retail_media_audience_v2_attributes import RetailMediaAudienceV2Attributes
from criteo_api_retailmedia_v2023_10.model.retail_media_audience_v2_list_response import RetailMediaAudienceV2ListResponse
from criteo_api_retailmedia_v2023_10.model.retail_media_audience_v2_response import RetailMediaAudienceV2Response
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_add_remove_keyword_model import RetailMediaExternalv1AddRemoveKeywordModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_add_remove_keywords_model import RetailMediaExternalv1AddRemoveKeywordsModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_add_remove_keywords_model_request import RetailMediaExternalv1AddRemoveKeywordsModelRequest
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_add_remove_keywords_model_resource import RetailMediaExternalv1AddRemoveKeywordsModelResource
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_input_keywords_model import RetailMediaExternalv1InputKeywordsModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_keyword_data_model import RetailMediaExternalv1KeywordDataModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_keywords_model import RetailMediaExternalv1KeywordsModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_keywords_model_resource import RetailMediaExternalv1KeywordsModelResource
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_keywords_model_response import RetailMediaExternalv1KeywordsModelResponse
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_problem_details import RetailMediaExternalv1ProblemDetails
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_proposal_status_model import RetailMediaExternalv1ProposalStatusModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_proposal_status_model_resource import RetailMediaExternalv1ProposalStatusModelResource
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_proposal_status_model_response import RetailMediaExternalv1ProposalStatusModelResponse
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_resource_outcome import RetailMediaExternalv1ResourceOutcome
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_set_bid_model import RetailMediaExternalv1SetBidModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_set_bids_model import RetailMediaExternalv1SetBidsModel
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_set_bids_model_request import RetailMediaExternalv1SetBidsModelRequest
from criteo_api_retailmedia_v2023_10.model.retail_media_externalv1_set_bids_model_resource import RetailMediaExternalv1SetBidsModelResource
from criteo_api_retailmedia_v2023_10.model.section import Section
from criteo_api_retailmedia_v2023_10.model.status_response import StatusResponse
from criteo_api_retailmedia_v2023_10.model.status_response_resource import StatusResponseResource
from criteo_api_retailmedia_v2023_10.model.store_ids_update_model202110_request import StoreIdsUpdateModel202110Request
from criteo_api_retailmedia_v2023_10.model.store_target202110_request import StoreTarget202110Request
from criteo_api_retailmedia_v2023_10.model.store_target202110_response import StoreTarget202110Response
from criteo_api_retailmedia_v2023_10.model.template import Template
from criteo_api_retailmedia_v2023_10.model.template_list_response import TemplateListResponse
from criteo_api_retailmedia_v2023_10.model.template_response import TemplateResponse
from criteo_api_retailmedia_v2023_10.model.template_variable import TemplateVariable
from criteo_api_retailmedia_v2023_10.model.template_variable_value import TemplateVariableValue
from criteo_api_retailmedia_v2023_10.model.text_variable_specification import TextVariableSpecification
from criteo_api_retailmedia_v2023_10.model.text_variable_value import TextVariableValue
from criteo_api_retailmedia_v2023_10.model.update_balance_model_request import UpdateBalanceModelRequest
from criteo_api_retailmedia_v2023_10.model.user_behavior_details import UserBehaviorDetails
from criteo_api_retailmedia_v2023_10.model.user_behavior_details_v2 import UserBehaviorDetailsV2
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_add_to_basket_ids_update_model202110 import ValueTypeResourceOfAddToBasketIdsUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_add_to_basket_target202110 import ValueTypeResourceOfAddToBasketTarget202110
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_audience_ids_update_model202110 import ValueTypeResourceOfAudienceIdsUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_audience_target202110 import ValueTypeResourceOfAudienceTarget202110
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_keyword_target202110 import ValueTypeResourceOfKeywordTarget202110
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_store_ids_update_model202110 import ValueTypeResourceOfStoreIdsUpdateModel202110
from criteo_api_retailmedia_v2023_10.model.value_type_resource_of_store_target202110 import ValueTypeResourceOfStoreTarget202110
