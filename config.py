import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OLLAMA_URL = os.getenv("OLLAMA_URL", "https://api.ollama.ai")
    OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-v3.2:cloud")

    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()