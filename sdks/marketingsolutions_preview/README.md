# Criteo API SDK for Python

## Introduction

API Client Libraries can facilitate your use of the Criteo API allowing you to build unique and customized solutions to serve your businesses and clients.
These libraries can reduce the amount of code you need to write in order to start accessing Criteo programmatically. They also can help expedite troubleshooting, should you encounter any issues.

More information: [https://developers.criteo.com/marketing-solutions/docs/python-api-client-library](https://developers.criteo.com/marketing-solutions/docs/python-api-client-library)

[![](https://img.shields.io/pypi/pyversions/criteo-marketing.svg)](https://pypi.org/project/criteo-marketing-transition/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 
- Package version: preview.1.211117

## Requirements

Python 2.7 and 3.5+

## Installation & Usage
### pip install

```sh
pip install criteo_api_marketingsolutions_preview
```
(you may need to run `pip` with root permission: `sudo pip install criteo_api_marketingsolutions_preview`)

Then import the package:
```python
import criteo_api_marketingsolutions_preview 
```

### Manual Installation using [Setuptools](http://pypi.python.org/pypi/setuptools)

Download the code or clone the repository locally, then execute the following command:

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import criteo_api_marketingsolutions_preview
```

## Example
Please see [examples/](examples/) for full examples to get a valid token and make a call to the API.

```sh
python ./examples/portfolio.py [client_id] [client_secret]
```

## Documentation for API Endpoints

The developers documentation is available at: *https://developers.criteo.com*.

All URIs are relative to *https://api.criteo.com*.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------


## Documentation For Models

 - [AdSetDeliveryLimitations](docs/AdSetDeliveryLimitations.md)
 - [AdSetFrequencyCapping](docs/AdSetFrequencyCapping.md)
 - [AdSetGeoLocation](docs/AdSetGeoLocation.md)
 - [AdSetSearchFilter](docs/AdSetSearchFilter.md)
 - [AdSetTargeting](docs/AdSetTargeting.md)
 - [AdSetTargetingRule](docs/AdSetTargetingRule.md)
 - [Audience](docs/Audience.md)
 - [AudienceAttributes](docs/AudienceAttributes.md)
 - [AudienceError](docs/AudienceError.md)
 - [AudienceNameDescription](docs/AudienceNameDescription.md)
 - [AudienceWarning](docs/AudienceWarning.md)
 - [BasicAudienceDefinition](docs/BasicAudienceDefinition.md)
 - [BidMessage](docs/BidMessage.md)
 - [CampaignBidChangeRequest](docs/CampaignBidChangeRequest.md)
 - [CampaignBidChangeResponse](docs/CampaignBidChangeResponse.md)
 - [CampaignBidChangeResponseMessageWithDetails](docs/CampaignBidChangeResponseMessageWithDetails.md)
 - [CampaignBidMessage](docs/CampaignBidMessage.md)
 - [CampaignMessage](docs/CampaignMessage.md)
 - [CategoryBidChangeRequest](docs/CategoryBidChangeRequest.md)
 - [CategoryBidMessage](docs/CategoryBidMessage.md)
 - [CategoryMessage](docs/CategoryMessage.md)
 - [CategoryUpdateError](docs/CategoryUpdateError.md)
 - [CategoryUpdateInput](docs/CategoryUpdateInput.md)
 - [CategoryUpdatesPerCatalog](docs/CategoryUpdatesPerCatalog.md)
 - [CategoryUpdatesPerCatalogError](docs/CategoryUpdatesPerCatalogError.md)
 - [CategoryUpdatesPerCatalogErrorMessageWithDetails](docs/CategoryUpdatesPerCatalogErrorMessageWithDetails.md)
 - [ContactlistAmendment](docs/ContactlistAmendment.md)
 - [ContactlistAmendmentAttributes](docs/ContactlistAmendmentAttributes.md)
 - [ContactlistAmendmentRequest](docs/ContactlistAmendmentRequest.md)
 - [ContactlistOperation](docs/ContactlistOperation.md)
 - [ContactlistOperationAttributes](docs/ContactlistOperationAttributes.md)
 - [CriteoApiDataOfPortfolioMessage](docs/CriteoApiDataOfPortfolioMessage.md)
 - [CriteoApiError](docs/CriteoApiError.md)
 - [CriteoApiWarning](docs/CriteoApiWarning.md)
 - [DeleteAudienceContactListResponse](docs/DeleteAudienceContactListResponse.md)
 - [DeleteAudienceResponse](docs/DeleteAudienceResponse.md)
 - [ErrorCodeResponse](docs/ErrorCodeResponse.md)
 - [ErrorMessage](docs/ErrorMessage.md)
 - [GetAudiencesResponse](docs/GetAudiencesResponse.md)
 - [GetPortfolioResponse](docs/GetPortfolioResponse.md)
 - [JwtModel](docs/JwtModel.md)
 - [ModifyAudienceResponse](docs/ModifyAudienceResponse.md)
 - [NewAudience](docs/NewAudience.md)
 - [NewAudienceAttributes](docs/NewAudienceAttributes.md)
 - [NewAudienceRequest](docs/NewAudienceRequest.md)
 - [NewAudienceResponse](docs/NewAudienceResponse.md)
 - [NillableAdSetTargetingRule](docs/NillableAdSetTargetingRule.md)
 - [NillableDateTime](docs/NillableDateTime.md)
 - [NillableDecimal](docs/NillableDecimal.md)
 - [OAuth2Error](docs/OAuth2Error.md)
 - [PatchAdSet](docs/PatchAdSet.md)
 - [PatchAdSetBidding](docs/PatchAdSetBidding.md)
 - [PatchAdSetBudget](docs/PatchAdSetBudget.md)
 - [PatchAdSetScheduling](docs/PatchAdSetScheduling.md)
 - [PortfolioMessage](docs/PortfolioMessage.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [ReadAdSet](docs/ReadAdSet.md)
 - [ReadAdSetBidding](docs/ReadAdSetBidding.md)
 - [ReadAdSetBudget](docs/ReadAdSetBudget.md)
 - [ReadAdSetSchedule](docs/ReadAdSetSchedule.md)
 - [ReadModelAdSetId](docs/ReadModelAdSetId.md)
 - [ReadModelReadAdSet](docs/ReadModelReadAdSet.md)
 - [ReplaceAudience](docs/ReplaceAudience.md)
 - [ReplaceAudienceRequest](docs/ReplaceAudienceRequest.md)
 - [ReplaceAudienceResponse](docs/ReplaceAudienceResponse.md)
 - [RequestAdSetSearch](docs/RequestAdSetSearch.md)
 - [RequestsAdSetId](docs/RequestsAdSetId.md)
 - [RequestsPatchAdSet](docs/RequestsPatchAdSet.md)
 - [ResponseAdSetId](docs/ResponseAdSetId.md)
 - [ResponseReadAdSet](docs/ResponseReadAdSet.md)
 - [ResponsesAdSetId](docs/ResponsesAdSetId.md)
 - [ResponsesReadAdSet](docs/ResponsesReadAdSet.md)
 - [StatisticsReportQueryMessage](docs/StatisticsReportQueryMessage.md)
 - [TransactionsReportQueryDataMessage](docs/TransactionsReportQueryDataMessage.md)
 - [TransactionsReportQueryEntityMessage](docs/TransactionsReportQueryEntityMessage.md)
 - [TransactionsReportQueryMessage](docs/TransactionsReportQueryMessage.md)
 - [WriteModelAdSetId](docs/WriteModelAdSetId.md)
 - [WriteModelPatchAdSet](docs/WriteModelPatchAdSet.md)


## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.