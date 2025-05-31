from langchain.prompts import PromptTemplate
from langchain_google_vertexai import ChatVertexAI

from settings import gemini_settings

# Gemini 체인
gemini_prompt = PromptTemplate.from_template("You are Gemini. Answer: {input}")
gemini_model = ChatVertexAI(
    model=gemini_settings.model,
    project=gemini_settings.project_id,   # Google Cloud용 프로젝트 ID
    location=gemini_settings.location     # ex: "us-central1"
)
gemini_chain = gemini_prompt | gemini_model