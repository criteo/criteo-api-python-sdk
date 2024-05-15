"""
    Criteo API

    Criteo API - MarketingSolutions  # noqa: E501

    The version of the OpenAPI document: 2024-04
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_v2024_04.model_utils import (  # noqa: F401
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
from criteo_api_marketingsolutions_v2024_04.exceptions import ApiAttributeError


def lazy_import():
    from criteo_api_marketingsolutions_v2024_04.model.adaptive_colors import AdaptiveColors
    from criteo_api_marketingsolutions_v2024_04.model.image_set_base64 import ImageSetBase64
    globals()['AdaptiveColors'] = AdaptiveColors
    globals()['ImageSetBase64'] = ImageSetBase64


class AdaptiveWriteAttributes(ModelNormal):
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
        ('layouts',): {
            'EDITORIAL': "Editorial",
            'MONTAGE': "Montage",
            'INBANNERVIDEO': "InBannerVideo",
        },
        ('image_display',): {
            'None': None,
            'SHOWFULLIMAGE': "ShowFullImage",
            'ZOOMONIMAGE': "ZoomOnImage",
        },
    }

    validations = {
        ('layouts',): {
            'min_items': 1,
        },
        ('calls_to_action',): {
            'min_items': 1,
        },
        ('image_sets_base64',): {
        },
        ('video_base64_strings',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
        lazy_import()
        return {
            'layouts': ([str],),  # noqa: E501
            'logo_base64_string': (str,),  # noqa: E501
            'headline_text': (str,),  # noqa: E501
            'headline_font': (str,),  # noqa: E501
            'description_text': (str,),  # noqa: E501
            'description_font': (str,),  # noqa: E501
            'calls_to_action': ([str],),  # noqa: E501
            'colors': (AdaptiveColors,),  # noqa: E501
            'landing_page_url': (str,),  # noqa: E501
            'image_sets_base64': ([ImageSetBase64], none_type,),  # noqa: E501
            'image_display': (str, none_type,),  # noqa: E501
            'video_base64_strings': ([str], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'layouts': 'layouts',  # noqa: E501
        'logo_base64_string': 'logoBase64String',  # noqa: E501
        'headline_text': 'headlineText',  # noqa: E501
        'headline_font': 'headlineFont',  # noqa: E501
        'description_text': 'descriptionText',  # noqa: E501
        'description_font': 'descriptionFont',  # noqa: E501
        'calls_to_action': 'callsToAction',  # noqa: E501
        'colors': 'colors',  # noqa: E501
        'landing_page_url': 'landingPageUrl',  # noqa: E501
        'image_sets_base64': 'imageSetsBase64',  # noqa: E501
        'image_display': 'imageDisplay',  # noqa: E501
        'video_base64_strings': 'videoBase64Strings',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, layouts, logo_base64_string, headline_text, headline_font, description_text, description_font, calls_to_action, colors, landing_page_url, *args, **kwargs):  # noqa: E501
        """AdaptiveWriteAttributes - a model defined in OpenAPI

        Args:
            layouts ([str]): The Adaptive layouts that are enabled.  It can contain any of the following values: \"Editorial\", “Montage“, \"InBannerVideo\".
            logo_base64_string (str): Logo image as a base-64 encoded string
            headline_text (str): The headline text of the banner
            headline_font (str): Font of the headline  Valid supported font like \"Arial\"
            description_text (str): The description text of the banner
            description_font (str): Font of the description  Valid supported font like \"Arial\"
            calls_to_action ([str]): A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”.
            colors (AdaptiveColors):
            landing_page_url (str): Web redirection of the landing page url.

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
            image_sets_base64 ([ImageSetBase64], none_type): Multiple image sets, each image set consists of multiple images as a base-64 encoded string and a headline text.. [optional]  # noqa: E501
            image_display (str, none_type): Value can be \"ShowFullImage\" or \"ZoomOnImage\". Choose whether your image set should fit inside the allocated  space (\"ShowFullImage\") or whether it should fill that space (\"ZoomOnImage\"). If you choose ZoomOnImage, there may be some  image cropping.. [optional]  # noqa: E501
            video_base64_strings ([str], none_type): Multiple videos potentially in different shapes, each video is a base-64 encoded string.. [optional]  # noqa: E501
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

        self.layouts = layouts
        self.logo_base64_string = logo_base64_string
        self.headline_text = headline_text
        self.headline_font = headline_font
        self.description_text = description_text
        self.description_font = description_font
        self.calls_to_action = calls_to_action
        self.colors = colors
        self.landing_page_url = landing_page_url
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
    def __init__(self, layouts, logo_base64_string, headline_text, headline_font, description_text, description_font, calls_to_action, colors, landing_page_url, *args, **kwargs):  # noqa: E501
        """AdaptiveWriteAttributes - a model defined in OpenAPI

        Args:
            layouts ([str]): The Adaptive layouts that are enabled.  It can contain any of the following values: \"Editorial\", “Montage“, \"InBannerVideo\".
            logo_base64_string (str): Logo image as a base-64 encoded string
            headline_text (str): The headline text of the banner
            headline_font (str): Font of the headline  Valid supported font like \"Arial\"
            description_text (str): The description text of the banner
            description_font (str): Font of the description  Valid supported font like \"Arial\"
            calls_to_action ([str]): A Call-to-Action (CTA) is an action-driven instruction to your audience intended to provoke an immediate  response, such as “Buy now” or “Go!”.
            colors (AdaptiveColors):
            landing_page_url (str): Web redirection of the landing page url.

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
            image_sets_base64 ([ImageSetBase64], none_type): Multiple image sets, each image set consists of multiple images as a base-64 encoded string and a headline text.. [optional]  # noqa: E501
            image_display (str, none_type): Value can be \"ShowFullImage\" or \"ZoomOnImage\". Choose whether your image set should fit inside the allocated  space (\"ShowFullImage\") or whether it should fill that space (\"ZoomOnImage\"). If you choose ZoomOnImage, there may be some  image cropping.. [optional]  # noqa: E501
            video_base64_strings ([str], none_type): Multiple videos potentially in different shapes, each video is a base-64 encoded string.. [optional]  # noqa: E501
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

        self.layouts = layouts
        self.logo_base64_string = logo_base64_string
        self.headline_text = headline_text
        self.headline_font = headline_font
        self.description_text = description_text
        self.description_font = description_font
        self.calls_to_action = calls_to_action
        self.colors = colors
        self.landing_page_url = landing_page_url
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
