from pydantic import BaseModel, UUID4, Field


class CreateCategoryRequest(BaseModel):
    title: str = Field(max_length=50)


class CategoryResponse(CreateCategoryRequest):
    id: UUID4

    class Config:
        orm_mode = True
