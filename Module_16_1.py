from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {"Welcome": 'Главная страница'}


@app.get("/user/admin")
async def admin() -> dict:
    return {"admin": 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def user_id(user_id: int) -> dict:
    return {"user_id": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def user(username: str, age: int) -> dict:
    return {"user": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
