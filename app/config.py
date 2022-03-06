import os
from decimal import Decimal
from typing import Optional

from pydantic import BaseSettings

from app.utils.get_project_root import get_project_root


class Settings(BaseSettings):
    some_random_string: str


environment = os.getenv("ENV")
environment_path = ""
if environment:
    environment_path = f".{environment}"

settings = Settings(
    _env_file=f"{get_project_root()}/dot_envs/.env{environment_path}",
    _env_file_encoding="utf-8",
)
