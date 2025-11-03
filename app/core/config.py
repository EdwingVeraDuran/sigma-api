from pydantic import ConfigDict

class Settings(ConfigDict):
    DATABASE_URL: str = ""
    PROJECT_NAME: str = "Sigma API"
    
settings = Settings()