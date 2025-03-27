"""
    Criteo API

    Criteo API - RetailMedia  # noqa: E501

    The version of the OpenAPI document: Preview
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_retailmedia_preview.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from criteo_api_retailmedia_preview.exceptions import ApiAttributeError



class LineItemKeywordReviewReport(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = True

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'line_item_id': (str,),  # noqa: E501
            'line_item_name': (str,),  # noqa: E501
            'retailer_id': (str,),  # noqa: E501
            'retailer_name': (str,),  # noqa: E501
            'campaign_id': (str,),  # noqa: E501
            'campaign_name': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'account_name': (str,),  # noqa: E501
            'count_keywords': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'line_item_id': 'lineItemId',  # noqa: E501
        'line_item_name': 'lineItemName',  # noqa: E501
        'retailer_id': 'retailerId',  # noqa: E501
        'retailer_name': 'retailerName',  # noqa: E501
        'campaign_id': 'campaignId',  # noqa: E501
        'campaign_name': 'campaignName',  # noqa: E501
        'account_id': 'accountId',  # noqa: E501
        'account_name': 'accountName',  # noqa: E501
        'count_keywords': 'countKeywords',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, line_item_id, line_item_name, retailer_id, retailer_name, campaign_id, campaign_name, account_id, account_name, count_keywords, *args, **kwargs):  # noqa: E501
        """LineItemKeywordReviewReport - a model defined in OpenAPI

        Args:
            line_item_id (str): External ID of the line item that this report is for
            line_item_name (str): Name of the line item that this report is for
            retailer_id (str): Retailer ID connected to the line item this report is for
            retailer_name (str): Name of the retailer connected to the line item this report is for
            campaign_id (str): External ID of the campaign containing the line item this report is for
            campaign_name (str): Name of the campaign containing the line item this report is for
            account_id (str): External ID of the account containing the campaign containing the line item this report is for
            account_name (str): Name of the account containing the campaign containing the line item this report is for
            count_keywords (int): Number of PositiveExactMatch keywords on this line item that are in either \"InReview\" or \"Pending\" state

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.line_item_id = line_item_id
        self.line_item_name = line_item_name
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.account_id = account_id
        self.account_name = account_name
        self.count_keywords = count_keywords
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, line_item_id, line_item_name, retailer_id, retailer_name, campaign_id, campaign_name, account_id, account_name, count_keywords, *args, **kwargs):  # noqa: E501
        """LineItemKeywordReviewReport - a model defined in OpenAPI

        Args:
            line_item_id (str): External ID of the line item that this report is for
            line_item_name (str): Name of the line item that this report is for
            retailer_id (str): Retailer ID connected to the line item this report is for
            retailer_name (str): Name of the retailer connected to the line item this report is for
            campaign_id (str): External ID of the campaign containing the line item this report is for
            campaign_name (str): Name of the campaign containing the line item this report is for
            account_id (str): External ID of the account containing the campaign containing the line item this report is for
            account_name (str): Name of the account containing the campaign containing the line item this report is for
            count_keywords (int): Number of PositiveExactMatch keywords on this line item that are in either \"InReview\" or \"Pending\" state

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.line_item_id = line_item_id
        self.line_item_name = line_item_name
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.account_id = account_id
        self.account_name = account_name
        self.count_keywords = count_keywords
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
