import logging
import os
from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    # App
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


def get_settings():
    log.info("Loading config settings from the environment .............")
    return Settings()
