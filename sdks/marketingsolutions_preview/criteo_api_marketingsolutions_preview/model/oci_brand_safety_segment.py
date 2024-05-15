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



class OciBrandSafetySegment(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'ADULT': "gv_adult",
            'ARMS': "gv_arms",
            'CRIME': "gv_crime",
            'DEATH_INJURY': "gv_death_injury",
            'DOWNLOAD': "gv_download",
            'DRUGS': "gv_drugs",
            'HATESPEECH': "gv_hatespeech",
            'MILITARY': "gv_military",
            'OBSCENITY': "gv_obscenity",
            'TERRORISM': "gv_terrorism",
            'TOBACCO': "gv_tobacco",
            'SAFE_ADULT': "gv_safe_adult",
            'SAFE_ARMS': "gv_safe_arms",
            'SAFE_CRIME': "gv_safe_crime",
            'SAFE_DEATH_INJURY': "gv_safe_death_injury",
            'SAFE_DOWNLOAD': "gv_safe_download",
            'SAFE_DRUGS': "gv_safe_drugs",
            'SAFE_HATESPEECH': "gv_safe_hatespeech",
            'SAFE_MILITARY': "gv_safe_military",
            'SAFE_OBSCENITY': "gv_safe_obscenity",
            'SAFE_TERRORISM': "gv_safe_terrorism",
            'SAFE_TOBACCO': "gv_safe_tobacco",
            'CRIME_OTHER': "gv_crime_other",
            'CRIME_SERIOUS': "gv_crime_serious",
            'CRIME_SEX': "gv_crime_sex",
            'CRIME_VIOLENT': "gv_crime_violent",
            'DEATH_INJURY_AIR': "gv_death_injury_air",
            'DEATH_INJURY_FIRE': "gv_death_injury_fire",
            'DEATH_INJURY_MISC': "gv_death_injury_misc",
            'DEATH_INJURY_RAIL': "gv_death_injury_rail",
            'DEATH_INJURY_ROAD': "gv_death_injury_road",
            'DEATH_INJURY_SEA': "gv_death_injury_sea",
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
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """OciBrandSafetySegment - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Represents Oci standard brand-safety segment.., must be one of ["gv_adult", "gv_arms", "gv_crime", "gv_death_injury", "gv_download", "gv_drugs", "gv_hatespeech", "gv_military", "gv_obscenity", "gv_terrorism", "gv_tobacco", "gv_safe_adult", "gv_safe_arms", "gv_safe_crime", "gv_safe_death_injury", "gv_safe_download", "gv_safe_drugs", "gv_safe_hatespeech", "gv_safe_military", "gv_safe_obscenity", "gv_safe_terrorism", "gv_safe_tobacco", "gv_crime_other", "gv_crime_serious", "gv_crime_sex", "gv_crime_violent", "gv_death_injury_air", "gv_death_injury_fire", "gv_death_injury_misc", "gv_death_injury_rail", "gv_death_injury_road", "gv_death_injury_sea", ]  # noqa: E501

        Keyword Args:
            value (str): Represents Oci standard brand-safety segment.., must be one of ["gv_adult", "gv_arms", "gv_crime", "gv_death_injury", "gv_download", "gv_drugs", "gv_hatespeech", "gv_military", "gv_obscenity", "gv_terrorism", "gv_tobacco", "gv_safe_adult", "gv_safe_arms", "gv_safe_crime", "gv_safe_death_injury", "gv_safe_download", "gv_safe_drugs", "gv_safe_hatespeech", "gv_safe_military", "gv_safe_obscenity", "gv_safe_terrorism", "gv_safe_tobacco", "gv_crime_other", "gv_crime_serious", "gv_crime_sex", "gv_crime_violent", "gv_death_injury_air", "gv_death_injury_fire", "gv_death_injury_misc", "gv_death_injury_rail", "gv_death_injury_road", "gv_death_injury_sea", ]  # noqa: E501
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
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """OciBrandSafetySegment - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Represents Oci standard brand-safety segment.., must be one of ["gv_adult", "gv_arms", "gv_crime", "gv_death_injury", "gv_download", "gv_drugs", "gv_hatespeech", "gv_military", "gv_obscenity", "gv_terrorism", "gv_tobacco", "gv_safe_adult", "gv_safe_arms", "gv_safe_crime", "gv_safe_death_injury", "gv_safe_download", "gv_safe_drugs", "gv_safe_hatespeech", "gv_safe_military", "gv_safe_obscenity", "gv_safe_terrorism", "gv_safe_tobacco", "gv_crime_other", "gv_crime_serious", "gv_crime_sex", "gv_crime_violent", "gv_death_injury_air", "gv_death_injury_fire", "gv_death_injury_misc", "gv_death_injury_rail", "gv_death_injury_road", "gv_death_injury_sea", ]  # noqa: E501

        Keyword Args:
            value (str): Represents Oci standard brand-safety segment.., must be one of ["gv_adult", "gv_arms", "gv_crime", "gv_death_injury", "gv_download", "gv_drugs", "gv_hatespeech", "gv_military", "gv_obscenity", "gv_terrorism", "gv_tobacco", "gv_safe_adult", "gv_safe_arms", "gv_safe_crime", "gv_safe_death_injury", "gv_safe_download", "gv_safe_drugs", "gv_safe_hatespeech", "gv_safe_military", "gv_safe_obscenity", "gv_safe_terrorism", "gv_safe_tobacco", "gv_crime_other", "gv_crime_serious", "gv_crime_sex", "gv_crime_violent", "gv_death_injury_air", "gv_death_injury_fire", "gv_death_injury_misc", "gv_death_injury_rail", "gv_death_injury_road", "gv_death_injury_sea", ]  # noqa: E501
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
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
