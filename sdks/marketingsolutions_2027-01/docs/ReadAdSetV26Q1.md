# ReadAdSetV26Q1

Ad set read model.                The ad set is the configuration unit that defines ads delivery. Its binds together the objective, budget,  scheduling, targeting options and ads.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str, none_type** | Advertiser id of the campaign this ad set belongs to  This value is a string-encoded integer. | [optional] 
**attribution_configuration** | [**ReadAdSetAttributionConfigurationV26Q1**](ReadAdSetAttributionConfigurationV26Q1.md) |  | [optional] 
**bidding** | [**ReadAdSetBiddingV26Q1**](ReadAdSetBiddingV26Q1.md) |  | [optional] 
**budget** | [**ReadAdSetBudgetV26Q1**](ReadAdSetBudgetV26Q1.md) |  | [optional] 
**campaign_id** | **str, none_type** | Campaign id this ad set belongs to.                This is a key to a MarketingCampaign entity, which can be retrieved using the MarketingCampaigns endpoints.  This value is a string-encoded integer. | [optional] 
**dataset_id** | **str, none_type** | Dataset id of this ad set  This value is a string-encoded integer. | [optional] 
**destination_environment** | **str, none_type** | The environment that an ad click will lead a user to.                Possible values:  - undefined: the ad set does not specify its destination environment  - web: the ad set lead users to a web page  - app: the ad set lead users to an app | [optional] 
**media_type** | **str, none_type** |  | [optional] 
**name** | **str, none_type** | Name of the ad set | [optional] 
**objective** | **str, none_type** | Ad set objective.                Possible values:  - customAction (previously \&quot;Actions\&quot;)  - clicks  - conversions  - displays  - appPromotion (previously \&quot;Installs\&quot;)  - revenue  - storeConversions  - value  - reach (previously \&quot;ViewedImpressions\&quot;)  - visits  - videoViews (previously \&quot;CompletedVideoViews\&quot;) | [optional] 
**schedule** | [**ReadAdSetScheduleV26Q1**](ReadAdSetScheduleV26Q1.md) |  | [optional] 
**targeting** | [**AdSetTargetingV26Q1**](AdSetTargetingV26Q1.md) |  | [optional] 
**video_channel** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


