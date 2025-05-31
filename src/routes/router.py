from fastapi import APIRouter
from langserve import add_routes
from chains import gpt_chain, claude_chain, gemini_chain

router = APIRouter()

add_routes(router, gpt_chain, path="/gpt")
add_routes(router, claude_chain, path="/claude")
add_routes(router, gemini_chain, path="/gemini")