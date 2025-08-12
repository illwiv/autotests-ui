from pydantic import BaseModel
from pydantic_core.core_schema import invalid_schema


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "test",
    "email": "test@mail.ru",
    "is_active": True,
}

user = User(**user_data)
print(user)
print(user.is_active)


invalid_data = {
    "id": 6,
    "username": "test",
    "email": "test@mail.ru",
    "is_active": True,
}


invalid_user = User(**invalid_data)
print(invalid_user)