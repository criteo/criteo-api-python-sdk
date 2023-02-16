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
)
from ..model_utils import OpenApiModel
from criteo_api_marketingsolutions_preview.exceptions import ApiAttributeError


def lazy_import():
    from criteo_api_marketingsolutions_preview.model.custom_attribute import CustomAttribute
    from criteo_api_marketingsolutions_preview.model.installment import Installment
    from criteo_api_marketingsolutions_preview.model.loyalty_points import LoyaltyPoints
    from criteo_api_marketingsolutions_preview.model.price import Price
    from criteo_api_marketingsolutions_preview.model.product_shipping import ProductShipping
    from criteo_api_marketingsolutions_preview.model.product_shipping_dimension import ProductShippingDimension
    from criteo_api_marketingsolutions_preview.model.product_shipping_weight import ProductShippingWeight
    from criteo_api_marketingsolutions_preview.model.product_tax import ProductTax
    from criteo_api_marketingsolutions_preview.model.product_unit_pricing_base_measure import ProductUnitPricingBaseMeasure
    from criteo_api_marketingsolutions_preview.model.product_unit_pricing_measure import ProductUnitPricingMeasure
    globals()['CustomAttribute'] = CustomAttribute
    globals()['Installment'] = Installment
    globals()['LoyaltyPoints'] = LoyaltyPoints
    globals()['Price'] = Price
    globals()['ProductShipping'] = ProductShipping
    globals()['ProductShippingDimension'] = ProductShippingDimension
    globals()['ProductShippingWeight'] = ProductShippingWeight
    globals()['ProductTax'] = ProductTax
    globals()['ProductUnitPricingBaseMeasure'] = ProductUnitPricingBaseMeasure
    globals()['ProductUnitPricingMeasure'] = ProductUnitPricingMeasure


class Product(ModelNormal):
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
        ('channel',): {
            'ONLINE': "online",
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
            'id': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'link': (str,),  # noqa: E501
            'image_link': (str,),  # noqa: E501
            'channel': (str,),  # noqa: E501
            'offer_id': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'additional_image_links': ([str],),  # noqa: E501
            'content_language': (str,),  # noqa: E501
            'target_country': (str,),  # noqa: E501
            'expiration_date': (str,),  # noqa: E501
            'adult': (bool,),  # noqa: E501
            'kind': (str,),  # noqa: E501
            'brand': (str,),  # noqa: E501
            'color': (str,),  # noqa: E501
            'google_product_category': (str,),  # noqa: E501
            'gtin': (str,),  # noqa: E501
            'item_group_id': (str,),  # noqa: E501
            'material': (str,),  # noqa: E501
            'mpn': (str,),  # noqa: E501
            'pattern': (str,),  # noqa: E501
            'price': (Price,),  # noqa: E501
            'sale_price': (Price,),  # noqa: E501
            'sale_price_effective_date': (str,),  # noqa: E501
            'shipping': ([ProductShipping],),  # noqa: E501
            'shipping_weight': (ProductShippingWeight,),  # noqa: E501
            'sizes': ([str],),  # noqa: E501
            'taxes': ([ProductTax],),  # noqa: E501
            'custom_attributes': ([CustomAttribute],),  # noqa: E501
            'identifier_exists': (bool,),  # noqa: E501
            'installment': (Installment,),  # noqa: E501
            'loyalty_points': (LoyaltyPoints,),  # noqa: E501
            'multipack': (int,),  # noqa: E501
            'custom_label0': (str,),  # noqa: E501
            'custom_label1': (str,),  # noqa: E501
            'custom_label2': (str,),  # noqa: E501
            'custom_label3': (str,),  # noqa: E501
            'custom_label4': (str,),  # noqa: E501
            'is_bundle': (bool,),  # noqa: E501
            'mobile_link': (str,),  # noqa: E501
            'availability_date': (str,),  # noqa: E501
            'shipping_label': (str,),  # noqa: E501
            'unit_pricing_measure': (ProductUnitPricingMeasure,),  # noqa: E501
            'unit_pricing_base_measure': (ProductUnitPricingBaseMeasure,),  # noqa: E501
            'shipping_length': (ProductShippingDimension,),  # noqa: E501
            'shipping_width': (ProductShippingDimension,),  # noqa: E501
            'shipping_height': (ProductShippingDimension,),  # noqa: E501
            'display_ads_id': (str,),  # noqa: E501
            'display_ads_similar_ids': ([str],),  # noqa: E501
            'display_ads_title': (str,),  # noqa: E501
            'display_ads_link': (str,),  # noqa: E501
            'display_ads_value': (float,),  # noqa: E501
            'sell_on_google_quantity': (int,),  # noqa: E501
            'promotion_ids': ([str],),  # noqa: E501
            'max_handling_time': (int,),  # noqa: E501
            'min_handling_time': (int,),  # noqa: E501
            'cost_of_goods_sold': (Price,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'included_destinations': ([str],),  # noqa: E501
            'excluded_destinations': ([str],),  # noqa: E501
            'ads_grouping': (str,),  # noqa: E501
            'ads_labels': ([str],),  # noqa: E501
            'ads_redirect': (str,),  # noqa: E501
            'product_types': ([str],),  # noqa: E501
            'age_group': (str,),  # noqa: E501
            'availability': (str,),  # noqa: E501
            'condition': (str,),  # noqa: E501
            'gender': (str,),  # noqa: E501
            'size_system': (str,),  # noqa: E501
            'size_type': (str,),  # noqa: E501
            'energy_efficiency_class': (str,),  # noqa: E501
            'min_energy_efficiency_class': (str,),  # noqa: E501
            'max_energy_efficiency_class': (str,),  # noqa: E501
            'tax_category': (str,),  # noqa: E501
            'transit_time_label': (str,),  # noqa: E501
            'seller_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'title': 'title',  # noqa: E501
        'link': 'link',  # noqa: E501
        'image_link': 'imageLink',  # noqa: E501
        'channel': 'channel',  # noqa: E501
        'offer_id': 'offerId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'additional_image_links': 'additionalImageLinks',  # noqa: E501
        'content_language': 'contentLanguage',  # noqa: E501
        'target_country': 'targetCountry',  # noqa: E501
        'expiration_date': 'expirationDate',  # noqa: E501
        'adult': 'adult',  # noqa: E501
        'kind': 'kind',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'color': 'color',  # noqa: E501
        'google_product_category': 'googleProductCategory',  # noqa: E501
        'gtin': 'gtin',  # noqa: E501
        'item_group_id': 'itemGroupId',  # noqa: E501
        'material': 'material',  # noqa: E501
        'mpn': 'mpn',  # noqa: E501
        'pattern': 'pattern',  # noqa: E501
        'price': 'price',  # noqa: E501
        'sale_price': 'salePrice',  # noqa: E501
        'sale_price_effective_date': 'salePriceEffectiveDate',  # noqa: E501
        'shipping': 'shipping',  # noqa: E501
        'shipping_weight': 'shippingWeight',  # noqa: E501
        'sizes': 'sizes',  # noqa: E501
        'taxes': 'taxes',  # noqa: E501
        'custom_attributes': 'customAttributes',  # noqa: E501
        'identifier_exists': 'identifierExists',  # noqa: E501
        'installment': 'installment',  # noqa: E501
        'loyalty_points': 'loyaltyPoints',  # noqa: E501
        'multipack': 'multipack',  # noqa: E501
        'custom_label0': 'customLabel0',  # noqa: E501
        'custom_label1': 'customLabel1',  # noqa: E501
        'custom_label2': 'customLabel2',  # noqa: E501
        'custom_label3': 'customLabel3',  # noqa: E501
        'custom_label4': 'customLabel4',  # noqa: E501
        'is_bundle': 'isBundle',  # noqa: E501
        'mobile_link': 'mobileLink',  # noqa: E501
        'availability_date': 'availabilityDate',  # noqa: E501
        'shipping_label': 'shippingLabel',  # noqa: E501
        'unit_pricing_measure': 'unitPricingMeasure',  # noqa: E501
        'unit_pricing_base_measure': 'unitPricingBaseMeasure',  # noqa: E501
        'shipping_length': 'shippingLength',  # noqa: E501
        'shipping_width': 'shippingWidth',  # noqa: E501
        'shipping_height': 'shippingHeight',  # noqa: E501
        'display_ads_id': 'displayAdsId',  # noqa: E501
        'display_ads_similar_ids': 'displayAdsSimilarIds',  # noqa: E501
        'display_ads_title': 'displayAdsTitle',  # noqa: E501
        'display_ads_link': 'displayAdsLink',  # noqa: E501
        'display_ads_value': 'displayAdsValue',  # noqa: E501
        'sell_on_google_quantity': 'sellOnGoogleQuantity',  # noqa: E501
        'promotion_ids': 'promotionIds',  # noqa: E501
        'max_handling_time': 'maxHandlingTime',  # noqa: E501
        'min_handling_time': 'minHandlingTime',  # noqa: E501
        'cost_of_goods_sold': 'costOfGoodsSold',  # noqa: E501
        'source': 'source',  # noqa: E501
        'included_destinations': 'includedDestinations',  # noqa: E501
        'excluded_destinations': 'excludedDestinations',  # noqa: E501
        'ads_grouping': 'adsGrouping',  # noqa: E501
        'ads_labels': 'adsLabels',  # noqa: E501
        'ads_redirect': 'adsRedirect',  # noqa: E501
        'product_types': 'productTypes',  # noqa: E501
        'age_group': 'ageGroup',  # noqa: E501
        'availability': 'availability',  # noqa: E501
        'condition': 'condition',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'size_system': 'sizeSystem',  # noqa: E501
        'size_type': 'sizeType',  # noqa: E501
        'energy_efficiency_class': 'energyEfficiencyClass',  # noqa: E501
        'min_energy_efficiency_class': 'minEnergyEfficiencyClass',  # noqa: E501
        'max_energy_efficiency_class': 'maxEnergyEfficiencyClass',  # noqa: E501
        'tax_category': 'taxCategory',  # noqa: E501
        'transit_time_label': 'transitTimeLabel',  # noqa: E501
        'seller_id': 'sellerId',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, title, link, image_link, *args, **kwargs):  # noqa: E501
        """Product - a model defined in OpenAPI

        Args:
            id (str): A unique identifier for the item. Aka Product ID.
            title (str): Title of the item. (500 UTF8 characters max).
            link (str): URL directly linking to your item's page on your website. (1000 UTF8 characters max).
            image_link (str): URL of an image of the item. Supported formats: PNG, JPEG, GIF. (2000 UTF8 characters max). 

        Keyword Args:
            channel (str): The item's channel (online only).. defaults to "online", must be one of ["online", ]  # noqa: E501
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
            offer_id (str): Not used by Criteo.. [optional]  # noqa: E501
            description (str): Description of the item. RECOMMENDED. (5000 UTF8 characters max).. [optional]  # noqa: E501
            additional_image_links ([str]): Additional URLs of images of the item.. [optional]  # noqa: E501
            content_language (str): The two-letter ISO 639-1 language code for the item.. [optional]  # noqa: E501
            target_country (str): The CLDR territory code for the item.. [optional]  # noqa: E501
            expiration_date (str): Date on which the item should expire, as specified upon insertion, in ISO 8601 format.. [optional]  # noqa: E501
            adult (bool): Set to true if the item is targeted towards adults. RECOMMENDED.. [optional]  # noqa: E501
            kind (str): Identifies what kind of resource this is.. [optional]  # noqa: E501
            brand (str): Brand of the item. RECOMMENDED.. [optional]  # noqa: E501
            color (str): Color of the item.. [optional]  # noqa: E501
            google_product_category (str): Google's category of the item (see Google product taxonomy). RECOMMENDED.. [optional]  # noqa: E501
            gtin (str): Global Trade Item Number (GTIN) of the item. RECOMMENDED.. [optional]  # noqa: E501
            item_group_id (str): Shared identifier for all variants of the same product. RECOMMENDED.. [optional]  # noqa: E501
            material (str): The material of which the item is made.. [optional]  # noqa: E501
            mpn (str): Manufacturer Part Number (MPN) of the item. RECOMMENDED.. [optional]  # noqa: E501
            pattern (str): The item's pattern (e.g. polka dots).. [optional]  # noqa: E501
            price (Price): [optional]  # noqa: E501
            sale_price (Price): [optional]  # noqa: E501
            sale_price_effective_date (str): Date range during which the item is on sale.. [optional]  # noqa: E501
            shipping ([ProductShipping]): Shipping rules.. [optional]  # noqa: E501
            shipping_weight (ProductShippingWeight): [optional]  # noqa: E501
            sizes ([str]): Size of the item. RECOMMENDED. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same itemGroupId value.. [optional]  # noqa: E501
            taxes ([ProductTax]): Tax information.. [optional]  # noqa: E501
            custom_attributes ([CustomAttribute]): A list of custom (merchant-provided) attributes. This is useful for submitting attributes not explicitly exposed by the API. Declaring attributes explicitly exposed by the API using is forbidden. [optional]  # noqa: E501
            identifier_exists (bool): False when the item does not have unique product identifiers appropriate to its category, such as GTIN, MPN, and brand. Required according to the Unique Product Identifier Rules for all target countries except for Canada.. [optional]  # noqa: E501
            installment (Installment): [optional]  # noqa: E501
            loyalty_points (LoyaltyPoints): [optional]  # noqa: E501
            multipack (int): The number of identical products in a merchant-defined multipack. To avoid any overflow issue, pass it as a string.. [optional]  # noqa: E501
            custom_label0 (str): Custom label 0 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label1 (str): Custom label 1 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label2 (str): Custom label 2 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label3 (str): Custom label 3 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label4 (str): Custom label 4 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            is_bundle (bool): Whether the item is a merchant-defined bundle. A bundle is a custom grouping of different products sold by a merchant for a single price.. [optional]  # noqa: E501
            mobile_link (str): accounts.link to a mobile-optimized version of the landing page.. [optional]  # noqa: E501
            availability_date (str): The day a pre-ordered product becomes available for delivery, in ISO 8601 format.. [optional]  # noqa: E501
            shipping_label (str): The shipping label of the product, used to group product in account-level shipping rules.. [optional]  # noqa: E501
            unit_pricing_measure (ProductUnitPricingMeasure): [optional]  # noqa: E501
            unit_pricing_base_measure (ProductUnitPricingBaseMeasure): [optional]  # noqa: E501
            shipping_length (ProductShippingDimension): [optional]  # noqa: E501
            shipping_width (ProductShippingDimension): [optional]  # noqa: E501
            shipping_height (ProductShippingDimension): [optional]  # noqa: E501
            display_ads_id (str): An identifier for an item for dynamic remarketing campaigns.. [optional]  # noqa: E501
            display_ads_similar_ids ([str]): Advertiser-specified recommendations.. [optional]  # noqa: E501
            display_ads_title (str): Title of an item for dynamic remarketing campaigns.. [optional]  # noqa: E501
            display_ads_link (str): URL directly to your item's landing page for dynamic remarketing campaigns.. [optional]  # noqa: E501
            display_ads_value (float): Offer margin for dynamic remarketing campaigns.. [optional]  # noqa: E501
            sell_on_google_quantity (int): The quantity of the product that is available for selling on Google. Supported only for online products.. [optional]  # noqa: E501
            promotion_ids ([str]): The unique ID of a promotion.. [optional]  # noqa: E501
            max_handling_time (int): Maximal product handling time (in business days).. [optional]  # noqa: E501
            min_handling_time (int): Minimal product handling time (in business days).. [optional]  # noqa: E501
            cost_of_goods_sold (Price): [optional]  # noqa: E501
            source (str): The source of the offer, i.e., how the offer was created.. [optional]  # noqa: E501
            included_destinations ([str]): The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in excludedDestinations.. [optional]  # noqa: E501
            excluded_destinations ([str]): The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).. [optional]  # noqa: E501
            ads_grouping (str): Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise.. [optional]  # noqa: E501
            ads_labels ([str]): Similar to adsGrouping, but only works on CPC.. [optional]  # noqa: E501
            ads_redirect (str): Allows advertisers to override the item URL when the product is shown within the context of Product Ads.. [optional]  # noqa: E501
            product_types ([str]): Categories of the item (formatted as in products data specification).. [optional]  # noqa: E501
            age_group (str): Target age group of the item.. [optional]  # noqa: E501
            availability (str): Availability status of the item. RECOMMENDED.. [optional]  # noqa: E501
            condition (str): Condition or state of the item.. [optional]  # noqa: E501
            gender (str): Target gender of the item.. [optional]  # noqa: E501
            size_system (str): System in which the size is specified. Recommended for apparel items.. [optional]  # noqa: E501
            size_type (str): The cut of the item. Recommended for apparel items.. [optional]  # noqa: E501
            energy_efficiency_class (str): The energy efficiency class as defined in EU directive 2010/30/EU.. [optional]  # noqa: E501
            min_energy_efficiency_class (str): The energy efficiency class as defined in EU directive 2010/30/EU.. [optional]  # noqa: E501
            max_energy_efficiency_class (str): The energy efficiency class as defined in EU directive 2010/30/EU.. [optional]  # noqa: E501
            tax_category (str): The tax category of the product, used to configure detailed tax nexus in account-level tax settings.. [optional]  # noqa: E501
            transit_time_label (str): The transit time label of the product, used to group product in account-level transit time tables.. [optional]  # noqa: E501
            seller_id (str): The ID of the seller (case sensitive and 50 UTF8 characters max). This information is required by the Criteo Offsite Ads.. [optional]  # noqa: E501
        """

        channel = kwargs.get('channel', "online")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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

        self.id = id
        self.title = title
        self.link = link
        self.image_link = image_link
        self.channel = channel
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
    def __init__(self, id, title, link, image_link, *args, **kwargs):  # noqa: E501
        """Product - a model defined in OpenAPI

        Args:
            id (str): A unique identifier for the item. Aka Product ID.
            title (str): Title of the item. (500 UTF8 characters max).
            link (str): URL directly linking to your item's page on your website. (1000 UTF8 characters max).
            image_link (str): URL of an image of the item. Supported formats: PNG, JPEG, GIF. (2000 UTF8 characters max). 

        Keyword Args:
            channel (str): The item's channel (online only).. defaults to "online", must be one of ["online", ]  # noqa: E501
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
            offer_id (str): Not used by Criteo.. [optional]  # noqa: E501
            description (str): Description of the item. RECOMMENDED. (5000 UTF8 characters max).. [optional]  # noqa: E501
            additional_image_links ([str]): Additional URLs of images of the item.. [optional]  # noqa: E501
            content_language (str): The two-letter ISO 639-1 language code for the item.. [optional]  # noqa: E501
            target_country (str): The CLDR territory code for the item.. [optional]  # noqa: E501
            expiration_date (str): Date on which the item should expire, as specified upon insertion, in ISO 8601 format.. [optional]  # noqa: E501
            adult (bool): Set to true if the item is targeted towards adults. RECOMMENDED.. [optional]  # noqa: E501
            kind (str): Identifies what kind of resource this is.. [optional]  # noqa: E501
            brand (str): Brand of the item. RECOMMENDED.. [optional]  # noqa: E501
            color (str): Color of the item.. [optional]  # noqa: E501
            google_product_category (str): Google's category of the item (see Google product taxonomy). RECOMMENDED.. [optional]  # noqa: E501
            gtin (str): Global Trade Item Number (GTIN) of the item. RECOMMENDED.. [optional]  # noqa: E501
            item_group_id (str): Shared identifier for all variants of the same product. RECOMMENDED.. [optional]  # noqa: E501
            material (str): The material of which the item is made.. [optional]  # noqa: E501
            mpn (str): Manufacturer Part Number (MPN) of the item. RECOMMENDED.. [optional]  # noqa: E501
            pattern (str): The item's pattern (e.g. polka dots).. [optional]  # noqa: E501
            price (Price): [optional]  # noqa: E501
            sale_price (Price): [optional]  # noqa: E501
            sale_price_effective_date (str): Date range during which the item is on sale.. [optional]  # noqa: E501
            shipping ([ProductShipping]): Shipping rules.. [optional]  # noqa: E501
            shipping_weight (ProductShippingWeight): [optional]  # noqa: E501
            sizes ([str]): Size of the item. RECOMMENDED. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same itemGroupId value.. [optional]  # noqa: E501
            taxes ([ProductTax]): Tax information.. [optional]  # noqa: E501
            custom_attributes ([CustomAttribute]): A list of custom (merchant-provided) attributes. This is useful for submitting attributes not explicitly exposed by the API. Declaring attributes explicitly exposed by the API using is forbidden. [optional]  # noqa: E501
            identifier_exists (bool): False when the item does not have unique product identifiers appropriate to its category, such as GTIN, MPN, and brand. Required according to the Unique Product Identifier Rules for all target countries except for Canada.. [optional]  # noqa: E501
            installment (Installment): [optional]  # noqa: E501
            loyalty_points (LoyaltyPoints): [optional]  # noqa: E501
            multipack (int): The number of identical products in a merchant-defined multipack. To avoid any overflow issue, pass it as a string.. [optional]  # noqa: E501
            custom_label0 (str): Custom label 0 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label1 (str): Custom label 1 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label2 (str): Custom label 2 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label3 (str): Custom label 3 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            custom_label4 (str): Custom label 4 for custom grouping of items in a Shopping campaign.. [optional]  # noqa: E501
            is_bundle (bool): Whether the item is a merchant-defined bundle. A bundle is a custom grouping of different products sold by a merchant for a single price.. [optional]  # noqa: E501
            mobile_link (str): accounts.link to a mobile-optimized version of the landing page.. [optional]  # noqa: E501
            availability_date (str): The day a pre-ordered product becomes available for delivery, in ISO 8601 format.. [optional]  # noqa: E501
            shipping_label (str): The shipping label of the product, used to group product in account-level shipping rules.. [optional]  # noqa: E501
            unit_pricing_measure (ProductUnitPricingMeasure): [optional]  # noqa: E501
            unit_pricing_base_measure (ProductUnitPricingBaseMeasure): [optional]  # noqa: E501
            shipping_length (ProductShippingDimension): [optional]  # noqa: E501
            shipping_width (ProductShippingDimension): [optional]  # noqa: E501
            shipping_height (ProductShippingDimension): [optional]  # noqa: E501
            display_ads_id (str): An identifier for an item for dynamic remarketing campaigns.. [optional]  # noqa: E501
            display_ads_similar_ids ([str]): Advertiser-specified recommendations.. [optional]  # noqa: E501
            display_ads_title (str): Title of an item for dynamic remarketing campaigns.. [optional]  # noqa: E501
            display_ads_link (str): URL directly to your item's landing page for dynamic remarketing campaigns.. [optional]  # noqa: E501
            display_ads_value (float): Offer margin for dynamic remarketing campaigns.. [optional]  # noqa: E501
            sell_on_google_quantity (int): The quantity of the product that is available for selling on Google. Supported only for online products.. [optional]  # noqa: E501
            promotion_ids ([str]): The unique ID of a promotion.. [optional]  # noqa: E501
            max_handling_time (int): Maximal product handling time (in business days).. [optional]  # noqa: E501
            min_handling_time (int): Minimal product handling time (in business days).. [optional]  # noqa: E501
            cost_of_goods_sold (Price): [optional]  # noqa: E501
            source (str): The source of the offer, i.e., how the offer was created.. [optional]  # noqa: E501
            included_destinations ([str]): The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in excludedDestinations.. [optional]  # noqa: E501
            excluded_destinations ([str]): The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).. [optional]  # noqa: E501
            ads_grouping (str): Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise.. [optional]  # noqa: E501
            ads_labels ([str]): Similar to adsGrouping, but only works on CPC.. [optional]  # noqa: E501
            ads_redirect (str): Allows advertisers to override the item URL when the product is shown within the context of Product Ads.. [optional]  # noqa: E501
            product_types ([str]): Categories of the item (formatted as in products data specification).. [optional]  # noqa: E501
            age_group (str): Target age group of the item.. [optional]  # noqa: E501
            availability (str): Availability status of the item. RECOMMENDED.. [optional]  # noqa: E501
            condition (str): Condition or state of the item.. [optional]  # noqa: E501
            gender (str): Target gender of the item.. [optional]  # noqa: E501
            size_system (str): System in which the size is specified. Recommended for apparel items.. [optional]  # noqa: E501
            size_type (str): The cut of the item. Recommended for apparel items.. [optional]  # noqa: E501
            energy_efficiency_class (str): The energy efficiency class as defined in EU directive 2010/30/EU.. [optional]  # noqa: E501
            min_energy_efficiency_class (str): The energy efficiency class as defined in EU directive 2010/30/EU.. [optional]  # noqa: E501
            max_energy_efficiency_class (str): The energy efficiency class as defined in EU directive 2010/30/EU.. [optional]  # noqa: E501
            tax_category (str): The tax category of the product, used to configure detailed tax nexus in account-level tax settings.. [optional]  # noqa: E501
            transit_time_label (str): The transit time label of the product, used to group product in account-level transit time tables.. [optional]  # noqa: E501
            seller_id (str): The ID of the seller (case sensitive and 50 UTF8 characters max). This information is required by the Criteo Offsite Ads.. [optional]  # noqa: E501
        """

        channel = kwargs.get('channel', "online")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.id = id
        self.title = title
        self.link = link
        self.image_link = image_link
        self.channel = channel
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
