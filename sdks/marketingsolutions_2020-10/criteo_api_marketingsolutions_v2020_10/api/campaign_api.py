"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_v2020_10.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_marketingsolutions_v2020_10.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_marketingsolutions_v2020_10.model.campaign_list_response import CampaignListResponse
from criteo_api_marketingsolutions_v2020_10.model.campaign_response import CampaignResponse
from criteo_api_marketingsolutions_v2020_10.model.campaign_search_request import CampaignSearchRequest
from criteo_api_marketingsolutions_v2020_10.model.patch_campaign_list_request import PatchCampaignListRequest
from criteo_api_marketingsolutions_v2020_10.model.patch_result_campaign_list_response import PatchResultCampaignListResponse
from criteo_api_marketingsolutions_v2020_10.model.request_ad_set_search import RequestAdSetSearch
from criteo_api_marketingsolutions_v2020_10.model.requests_ad_set_id import RequestsAdSetId
from criteo_api_marketingsolutions_v2020_10.model.requests_patch_ad_set import RequestsPatchAdSet
from criteo_api_marketingsolutions_v2020_10.model.response_ad_set_id import ResponseAdSetId
from criteo_api_marketingsolutions_v2020_10.model.response_read_ad_set import ResponseReadAdSet
from criteo_api_marketingsolutions_v2020_10.model.responses_ad_set_id import ResponsesAdSetId
from criteo_api_marketingsolutions_v2020_10.model.responses_read_ad_set import ResponsesReadAdSet


class CampaignApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_ad_set(
            self,
            ad_set_id,
            **kwargs
        ):
            """get_ad_set  # noqa: E501

            Get the data for the specified ad set  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_ad_set(ad_set_id, async_req=True)
            >>> result = thread.get()

            Args:
                ad_set_id (str): Id of the ad set

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ResponseReadAdSet
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['ad_set_id'] = \
                ad_set_id
            return self.call_with_http_info(**kwargs)

        self.get_ad_set = _Endpoint(
            settings={
                'response_type': (ResponseReadAdSet,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/ad-sets/{adSetId}',
                'operation_id': 'get_ad_set',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_set_id',
                ],
                'required': [
                    'ad_set_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_set_id':
                        (str,),
                },
                'attribute_map': {
                    'ad_set_id': 'adSetId',
                },
                'location_map': {
                    'ad_set_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_ad_set
        )

        def __get_campaign(
            self,
            campaign_id,
            **kwargs
        ):
            """get_campaign  # noqa: E501

            Get the data for the specified campaign  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_campaign(campaign_id, async_req=True)
            >>> result = thread.get()

            Args:
                campaign_id (str): Id of the campaign

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CampaignResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['campaign_id'] = \
                campaign_id
            return self.call_with_http_info(**kwargs)

        self.get_campaign = _Endpoint(
            settings={
                'response_type': (CampaignResponse,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/campaigns/{campaign-id}',
                'operation_id': 'get_campaign',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'campaign_id',
                ],
                'required': [
                    'campaign_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'campaign_id':
                        (str,),
                },
                'attribute_map': {
                    'campaign_id': 'campaign-id',
                },
                'location_map': {
                    'campaign_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_campaign
        )

        def __patch_ad_sets(
            self,
            **kwargs
        ):
            """patch_ad_sets  # noqa: E501

            Patch a list of AdSets.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_ad_sets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                requests_patch_ad_set (RequestsPatchAdSet): List of adsets to patch.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ResponseAdSetId
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.patch_ad_sets = _Endpoint(
            settings={
                'response_type': (ResponseAdSetId,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/ad-sets',
                'operation_id': 'patch_ad_sets',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'requests_patch_ad_set',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'requests_patch_ad_set':
                        (RequestsPatchAdSet,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'requests_patch_ad_set': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__patch_ad_sets
        )

        def __patch_campaigns(
            self,
            **kwargs
        ):
            """patch_campaigns  # noqa: E501

            Patch a list of Campaigns.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_campaigns(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                patch_campaign_list_request (PatchCampaignListRequest): List of campaigns to patch.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PatchResultCampaignListResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.patch_campaigns = _Endpoint(
            settings={
                'response_type': (PatchResultCampaignListResponse,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/campaigns',
                'operation_id': 'patch_campaigns',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'patch_campaign_list_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'patch_campaign_list_request':
                        (PatchCampaignListRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'patch_campaign_list_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__patch_campaigns
        )

        def __search_ad_sets(
            self,
            **kwargs
        ):
            """search_ad_sets  # noqa: E501

            Search for ad sets  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_ad_sets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                request_ad_set_search (RequestAdSetSearch): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ResponsesReadAdSet
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.search_ad_sets = _Endpoint(
            settings={
                'response_type': (ResponsesReadAdSet,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/ad-sets/search',
                'operation_id': 'search_ad_sets',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'request_ad_set_search',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'request_ad_set_search':
                        (RequestAdSetSearch,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'request_ad_set_search': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__search_ad_sets
        )

        def __search_campaigns(
            self,
            **kwargs
        ):
            """search_campaigns  # noqa: E501

            Search for campaigns  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_campaigns(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                campaign_search_request (CampaignSearchRequest): filters on campaigns. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CampaignListResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.search_campaigns = _Endpoint(
            settings={
                'response_type': (CampaignListResponse,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/campaigns/search',
                'operation_id': 'search_campaigns',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'campaign_search_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'campaign_search_request':
                        (CampaignSearchRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'campaign_search_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__search_campaigns
        )

        def __start_ad_sets(
            self,
            **kwargs
        ):
            """start_ad_sets  # noqa: E501

            Start the specified list of ad sets  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.start_ad_sets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                requests_ad_set_id (RequestsAdSetId): All the ad sets to start. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ResponsesAdSetId
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.start_ad_sets = _Endpoint(
            settings={
                'response_type': (ResponsesAdSetId,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/ad-sets/start',
                'operation_id': 'start_ad_sets',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'requests_ad_set_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'requests_ad_set_id':
                        (RequestsAdSetId,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'requests_ad_set_id': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__start_ad_sets
        )

        def __stop_ad_sets(
            self,
            **kwargs
        ):
            """stop_ad_sets  # noqa: E501

            Stop the specified list of ad sets  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stop_ad_sets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                requests_ad_set_id (RequestsAdSetId): All the ad sets to stop. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ResponsesAdSetId
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.stop_ad_sets = _Endpoint(
            settings={
                'response_type': (ResponsesAdSetId,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2021-10/marketing-solutions/ad-sets/stop',
                'operation_id': 'stop_ad_sets',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'requests_ad_set_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'requests_ad_set_id':
                        (RequestsAdSetId,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'requests_ad_set_id': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__stop_ad_sets
        )
