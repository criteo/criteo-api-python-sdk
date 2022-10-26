import re
import sys
from pprint import pprint
from datetime import datetime

from criteo_api_retailmedia_v2022_01.api.analytics_api import AnalyticsApi
from criteo_api_retailmedia_v2022_01.models import StatisticsReportQueryMessage
from criteo_api_retailmedia_v2022_01 import Configuration, ApiClient

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration(username=sys.argv[1], password=sys.argv[2])

    client = ApiClient(configuration)

    api = AnalyticsApi(client)
    stats_query_message = StatisticsReportQueryMessage(
        dimensions=["AdsetId"],
        metrics=["Clicks"],
        start_date=datetime.strptime("2022-07-01", '%Y-%m-%d'),
        end_date=datetime.strptime("2022-07-31", '%Y-%m-%d'),
        currency="EUR",
        format="Csv")

    # Use the method with 'with_http_info' if you want to retrieve the filename
    # Otherwise, you can directly call the get_adset_report method
    response_content = api.get_adset_report(statistics_report_query_message=stats_query_message)
    pprint(response_content)
