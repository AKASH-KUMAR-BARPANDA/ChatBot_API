from GROQ_SERVER import GROQ_SERVER_API




def get_bot_response(user_message):
    message = user_message.lower()
    response_from_server = GROQ_SERVER_API.GROQ_Server_INJECTION(message)
    return response_from_server


