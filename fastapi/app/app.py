from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["ROOT"])
async def root() -> dict:
    return {"Ping": "Pong"}


@app.get("/todo", tags=["todos"])
async def get_todo() -> dict:
    return {"data": todos}


@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "Successfully added todo item."}


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["text"] = body["text"]
            return {"data": f"Successfully updated todo id {id}"}
    return {"data": f"Todo id {id} not found."}


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {"data": "Sucessfully deleted todo id {id}"}
    return {"data": f"Todo id {id} not found."}


todos = [
    {"id": "1", "text": "jogging for 2 hours at 7 am."},
    {"id": "2", "text": "writing a fiction book at 2pm."},
]
