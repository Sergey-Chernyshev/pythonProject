# app/routes/admin_routes.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from models import Admin
from schemas.schemas import AdminCreateRequest
import jwt
import datetime
from typing import Dict
from peewee import DoesNotExist
from dependencies import get_current_user

router = APIRouter()

SECRET_KEY = "76HB27y4hhHJHWLDSdkans32"
ALGORITHM = "HS256"

class LoginData(BaseModel):
    username: str
    password: str

def create_jwt_token(username: str) -> str:
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "iat": datetime.datetime.utcnow(),
        "sub": username
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/admin/")
async def create_admin(admin_data: AdminCreateRequest):
    try:
        admin = Admin.create_admin(username=admin_data.username, password=admin_data.password)
        return {"message": "Admin created successfully", "admin": admin.username}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/admin/login/")
async def admin_login(login_data: LoginData):
    try:
        admin = Admin.get(Admin.username == login_data.username)
        if admin.verify_password(login_data.password):
            token = create_jwt_token(login_data.username)
            return {"token": token}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except DoesNotExist:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/admins/")
async def admins_get(current_user: Admin = Depends(get_current_user)):
    admins_filtered = Admin.select(Admin.id, Admin.username).dicts()
    admins = [{'id': admin['id'], 'username': admin['username']} for admin in admins_filtered]
    return admins

@router.delete("/admins/{admin_id}")
async def delete_admin(admin_id: int, current_user: Admin = Depends(get_current_user)):
    try:
        admin = Admin.get(Admin.id == admin_id)
        admin.delete_instance()
        return {"message": "Admin deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Admin not found")
