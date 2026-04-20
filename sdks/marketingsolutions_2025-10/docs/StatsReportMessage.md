# StatsReportMessage

A tabular stats report with column headers and data rows. Each row in 'data' is an array of values matching the order of 'columns'.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **[str], none_type** | List of column names for the report (e.g. campaignId, sellerId, day, impressions, clicks, cost, etc.) | [optional] 
**data** | **[[bool, date, datetime, dict, float, int, list, str, none_type]], none_type** | Array of data rows, each row is an array of values matching the columns order | [optional] 
**links** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Pagination links (empty object if no pagination) | [optional] 
**rows** | **int, none_type** | Total number of data rows in the report | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


