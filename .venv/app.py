# app/main.py
from fastapi import FastAPI
import models
from models import initialize_db
from routes import admin_routes, message_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Мое API",
    description="Это пример API с использованием FastAPI и Peewee.",
    version="1.0.0",
    docs_url="/swagger",  # Изменить путь к Swagger UI
)

# Инициализация базы данных
initialize_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любого источника
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы HTTP (GET, POST, PUT, DELETE, и т.д.)
    allow_headers=["*"],  # Разрешает все заголовки
)

# Включение маршрутов
app.include_router(admin_routes.router)
app.include_router(message_routes.router)
