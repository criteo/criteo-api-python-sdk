# PageMeta

Represents metadata for paginated data, including information about the current page, page size,  total items, and  total pages in a search result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page_index** | **int, none_type** | The 0 indexed page index you would like to receive given the page size | [optional]  if omitted the server will use the default value of 0
**current_page_size** | **int, none_type** | The maximum number of items you would like to receive in this request | [optional]  if omitted the server will use the default value of 25
**total_items_across_all_pages** | **int, none_type** | Total Items in search result across all pages | [optional] 
**total_pages** | **int, none_type** | total pages in search result | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


