from pydantic import BaseModel, UUID4, validator, Field

from mindbox_backend.schemas.category import CategoryResponse


class CreateItemRequest(BaseModel):
    title: str = Field(max_length=50)
    cost: float = Field(gt=0, le=1_000_000_000)
    categories: list[UUID4] = Field(default=None)

    @validator("cost")
    def cost_validator(cls, cost: float):
        return float("{0:.2f}".format(cost))


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
