from __future__ import print_function

import logging
import sys
from pprint import pprint

from criteo_api_retailmedia_preview.api.advertiser_api import AdvertiserApi 

from criteo_api_retailmedia_preview import Configuration, ApiClient

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration(username=sys.argv[1], password=sys.argv[2])

    # Enable/Disable debug httplib and criteo_marketing packages
    # logging.basicConfig(level=logging.DEBUG)
    # configuration.debug = True

    client = ApiClient(configuration)

    # Reuse the same client to benefit from the configuration in order to automatically refresh expired token
    api = AdvertiserApi(client)

    portfolio_response = api.api_portfolio_get()
    pprint(portfolio_response)
