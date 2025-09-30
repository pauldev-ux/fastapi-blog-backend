#app/config.py
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()

class Settings(BaseModel):
    DATABASE_URL : str = os.getenv("DATABASE_URL")
    ENV : str = os.getenv("ENV", "dev")

settings = Settings()
