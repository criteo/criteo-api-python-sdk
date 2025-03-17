
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from criteo_api_retailmedia_preview.api.accounts_api import AccountsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from criteo_api_retailmedia_preview.api.accounts_api import AccountsApi
from criteo_api_retailmedia_preview.api.analytics_api import AnalyticsApi
from criteo_api_retailmedia_preview.api.audience_api import AudienceApi
from criteo_api_retailmedia_preview.api.balance_api import BalanceApi
from criteo_api_retailmedia_preview.api.billing_api import BillingApi
from criteo_api_retailmedia_preview.api.campaign_api import CampaignApi
from criteo_api_retailmedia_preview.api.catalog_api import CatalogApi
from criteo_api_retailmedia_preview.api.gateway_api import GatewayApi
from criteo_api_retailmedia_preview.api.on_site_recommendation_api import OnSiteRecommendationApi
