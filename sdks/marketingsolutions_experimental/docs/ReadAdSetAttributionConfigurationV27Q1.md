# ReadAdSetAttributionConfigurationV27Q1

Read model for an ad set's attribution configuration.                The lookback window is only set for ad sets with an attribution method that is postClick or lastClick.  It will be null with any other attribution method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_method** | **str, none_type** | Ad set attribution method.  This defines how certain events (visits, clicks, sales...) are attributed to the ad set.                Note: Old Google Analytics attribution methods (lastClickGoogleAnalytics &#x3D; 2 and googleAnalyticsDataDriven &#x3D; 3) are not supported anymore. Use the new Google Analytics attribution method instead (googleAnalytics).                Possible values:  - unknown  - criteoAttribution (default attribution method)  - lastClick  - postClick  - sftp  - googleAnalytics (requires Google Analytics integration) | [optional] 
**lookback_window** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


