# ReportOkResponse

The report on a given operationToken is ready. The report is available for 4 days

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the operation. The operation is completed when the status is one of (VALIDATED,VALIDATED_WITH_ERRORS,FAILED) | 
**import_request_timestamp** | **int** | The date when the original batch request was sent. | 
**number_of_products_in_the_batch** | **int** | The number of products present in the batch. | 
**number_of_products_upserted** | **int** | The number of products upserted. | 
**number_of_products_deleted** | **int** | The number of products deleted. | 
**number_of_products_with_errors** | **int** | The number of products with errors. | 
**error_details** | [**[ReportDetailErrors]**](ReportDetailErrors.md) | The list of errors with details. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


