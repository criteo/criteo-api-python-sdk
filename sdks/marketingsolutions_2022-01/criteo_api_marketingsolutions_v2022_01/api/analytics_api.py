"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

    The version of the OpenAPI document: 2022-01
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_v2022_01.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_marketingsolutions_v2022_01.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_marketingsolutions_v2022_01.model.error_message import ErrorMessage
from criteo_api_marketingsolutions_v2022_01.model.placements_report_query_data_message import PlacementsReportQueryDataMessage
from criteo_api_marketingsolutions_v2022_01.model.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_api_marketingsolutions_v2022_01.model.transactions_report_query_data_message import TransactionsReportQueryDataMessage
from criteo_api_marketingsolutions_v2022_01.model.transparency_query_message import TransparencyQueryMessage
from criteo_api_marketingsolutions_v2022_01.model.transparency_report_data_message import TransparencyReportDataMessage


class AnalyticsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_adset_report(
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
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_adset_report = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2022-01/statistics/report',
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
            callable=__get_adset_report
        )

        def __get_placements_report(
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
                placements_report_query_data_message (PlacementsReportQueryDataMessage): [optional]
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_placements_report = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2022-01/placements/report',
                'operation_id': 'get_placements_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'placements_report_query_data_message',
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
                    'placements_report_query_data_message':
                        (PlacementsReportQueryDataMessage,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'placements_report_query_data_message': 'body',
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
            callable=__get_placements_report
        )

        def __get_transactions_report(
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
                transactions_report_query_data_message (TransactionsReportQueryDataMessage): [optional]
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_transactions_report = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2022-01/transactions/report',
                'operation_id': 'get_transactions_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'transactions_report_query_data_message',
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
                    'transactions_report_query_data_message':
                        (TransactionsReportQueryDataMessage,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'transactions_report_query_data_message': 'body',
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
            callable=__get_transactions_report
        )

        def __get_transparency_report(
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
                transparency_query_message (TransparencyQueryMessage): [optional]
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
                TransparencyReportDataMessage
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
            kwargs['advertiser_id'] = \
                advertiser_id
            return self.call_with_http_info(**kwargs)

        self.get_transparency_report = _Endpoint(
            settings={
                'response_type': (TransparencyReportDataMessage,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/2022-01/log-level/advertisers/{advertiser-id}/report',
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
                    'application/json',
                    'text/plain',
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
            callable=__get_transparency_report
        )
