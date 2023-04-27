"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

    The version of the OpenAPI document: 2022-07
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_retailmedia_v2022_07.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_retailmedia_v2022_07.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_retailmedia_v2022_07.model.create_retail_media_audience_request import CreateRetailMediaAudienceRequest
from criteo_api_retailmedia_v2022_07.model.create_retail_media_audience_response import CreateRetailMediaAudienceResponse
from criteo_api_retailmedia_v2022_07.model.get_page_of_audiences_by_account_id_response import GetPageOfAudiencesByAccountIdResponse


class AudienceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_audience_endpoint = _Endpoint(
            settings={
                'response_type': (CreateRetailMediaAudienceResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/retail-media/accounts/{accountId}/audiences',
                'operation_id': 'create_audience',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'create_retail_media_audience_request',
                ],
                'required': [
                    'account_id',
                    'create_retail_media_audience_request',
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
                    'account_id':
                        (str,),
                    'create_retail_media_audience_request':
                        (CreateRetailMediaAudienceRequest,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'create_retail_media_audience_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_audiences_by_account_id_endpoint = _Endpoint(
            settings={
                'response_type': (GetPageOfAudiencesByAccountIdResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/retail-media/accounts/{accountId}/audiences',
                'operation_id': 'get_audiences_by_account_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'limit_to_id',
                    'page_size',
                    'page_index',
                ],
                'required': [
                    'account_id',
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
                    'account_id':
                        (str,),
                    'limit_to_id':
                        ([str],),
                    'page_size':
                        (int,),
                    'page_index':
                        (int,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'limit_to_id': 'limitToId',
                    'page_size': 'pageSize',
                    'page_index': 'pageIndex',
                },
                'location_map': {
                    'account_id': 'path',
                    'limit_to_id': 'query',
                    'page_size': 'query',
                    'page_index': 'query',
                },
                'collection_format_map': {
                    'limit_to_id': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_audience(
        self,
        account_id,
        create_retail_media_audience_request,
        **kwargs
    ):
        """create_audience  # noqa: E501

        Create an audience for a given account ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_audience(account_id, create_retail_media_audience_request, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): ID of the account to which this audience belongs.
            create_retail_media_audience_request (CreateRetailMediaAudienceRequest):

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
            CreateRetailMediaAudienceResponse
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
        kwargs['account_id'] = \
            account_id
        kwargs['create_retail_media_audience_request'] = \
            create_retail_media_audience_request
        return self.create_audience_endpoint.call_with_http_info(**kwargs)

    def get_audiences_by_account_id(
        self,
        account_id,
        **kwargs
    ):
        """get_audiences_by_account_id  # noqa: E501

        Get a page of audiences for a given account ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_audiences_by_account_id(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): External account ID which owns audience.

        Keyword Args:
            limit_to_id ([str]): Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2. [optional]
            page_size (int): Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page. [optional]
            page_index (int): Returns the specified page of results given a pageSize; pages are 0-indexed. [optional]
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
            GetPageOfAudiencesByAccountIdResponse
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
        kwargs['account_id'] = \
            account_id
        return self.get_audiences_by_account_id_endpoint.call_with_http_info(**kwargs)

