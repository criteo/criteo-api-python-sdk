# CampaignAvailability

Information about the availability of a specific campaign type and buy type combination, and page types and environments supported for that combination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy_type** | **str, none_type** | The buy type this object represents availability for | [optional] 
**campaign_type** | **str, none_type** | The type of campaign this object represents availability for | [optional] 
**is_available** | **bool, none_type** | Indicates whether the campaign type and buy type combination is available for the retailer | [optional] 
**valid_combinations** | [**[PageTypeCombination], none_type**](PageTypeCombination.md) | PageType-PageEnvironmentType pairs which are supported for this campaign-buy type combination | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


