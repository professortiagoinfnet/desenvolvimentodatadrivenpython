from fastapi import APIRouter
from model import Todo, TodoOut

todo_router = APIRouter()

todo_list = ["abacate", "maçã"]

@todo_router.get("/")
async def welcome():
    return {'message': 'Hello World!!!'}

@todo_router.get("/status")
async def status_outro_nome():
    return {'status': 'ok'}

@todo_router.post("/todo")
async def add(item: str):
    todo_list.append(item)
    return {"message": f"item '{item} foi adicionado para todo_list"}

@todo_router.get("/todo")
async def retrieve():
    return {"todo_list": todo_list}

todo_dict = {0: "abacate", 1: "maçã"}

@todo_router.post("/todo_pydantic")
async def add_pydantic(todo_item: Todo):
    todo_dict[todo_item.id] = todo_item.item
    return {"message": f'O item {todo_item.item} com id {todo_item.id} foi adicionado.'}

@todo_router.get("/todo_pydantic")
async def retrieve_pydantic():
    return {"todo_dict": todo_dict}

@todo_router.get("/todo_pydantic/{todo_id}")
async def retrieve_item_pydantic(todo_id: int):
    for id in todo_dict:
        if id == todo_id:
            return {"todo_item": {id: todo_dict[id]}}

    return {"message": f"item com id {todo_id} não foi encontrado."}

@todo_router.get("/todo_min_size_pydantic")
async def retrieve_min_size_pydantic(min_size: int):
    final_dict = {}
    for id in todo_dict:
        if len(todo_dict[id]) > min_size:
            final_dict[id] = todo_dict[id]

    return final_dict

todos = [Todo(id=0, item="abacate"), Todo(id=1, item="maçã")]

@todo_router.get("/todo_semresponsemodel/{todo_id}")
async def retreive_todo_semresponsemodel(todo_id: int):
    for todo in todos:
        if todo_id == todo.id:
            return todo
    return Todo(id=-1, item="")

@todo_router.get("/todo_responsemodel/{todo_id}", response_model=TodoOut)
async def retreive_todo_responsemodel(todo_id: int):
    for todo in todos:
        if todo_id == todo.id:
            return todo

    return Todo(id=-1, item="")

@todo_router.get("/todos_responsemodel", response_model=list[TodoOut])
async def todos_responsemodel():
    return todos



