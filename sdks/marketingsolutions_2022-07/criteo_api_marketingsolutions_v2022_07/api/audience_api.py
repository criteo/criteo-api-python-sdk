"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

    The version of the OpenAPI document: 2022-07
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_v2022_07.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_marketingsolutions_v2022_07.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_marketingsolutions_v2022_07.model.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_api_marketingsolutions_v2022_07.model.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_api_marketingsolutions_v2022_07.model.delete_audience_response import DeleteAudienceResponse
from criteo_api_marketingsolutions_v2022_07.model.error_code_response import ErrorCodeResponse
from criteo_api_marketingsolutions_v2022_07.model.get_audiences_response import GetAudiencesResponse
from criteo_api_marketingsolutions_v2022_07.model.modify_audience_response import ModifyAudienceResponse
from criteo_api_marketingsolutions_v2022_07.model.new_audience_request import NewAudienceRequest
from criteo_api_marketingsolutions_v2022_07.model.new_audience_response import NewAudienceResponse
from criteo_api_marketingsolutions_v2022_07.model.replace_audience_request import ReplaceAudienceRequest
from criteo_api_marketingsolutions_v2022_07.model.replace_audience_response import ReplaceAudienceResponse


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
                'response_type': (NewAudienceResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/audiences',
                'operation_id': 'create_audience',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'new_audience_request',
                ],
                'required': [
                    'new_audience_request',
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
                    'new_audience_request':
                        (NewAudienceRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'new_audience_request': 'body',
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
        self.delete_identifiers_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteAudienceContactListResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/audiences/{audience-id}/contactlist',
                'operation_id': 'delete_identifiers',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'audience_id',
                ],
                'required': [
                    'audience_id',
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
                    'audience_id':
                        (str,),
                },
                'attribute_map': {
                    'audience_id': 'audience-id',
                },
                'location_map': {
                    'audience_id': 'path',
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
        self.get_audiences_endpoint = _Endpoint(
            settings={
                'response_type': (GetAudiencesResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/audiences',
                'operation_id': 'get_audiences',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'advertiser_id',
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
                    'advertiser_id':
                        (str,),
                },
                'attribute_map': {
                    'advertiser_id': 'advertiser-id',
                },
                'location_map': {
                    'advertiser_id': 'query',
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
        self.modify_audience_endpoint = _Endpoint(
            settings={
                'response_type': (ReplaceAudienceResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/audiences/{audience-id}',
                'operation_id': 'modify_audience',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'audience_id',
                    'replace_audience_request',
                ],
                'required': [
                    'audience_id',
                    'replace_audience_request',
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
                    'audience_id':
                        (str,),
                    'replace_audience_request':
                        (ReplaceAudienceRequest,),
                },
                'attribute_map': {
                    'audience_id': 'audience-id',
                },
                'location_map': {
                    'audience_id': 'path',
                    'replace_audience_request': 'body',
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
        self.modify_audience_users_endpoint = _Endpoint(
            settings={
                'response_type': (ModifyAudienceResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/audiences/{audience-id}/contactlist',
                'operation_id': 'modify_audience_users',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'audience_id',
                    'contactlist_amendment_request',
                ],
                'required': [
                    'audience_id',
                    'contactlist_amendment_request',
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
                    'audience_id':
                        (str,),
                    'contactlist_amendment_request':
                        (ContactlistAmendmentRequest,),
                },
                'attribute_map': {
                    'audience_id': 'audience-id',
                },
                'location_map': {
                    'audience_id': 'path',
                    'contactlist_amendment_request': 'body',
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
        self.remove_audience_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteAudienceResponse,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/2022-07/audiences/{audience-id}',
                'operation_id': 'remove_audience',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'audience_id',
                ],
                'required': [
                    'audience_id',
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
                    'audience_id':
                        (str,),
                },
                'attribute_map': {
                    'audience_id': 'audience-id',
                },
                'location_map': {
                    'audience_id': 'path',
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

    def create_audience(
        self,
        new_audience_request,
        **kwargs
    ):
        """create_audience  # noqa: E501

        Create an Audience for an Advertiser  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_audience(new_audience_request, async_req=True)
        >>> result = thread.get()

        Args:
            new_audience_request (NewAudienceRequest):

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
            NewAudienceResponse
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
        kwargs['new_audience_request'] = \
            new_audience_request
        return self.create_audience_endpoint.call_with_http_info(**kwargs)

    def delete_identifiers(
        self,
        audience_id,
        **kwargs
    ):
        """delete_identifiers  # noqa: E501

        delete all identifiers from an Audience  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_identifiers(audience_id, async_req=True)
        >>> result = thread.get()

        Args:
            audience_id (str): The id of the audience to amend

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
            DeleteAudienceContactListResponse
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
        kwargs['audience_id'] = \
            audience_id
        return self.delete_identifiers_endpoint.call_with_http_info(**kwargs)

    def get_audiences(
        self,
        **kwargs
    ):
        """get_audiences  # noqa: E501

        Get a list of all the audiences for the user or for the given advertiser_id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_audiences(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            advertiser_id (str): The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don't provide it, we will take into account the advertisers from your portfolio. [optional]
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
            GetAudiencesResponse
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
        return self.get_audiences_endpoint.call_with_http_info(**kwargs)

    def modify_audience(
        self,
        audience_id,
        replace_audience_request,
        **kwargs
    ):
        """modify_audience  # noqa: E501

        Update user audience specified by the audience id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_audience(audience_id, replace_audience_request, async_req=True)
        >>> result = thread.get()

        Args:
            audience_id (str): The id of the audience to amend
            replace_audience_request (ReplaceAudienceRequest):

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
            ReplaceAudienceResponse
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
        kwargs['audience_id'] = \
            audience_id
        kwargs['replace_audience_request'] = \
            replace_audience_request
        return self.modify_audience_endpoint.call_with_http_info(**kwargs)

    def modify_audience_users(
        self,
        audience_id,
        contactlist_amendment_request,
        **kwargs
    ):
        """modify_audience_users  # noqa: E501

        Add/remove users to or from an audience  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_audience_users(audience_id, contactlist_amendment_request, async_req=True)
        >>> result = thread.get()

        Args:
            audience_id (str): The id of the audience to amend
            contactlist_amendment_request (ContactlistAmendmentRequest):

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
            ModifyAudienceResponse
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
        kwargs['audience_id'] = \
            audience_id
        kwargs['contactlist_amendment_request'] = \
            contactlist_amendment_request
        return self.modify_audience_users_endpoint.call_with_http_info(**kwargs)

    def remove_audience(
        self,
        audience_id,
        **kwargs
    ):
        """remove_audience  # noqa: E501

        Delete an audience by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_audience(audience_id, async_req=True)
        >>> result = thread.get()

        Args:
            audience_id (str): The id of the audience to amend

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
            DeleteAudienceResponse
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
        kwargs['audience_id'] = \
            audience_id
        return self.remove_audience_endpoint.call_with_http_info(**kwargs)

