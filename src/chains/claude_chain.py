from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

from settings import anthropic_settings
# Claude 체인
claude_prompt = PromptTemplate.from_template("You are Claude. Answer: {input}")
claude_model = ChatAnthropic(
    model=anthropic_settings.model,
    api_key=anthropic_settings.api_key,
    temperature=0
)
claude_chain = claude_prompt | claude_model