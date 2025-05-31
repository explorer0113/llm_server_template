from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


from settings import openai_settings

# GPT-4o 체인
gpt4_prompt = PromptTemplate.from_template("You are GPT-4. Answer: {input}")
gpt4_model = ChatOpenAI(
    model=openai_settings.model,
    api_key=openai_settings.api_key,
    temperature=0
)
gpt4_chain = gpt4_prompt | gpt4_model