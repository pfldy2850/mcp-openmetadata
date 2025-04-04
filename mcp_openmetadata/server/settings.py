from typing import Optional

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # openmetadata settings
    openmetadata_uri: str

    # one of basic auth or jwt token should be provided
    openmetadata_basic_username: Optional[str] = None
    openmetadata_basic_password: Optional[str] = None
    openmetadata_jwt_token: Optional[str] = None

    # mcp settings
    tools: Optional[str] = (
        "search_entities_with_query"  # comma separated tools to mount
    )

    model_config = SettingsConfigDict()

    @model_validator(mode="after")
    def validate_auth(self):
        if self.openmetadata_basic_username and self.openmetadata_basic_password:
            return self
        if self.openmetadata_jwt_token:
            return self
        raise ValueError("one of basic auth or jwt token should be provided")

    @property
    def authorization(self) -> dict:
        if self.openmetadata_basic_username and self.openmetadata_basic_password:
            return {
                "Authorization": f"Basic {self.openmetadata_basic_username}:{self.openmetadata_basic_password}"
            }
        if self.openmetadata_jwt_token:
            return {"Authorization": f"Bearer {self.openmetadata_jwt_token}"}
        raise ValueError("one of basic auth or jwt token should be provided")
