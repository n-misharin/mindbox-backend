from pydantic import BaseModel, UUID4, Extra, Field


class CreateItemRequest(BaseModel):
    title: str
    cost: float


class PutItemRequest(CreateItemRequest):
    title: str | None
    cost: float | None


class ItemResponse(CreateItemRequest):
    id: UUID4

    class Config:
        orm_mode = True
