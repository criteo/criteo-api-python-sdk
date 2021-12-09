import re
import sys

from criteo_api_sdk.api.analytics_api import AnalyticsApi
from criteo_api_sdk.models import StatisticsReportQueryMessage
from criteo_api_sdk import Configuration, ApiClient

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration(username=sys.argv[1], password=sys.argv[2])

    client = ApiClient(configuration)

    api = AnalyticsApi(client)
    stats_query_message = StatisticsReportQueryMessage(
        dimensions=["AdsetId"],
        metrics=["Clicks"],
        start_date="2019-01-01",
        end_date="2019-01-31",
        currency="EUR",
        format="Csv")

    # Use the method with 'with_http_info' if you want to retrieve the filename
    # Otherwise, you can directly call the get_adset_report method
    [response_content, http_code, response_headers] = api.get_adset_report_with_http_info(statistics_report_query_message=stats_query_message)
    if 200 == http_code:
        content_disposition = response_headers["Content-Disposition"]
        if content_disposition:
            print(response_content)
