"""
    Criteo API

    Criteo API - RetailMedia  # noqa: E501

    The version of the OpenAPI document: Preview
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_retailmedia_preview.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_retailmedia_preview.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_of_retail_media_child_account import EntityResourceCollectionOutcomeOfRetailMediaChildAccount
from criteo_api_retailmedia_preview.model.grant_consent_input import GrantConsentInput
from criteo_api_retailmedia_preview.model.outcome import Outcome
from criteo_api_retailmedia_preview.model.value_resource_collection_outcome_of_seller_search_result import ValueResourceCollectionOutcomeOfSellerSearchResult
from criteo_api_retailmedia_preview.model.value_resource_input_of_seller_search import ValueResourceInputOfSellerSearch


class AccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_api_external_v1_account_private_market_child_accounts_by_account_id_endpoint = _Endpoint(
            settings={
                'response_type': (EntityResourceCollectionOutcomeOfRetailMediaChildAccount,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/retail-media/account-management/accounts/{accountId}/private-market-child-accounts',
                'operation_id': 'get_api_external_v1_account_private_market_child_accounts_by_account_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'offset',
                    'limit',
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
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'offset': 'offset',
                    'limit': 'limit',
                },
                'location_map': {
                    'account_id': 'path',
                    'offset': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
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
        self.grant_consent_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/retail-media/accounts/{accountId}/grant-consent',
                'operation_id': 'grant_consent',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'grant_consent_input',
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
                    'grant_consent_input':
                        (GrantConsentInput,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'grant_consent_input': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client
        )
        self.search_sellers_endpoint = _Endpoint(
            settings={
                'response_type': (ValueResourceCollectionOutcomeOfSellerSearchResult,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/retail-media/accounts/sellers/search',
                'operation_id': 'search_sellers',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'value_resource_input_of_seller_search',
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
                    'value_resource_input_of_seller_search':
                        (ValueResourceInputOfSellerSearch,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'value_resource_input_of_seller_search': 'body',
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

    def get_api_external_v1_account_private_market_child_accounts_by_account_id(
        self,
        account_id,
        **kwargs
    ):
        """get_api_external_v1_account_private_market_child_accounts_by_account_id  # noqa: E501

        Gets page of private market child accounts that are associated with the given account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_external_v1_account_private_market_child_accounts_by_account_id(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Account Id

        Keyword Args:
            offset (int): The (zero-based) offset into the collection of accounts. The default is 0.. [optional] if omitted the server will use the default value of 0
            limit (int): The number of accounts to be returned. The default is 25.. [optional] if omitted the server will use the default value of 25
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
            EntityResourceCollectionOutcomeOfRetailMediaChildAccount
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
        return self.get_api_external_v1_account_private_market_child_accounts_by_account_id_endpoint.call_with_http_info(**kwargs)

    def grant_consent(
        self,
        account_id,
        **kwargs
    ):
        """  # noqa: E501

        Grant consent to a business application on behalf of a Private Market demand account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.grant_consent(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): The demand account ID on which to grant consent

        Keyword Args:
            grant_consent_input (GrantConsentInput): [optional]
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
            None
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
        return self.grant_consent_endpoint.call_with_http_info(**kwargs)

    def search_sellers(
        self,
        **kwargs
    ):
        """search_sellers  # noqa: E501

        Get the sellers mapped to provided accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_sellers(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            value_resource_input_of_seller_search (ValueResourceInputOfSellerSearch): . [optional]
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
            ValueResourceCollectionOutcomeOfSellerSearchResult
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
        return self.search_sellers_endpoint.call_with_http_info(**kwargs)

