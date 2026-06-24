
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from criteo_api_retailmedia_experimental.api.accounts_api import AccountsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from criteo_api_retailmedia_experimental.api.accounts_api import AccountsApi
from criteo_api_retailmedia_experimental.api.analytics_api import AnalyticsApi
from criteo_api_retailmedia_experimental.api.audience_api import AudienceApi
from criteo_api_retailmedia_experimental.api.balance_api import BalanceApi
from criteo_api_retailmedia_experimental.api.campaign_api import CampaignApi
from criteo_api_retailmedia_experimental.api.catalog_api import CatalogApi
from criteo_api_retailmedia_experimental.api.gateway_api import GatewayApi
from criteo_api_retailmedia_experimental.api.on_site_recommendation_api import OnSiteRecommendationApi
from criteo_api_retailmedia_experimental.api.third_party_accounts_api import ThirdPartyAccountsApi
