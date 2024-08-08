"""
    Criteo API

    Criteo API - MarketingSolutions  # noqa: E501

    The version of the OpenAPI document: 2023-10
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_v2023_10.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_marketingsolutions_v2023_10.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_marketingsolutions_v2023_10.model.outcome import Outcome
from criteo_api_marketingsolutions_v2023_10.model.placements_report_query_message_list_request import PlacementsReportQueryMessageListRequest
from criteo_api_marketingsolutions_v2023_10.model.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_api_marketingsolutions_v2023_10.model.transactions_report_query_message_list_request import TransactionsReportQueryMessageListRequest
from criteo_api_marketingsolutions_v2023_10.model.transparency_query_message import TransparencyQueryMessage
from criteo_api_marketingsolutions_v2023_10.model.transparency_report_list_response import TransparencyReportListResponse


class AnalyticsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_adset_report_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2023-10/statistics/report',
                'operation_id': 'get_adset_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'statistics_report_query_message',
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
                    'statistics_report_query_message':
                        (StatisticsReportQueryMessage,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'statistics_report_query_message': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json',
                    'text/csv',
                    'text/xml',
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client
        )
        self.get_placements_report_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2023-10/placements/report',
                'operation_id': 'get_placements_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'placements_report_query_message_list_request',
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
                    'placements_report_query_message_list_request':
                        (PlacementsReportQueryMessageListRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'placements_report_query_message_list_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client
        )
        self.get_transactions_report_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2023-10/transactions/report',
                'operation_id': 'get_transactions_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'transactions_report_query_message_list_request',
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
                    'transactions_report_query_message_list_request':
                        (TransactionsReportQueryMessageListRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'transactions_report_query_message_list_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json',
                    'text/csv',
                    'text/xml',
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client
        )
        self.get_transparency_report_endpoint = _Endpoint(
            settings={
                'response_type': (TransparencyReportListResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2023-10/log-level/advertisers/{advertiser-id}/report',
                'operation_id': 'get_transparency_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'advertiser_id',
                    'transparency_query_message',
                ],
                'required': [
                    'advertiser_id',
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
                    'advertiser_id':
                        (int,),
                    'transparency_query_message':
                        (TransparencyQueryMessage,),
                },
                'attribute_map': {
                    'advertiser_id': 'advertiser-id',
                },
                'location_map': {
                    'advertiser_id': 'path',
                    'transparency_query_message': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client
        )

    def get_adset_report(
        self,
        **kwargs
    ):
        """get_adset_report  # noqa: E501

        This Statistics endpoint provides adset related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adset_report(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            statistics_report_query_message (StatisticsReportQueryMessage): [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_adset_report_endpoint.call_with_http_info(**kwargs)

    def get_placements_report(
        self,
        **kwargs
    ):
        """get_placements_report  # noqa: E501

        Your ads are placed in different domains (publishers) and environments (websites and apps). Thanks to the placements endpoint, you can analyse the performances for each publisher, comparing displays, clicks and sales generated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_placements_report(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            placements_report_query_message_list_request (PlacementsReportQueryMessageListRequest): [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_placements_report_endpoint.call_with_http_info(**kwargs)

    def get_transactions_report(
        self,
        **kwargs
    ):
        """get_transactions_report  # noqa: E501

        This Transactions endpoint provides transactions id related data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transactions_report(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            transactions_report_query_message_list_request (TransactionsReportQueryMessageListRequest): [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_transactions_report_endpoint.call_with_http_info(**kwargs)

    def get_transparency_report(
        self,
        advertiser_id,
        **kwargs
    ):
        """get_transparency_report  # noqa: E501

        This Statistics endpoint provides publisher data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transparency_report(advertiser_id, async_req=True)
        >>> result = thread.get()

        Args:
            advertiser_id (int): The advertiser id to fetch the transparency data.

        Keyword Args:
            transparency_query_message (TransparencyQueryMessage): The query message.. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TransparencyReportListResponse
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['advertiser_id'] = \
            advertiser_id
        return self.get_transparency_report_endpoint.call_with_http_info(**kwargs)

