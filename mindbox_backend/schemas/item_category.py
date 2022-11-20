from pydantic import BaseModel

from mindbox_backend.schemas.category import CategoryResponse
from mindbox_backend.schemas.item import ItemResponse, ItemWithoutCategoryResponse


class ItemWithCategories(ItemResponse):
    categories: list[CategoryResponse]


class CategoryWithItems(CategoryResponse):
    items: list[ItemWithoutCategoryResponse]


class ItemCategoryResponse(BaseModel):
    item: ItemWithoutCategoryResponse
    category: CategoryResponse

    class Config:
        orm_mode = True
