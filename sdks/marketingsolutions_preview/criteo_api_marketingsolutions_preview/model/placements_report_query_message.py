"""
    Criteo API

    Criteo API - MarketingSolutions  # noqa: E501

    The version of the OpenAPI document: Preview
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_preview.model_utils import (  # noqa: F401
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
from criteo_api_marketingsolutions_preview.exceptions import ApiAttributeError



class PlacementsReportQueryMessage(ModelNormal):
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
        ('dimensions',): {
            'ADSETID': "AdsetId",
            'ADVERTISERID': "AdvertiserId",
            'PLACEMENT': "Placement",
            'ENVIRONMENT': "Environment",
            'ADSETNAME': "AdsetName",
            'ADVERTISERNAME': "AdvertiserName",
            'CAMPAIGNID': "CampaignId",
            'CAMPAIGNNAME': "CampaignName",
            'ADCHANNEL': "AdChannel",
            'SOCIALPLATFORM': "SocialPlatform",
            'CATEGORYID': "CategoryId",
            'CATEGORYNAME': "CategoryName",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

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
            'advertiser_ids': (str,),  # noqa: E501
            'dimensions': ([str],),  # noqa: E501
            'metrics': ([str],),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'format': (str,),  # noqa: E501
            'start_date': (datetime,),  # noqa: E501
            'end_date': (datetime,),  # noqa: E501
            'campaign_ids': (str, none_type,),  # noqa: E501
            'adset_ids': (str, none_type,),  # noqa: E501
            'environment': (str, none_type,),  # noqa: E501
            'placement': (str, none_type,),  # noqa: E501
            'disclosed': (bool,),  # noqa: E501
            'timezone': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'advertiser_ids': 'advertiserIds',  # noqa: E501
        'dimensions': 'dimensions',  # noqa: E501
        'metrics': 'metrics',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'format': 'format',  # noqa: E501
        'start_date': 'startDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'campaign_ids': 'campaignIds',  # noqa: E501
        'adset_ids': 'adsetIds',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'placement': 'placement',  # noqa: E501
        'disclosed': 'disclosed',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, advertiser_ids, dimensions, metrics, currency, format, start_date, end_date, *args, **kwargs):  # noqa: E501
        """PlacementsReportQueryMessage - a model defined in OpenAPI

        Args:
            advertiser_ids (str): The comma-separated list of advertiser ids.
            dimensions ([str]): The dimensions for the report.
            metrics ([str]): The list of metrics to report.
            currency (str): The currency used for the report. ISO 4217 code (three-letter capitals).
            format (str): The file format of the generated report: csv, xml, excel or json.
            start_date (datetime): Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.
            end_date (datetime): End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.

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
            campaign_ids (str, none_type): The comma-separated list of campaign ids.. [optional]  # noqa: E501
            adset_ids (str, none_type): The comma-separated list of adSet ids.. [optional]  # noqa: E501
            environment (str, none_type): Type of environment: Web, Android or iOS.. [optional]  # noqa: E501
            placement (str, none_type): Filter the value of the placement. [optional]  # noqa: E501
            disclosed (bool): Returns disclosed or undisclosed placements.. [optional] if omitted the server will use the default value of True  # noqa: E501
            timezone (str, none_type): The timezone used for the report. Timezone Database format (Tz).. [optional] if omitted the server will use the default value of "UTC"  # noqa: E501
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

        self.advertiser_ids = advertiser_ids
        self.dimensions = dimensions
        self.metrics = metrics
        self.currency = currency
        self.format = format
        self.start_date = start_date
        self.end_date = end_date
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
    def __init__(self, advertiser_ids, dimensions, metrics, currency, format, start_date, end_date, *args, **kwargs):  # noqa: E501
        """PlacementsReportQueryMessage - a model defined in OpenAPI

        Args:
            advertiser_ids (str): The comma-separated list of advertiser ids.
            dimensions ([str]): The dimensions for the report.
            metrics ([str]): The list of metrics to report.
            currency (str): The currency used for the report. ISO 4217 code (three-letter capitals).
            format (str): The file format of the generated report: csv, xml, excel or json.
            start_date (datetime): Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.
            end_date (datetime): End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.

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
            campaign_ids (str, none_type): The comma-separated list of campaign ids.. [optional]  # noqa: E501
            adset_ids (str, none_type): The comma-separated list of adSet ids.. [optional]  # noqa: E501
            environment (str, none_type): Type of environment: Web, Android or iOS.. [optional]  # noqa: E501
            placement (str, none_type): Filter the value of the placement. [optional]  # noqa: E501
            disclosed (bool): Returns disclosed or undisclosed placements.. [optional] if omitted the server will use the default value of True  # noqa: E501
            timezone (str, none_type): The timezone used for the report. Timezone Database format (Tz).. [optional] if omitted the server will use the default value of "UTC"  # noqa: E501
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

        self.advertiser_ids = advertiser_ids
        self.dimensions = dimensions
        self.metrics = metrics
        self.currency = currency
        self.format = format
        self.start_date = start_date
        self.end_date = end_date
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
