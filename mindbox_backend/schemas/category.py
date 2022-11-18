from pydantic import BaseModel, UUID4


class CreateCategoryRequest(BaseModel):
    title: str


class CategoryResponse(CreateCategoryRequest):
    id: UUID4

    class Config:
        orm_mode = True
