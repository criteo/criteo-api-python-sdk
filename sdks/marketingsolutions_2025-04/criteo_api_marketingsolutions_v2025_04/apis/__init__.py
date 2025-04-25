
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from criteo_api_marketingsolutions_v2025_04.api.advertiser_api import AdvertiserApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from criteo_api_marketingsolutions_v2025_04.api.advertiser_api import AdvertiserApi
from criteo_api_marketingsolutions_v2025_04.api.analytics_api import AnalyticsApi
from criteo_api_marketingsolutions_v2025_04.api.audience_api import AudienceApi
from criteo_api_marketingsolutions_v2025_04.api.campaign_api import CampaignApi
from criteo_api_marketingsolutions_v2025_04.api.creative_api import CreativeApi
from criteo_api_marketingsolutions_v2025_04.api.gateway_api import GatewayApi
