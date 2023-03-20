"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

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



class GenerateStatisticsReportRequestAttributes(ModelNormal):
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
            'ADVERTISERID': "AdvertiserId",
            'ADVERTISER': "Advertiser",
            'CAMPAIGNID': "CampaignId",
            'CAMPAIGN': "Campaign",
            'ADSETID': "AdSetId",
            'ADSET': "AdSet",
            'CHANNELID': "ChannelId",
            'CHANNEL': "Channel",
            'CATEGORYID': "CategoryId",
            'CATEGORY': "Category",
            'DEVICE': "Device",
            'OS': "Os",
            'ADID': "AdId",
            'AD': "Ad",
            'COUPONID': "CouponId",
            'COUPON': "Coupon",
            'YEAR': "Year",
            'MONTH': "Month",
            'WEEK': "Week",
            'DAY': "Day",
            'HOUR': "Hour",
            'MARKETINGCAMPAIGNGOAL': "MarketingCampaignGoal",
            'MARKETINGOBJECTIVE': "MarketingObjective",
            'MARKETINGOBJECTIVEID': "MarketingObjectiveId",
            'VIDEOPLAYERSIZE': "VideoPlayerSize",
            'VIDEOPLACEMENT': "VideoPlacement",
            'VIDEOPLAYBACKMETHOD': "VideoPlaybackMethod",
            'SSP': "SSP",
            'VIDEODURATIONINSECONDS': "VideoDurationInSeconds",
            'MEDIATYPE': "MediaType",
            'ADFORMAT': "AdFormat",
            'DISPLAYSIZE': "DisplaySize",
            'VIDEOPLAYERRATIO': "VideoPlayerRatio",
        },
        ('metrics',): {
            'CLICKS': "Clicks",
            'DISPLAYS': "Displays",
            'ADVERTISERCOST': "AdvertiserCost",
            'SALESPC30DCLIENTATTRIBUTION': "SalesPc30dClientAttribution",
            'SALESALLPC30DCLIENTATTRIBUTION': "SalesAllPc30dClientAttribution",
            'SALESCLIENTATTRIBUTION': "SalesClientAttribution",
            'SALESALLCLIENTATTRIBUTION': "SalesAllClientAttribution",
            'SALESPC30D': "SalesPc30d",
            'SALESALLPC30D': "SalesAllPc30d",
            'SALESPC1D': "SalesPc1d",
            'SALESALLPC1D': "SalesAllPc1d",
            'SALESPC7D': "SalesPc7d",
            'SALESALLPC7D': "SalesAllPc7d",
            'SALESPC7DPV24': "SalesPc7dPv24",
            'SALESALLPC7DPV24': "SalesAllPc7dPv24",
            'SALESPC7DPV24H': "SalesPc7dPv24h",
            'SALESALLPC7DPV24H': "SalesAllPc7dPv24h",
            'SALESPV24H': "SalesPv24h",
            'SALESALLPV24H': "SalesAllPv24h",
            'SALESPC30PV24': "SalesPc30Pv24",
            'SALESALLPC30PV24': "SalesAllPc30Pv24",
            'SALESPC30DPV24H': "SalesPc30dPv24h",
            'SALESALLPC30DPV24H': "SalesAllPc30dPv24h",
            'SALESPIPC': "SalesPiPc",
            'SALESPIPV': "SalesPiPv",
            'SALESPIPCPV': "SalesPiPcPv",
            'POSTINSTALLSALES': "PostInstallSales",
            'SALESOFFLINEPC': "SalesOfflinePc",
            'SALESOFFLINEPV': "SalesOfflinePv",
            'SALESOFFLINEPC30D': "SalesOfflinePc30d",
            'SALESOFFLINEPV24H': "SalesOfflinePv24h",
            'REVENUEGENERATEDPC30DCLIENTATTRIBUTION': "RevenueGeneratedPc30dClientAttribution",
            'REVENUEGENERATEDALLPC30DCLIENTATTRIBUTION': "RevenueGeneratedAllPc30dClientAttribution",
            'REVENUEGENERATEDCLIENTATTRIBUTION': "RevenueGeneratedClientAttribution",
            'REVENUEGENERATEDALLCLIENTATTRIBUTION': "RevenueGeneratedAllClientAttribution",
            'REVENUEGENERATEDPC30D': "RevenueGeneratedPc30d",
            'REVENUEGENERATEDALLPC30D': "RevenueGeneratedAllPc30d",
            'REVENUEGENERATEDPC1D': "RevenueGeneratedPc1d",
            'REVENUEGENERATEDALLPC1D': "RevenueGeneratedAllPc1d",
            'REVENUEGENERATEDPC7D': "RevenueGeneratedPc7d",
            'REVENUEGENERATEDALLPC7D': "RevenueGeneratedAllPc7d",
            'REVENUEGENERATEDPV24H': "RevenueGeneratedPv24h",
            'REVENUEGENERATEDALLPV24H': "RevenueGeneratedAllPv24h",
            'REVENUEGENERATEDPC30PV24': "RevenueGeneratedPc30Pv24",
            'REVENUEGENERATEDALLPC30PV24': "RevenueGeneratedAllPc30Pv24",
            'REVENUEGENERATEDPC30DPV24H': "RevenueGeneratedPc30dPv24h",
            'REVENUEGENERATEDALLPC30DPV24H': "RevenueGeneratedAllPc30dPv24h",
            'REVENUEGENERATEDPC7DPV24H': "RevenueGeneratedPc7dPv24h",
            'REVENUEGENERATEDALLPC7DPV24H': "RevenueGeneratedAllPc7dPv24h",
            'REVENUEGENERATEDPC7DPV24': "RevenueGeneratedPc7dPv24",
            'REVENUEGENERATEDALLPC7DPV24': "RevenueGeneratedAllPc7dPv24",
            'REVENUEGENERATEDOFFLINEPC': "RevenueGeneratedOfflinePc",
            'REVENUEGENERATEDOFFLINEPV': "RevenueGeneratedOfflinePv",
            'REVENUEGENERATEDOFFLINEPC30D': "RevenueGeneratedOfflinePc30d",
            'REVENUEGENERATEDOFFLINEPV24H': "RevenueGeneratedOfflinePv24h",
            'CONVERSIONRATEPC30DCLIENTATTRIBUTION': "ConversionRatePc30dClientAttribution",
            'CONVERSIONRATEALLPC30DCLIENTATTRIBUTION': "ConversionRateAllPc30dClientAttribution",
            'CONVERSIONRATECLIENTATTRIBUTION': "ConversionRateClientAttribution",
            'CONVERSIONRATEALLCLIENTATTRIBUTION': "ConversionRateAllClientAttribution",
            'CONVERSIONRATEPC30D': "ConversionRatePc30d",
            'CONVERSIONRATEALLPC30D': "ConversionRateAllPc30d",
            'CONVERSIONRATEPC1D': "ConversionRatePc1d",
            'CONVERSIONRATEALLPC1D': "ConversionRateAllPc1d",
            'CONVERSIONRATEPC7D': "ConversionRatePc7d",
            'CONVERSIONRATEALLPC7D': "ConversionRateAllPc7d",
            'CONVERSIONRATEPV24H': "ConversionRatePv24h",
            'CONVERSIONRATEALLPV24H': "ConversionRateAllPv24h",
            'CONVERSIONRATEPC30PV24': "ConversionRatePc30Pv24",
            'CONVERSIONRATEALLPC30PV24': "ConversionRateAllPc30Pv24",
            'CONVERSIONRATEPC30DPV24H': "ConversionRatePc30dPv24h",
            'CONVERSIONRATEALLPC30DPV24H': "ConversionRateAllPc30dPv24h",
            'CONVERSIONRATEPC7DPV24': "ConversionRatePc7dPv24",
            'CONVERSIONRATEALLPC7DPV24': "ConversionRateAllPc7dPv24",
            'CONVERSIONRATEPC7DPV24H': "ConversionRatePc7dPv24h",
            'CONVERSIONRATEALLPC7DPV24H': "ConversionRateAllPc7dPv24h",
            'CONVERSIONRATEPIPCPV': "ConversionRatePiPcPv",
            'POSTINSTALLCONVERSIONRATE': "PostInstallConversionRate",
            'ECOSPC30DCLIENTATTRIBUTION': "ECosPc30dClientAttribution",
            'ECOSALLPC30DCLIENTATTRIBUTION': "ECosAllPc30dClientAttribution",
            'ECOSCLIENTATTRIBUTION': "ECosClientAttribution",
            'ECOSALLCLIENTATTRIBUTION': "ECosAllClientAttribution",
            'ECOSPC30D': "ECosPc30d",
            'ECOSALLPC30D': "ECosAllPc30d",
            'ECOSPC1D': "ECosPc1d",
            'ECOSALLPC1D': "ECosAllPc1d",
            'ECOSPC7D': "ECosPc7d",
            'ECOSALLPC7D': "ECosAllPc7d",
            'ECOSPV24H': "ECosPv24h",
            'ECOSALLPV24H': "ECosAllPv24h",
            'ECOSPC30PV24': "ECosPc30Pv24",
            'ECOSALLPC30PV24': "ECosAllPc30Pv24",
            'ECOSPC30DPV24H': "ECosPc30dPv24h",
            'ECOSALLPC30DPV24H': "ECosAllPc30dPv24h",
            'ECOSPC7DPV24H': "ECosPc7dPv24h",
            'ECOSALLPC7DPV24H': "ECosAllPc7dPv24h",
            'ECOSPC7DPV24': "ECosPc7dPv24",
            'ECOSALLPC7DPV24': "ECosAllPc7dPv24",
            'COSTPERORDERPC30DCLIENTATTRIBUTION': "CostPerOrderPc30dClientAttribution",
            'COSTPERORDERALLPC30DCLIENTATTRIBUTION': "CostPerOrderAllPc30dClientAttribution",
            'COSTPERORDERCLIENTATTRIBUTION': "CostPerOrderClientAttribution",
            'COSTPERORDERALLCLIENTATTRIBUTION': "CostPerOrderAllClientAttribution",
            'COSTPERORDERPC30D': "CostPerOrderPc30d",
            'COSTPERORDERALLPC30D': "CostPerOrderAllPc30d",
            'COSTPERORDERPC1D': "CostPerOrderPc1d",
            'COSTPERORDERALLPC1D': "CostPerOrderAllPc1d",
            'COSTPERORDERPC7D': "CostPerOrderPc7d",
            'COSTPERORDERALLPC7D': "CostPerOrderAllPc7d",
            'COSTPERORDERPV24H': "CostPerOrderPv24h",
            'COSTPERORDERALLPV24H': "CostPerOrderAllPv24h",
            'COSTPERORDERPC30PV24': "CostPerOrderPc30Pv24",
            'COSTPERORDERALLPC30PV24': "CostPerOrderAllPc30Pv24",
            'COSTPERORDERPC30DPV24H': "CostPerOrderPc30dPv24h",
            'COSTPERORDERALLPC30DPV24H': "CostPerOrderAllPc30dPv24h",
            'COSTPERORDERPC7DPV24H': "CostPerOrderPc7dPv24h",
            'COSTPERORDERALLPC7DPV24H': "CostPerOrderAllPc7dPv24h",
            'COSTPERORDERPC7DPV24': "CostPerOrderPc7dPv24",
            'COSTPERORDERALLPC7DPV24': "CostPerOrderAllPc7dPv24",
            'EXPOSEDUSERS': "ExposedUsers",
            'AUDIENCE': "Audience",
            'REACH': "Reach",
            'AVERAGECARTPC30DCLIENTATTRIBUTION': "AverageCartPc30dClientAttribution",
            'AVERAGECARTALLPC30DCLIENTATTRIBUTION': "AverageCartAllPc30dClientAttribution",
            'AVERAGECARTCLIENTATTRIBUTION': "AverageCartClientAttribution",
            'AVERAGECARTALLCLIENTATTRIBUTION': "AverageCartAllClientAttribution",
            'AVERAGECARTPC30D': "AverageCartPc30d",
            'AVERAGECARTALLPC30D': "AverageCartAllPc30d",
            'AVERAGECARTPV24H': "AverageCartPv24h",
            'AVERAGECARTALLPV24H': "AverageCartAllPv24h",
            'AVERAGECARTPC1D': "AverageCartPc1d",
            'AVERAGECARTALLPC1D': "AverageCartAllPc1d",
            'AVERAGECARTPC7D': "AverageCartPc7d",
            'AVERAGECARTALLPC7D': "AverageCartAllPc7d",
            'AVERAGECARTPC30PV24': "AverageCartPc30Pv24",
            'AVERAGECARTALLPC30PV24': "AverageCartAllPc30Pv24",
            'AVERAGECARTPC30DPV24H': "AverageCartPc30dPv24h",
            'AVERAGECARTALLPC30DPV24H': "AverageCartAllPc30dPv24h",
            'AVERAGECARTPC7DPV24H': "AverageCartPc7dPv24h",
            'AVERAGECARTALLPC7DPV24H': "AverageCartAllPc7dPv24h",
            'AVERAGECARTPC7DPV24': "AverageCartPc7dPv24",
            'AVERAGECARTALLPC7DPV24': "AverageCartAllPc7dPv24",
            'CLICKTHROUGHRATE': "ClickThroughRate",
            'ECPC': "ECpc",
            'CPC': "Cpc",
            'ECPM': "ECpm",
            'RETURNONADVERTISINGSPENDINGCLIENTATTRIBUTION': "ReturnOnAdvertisingSpendingClientAttribution",
            'RETURNONADVERTISINGSPENDINGALLCLIENTATTRIBUTION': "ReturnOnAdvertisingSpendingAllClientAttribution",
            'ADVERTISERVALUE': "AdvertiserValue",
            'ADVERTISERALLVALUE': "AdvertiserAllValue",
            'COSTOFADVERTISERVALUE': "CostOfAdvertiserValue",
            'COSTOFADVERTISERVALUEALL': "CostOfAdvertiserValueAll",
            'APPINSTALLSPCPV': "AppInstallsPcPv",
            'APPINSTALLS': "AppInstalls",
            'QUALIFIEDVISITS': "QualifiedVisits",
            'VISITS': "Visits",
            'ORDERVALUEPI': "OrderValuePi",
            'POSTINSTALLORDERVALUE': "PostInstallOrderValue",
            'BOUNCERATE': "BounceRate",
            'COSTPERINSTALLPCPV': "CostPerInstallPcPv",
            'COSTPERINSTALL': "CostPerInstall",
            'COSTPERVISIT': "CostPerVisit",
            'INSTALLRATEPCPV': "InstallRatePcPv",
            'INSTALLRATE': "InstallRate",
            'OMNICHANNELROASPC30D': "OmniChannelRoasPc30d",
            'OMNICHANNELROASALLPC30D': "OmnichannelRoasAllPc30d",
            'OMNICHANNELREVENUEPC30D': "OmniChannelRevenuePc30d",
            'OMNICHANNELREVENUEALLPC30D': "OmnichannelRevenueAllPc30d",
            'OMNICHANNELSALESPC30D': "OmniChannelSalesPc30d",
            'OMNICHANNELSALESALLPC30D': "OmnichannelSalesAllPc30d",
            'OMNICHANNELROASALLPV24H': "OmnichannelRoasAllPv24h",
            'OMNICHANNELROASPV24H': "OmnichannelRoasPv24h",
            'OMNICHANNELREVENUEALLPV24H': "OmnichannelRevenueAllPv24h",
            'OMNICHANNELREVENUEPV24H': "OmnichannelRevenuePv24h",
            'OMNICHANNELSALESALLPV24H': "OmnichannelSalesAllPv24h",
            'OMNICHANNELSALESPV24H': "OmnichannelSalesPv24h",
            'OMNICHANNELROASCLIENTATTRIBUTION': "OmnichannelRoasClientAttribution",
            'OMNICHANNELREVENUECLIENTATTRIBUTION': "OmnichannelRevenueClientAttribution",
            'OMNICHANNELSALESCLIENTATTRIBUTION': "OmnichannelSalesClientAttribution",
            'ROASALLPC30DCLIENTATTRIBUTION': "RoasAllPc30dClientAttribution",
            'ROASPC30DCLIENTATTRIBUTION': "RoasPc30dClientAttribution",
            'ROASALLCLIENTATTRIBUTION': "RoasAllClientAttribution",
            'ROASCLIENTATTRIBUTION': "RoasClientAttribution",
            'ROASALLPC30D': "RoasAllPc30d",
            'ROASPC30D': "RoasPc30d",
            'ROASALLPC7D': "RoasAllPc7d",
            'ROASPC7D': "RoasPc7d",
            'ROASALLPC1D': "RoasAllPc1d",
            'ROASPC1D': "RoasPc1d",
            'ROASALLPV24H': "RoasAllPv24h",
            'ROASPV24H': "RoasPv24h",
            'ROASPC30PV24': "RoasPc30Pv24",
            'ROASALLPC30PV24': "RoasAllPc30Pv24",
            'ROASPC30DPV24H': "RoasPc30dPv24h",
            'ROASALLPC30DPV24H': "RoasAllPc30dPv24h",
            'ROASPC7DPV24': "RoasPc7dPv24",
            'ROASALLPC7DPV24': "RoasAllPc7dPv24",
            'ROASPC7DPV24H': "RoasPc7dPv24h",
            'ROASALLPC7DPV24H': "RoasAllPc7dPv24h",
            'COSTOFSALEPI': "CostOfSalePi",
            'COSTPERORDERPI': "CostPerOrderPi",
            'POSTINSTALLCOSTOFSALE': "PostInstallCostOfSale",
            'POSTINSTALLCOSTPERORDER': "PostInstallCostPerOrder",
            'RETURNONADVERTISERSPENDINGPI': "ReturnOnAdvertiserSpendingPi",
            'POSTINSTALLROAS': "PostInstallRoas",
            'RETURNONADVERTISERSPENDINGOFFLINEPC': "ReturnOnAdvertiserSpendingOfflinePc",
            'RETURNONADVERTISERSPENDINGOFFLINEPV': "ReturnOnAdvertiserSpendingOfflinePv",
            'ROASOFFLINEPC30D': "RoasOfflinePc30d",
            'ROASOFFLINEPV24H': "RoasOfflinePv24h",
            'POTENTIALDISPLAYS': "PotentialDisplays",
            'OVERALLCOMPETITIONWIN': "OverallCompetitionWin",
            'VIEWABLEDISPLAYS': "ViewableDisplays",
            'NONVIEWABLEDISPLAYS': "NonViewableDisplays",
            'UNTRACKABLEDISPLAYS': "UntrackableDisplays",
            'FREQUENCY': "Frequency",
            'INVALIDCLICKS': "InvalidClicks",
            'INVALIDDISPLAYS': "InvalidDisplays",
            'RESULTTYPE': "ResultType",
            'COSTPERQUALIFIEDVISIT': "CostPerQualifiedVisit",
        },
    }

    validations = {
        ('dimensions',): {
        },
        ('metrics',): {
        },
        ('advertiser_ids',): {
        },
        ('ad_set_ids',): {
        },
        ('ad_set_names',): {
        },
        ('ad_set_status',): {
        },
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
            'dimensions': ([str],),  # noqa: E501
            'metrics': ([str],),  # noqa: E501
            'advertiser_ids': ([str],),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'ad_set_ids': ([str],),  # noqa: E501
            'ad_set_names': ([str],),  # noqa: E501
            'ad_set_status': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'start_date': 'startDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'dimensions': 'dimensions',  # noqa: E501
        'metrics': 'metrics',  # noqa: E501
        'advertiser_ids': 'advertiserIds',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'ad_set_ids': 'adSetIds',  # noqa: E501
        'ad_set_names': 'adSetNames',  # noqa: E501
        'ad_set_status': 'adSetStatus',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, start_date, end_date, dimensions, metrics, *args, **kwargs):  # noqa: E501
        """GenerateStatisticsReportRequestAttributes - a model defined in OpenAPI

        Args:
            start_date (datetime): Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.
            end_date (datetime): End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.
            dimensions ([str]): The dimensions for the report.
            metrics ([str]): The list of metrics to report.

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
            advertiser_ids ([str]): The of advertiser ids. [optional]  # noqa: E501
            timezone (str): The timezone used for the report. Timezone Database format (Tz).. [optional]  # noqa: E501
            currency (str): The currency used for the report. ISO 4217 code (three-letter capitals).. [optional]  # noqa: E501
            ad_set_ids ([str]): The list of adSets ids. If empty, all the adSets will be fetched. [optional]  # noqa: E501
            ad_set_names ([str]): The list of adSets names. If empty, all the adSets will be fetched. [optional]  # noqa: E501
            ad_set_status ([str]): The list of adSets status. If empty, all the adSets will be fetched. [optional]  # noqa: E501
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
        self.dimensions = dimensions
        self.metrics = metrics
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
    def __init__(self, start_date, end_date, dimensions, metrics, *args, **kwargs):  # noqa: E501
        """GenerateStatisticsReportRequestAttributes - a model defined in OpenAPI

        Args:
            start_date (datetime): Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.
            end_date (datetime): End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored.
            dimensions ([str]): The dimensions for the report.
            metrics ([str]): The list of metrics to report.

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
            advertiser_ids ([str]): The of advertiser ids. [optional]  # noqa: E501
            timezone (str): The timezone used for the report. Timezone Database format (Tz).. [optional]  # noqa: E501
            currency (str): The currency used for the report. ISO 4217 code (three-letter capitals).. [optional]  # noqa: E501
            ad_set_ids ([str]): The list of adSets ids. If empty, all the adSets will be fetched. [optional]  # noqa: E501
            ad_set_names ([str]): The list of adSets names. If empty, all the adSets will be fetched. [optional]  # noqa: E501
            ad_set_status ([str]): The list of adSets status. If empty, all the adSets will be fetched. [optional]  # noqa: E501
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
        self.dimensions = dimensions
        self.metrics = metrics
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
