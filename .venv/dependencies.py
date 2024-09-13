# app/dependencies.py
from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from models import Admin
from typing import Optional

SECRET_KEY = "76HB27y4hhHJHWLDSdkans32"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> Admin:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        admin = Admin.get(Admin.username == username)
        return admin
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Admin.DoesNotExist:
        raise HTTPException(status_code=401, detail="Admin not found")
