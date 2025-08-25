# from pydantic import BaseSettings untuk dibawah <2.0.0
from pydantic import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables.

    Providing sensible defaults here allows the application and its tests to
    run out of the box without requiring a separate ``.env`` file.  The
    values can still be overridden via environment variables when needed.
    """

    SECRET_KEY: str = "change-me"  # nosec B105 - used for tests only
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite:///./test.db"

    # class Config:
    #     env_file = ".env"
    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()
