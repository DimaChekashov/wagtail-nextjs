from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    id: Optional[int] = None
    heading: str
    status: bool = False

todos: List[Todo] = []
current_id = 0

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.post("/todos")
def create_todo(todo: Todo):
    global current_id
    current_id += 1
    todo.id = current_id
    todos.append(todo)
    return {"message": "Todo created!", "todo": todo}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(status_code=404, detail="Todo not found!")