#MODEL_PATH = "./model/PredictPeriodOfDay.pkl"
#DATA_PATH = "./data"
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    """
    This class is used to manage the configuration settings for the application.
    """
    MODEL_PATH: Path = Path("./model/PredictPeriodOfDay.pkl")
    DATA_PATH: Path = Path("./data/periods.csv")
    LOGGING_PATH: Path = Path("./logs/app.log")
    LOGGING_LEVEL: str = "INFO"
    LOGGING_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOGGING_DATEFMT: str = "%Y-%m-%d %H:%M:%S"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()    

