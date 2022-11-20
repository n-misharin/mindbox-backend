from pydantic import BaseModel, UUID4

from mindbox_backend.schemas.category import CategoryResponse


class CreateItemRequest(BaseModel):
    title: str
    cost: float
    categories: list[UUID4] | None


class PutItemRequest(CreateItemRequest):
    pass


class ItemResponse(CreateItemRequest):
    id: UUID4
    categories: list[CategoryResponse]

    class Config:
        orm_mode = True
