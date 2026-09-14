# CatalogIngestionSummary

Summary report of a catalog ingestion: identification, timing, status, volume, delta and data quality.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_id** | **str, none_type** |  | [optional] 
**data_quality** | [**CatalogIngestionReportingDataQuality**](CatalogIngestionReportingDataQuality.md) |  | [optional] 
**delta** | [**CatalogIngestionReportingDelta**](CatalogIngestionReportingDelta.md) |  | [optional] 
**duration** | **str, none_type** | Total ingestion processing time as an ISO 8601 duration. | [optional] 
**end_time** | **datetime, none_type** |  | [optional] 
**error** | [**CatalogIngestionReportingError**](CatalogIngestionReportingError.md) |  | [optional] 
**ingestion_status** | [**IngestionStatus**](IngestionStatus.md) |  | [optional] 
**ingestion_type** | [**IngestionType**](IngestionType.md) |  | [optional] 
**merchant_id** | **str, none_type** |  | [optional] 
**merchant_name** | **str, none_type** |  | [optional] 
**multi_source** | [**MultiSourceReporting**](MultiSourceReporting.md) |  | [optional] 
**multi_source_reporting_status** | [**MultiSourceReportingStatus**](MultiSourceReportingStatus.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**trigger** | [**CatalogIngestionReportingTrigger**](CatalogIngestionReportingTrigger.md) |  | [optional] 
**volume** | [**CatalogIngestionReportingVolume**](CatalogIngestionReportingVolume.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


