# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class MessageSchema(BaseModel):
    phoneNumber: str
    userName: str
    userEmail: Optional[EmailStr] = None
    userMessage: Optional[str] = None
    createdAt: Optional[datetime] = None

class LoginData(BaseModel):
    username: str
    password: str

class AdminCreateRequest(BaseModel):
    username: str
    password: str