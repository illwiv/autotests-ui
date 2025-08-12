from dataclasses import field
from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше 0")
    tags: list[str] = field(default_factory=list)
    market: Market




product_data = {
    "name": "Phone",
    "price": 123,
    "tags": ["phone"],
    "market": {
        "id": 10,
        "name": "PhoneM",
    }

}

phone = Product(**product_data)
print(phone.market)


new_product = Product(name="Phone", price=123, tags=["phone"], market=Market(id=10, name="PhoneM"))
print(new_product)
