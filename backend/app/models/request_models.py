#creating data validation model
from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

