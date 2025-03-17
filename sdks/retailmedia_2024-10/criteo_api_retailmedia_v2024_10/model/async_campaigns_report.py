"""
    Criteo API

    Criteo API - RetailMedia  # noqa: E501

    The version of the OpenAPI document: 2024-10
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_retailmedia_v2024_10.model_utils import (  # noqa: F401
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
from criteo_api_retailmedia_v2024_10.exceptions import ApiAttributeError



class AsyncCampaignsReport(ModelNormal):
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
        ('search_term_types',): {
            'UNKNOWN': "unknown",
            'SEARCHED': "searched",
            'ENTERED': "entered",
        },
        ('search_term_targetings',): {
            'UNKNOWN': "unknown",
            'AUTOMATIC': "automatic",
            'MANUAL': "manual",
        },
        ('campaign_type',): {
            'ALL': "all",
            'SPONSOREDPRODUCTS': "sponsoredProducts",
            'ONSITEDISPLAYS': "onSiteDisplays",
        },
        ('sales_channel',): {
            'ALL': "all",
            'OFFLINE': "offline",
            'ONLINE': "online",
        },
        ('format',): {
            'JSON': "json",
            'JSON-COMPACT': "json-compact",
            'JSON-NEWLINE': "json-newline",
            'CSV': "csv",
        },
        ('report_type',): {
            'SUMMARY': "summary",
            'PAGETYPE': "pageType",
            'KEYWORD': "keyword",
            'PRODUCTCATEGORY': "productCategory",
            'PRODUCT': "product",
            'ATTRIBUTEDTRANSACTIONS': "attributedTransactions",
            'ENVIRONMENT': "environment",
            'SERVEDCATEGORY': "servedCategory",
            'CAPOUT': "capout",
        },
        ('click_attribution_window',): {
            'NONE': "none",
            '7D': "7D",
            '14D': "14D",
            '30D': "30D",
        },
        ('view_attribution_window',): {
            'NONE': "none",
            '1D': "1D",
            '7D': "7D",
            '14D': "14D",
            '30D': "30D",
        },
        ('dimensions',): {
            'DATE': "date",
            'HOUR': "hour",
            'ACCOUNTID': "accountId",
            'ACCOUNTNAME': "accountName",
            'CAMPAIGNID': "campaignId",
            'CAMPAIGNNAME': "campaignName",
            'CAMPAIGNTYPENAME': "campaignTypeName",
            'LINEITEMID': "lineItemId",
            'LINEITEMNAME': "lineItemName",
            'RETAILERID': "retailerId",
            'RETAILERNAME': "retailerName",
            'BRANDID': "brandId",
            'BRANDNAME': "brandName",
            'ADVPRODUCTCATEGORY': "advProductCategory",
            'ADVPRODUCTID': "advProductId",
            'ADVPRODUCTNAME': "advProductName",
            'SALESCHANNEL': "salesChannel",
            'ENVIRONMENT': "environment",
            'PAGETYPENAME': "pageTypeName",
            'PAGECATEGORY': "pageCategory",
            'SERVEDCATEGORY': "servedCategory",
            'TAXONOMYBREADCRUMB': "taxonomyBreadcrumb",
            'KEYWORD': "keyword",
            'SEARCHTERM': "searchTerm",
            'SEARCHTERMTYPE': "searchTermType",
            'SEARCHTERMTARGETING': "searchTermTargeting",
            'CREATIVEID': "creativeId",
            'CREATIVENAME': "creativeName",
            'CREATIVETYPEID': "creativeTypeId",
            'CREATIVETYPENAME': "creativeTypeName",
            'CREATIVETEMPLATEID': "creativeTemplateId",
            'CREATIVETEMPLATENAME': "creativeTemplateName",
        },
        ('metrics',): {
            'IMPRESSIONS': "impressions",
            'CLICKS': "clicks",
            'SPEND': "spend",
            'ATTRIBUTEDSALES': "attributedSales",
            'ATTRIBUTEDUNITS': "attributedUnits",
            'ATTRIBUTEDORDERS': "attributedOrders",
            'ASSISTEDSALES': "assistedSales",
            'ASSISTEDUNITS': "assistedUnits",
            'CTR': "ctr",
            'CPC': "cpc",
            'CPO': "cpo",
            'CPM': "cpm",
            'ROAS': "roas",
            'VIDEOVIEWS': "videoViews",
            'VIDEOSSTARTED': "videosStarted",
            'VIDEOSPLAYEDTO25': "videosPlayedTo25",
            'VIDEOSPLAYEDTO50': "videosPlayedTo50",
            'VIDEOSPLAYEDTO75': "videosPlayedTo75",
            'VIDEOSPLAYEDTO100': "videosPlayedTo100",
            'VIDEOPLAYINGRATE': "videoPlayingRate",
            'VIDEOCOMPLETIONRATE': "videoCompletionRate",
            'VIDEOIMPRESSIONS': "videoImpressions",
            'VIDEOMUTED': "videoMuted",
            'VIDEOUNMUTED': "videoUnmuted",
            'VIDEOPAUSED': "videoPaused",
            'VIDEORESUMED': "videoResumed",
            'VIDEOAVGINTERACTIONRATE': "videoAvgInteractionRate",
            'VIDEOVIEWABILITY': "videoViewability",
            'VIDEOSTARTINGRATE': "videoStartingRate",
            'VIDEOCPC': "videoCPC",
            'VIDEOCPCV': "videoCPCV",
            'NEWTOBRANDATTRIBUTEDSALES': "newToBrandAttributedSales",
            'NEWTOBRANDATTRIBUTEDSALESRATE': "newToBrandAttributedSalesRate",
            'NEWTOBRANDATTRIBUTEDUNITS': "newToBrandAttributedUnits",
            'NEWTOBRANDATTRIBUTEDUNITSRATE': "newToBrandAttributedUnitsRate",
            'UNIQUEVISITORS': "uniqueVisitors",
            'FREQUENCY': "frequency",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'start_date': (datetime,),  # noqa: E501
            'end_date': (datetime,),  # noqa: E501
            'ids': ([str],),  # noqa: E501
            'id': (str,),  # noqa: E501
            'search_term_types': ([str],),  # noqa: E501
            'search_term_targetings': ([str],),  # noqa: E501
            'campaign_type': (str,),  # noqa: E501
            'sales_channel': (str,),  # noqa: E501
            'format': (str,),  # noqa: E501
            'report_type': (str,),  # noqa: E501
            'click_attribution_window': (str,),  # noqa: E501
            'view_attribution_window': (str,),  # noqa: E501
            'dimensions': ([str],),  # noqa: E501
            'metrics': ([str],),  # noqa: E501
            'timezone': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'start_date': 'startDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'ids': 'ids',  # noqa: E501
        'id': 'id',  # noqa: E501
        'search_term_types': 'searchTermTypes',  # noqa: E501
        'search_term_targetings': 'searchTermTargetings',  # noqa: E501
        'campaign_type': 'campaignType',  # noqa: E501
        'sales_channel': 'salesChannel',  # noqa: E501
        'format': 'format',  # noqa: E501
        'report_type': 'reportType',  # noqa: E501
        'click_attribution_window': 'clickAttributionWindow',  # noqa: E501
        'view_attribution_window': 'viewAttributionWindow',  # noqa: E501
        'dimensions': 'dimensions',  # noqa: E501
        'metrics': 'metrics',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, start_date, end_date, *args, **kwargs):  # noqa: E501
        """AsyncCampaignsReport - a model defined in OpenAPI

        Args:
            start_date (datetime): Start date
            end_date (datetime): End date

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
            ids ([str]): Campaign ids to report on. [optional]  # noqa: E501
            id (str): Campaign id to report on. [optional]  # noqa: E501
            search_term_types ([str]): Filter on the type of search term type: unknown, searched, entered. [optional]  # noqa: E501
            search_term_targetings ([str]): Filter on the type of search term targeting: unknown, automatic, manual. [optional]  # noqa: E501
            campaign_type (str): Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays. [optional] if omitted the server will use the default value of "all"  # noqa: E501
            sales_channel (str): Filter on specific sales channel: offline or online. [optional] if omitted the server will use the default value of "all"  # noqa: E501
            format (str): Format of the output. [optional] if omitted the server will use the default value of "json-compact"  # noqa: E501
            report_type (str): Type of report, if no dimensions/metrics are provided, falls back to summary reportType. [optional] if omitted the server will use the default value of "summary"  # noqa: E501
            click_attribution_window (str): Click attribution window. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            view_attribution_window (str): View attribution window. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            dimensions ([str]): List of dimensions to report on. [optional]  # noqa: E501
            metrics ([str]): List of metrics to report on. [optional]  # noqa: E501
            timezone (str): Time zone : see criteo developer portal for supported time zones. [optional] if omitted the server will use the default value of "UTC"  # noqa: E501
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
    def __init__(self, start_date, end_date, *args, **kwargs):  # noqa: E501
        """AsyncCampaignsReport - a model defined in OpenAPI

        Args:
            start_date (datetime): Start date
            end_date (datetime): End date

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
            ids ([str]): Campaign ids to report on. [optional]  # noqa: E501
            id (str): Campaign id to report on. [optional]  # noqa: E501
            search_term_types ([str]): Filter on the type of search term type: unknown, searched, entered. [optional]  # noqa: E501
            search_term_targetings ([str]): Filter on the type of search term targeting: unknown, automatic, manual. [optional]  # noqa: E501
            campaign_type (str): Filter the type of campaigns to report on: sponsoredProducts or onSiteDisplays. [optional] if omitted the server will use the default value of "all"  # noqa: E501
            sales_channel (str): Filter on specific sales channel: offline or online. [optional] if omitted the server will use the default value of "all"  # noqa: E501
            format (str): Format of the output. [optional] if omitted the server will use the default value of "json-compact"  # noqa: E501
            report_type (str): Type of report, if no dimensions/metrics are provided, falls back to summary reportType. [optional] if omitted the server will use the default value of "summary"  # noqa: E501
            click_attribution_window (str): Click attribution window. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            view_attribution_window (str): View attribution window. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            dimensions ([str]): List of dimensions to report on. [optional]  # noqa: E501
            metrics ([str]): List of metrics to report on. [optional]  # noqa: E501
            timezone (str): Time zone : see criteo developer portal for supported time zones. [optional] if omitted the server will use the default value of "UTC"  # noqa: E501
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
