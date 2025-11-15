from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./offers.db"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
