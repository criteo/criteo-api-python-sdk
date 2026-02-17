
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from criteo_api_commercegrid_v2026_01.api.gateway_api import GatewayApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from criteo_api_commercegrid_v2026_01.api.gateway_api import GatewayApi
from criteo_api_commercegrid_v2026_01.api.segment_api import SegmentApi
