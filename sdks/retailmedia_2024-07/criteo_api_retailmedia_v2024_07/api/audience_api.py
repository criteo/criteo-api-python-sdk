"""
    Criteo API

    Criteo API - RetailMedia  # noqa: E501

    The version of the OpenAPI document: 2024-07
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_retailmedia_v2024_07.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_retailmedia_v2024_07.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_retailmedia_v2024_07.model.rm_legacy_audience_create_entity_v1_response import RmLegacyAudienceCreateEntityV1Response
from criteo_api_retailmedia_v2024_07.model.rm_legacy_audience_create_entity_v2_response import RmLegacyAudienceCreateEntityV2Response
from criteo_api_retailmedia_v2024_07.model.rm_legacy_audience_create_input_entity_v1 import RmLegacyAudienceCreateInputEntityV1
from criteo_api_retailmedia_v2024_07.model.rm_legacy_audience_create_input_entity_v2 import RmLegacyAudienceCreateInputEntityV2
from criteo_api_retailmedia_v2024_07.model.rm_legacy_audience_get_entity_v1_list_response import RmLegacyAudienceGetEntityV1ListResponse
from criteo_api_retailmedia_v2024_07.model.rm_legacy_audience_get_entity_v2_list_response import RmLegacyAudienceGetEntityV2ListResponse


class AudienceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.legacy_create_audience_v1_endpoint = _Endpoint(
            settings={
                'response_type': (RmLegacyAudienceCreateEntityV1Response,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2024-07/retail-media/accounts/{accountId}/audiences',
                'operation_id': 'legacy_create_audience_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'rm_legacy_audience_create_input_entity_v1',
                ],
                'required': [
                    'account_id',
                    'rm_legacy_audience_create_input_entity_v1',
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
                        (int,),
                    'rm_legacy_audience_create_input_entity_v1':
                        (RmLegacyAudienceCreateInputEntityV1,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'rm_legacy_audience_create_input_entity_v1': 'body',
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
            api_client=api_client
        )
        self.legacy_get_audience_v1_endpoint = _Endpoint(
            settings={
                'response_type': (RmLegacyAudienceGetEntityV1ListResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2024-07/retail-media/accounts/{accountId}/audiences',
                'operation_id': 'legacy_get_audience_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'limit_to_id',
                    'page_index',
                    'page_size',
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
                        (int,),
                    'limit_to_id':
                        ([int],),
                    'page_index':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'limit_to_id': 'limitToId',
                    'page_index': 'pageIndex',
                    'page_size': 'pageSize',
                },
                'location_map': {
                    'account_id': 'path',
                    'limit_to_id': 'query',
                    'page_index': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                    'limit_to_id': 'multi',
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
            api_client=api_client
        )
        self.legacy_get_audience_v2_endpoint = _Endpoint(
            settings={
                'response_type': (RmLegacyAudienceGetEntityV2ListResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2024-07/retail-media/v2/accounts/{accountId}/audiences',
                'operation_id': 'legacy_get_audience_v2',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'limit_to_id',
                    'page_index',
                    'page_size',
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
                        (int,),
                    'limit_to_id':
                        ([int],),
                    'page_index':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'limit_to_id': 'limitToId',
                    'page_index': 'pageIndex',
                    'page_size': 'pageSize',
                },
                'location_map': {
                    'account_id': 'path',
                    'limit_to_id': 'query',
                    'page_index': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                    'limit_to_id': 'multi',
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
            api_client=api_client
        )
        self.legacy_update_audience_v2_endpoint = _Endpoint(
            settings={
                'response_type': (RmLegacyAudienceCreateEntityV2Response,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2024-07/retail-media/v2/accounts/{accountId}/audiences',
                'operation_id': 'legacy_update_audience_v2',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'rm_legacy_audience_create_input_entity_v2',
                ],
                'required': [
                    'account_id',
                    'rm_legacy_audience_create_input_entity_v2',
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
                        (int,),
                    'rm_legacy_audience_create_input_entity_v2':
                        (RmLegacyAudienceCreateInputEntityV2,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'rm_legacy_audience_create_input_entity_v2': 'body',
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
            api_client=api_client
        )

    def legacy_create_audience_v1(
        self,
        account_id,
        rm_legacy_audience_create_input_entity_v1,
        **kwargs
    ):
        """legacy_create_audience_v1  # noqa: E501

        Create an Audience (deprecated Public API)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.legacy_create_audience_v1(account_id, rm_legacy_audience_create_input_entity_v1, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (int): ID of the account to which this audience belongs.
            rm_legacy_audience_create_input_entity_v1 (RmLegacyAudienceCreateInputEntityV1): Audience creation request.

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
            RmLegacyAudienceCreateEntityV1Response
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
        kwargs['rm_legacy_audience_create_input_entity_v1'] = \
            rm_legacy_audience_create_input_entity_v1
        return self.legacy_create_audience_v1_endpoint.call_with_http_info(**kwargs)

    def legacy_get_audience_v1(
        self,
        account_id,
        **kwargs
    ):
        """legacy_get_audience_v1  # noqa: E501

        Get a page of Audiences. (deprecated Public API)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.legacy_get_audience_v1(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (int): ID of the account to which this audience belongs.

        Keyword Args:
            limit_to_id ([int]): Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2. [optional]
            page_index (int): Returns the specified page of results given a pageSize; pages are 0-indexed.. [optional]
            page_size (int): Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page.. [optional]
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
            RmLegacyAudienceGetEntityV1ListResponse
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
        return self.legacy_get_audience_v1_endpoint.call_with_http_info(**kwargs)

    def legacy_get_audience_v2(
        self,
        account_id,
        **kwargs
    ):
        """legacy_get_audience_v2  # noqa: E501

        Get a page of Audiences. (deprecated Public API)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.legacy_get_audience_v2(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (int): ID of the account to which this audience belongs.

        Keyword Args:
            limit_to_id ([int]): Limits results to the entity IDs specified; parameter key is repeated, eg. limitToId=1&limitToId=2. [optional]
            page_index (int): Returns the specified page of results given a pageSize; pages are 0-indexed.. [optional]
            page_size (int): Specifies the maximum number of entities returned in a single page; defaults to 25 entities per page.. [optional]
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
            RmLegacyAudienceGetEntityV2ListResponse
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
        return self.legacy_get_audience_v2_endpoint.call_with_http_info(**kwargs)

    def legacy_update_audience_v2(
        self,
        account_id,
        rm_legacy_audience_create_input_entity_v2,
        **kwargs
    ):
        """legacy_update_audience_v2  # noqa: E501

        Create an Audience (deprecated Public API)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.legacy_update_audience_v2(account_id, rm_legacy_audience_create_input_entity_v2, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (int): ID of the account to which this audience belongs.
            rm_legacy_audience_create_input_entity_v2 (RmLegacyAudienceCreateInputEntityV2): Audience creation request.

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
            RmLegacyAudienceCreateEntityV2Response
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
        kwargs['rm_legacy_audience_create_input_entity_v2'] = \
            rm_legacy_audience_create_input_entity_v2
        return self.legacy_update_audience_v2_endpoint.call_with_http_info(**kwargs)

