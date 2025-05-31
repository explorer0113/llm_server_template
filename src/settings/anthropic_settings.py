from pydantic import BaseSettings, Field

class AnthropicSettings(BaseSettings):
    api_key: str = Field(..., env="ANTHROPIC_API_KEY")
    model: str = "claude-3-opus-20240229"

anthropic_settings = AnthropicSettings()