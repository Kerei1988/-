from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, conint, constr

app = FastAPI()
users = []


class User(BaseModel):
    id: conint(ge=1, le=100)
    username: constr(min_length=3, max_length=20)
    age: conint(ge=18, le=65)


@app.get("/users")
async def all_user() -> list[User]:
    return users


@app.post("/user/{username}/{age}")
def create_user(user: User,
                username: str = Path(min_length=3, max_length=20, description='Enter name', example='UrbanName'),
                age: int = Path(ge=16, le=65, description='Enter age', example='30')) -> User:
    if len(users) == 0:
        user.id = 1
        user.username = username
        user.age = age
        users.append(user)
        return user
    user.id = int(max([i.id for i in users])) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int = Path(ge=1, le=100, description='Enter ID user', example='1'),
                username: str = Path(min_length=3, max_length=20, description='Enter name', example='UrbanName'),
                age: int = Path(ge=16, le=65, description='Enter age', example='30')) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int = Path(ge=1, le=100, description='Enter user_id', example='1')) -> list[User]:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return users
    raise HTTPException(status_code=404, detail="User was not found")
