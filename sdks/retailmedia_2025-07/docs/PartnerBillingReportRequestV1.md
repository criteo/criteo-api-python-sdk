# PartnerBillingReportRequestV1

The request object of a Partner Billing Report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | End date of the report (ISO 8601 format, e.g. YYYY-MM-DD). | 
**start_date** | **date** | Start date of the report (ISO 8601 format, e.g. YYYY-MM-DD). | 
**account_ids** | **[str], none_type** | On which accounts the report is created. | [optional] 
**format** | **str** | Format type of the report. | [optional]  if omitted the server will use the default value of "json"
**retailer_ids** | **[int], none_type** | On which retailers the report is created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


