import json

from fastapi import FastAPI, Path, HTTPException, Body

app = FastAPI()
users = {"1": "Имя: Example, возраст: 18"}


@app.get("/")
async def welcome():
    return 'Welcome!'


@app.get("/users")
async def all_user() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str = Path(min_length=3, max_length=20, description='Enter name', example='Jon'),
                      age: int = Path(ge=18, le=65, description='Enter age', example='55')) -> str:
    if len(users) == 0:
        user_id = '1'
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"User {user_id} is registered"
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(min_length=1, max_length=100, description='Enter user_id', example='1'),
                      username: str = Path(min_length=3, max_length=20, description='Enter name', example='Jon'),
                      age: int = Path(ge=18, le=65, description='Enter age', example='55')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"


@app.delete("/users/{user_id")
async def delete_user(user_id: str = Path(min_length=1, max_length=100, description='Enter user_id', example='1')) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
