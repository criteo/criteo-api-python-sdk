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
from criteo_api_retailmedia_preview.model.batch_accepted_response import BatchAcceptedResponse
from criteo_api_retailmedia_preview.model.entity_resource_collection_outcome_brand_id_search_result import EntityResourceCollectionOutcomeBrandIdSearchResult
from criteo_api_retailmedia_preview.model.fail_response import FailResponse
from criteo_api_retailmedia_preview.model.products_custom_batch_request import ProductsCustomBatchRequest
from criteo_api_retailmedia_preview.model.report_ok_response import ReportOkResponse
from criteo_api_retailmedia_preview.model.value_resource_input_brand_id_search_request import ValueResourceInputBrandIdSearchRequest


class CatalogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.preview_retail_media_catalog_products_batch_post_endpoint = _Endpoint(
            settings={
                'response_type': (BatchAcceptedResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/retail-media/catalog/products/batch',
                'operation_id': 'preview_retail_media_catalog_products_batch_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'products_custom_batch_request',
                ],
                'required': [
                    'products_custom_batch_request',
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
                    'products_custom_batch_request':
                        (ProductsCustomBatchRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'products_custom_batch_request': 'body',
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
        self.preview_retail_media_catalog_products_batch_report_operation_token_get_endpoint = _Endpoint(
            settings={
                'response_type': (ReportOkResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/retail-media/catalog/products/batch/report/{operation-token}',
                'operation_id': 'preview_retail_media_catalog_products_batch_report_operation_token_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'operation_token',
                ],
                'required': [
                    'operation_token',
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
                    'operation_token':
                        (str,),
                },
                'attribute_map': {
                    'operation_token': 'operation-token',
                },
                'location_map': {
                    'operation_token': 'path',
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
        self.search_brands_by_name_async_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EntityResourceCollectionOutcomeBrandIdSearchResult,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/preview/retail-media/brands/search',
                'operation_id': 'search_brands_by_name_async_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'value_resource_input_brand_id_search_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'offset',
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('offset',): {

                        'inclusive_maximum': 2147483647,
                        'inclusive_minimum': 0,
                    },
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'value_resource_input_brand_id_search_request':
                        (ValueResourceInputBrandIdSearchRequest,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'value_resource_input_brand_id_search_request': 'body',
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

    def preview_retail_media_catalog_products_batch_post(
        self,
        products_custom_batch_request,
        **kwargs
    ):
        """preview_retail_media_catalog_products_batch_post  # noqa: E501

        Used to publish a batch of operations to insert, update and deletes products.  The batch is processed asynchronously.The response provides an operationToken which can be used to track  the status of the report of the operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.preview_retail_media_catalog_products_batch_post(products_custom_batch_request, async_req=True)
        >>> result = thread.get()

        Args:
            products_custom_batch_request (ProductsCustomBatchRequest):

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
            BatchAcceptedResponse
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
        kwargs['products_custom_batch_request'] = \
            products_custom_batch_request
        return self.preview_retail_media_catalog_products_batch_post_endpoint.call_with_http_info(**kwargs)

    def preview_retail_media_catalog_products_batch_report_operation_token_get(
        self,
        operation_token,
        **kwargs
    ):
        """preview_retail_media_catalog_products_batch_report_operation_token_get  # noqa: E501

        Get the report of an asynchronous batch operation previously requested  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.preview_retail_media_catalog_products_batch_report_operation_token_get(operation_token, async_req=True)
        >>> result = thread.get()

        Args:
            operation_token (str): The token returned by the batch endpoint.

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
            ReportOkResponse
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
        kwargs['operation_token'] = \
            operation_token
        return self.preview_retail_media_catalog_products_batch_report_operation_token_get_endpoint.call_with_http_info(**kwargs)

    def search_brands_by_name_async_v1(
        self,
        **kwargs
    ):
        """search_brands_by_name_async_v1  # noqa: E501

        Search for brands given a retailer ID and search term.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_brands_by_name_async_v1(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            offset (int): offset of paginated results. [optional] if omitted the server will use the default value of 0
            limit (int): the number of brands to return. [optional] if omitted the server will use the default value of 25
            value_resource_input_brand_id_search_request (ValueResourceInputBrandIdSearchRequest): BrandIdSearchRequest which contains the request parameters. [optional]
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
            EntityResourceCollectionOutcomeBrandIdSearchResult
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
        return self.search_brands_by_name_async_v1_endpoint.call_with_http_info(**kwargs)

