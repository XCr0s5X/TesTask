from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    debug: bool = True
    env: str | None = None

    class Config:
        env_file = "../.env"  # відносно робочої директорії при запуску через docker-compose
        env_file_encoding = "utf-8"


settings = Settings()
