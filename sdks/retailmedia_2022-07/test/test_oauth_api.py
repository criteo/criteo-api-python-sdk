import pytest
import os

from criteo_api_retailmedia_v2022_07.configuration import Configuration
from criteo_api_retailmedia_v2022_07.api.o_auth_api import OAuthApi
from criteo_api_retailmedia_v2022_07.api_client import ApiClient
from criteo_api_retailmedia_v2022_07.rest import ApiException

class TestOAuthApi:
  @pytest.fixture(autouse=True)
  def before_each(self):
    self.grant_type = "client_credentials"
    self.client_id = os.environ.get("TEST_CLIENT_ID")
    self.client_secret = os.environ.get("TEST_CLIENT_SECRET")
    self.application_id = os.environ.get("TEST_APPLICATION_ID")
  
    self.client = ApiClient(Configuration(username=self.client_id, password=self.client_secret))

  def test_environment_variables(self):
    assert len(self.client_id) > 0, "Environment variable \"TEST_CLIENT_ID\" not found."
    assert len(self.client_secret) > 0, "Environment variable \"TEST_CLIENT_SECRET\" not found."
    assert len(self.application_id) > 0, "Environment variable \"TEST_APPLICATION_ID\" not found."

  def test_get_token_should_succeed_with_valid_credentials(self):
    # Arrange
    api = OAuthApi(self.client)

    # Act
    http_response = api.get_token(self.grant_type, self.client_id, self.client_secret)

    # Assert
    assert len(http_response.access_token) > 0


  def test_get_token_should_fail_with_invalid_credentials(self):
    # Arrange
    invalid_client_id = "invalid-client-id"
    invalid_client_secret = "invalid-client-secret"
    api = OAuthApi(ApiClient(Configuration(username=invalid_client_id, password=invalid_client_secret)))

    # Act
    try:
      api.get_token(self.grant_type, invalid_client_id, invalid_client_secret)
    # Assert
    except ApiException as exception:
      assert exception.status == 401
