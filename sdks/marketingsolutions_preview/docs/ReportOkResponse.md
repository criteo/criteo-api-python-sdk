# ReportOkResponse

The report on a given operationToken is ready. The report is available for 4 days

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_details** | [**[ReportDetailErrors]**](ReportDetailErrors.md) | The list of errors with details. | 
**import_request_timestamp** | **str, none_type** | The date when the original batch request was sent. | 
**number_of_products_deleted** | **str, none_type** | The number of products deleted. | 
**number_of_products_in_the_batch** | **str, none_type** | The number of products present in the batch. | 
**number_of_products_upserted** | **str, none_type** | The number of products upserted. | 
**number_of_products_with_errors** | **str, none_type** | The number of products with errors. | 
**number_of_products_with_warnings** | **str, none_type** | The number of products with Warnings. | 
**status** | **str** | The status of the operation. The operation is completed when the status is one of (VALIDATED,VALIDATED_WITH_ERRORS,FAILED) | 
**warning_details** | [**[ReportDetailWarnings]**](ReportDetailWarnings.md) | The list of Warnings with details. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


