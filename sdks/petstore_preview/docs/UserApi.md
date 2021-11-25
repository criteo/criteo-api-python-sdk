# criteo_api_petstore_preview.UserApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /user | Create user
[**create_users_with_list_input**](UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
[**get_user_by_name**](UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
[**login_user**](UserApi.md#login_user) | **GET** /user/login | Logs user into the system
[**logout_user**](UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
[**update_user**](UserApi.md#update_user) | **PUT** /user/{username} | Update user


# **create_user**
> User create_user()

Create user

This can only be done by the logged in user.

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from criteo_api_petstore_preview.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user = User(
        id=10,
        username="theUser",
        first_name="John",
        last_name="James",
        email="john@email.com",
        password="12345",
        phone="12345",
        user_status=1,
    ) # User | Created user object (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create user
        api_response = api_instance.create_user(user=user)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| Created user object | [optional]

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_users_with_list_input**
> User create_users_with_list_input()

Creates list of users with given input array

Creates list of users with given input array

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from criteo_api_petstore_preview.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user = [
        User(
            id=10,
            username="theUser",
            first_name="John",
            last_name="James",
            email="john@email.com",
            password="12345",
            phone="12345",
            user_status=1,
        ),
    ] # [User] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates list of users with given input array
        api_response = api_instance.create_users_with_list_input(user=user)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->create_users_with_list_input: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**[User]**](User.md)|  | [optional]

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(username)

Delete user

This can only be done by the logged in user.

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    username = "username_example" # str | The name that needs to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_instance.delete_user(username)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be deleted |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid username supplied |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_name**
> User get_user_by_name(username)

Get user by user name

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from criteo_api_petstore_preview.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    username = "username_example" # str | The name that needs to be fetched. Use user1 for testing. 

    # example passing only required values which don't have defaults set
    try:
        # Get user by user name
        api_response = api_instance.get_user_by_name(username)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->get_user_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be fetched. Use user1 for testing.  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid username supplied |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user**
> str login_user()

Logs user into the system

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    username = "username_example" # str | The user name for login (optional)
    password = "password_example" # str | The password for login in clear text (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Logs user into the system
        api_response = api_instance.login_user(username=username, password=password)
        pprint(api_response)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->login_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user name for login | [optional]
 **password** | **str**| The password for login in clear text | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-Rate-Limit - calls per hour allowed by the user <br>  * X-Expires-After - date in UTC when token expires <br>  |
**400** | Invalid username/password supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_user**
> logout_user()

Logs out current logged in user session

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logs out current logged in user session
        api_instance.logout_user()
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->logout_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(username)

Update user

This can only be done by the logged in user.

### Example

```python
import time
import criteo_api_petstore_preview
from criteo_api_petstore_preview.api import user_api
from criteo_api_petstore_preview.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_petstore_preview.Configuration(
    host = "http://localhost/api/v3"
)


# Enter a context with an instance of the API client
with criteo_api_petstore_preview.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    username = "username_example" # str | name that need to be deleted
    user = User(
        id=10,
        username="theUser",
        first_name="John",
        last_name="James",
        email="john@email.com",
        password="12345",
        phone="12345",
        user_status=1,
    ) # User | Update an existent user in the store (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update user
        api_instance.update_user(username)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update user
        api_instance.update_user(username, user=user)
    except criteo_api_petstore_preview.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| name that need to be deleted |
 **user** | [**User**](User.md)| Update an existent user in the store | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

