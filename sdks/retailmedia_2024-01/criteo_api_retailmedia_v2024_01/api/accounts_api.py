"""
    Criteo API

    Criteo API - RetailMedia  # noqa: E501

    The version of the OpenAPI document: 2024-01
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_retailmedia_v2024_01.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_retailmedia_v2024_01.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_retailmedia_v2024_01.model.json_api_page_response_of_account import JsonApiPageResponseOfAccount


class AccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_api_v1_external_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiPageResponseOfAccount,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2024-01/retail-media/accounts',
                'operation_id': 'get_api_v1_external_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit_to_id',
                    'page_index',
                    'page_size',
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
                    'limit_to_id':
                        ([str],),
                    'page_index':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'limit_to_id': 'limitToId',
                    'page_index': 'pageIndex',
                    'page_size': 'pageSize',
                },
                'location_map': {
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

    def get_api_v1_external_accounts(
        self,
        **kwargs
    ):
        """get_api_v1_external_accounts  # noqa: E501

        Gets page of account objects that the current user can access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_v1_external_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit_to_id ([str]): The ids that you would like to limit your result set to. [optional]
            page_index (int): The 0 indexed page index you would like to receive given the page size. [optional] if omitted the server will use the default value of 0
            page_size (int): The maximum number of items you would like to receive in this request. [optional] if omitted the server will use the default value of 25
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
            JsonApiPageResponseOfAccount
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
        return self.get_api_v1_external_accounts_endpoint.call_with_http_info(**kwargs)

