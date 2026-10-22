# OnSiteRecoRequestConversational

Conversational recommendation request parameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_set_id** | **int** | Id of the AdSet. This field is optional and is resolved automatically for adsets previously configured. | 
**conversation** | [**[OnSiteRecoChatMessage]**](OnSiteRecoChatMessage.md) | Conversation between the user and the agent. | 
**nb_requested_products** | **int** | Amount of products to recommend. | 
**partner_id** | **int** | Id of the partner. | 
**user_id** | **str** | One user identifier: a Criteo bundle, GAID, IDFA, internal user id, or an agentic partner user id. | 
**ad_id** | **int** | Id of the Ad. This field is optional, it allows to setup Reco controls at Ad level. | [optional] 
**identity_type** | **str** | Type of the user identifier (CtoBundle, Idfa, Gaid, AgenticUserId...) Optional if its type is CtoBundle | [optional] 
**product** | [**ProductContext**](ProductContext.md) |  | [optional] 
**user_id_origin** | **str** | When IdentityType is AgenticUserId, the issuer should recognize themselves with their organization name issued by Criteo. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


