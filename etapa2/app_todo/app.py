from fastapi import FastAPI
from etapa2.app_todo.todo import todo_router

app = FastAPI()
app.include_router(todo_router)

