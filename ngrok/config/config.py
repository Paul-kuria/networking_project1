import os
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

class Configuration(BaseSettings):
    """Simplified config that works in both Lambda and local dev"""
    # Weather Underground
    NGROK_AUTH_TOKEN: str = os.getenv("NGROK_AUTH_TOKEN")
    NGROK_API_KEY1: str = os.getenv("NGROK_API_KEY1")

    # Defaults
    TIMEZONE: str = "Africa/Nairobi"
    LOG_LEVEL: str = "INFO"

        
# Singleton instance
configuration = Configuration()
