from pydantic import BaseSettings, Field

class OpenAISettings(BaseSettings):
    api_key: str = Field(..., env="OPENAI_API_KEY")
    model: str = "gpt-4o"

openai_settings = OpenAISettings()