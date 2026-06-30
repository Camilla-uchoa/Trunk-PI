from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    database_url: str = "sqlite:///./database.sqlite3"
    secret_key: str = "trunk-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 480
    upload_dir: str = "./uploads"
    max_upload_size_mb: int = 10

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
BASE_DIR = Path(__file__).resolve().parent.parent.parent