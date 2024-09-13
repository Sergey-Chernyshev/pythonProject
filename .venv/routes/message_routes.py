# app/routes/message_routes.py
from fastapi import APIRouter, HTTPException, Depends
import models
from models import MessagesFromUser, Admin
from schemas.schemas import MessageSchema, MessageSchema
from dependencies import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/message/")
async def send_message(message_data: MessageSchema):
    try:
        message = MessagesFromUser.create(
            phoneNumber=message_data.phoneNumber,
            userName=message_data.userName,
            userEmail=message_data.userEmail,
            userMessage=message_data.userMessage,
            createdAt = datetime.utcnow()
        )
        return {"status": "Message created successfully", "id": message.id}
    except Exception as e:
        print("Error:", str(e))
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/messages/")
async def get_messages(current_user: Admin = Depends(get_current_user)):
    messages = [message for message in MessagesFromUser.select().dicts()]
    return messages
