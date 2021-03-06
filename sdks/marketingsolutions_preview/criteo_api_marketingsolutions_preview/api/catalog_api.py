"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

    The version of the OpenAPI document: Preview
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
from criteo_api_marketingsolutions_preview.model.batch_accepted_response import BatchAcceptedResponse
from criteo_api_marketingsolutions_preview.model.fail_response import FailResponse
from criteo_api_marketingsolutions_preview.model.products_custom_batch_request import ProductsCustomBatchRequest
from criteo_api_marketingsolutions_preview.model.report_ok_response import ReportOkResponse


class CatalogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __preview_catalog_products_batch_post(
            self,
            products_custom_batch_request,
            **kwargs
        ):
            """preview_catalog_products_batch_post  # noqa: E501

            Used to publish a batch of operations to insert, update and deletes products.  The batch is processed asynchronously.The response provides an operationToken which can be used to track  the status of the report of the operation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.preview_catalog_products_batch_post(products_custom_batch_request, async_req=True)
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
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['products_custom_batch_request'] = \
                products_custom_batch_request
            return self.call_with_http_info(**kwargs)

        self.preview_catalog_products_batch_post = _Endpoint(
            settings={
                'response_type': (BatchAcceptedResponse,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/preview/catalog/products/batch',
                'operation_id': 'preview_catalog_products_batch_post',
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
            api_client=api_client,
            callable=__preview_catalog_products_batch_post
        )

        def __preview_catalog_products_batch_report_operation_token_get(
            self,
            operation_token,
            **kwargs
        ):
            """preview_catalog_products_batch_report_operation_token_get  # noqa: E501

            Get the report of an asynchronous batch operation previously requested  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.preview_catalog_products_batch_report_operation_token_get(operation_token, async_req=True)
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
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['operation_token'] = \
                operation_token
            return self.call_with_http_info(**kwargs)

        self.preview_catalog_products_batch_report_operation_token_get = _Endpoint(
            settings={
                'response_type': (ReportOkResponse,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/preview/catalog/products/batch/report/{operation-token}',
                'operation_id': 'preview_catalog_products_batch_report_operation_token_get',
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
            api_client=api_client,
            callable=__preview_catalog_products_batch_report_operation_token_get
        )
