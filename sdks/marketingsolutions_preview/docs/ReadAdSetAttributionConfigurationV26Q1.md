# ReadAdSetAttributionConfigurationV26Q1

Read model for an ad set's attribution configuration.                The lookback window is only set for ad sets with an attribution method that is postClick or googleAnalyticsLastClick.  It will be null with any other attribution method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_method** | **str, none_type** | Ad set attribution method.  This defines how certain events (visits, clicks, sales...) are attributed to the ad set.                Possible values:  - unknown  - criteoAttribution (default attribution method)  - googleAnalyticsLastClick (requires Google Analytics integration)  - postClick  - sftp  - googleAnalytics (requires Google Analytics integration) | [optional] 
**lookback_window** | **str, none_type** | The lookback window. Optional, should be specified only for attribution methods PostClick and LastClick. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


