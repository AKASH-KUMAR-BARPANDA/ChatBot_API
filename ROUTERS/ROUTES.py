
from  fastapi import APIRouter
from BASE_PYDANTIC import BASEMODEL
from REPOSITORY import CHAT


router = APIRouter(
    tags = ["CHAT"],
    prefix = '/chats'
)


@router.post('')
def chat( request : BASEMODEL.ChatRequest):
    replay = CHAT.get_bot_response(request.Message)
    return {"replay" : replay}