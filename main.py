from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConnection
from schema.user_schema import UserSchema, UserCreate


app = FastAPI()
conn = UserConnection()

@app.get("/", status_code=HTTP_200_OK)
def root():
    return conn.read_all()


@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(user_data: UserSchema):
    data = user_data.model_dump()
    data.pop("id")
    conn.write(data)
    return Response(status_code=HTTP_200_OK)
    
    
@app.get("/api/user/{id}", status_code=HTTP_200_OK)
def get_one(id: int):
    return conn.read_one(id)


@app.delete("/api/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
    
@app.put("/api/update/{id}", status_code=HTTP_204_NO_CONTENT)
def update(user_data: UserSchema, id: str):
    data = user_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
