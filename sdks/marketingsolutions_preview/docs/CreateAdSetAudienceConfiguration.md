# CreateAdSetAudienceConfiguration

ad set audience create model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_days_since_last_visit** | **int** | The minimum days since last visit on the advertiser web site for being part of this audience, if not null | [optional] 
**max_days_since_last_visit** | **int** | The maximum days since last visit on the advertiser web site for being part of this audience, if not null | [optional] 
**excluded_audience_ids** | **[str]** | The list of audience ids that define who CANNOT be targeted by the ad set. So far, only contact list are supported here | [optional] 
**audience_website_visitor** | [**AudienceWebsiteVisitor**](AudienceWebsiteVisitor.md) |  | [optional] 
**audience_custom** | [**AudienceCustom**](AudienceCustom.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


