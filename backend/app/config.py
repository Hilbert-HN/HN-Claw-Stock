"""
HN-Claw-Stock Backend Configuration
"""
from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    # App
    APP_NAME: str = "HN-Claw-Stock"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    
    # API
    API_PREFIX: str = "/api"
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]
    
    # Dashscope AI (for stock analysis)
    DASHSCOPE_API_KEY: Optional[str] = None
    
    # Database
    DATABASE_URL: str = "sqlite:///./data/stocks.db"
    
    # Data
    DATA_DIR: str = "./data"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
