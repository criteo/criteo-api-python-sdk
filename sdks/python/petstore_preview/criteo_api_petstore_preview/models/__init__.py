# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from criteo_api_petstore_preview.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_petstore_preview.model.address import Address
from criteo_api_petstore_preview.model.api_response import ApiResponse
from criteo_api_petstore_preview.model.category import Category
from criteo_api_petstore_preview.model.customer import Customer
from criteo_api_petstore_preview.model.order import Order
from criteo_api_petstore_preview.model.pet import Pet
from criteo_api_petstore_preview.model.tag import Tag
from criteo_api_petstore_preview.model.user import User
