# OnSiteRecoRequest

Recommendation request parameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nb_requested_products** | **int** | Amount of products to recommend. | 
**partner_id** | **int** | Id of the partner. | 
**ad_id** | **int** | Id of the Ad. This field is optional, it allows to setup Reco controls at Ad level. | [optional] 
**ad_set_id** | **int** | Id of the AdSet. This field is optional and is resolved automatically for adsets previously configured. | [optional] 
**identity_type** | **str** | Type of the user identifier (CtoBundle, Idfa, Gaid...) Optional if its type is CtoBundle | [optional] 
**user_id** | **str** | Used to retrieve user events from Criteo trackers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


