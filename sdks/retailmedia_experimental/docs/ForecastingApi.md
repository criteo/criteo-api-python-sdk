# criteo_api_retailmedia_experimental.ForecastingApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_onsite_display_forecast**](ForecastingApi.md#compute_onsite_display_forecast) | **POST** /experimental/retail-media/accounts/{account-id}/compute-onsite-display-forecast | /experimental/retail-media/accounts/{account-id}/compute-onsite-display-forecast


# **compute_onsite_display_forecast**
> OnsiteDisplayForecastListResponse compute_onsite_display_forecast(account_id, compute_onsite_display_forecast_request)

/experimental/retail-media/accounts/{account-id}/compute-onsite-display-forecast

Computes a forecast of available impressions and budget for a retailer account. <br /> This endpoint is subject to specific rate limits.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_retailmedia_experimental
from criteo_api_retailmedia_experimental.api import forecasting_api
from criteo_api_retailmedia_experimental.model.compute_onsite_display_forecast_request import ComputeOnsiteDisplayForecastRequest
from criteo_api_retailmedia_experimental.model.onsite_display_forecast_list_response import OnsiteDisplayForecastListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_retailmedia_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_retailmedia_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forecasting_api.ForecastingApi(api_client)
    account_id = "account-id_example" # str | ID of the retailer account for which to compute the onsite display forecast.
    compute_onsite_display_forecast_request = ComputeOnsiteDisplayForecastRequest(
        data=ComputeOnsiteDisplayForecastRequestData(None),
    ) # ComputeOnsiteDisplayForecastRequest | Forecast computation parameters.

    # example passing only required values which don't have defaults set
    try:
        # /experimental/retail-media/accounts/{account-id}/compute-onsite-display-forecast
        api_response = api_instance.compute_onsite_display_forecast(account_id, compute_onsite_display_forecast_request)
        pprint(api_response)
    except criteo_api_retailmedia_experimental.ApiException as e:
        print("Exception when calling ForecastingApi->compute_onsite_display_forecast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the retailer account for which to compute the onsite display forecast. |
 **compute_onsite_display_forecast_request** | [**ComputeOnsiteDisplayForecastRequest**](ComputeOnsiteDisplayForecastRequest.md)| Forecast computation parameters. |

### Return type

[**OnsiteDisplayForecastListResponse**](OnsiteDisplayForecastListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

