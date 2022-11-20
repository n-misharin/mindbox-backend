from pydantic import BaseModel, UUID4

from mindbox_backend.schemas.category import CategoryResponse


class CreateItemRequest(BaseModel):
    title: str
    cost: float
    categories: list[UUID4] | None


class PutItemRequest(CreateItemRequest):
    pass


class ItemWithoutCategoryResponse(BaseModel):
    id: UUID4
    title: str
    cost: float

    class Config:
        orm_mode = True


class ItemResponse(CreateItemRequest):
    id: UUID4
    categories: list[CategoryResponse]

    class Config:
        orm_mode = True
