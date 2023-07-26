# ReportRequestAttributes

Report Request Attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | YYYY-MM-DD, must not be before startDate and not more than 100 days later | 
**report_type** | **str** | One of \&quot;summary\&quot;, \&quot;keyword\&quot;, \&quot;pageType\&quot;, \&quot;productCategory\&quot;, \&quot;product\&quot;, or \&quot;attributedTransactions\&quot; | 
**start_date** | **date** | YYYY-MM-DD | 
**click_attribution_window** | **str** | Defaults to value from campaign or one of \&quot;7D\&quot;, \&quot;14D\&quot;, or \&quot;30D\&quot;. If specified, viewAttributionWindow must also be specified | [optional] 
**format** | **str** | One of \&quot;json\&quot; (default),\&quot;json-compact\&quot;,\&quot;json-newline\&quot; or \&quot;csv\&quot; | [optional]  if omitted the server will use the default value of "json"
**id** | **str** | The id of the campaign or line item.  Either &#39;id&#39; or &#39;ids&#39; must be specified, but not both | [optional] 
**ids** | **[str]** | The ids of the campaigns or line items.  Either &#39;id&#39; or &#39;ids&#39; must be specified, but not both | [optional] 
**revenue_type** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**view_attribution_window** | **str** | Defaults to value from campaign or one of \&quot;none\&quot;, \&quot;1D\&quot;, \&quot;7D\&quot;, \&quot;14D\&quot;, or \&quot;30D\&quot;. If specified, must be less than clickAttributionWindow, which must also be specified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


