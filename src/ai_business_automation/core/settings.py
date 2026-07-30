from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ai_provider: str = "gemini"

    openai_api_key: str = ""

    gemini_api_key: str = ""

    model_name: str = "gemini-2.5-flash"

    temperature: float = 0.2

    language: str = "pt-BR"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()