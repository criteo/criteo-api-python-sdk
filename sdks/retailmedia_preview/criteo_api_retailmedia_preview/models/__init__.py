# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from criteo_api_retailmedia_preview.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_retailmedia_preview.model.application_summary_model import ApplicationSummaryModel
from criteo_api_retailmedia_preview.model.application_summary_model_resource import ApplicationSummaryModelResource
from criteo_api_retailmedia_preview.model.application_summary_model_response import ApplicationSummaryModelResponse
from criteo_api_retailmedia_preview.model.bad_request import BadRequest
from criteo_api_retailmedia_preview.model.brand_preview import BrandPreview
from criteo_api_retailmedia_preview.model.brand_preview_list_response import BrandPreviewListResponse
from criteo_api_retailmedia_preview.model.campaign_report import CampaignReport
from criteo_api_retailmedia_preview.model.campaign_report_request import CampaignReportRequest
from criteo_api_retailmedia_preview.model.campaign_report_resource import CampaignReportResource
from criteo_api_retailmedia_preview.model.category202204 import Category202204
from criteo_api_retailmedia_preview.model.choice_option import ChoiceOption
from criteo_api_retailmedia_preview.model.choice_variable_specification import ChoiceVariableSpecification
from criteo_api_retailmedia_preview.model.choice_variable_value import ChoiceVariableValue
from criteo_api_retailmedia_preview.model.color_variable_value import ColorVariableValue
from criteo_api_retailmedia_preview.model.common_error import CommonError
from criteo_api_retailmedia_preview.model.common_problem import CommonProblem
from criteo_api_retailmedia_preview.model.common_status_code_response import CommonStatusCodeResponse
from criteo_api_retailmedia_preview.model.common_warning import CommonWarning
from criteo_api_retailmedia_preview.model.cpc_rate_card_preview import CpcRateCardPreview
from criteo_api_retailmedia_preview.model.cpc_rate_card_preview_response import CpcRateCardPreviewResponse
from criteo_api_retailmedia_preview.model.create_retail_media_audience import CreateRetailMediaAudience
from criteo_api_retailmedia_preview.model.create_retail_media_audience_attributes import CreateRetailMediaAudienceAttributes
from criteo_api_retailmedia_preview.model.create_retail_media_audience_body import CreateRetailMediaAudienceBody
from criteo_api_retailmedia_preview.model.create_retail_media_audience_request import CreateRetailMediaAudienceRequest
from criteo_api_retailmedia_preview.model.create_retail_media_audience_response import CreateRetailMediaAudienceResponse
from criteo_api_retailmedia_preview.model.create_retail_media_audience_v2 import CreateRetailMediaAudienceV2
from criteo_api_retailmedia_preview.model.create_retail_media_audience_v2_attributes import CreateRetailMediaAudienceV2Attributes
from criteo_api_retailmedia_preview.model.create_retail_media_audience_v2_data import CreateRetailMediaAudienceV2Data
from criteo_api_retailmedia_preview.model.create_retail_media_audience_v2_request import CreateRetailMediaAudienceV2Request
from criteo_api_retailmedia_preview.model.create_user_behavior_segment_v2 import CreateUserBehaviorSegmentV2
from criteo_api_retailmedia_preview.model.creative202210 import Creative202210
from criteo_api_retailmedia_preview.model.creative202210_list_response import Creative202210ListResponse
from criteo_api_retailmedia_preview.model.creative202210_response import Creative202210Response
from criteo_api_retailmedia_preview.model.creative_create_model202207 import CreativeCreateModel202207
from criteo_api_retailmedia_preview.model.creative_update_model202207 import CreativeUpdateModel202207
from criteo_api_retailmedia_preview.model.customer_list_details import CustomerListDetails
from criteo_api_retailmedia_preview.model.envelope_report_request import EnvelopeReportRequest
from criteo_api_retailmedia_preview.model.envelope_report_status import EnvelopeReportStatus
from criteo_api_retailmedia_preview.model.error import Error
from criteo_api_retailmedia_preview.model.export_report_column import ExportReportColumn
from criteo_api_retailmedia_preview.model.export_report_meta_data import ExportReportMetaData
from criteo_api_retailmedia_preview.model.external_account import ExternalAccount
from criteo_api_retailmedia_preview.model.external_brand import ExternalBrand
from criteo_api_retailmedia_preview.model.external_catalog_request_preview import ExternalCatalogRequestPreview
from criteo_api_retailmedia_preview.model.external_catalog_status import ExternalCatalogStatus
from criteo_api_retailmedia_preview.model.external_product_button_request import ExternalProductButtonRequest
from criteo_api_retailmedia_preview.model.external_product_button_response import ExternalProductButtonResponse
from criteo_api_retailmedia_preview.model.external_retailer import ExternalRetailer
from criteo_api_retailmedia_preview.model.files_variable_value import FilesVariableValue
from criteo_api_retailmedia_preview.model.files_variables_specification import FilesVariablesSpecification
from criteo_api_retailmedia_preview.model.get_page_of_audiences_by_account_id_response import GetPageOfAudiencesByAccountIdResponse
from criteo_api_retailmedia_preview.model.global_brand import GlobalBrand
from criteo_api_retailmedia_preview.model.hyperlink_variable_value import HyperlinkVariableValue
from criteo_api_retailmedia_preview.model.json_api_body_with_id_of_int64_and_account_and_account import JsonApiBodyWithIdOfInt64AndAccountAndAccount
from criteo_api_retailmedia_preview.model.json_api_body_with_id_of_int64_and_brand_and_brand import JsonApiBodyWithIdOfInt64AndBrandAndBrand
from criteo_api_retailmedia_preview.model.json_api_body_with_id_of_int64_and_catalog_status_and_catalog_status import JsonApiBodyWithIdOfInt64AndCatalogStatusAndCatalogStatus
from criteo_api_retailmedia_preview.model.json_api_body_with_id_of_int64_and_line_item_bid_multipliers_and_line_item_bid_multipliers import JsonApiBodyWithIdOfInt64AndLineItemBidMultipliersAndLineItemBidMultipliers
from criteo_api_retailmedia_preview.model.json_api_body_with_id_of_int64_and_retailer_and_retailer import JsonApiBodyWithIdOfInt64AndRetailerAndRetailer
from criteo_api_retailmedia_preview.model.json_api_body_without_id_of_catalog_request_and_catalog_request_preview import JsonApiBodyWithoutIdOfCatalogRequestAndCatalogRequestPreview
from criteo_api_retailmedia_preview.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount
from criteo_api_retailmedia_preview.model.json_api_page_response_of_brand import JsonApiPageResponseOfBrand
from criteo_api_retailmedia_preview.model.json_api_page_response_of_retailer import JsonApiPageResponseOfRetailer
from criteo_api_retailmedia_preview.model.json_api_request_of_catalog_request_preview import JsonApiRequestOfCatalogRequestPreview
from criteo_api_retailmedia_preview.model.json_api_single_response_of_catalog_status import JsonApiSingleResponseOfCatalogStatus
from criteo_api_retailmedia_preview.model.json_api_single_response_of_line_item_bid_multipliers import JsonApiSingleResponseOfLineItemBidMultipliers
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers import LineItemBidMultipliers
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers_request import LineItemBidMultipliersRequest
from criteo_api_retailmedia_preview.model.line_item_bid_multipliers_response import LineItemBidMultipliersResponse
from criteo_api_retailmedia_preview.model.line_item_report import LineItemReport
from criteo_api_retailmedia_preview.model.line_item_report_request import LineItemReportRequest
from criteo_api_retailmedia_preview.model.line_item_report_resource import LineItemReportResource
from criteo_api_retailmedia_preview.model.map_string import MapString
from criteo_api_retailmedia_preview.model.page_metadata import PageMetadata
from criteo_api_retailmedia_preview.model.page_type_environment import PageTypeEnvironment
from criteo_api_retailmedia_preview.model.placement_preview import PlacementPreview
from criteo_api_retailmedia_preview.model.placement_preview_list_response import PlacementPreviewListResponse
from criteo_api_retailmedia_preview.model.problem_details import ProblemDetails
from criteo_api_retailmedia_preview.model.product_button_list_request import ProductButtonListRequest
from criteo_api_retailmedia_preview.model.product_button_list_response import ProductButtonListResponse
from criteo_api_retailmedia_preview.model.product_button_request import ProductButtonRequest
from criteo_api_retailmedia_preview.model.product_button_response import ProductButtonResponse
from criteo_api_retailmedia_preview.model.report_data_response_resource import ReportDataResponseResource
from criteo_api_retailmedia_preview.model.report_outcome import ReportOutcome
from criteo_api_retailmedia_preview.model.report_request import ReportRequest
from criteo_api_retailmedia_preview.model.report_request_attributes import ReportRequestAttributes
from criteo_api_retailmedia_preview.model.report_response import ReportResponse
from criteo_api_retailmedia_preview.model.report_status import ReportStatus
from criteo_api_retailmedia_preview.model.report_status_attributes import ReportStatusAttributes
from criteo_api_retailmedia_preview.model.resource_of_brand_preview import ResourceOfBrandPreview
from criteo_api_retailmedia_preview.model.resource_of_cpc_rate_card_preview import ResourceOfCpcRateCardPreview
from criteo_api_retailmedia_preview.model.resource_of_creative202210 import ResourceOfCreative202210
from criteo_api_retailmedia_preview.model.resource_of_line_item_bid_multipliers import ResourceOfLineItemBidMultipliers
from criteo_api_retailmedia_preview.model.resource_of_placement_preview import ResourceOfPlacementPreview
from criteo_api_retailmedia_preview.model.resource_of_product_button_request import ResourceOfProductButtonRequest
from criteo_api_retailmedia_preview.model.resource_of_product_button_response import ResourceOfProductButtonResponse
from criteo_api_retailmedia_preview.model.resource_of_seller_preview import ResourceOfSellerPreview
from criteo_api_retailmedia_preview.model.resource_of_sku_data_preview import ResourceOfSkuDataPreview
from criteo_api_retailmedia_preview.model.resource_of_sku_search_request_preview import ResourceOfSkuSearchRequestPreview
from criteo_api_retailmedia_preview.model.resource_of_sku_search_request_slim_preview import ResourceOfSkuSearchRequestSlimPreview
from criteo_api_retailmedia_preview.model.resource_of_sku_search_request_slim_v2_preview import ResourceOfSkuSearchRequestSlimV2Preview
from criteo_api_retailmedia_preview.model.resource_of_sku_slim_data_preview import ResourceOfSkuSlimDataPreview
from criteo_api_retailmedia_preview.model.resource_of_sku_slim_data_v2 import ResourceOfSkuSlimDataV2
from criteo_api_retailmedia_preview.model.resource_of_template import ResourceOfTemplate
from criteo_api_retailmedia_preview.model.retail_media_audience import RetailMediaAudience
from criteo_api_retailmedia_preview.model.retail_media_audience_attributes import RetailMediaAudienceAttributes
from criteo_api_retailmedia_preview.model.retail_media_audience_v2 import RetailMediaAudienceV2
from criteo_api_retailmedia_preview.model.retail_media_audience_v2_attributes import RetailMediaAudienceV2Attributes
from criteo_api_retailmedia_preview.model.retail_media_audience_v2_list_response import RetailMediaAudienceV2ListResponse
from criteo_api_retailmedia_preview.model.retail_media_audience_v2_response import RetailMediaAudienceV2Response
from criteo_api_retailmedia_preview.model.retail_media_externalv1_add_remove_keyword_model import RetailMediaExternalv1AddRemoveKeywordModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_add_remove_keywords_model import RetailMediaExternalv1AddRemoveKeywordsModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_add_remove_keywords_model_request import RetailMediaExternalv1AddRemoveKeywordsModelRequest
from criteo_api_retailmedia_preview.model.retail_media_externalv1_add_remove_keywords_model_resource import RetailMediaExternalv1AddRemoveKeywordsModelResource
from criteo_api_retailmedia_preview.model.retail_media_externalv1_input_keywords_model import RetailMediaExternalv1InputKeywordsModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_keyword_data_model import RetailMediaExternalv1KeywordDataModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_keywords_model import RetailMediaExternalv1KeywordsModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_keywords_model_resource import RetailMediaExternalv1KeywordsModelResource
from criteo_api_retailmedia_preview.model.retail_media_externalv1_keywords_model_response import RetailMediaExternalv1KeywordsModelResponse
from criteo_api_retailmedia_preview.model.retail_media_externalv1_problem_details import RetailMediaExternalv1ProblemDetails
from criteo_api_retailmedia_preview.model.retail_media_externalv1_proposal_status_model import RetailMediaExternalv1ProposalStatusModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_proposal_status_model_resource import RetailMediaExternalv1ProposalStatusModelResource
from criteo_api_retailmedia_preview.model.retail_media_externalv1_proposal_status_model_response import RetailMediaExternalv1ProposalStatusModelResponse
from criteo_api_retailmedia_preview.model.retail_media_externalv1_resource_outcome import RetailMediaExternalv1ResourceOutcome
from criteo_api_retailmedia_preview.model.retail_media_externalv1_set_bid_model import RetailMediaExternalv1SetBidModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_set_bids_model import RetailMediaExternalv1SetBidsModel
from criteo_api_retailmedia_preview.model.retail_media_externalv1_set_bids_model_request import RetailMediaExternalv1SetBidsModelRequest
from criteo_api_retailmedia_preview.model.retail_media_externalv1_set_bids_model_resource import RetailMediaExternalv1SetBidsModelResource
from criteo_api_retailmedia_preview.model.retailer_brand import RetailerBrand
from criteo_api_retailmedia_preview.model.retailer_category import RetailerCategory
from criteo_api_retailmedia_preview.model.section import Section
from criteo_api_retailmedia_preview.model.seller_preview import SellerPreview
from criteo_api_retailmedia_preview.model.seller_preview_response import SellerPreviewResponse
from criteo_api_retailmedia_preview.model.sku_data_preview import SkuDataPreview
from criteo_api_retailmedia_preview.model.sku_data_preview_list_response import SkuDataPreviewListResponse
from criteo_api_retailmedia_preview.model.sku_search_request_preview import SkuSearchRequestPreview
from criteo_api_retailmedia_preview.model.sku_search_request_preview_request import SkuSearchRequestPreviewRequest
from criteo_api_retailmedia_preview.model.sku_search_request_slim_preview import SkuSearchRequestSlimPreview
from criteo_api_retailmedia_preview.model.sku_search_request_slim_preview_request import SkuSearchRequestSlimPreviewRequest
from criteo_api_retailmedia_preview.model.sku_search_request_slim_v2_preview import SkuSearchRequestSlimV2Preview
from criteo_api_retailmedia_preview.model.sku_search_request_slim_v2_preview_request import SkuSearchRequestSlimV2PreviewRequest
from criteo_api_retailmedia_preview.model.sku_slim_data_preview import SkuSlimDataPreview
from criteo_api_retailmedia_preview.model.sku_slim_data_preview_list_response import SkuSlimDataPreviewListResponse
from criteo_api_retailmedia_preview.model.sku_slim_data_v2 import SkuSlimDataV2
from criteo_api_retailmedia_preview.model.sku_slim_data_v2_list_response import SkuSlimDataV2ListResponse
from criteo_api_retailmedia_preview.model.template import Template
from criteo_api_retailmedia_preview.model.template_list_response import TemplateListResponse
from criteo_api_retailmedia_preview.model.template_response import TemplateResponse
from criteo_api_retailmedia_preview.model.template_variable import TemplateVariable
from criteo_api_retailmedia_preview.model.template_variable_value import TemplateVariableValue
from criteo_api_retailmedia_preview.model.text_variable_specification import TextVariableSpecification
from criteo_api_retailmedia_preview.model.text_variable_value import TextVariableValue
from criteo_api_retailmedia_preview.model.user_behavior_details import UserBehaviorDetails
from criteo_api_retailmedia_preview.model.user_behavior_details_v2 import UserBehaviorDetailsV2
