# CatalogIngestionReport

Identification, timing and status of a single catalog ingestion. The summary report of the same ingestion repeats these fields and adds its volume, delta and data quality.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_id** | **str, none_type** |  | [optional] 
**duration** | **str, none_type** |  | [optional] 
**end_time** | **datetime, none_type** |  | [optional] 
**ingestion_status** | [**IngestionStatus**](IngestionStatus.md) |  | [optional] 
**ingestion_type** | [**IngestionType**](IngestionType.md) |  | [optional] 
**merchant_id** | **str, none_type** |  | [optional] 
**multi_source_reporting_status** | [**MultiSourceReportingStatus**](MultiSourceReportingStatus.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


