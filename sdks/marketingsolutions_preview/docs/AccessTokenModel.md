# AccessTokenModel

Access Token to be used with other services

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token issued by the authorization server. | [optional] 
**token_type** | **str** | The type of the token issued. | [optional] 
**refresh_token** | **str, none_type** | The refresh token issued by the authorization server.  /// | [optional] 
**expires_in** | **int** | The lifetime in seconds of the access token.For  example, the value \&quot;3600\&quot; denotes that the access token will  expire in one hour from the time the response was generated.  If omitted, the authorization server SHOULD provide the  expiration time via other means or document the default value. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


