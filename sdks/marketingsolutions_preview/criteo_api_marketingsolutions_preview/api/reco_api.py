"""
    Criteo API

    Criteo API - MarketingSolutions  # noqa: E501

    The version of the OpenAPI document: preview
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_preview.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_marketingsolutions_preview.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_marketingsolutions_preview.model.ok_response import OkResponse
from criteo_api_marketingsolutions_preview.model.outcome import Outcome
from criteo_api_marketingsolutions_preview.model.preview_fail_response import PreviewFailResponse
from criteo_api_marketingsolutions_preview.model.product_set_statistics_query import ProductSetStatisticsQuery
from criteo_api_marketingsolutions_preview.model.resource_collection_outcome_of_product_set import ResourceCollectionOutcomeOfProductSet
from criteo_api_marketingsolutions_preview.model.resource_outcome_of_product_set import ResourceOutcomeOfProductSet
from criteo_api_marketingsolutions_preview.model.value_resource_input_of_create_product_set_request import ValueResourceInputOfCreateProductSetRequest


class RecoApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_product_set_endpoint = _Endpoint(
            settings={
                'response_type': (ResourceOutcomeOfProductSet,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/product-sets',
                'operation_id': 'create_product_set',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'value_resource_input_of_create_product_set_request',
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
                    'value_resource_input_of_create_product_set_request':
                        (ValueResourceInputOfCreateProductSetRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'value_resource_input_of_create_product_set_request': 'body',
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
        self.fetch_product_set_endpoint = _Endpoint(
            settings={
                'response_type': (ResourceOutcomeOfProductSet,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/product-sets/{product-set-id}',
                'operation_id': 'fetch_product_set',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_set_id',
                ],
                'required': [
                    'product_set_id',
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
                    'product_set_id':
                        (str,),
                },
                'attribute_map': {
                    'product_set_id': 'product-set-id',
                },
                'location_map': {
                    'product_set_id': 'path',
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
            api_client=api_client
        )
        self.fetch_product_sets_endpoint = _Endpoint(
            settings={
                'response_type': (ResourceCollectionOutcomeOfProductSet,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/product-sets/dataset/{dataset-id}',
                'operation_id': 'fetch_product_sets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                ],
                'required': [
                    'dataset_id',
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
                    'dataset_id':
                        (str,),
                },
                'attribute_map': {
                    'dataset_id': 'dataset-id',
                },
                'location_map': {
                    'dataset_id': 'path',
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
            api_client=api_client
        )
        self.preview_product_sets_preview_post_endpoint = _Endpoint(
            settings={
                'response_type': (OkResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/product-sets/preview',
                'operation_id': 'preview_product_sets_preview_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_set_statistics_query',
                ],
                'required': [
                    'product_set_statistics_query',
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
                    'product_set_statistics_query':
                        (ProductSetStatisticsQuery,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'product_set_statistics_query': 'body',
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
        self.remove_product_set_endpoint = _Endpoint(
            settings={
                'response_type': (Outcome,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/product-sets/{product-set-id}',
                'operation_id': 'remove_product_set',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_set_id',
                ],
                'required': [
                    'product_set_id',
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
                    'product_set_id':
                        (str,),
                },
                'attribute_map': {
                    'product_set_id': 'product-set-id',
                },
                'location_map': {
                    'product_set_id': 'path',
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
            api_client=api_client
        )

    def create_product_set(
        self,
        **kwargs
    ):
        """create_product_set  # noqa: E501

        Create a new product set  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_product_set(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            value_resource_input_of_create_product_set_request (ValueResourceInputOfCreateProductSetRequest): [optional]
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
            ResourceOutcomeOfProductSet
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
        return self.create_product_set_endpoint.call_with_http_info(**kwargs)

    def fetch_product_set(
        self,
        product_set_id,
        **kwargs
    ):
        """fetch_product_set  # noqa: E501

        Fetch an existing product set  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_product_set(product_set_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_set_id (str): ID of the product set

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
            ResourceOutcomeOfProductSet
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
        kwargs['product_set_id'] = \
            product_set_id
        return self.fetch_product_set_endpoint.call_with_http_info(**kwargs)

    def fetch_product_sets(
        self,
        dataset_id,
        **kwargs
    ):
        """fetch_product_sets  # noqa: E501

        Fetch product sets of a given dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_product_sets(dataset_id, async_req=True)
        >>> result = thread.get()

        Args:
            dataset_id (str): The ID of the dataset that should be used for product set retrieval

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
            ResourceCollectionOutcomeOfProductSet
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
        kwargs['dataset_id'] = \
            dataset_id
        return self.fetch_product_sets_endpoint.call_with_http_info(**kwargs)

    def preview_product_sets_preview_post(
        self,
        product_set_statistics_query,
        **kwargs
    ):
        """preview_product_sets_preview_post  # noqa: E501

        Display a preview of product set rules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.preview_product_sets_preview_post(product_set_statistics_query, async_req=True)
        >>> result = thread.get()

        Args:
            product_set_statistics_query (ProductSetStatisticsQuery):

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
            OkResponse
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
        kwargs['product_set_statistics_query'] = \
            product_set_statistics_query
        return self.preview_product_sets_preview_post_endpoint.call_with_http_info(**kwargs)

    def remove_product_set(
        self,
        product_set_id,
        **kwargs
    ):
        """remove_product_set  # noqa: E501

        Remove a product set  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_product_set(product_set_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_set_id (str): ID of the product set to remove

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
            Outcome
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
        kwargs['product_set_id'] = \
            product_set_id
        return self.remove_product_set_endpoint.call_with_http_info(**kwargs)

