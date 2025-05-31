from pydantic import BaseSettings, Field

class GeminiSettings(BaseSettings):
    api_key: str = Field(..., env="GEMINI_API_KEY")
    model: str = "gemini-1.5-pro-latest"

gemini_settings = GeminiSettings()