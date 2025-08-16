from pydantic import BaseModel


class ChatRequest(BaseModel):
    Message : str
