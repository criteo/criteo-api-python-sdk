# SellerSearch

request body for the seller search endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | list of accounts to return seller information for. max length of 25 | 
**include_details** | **bool, none_type** | whether to include additional fields beyond the sellerId and retailerId in the response.  May improve performance when set to false. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


