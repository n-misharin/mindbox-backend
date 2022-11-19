from pydantic import BaseModel

from mindbox_backend.schemas.category import CategoryResponse
from mindbox_backend.schemas.item import ItemResponse


class ItemWithCategories(ItemResponse):
    categories: list[CategoryResponse]


class CategoryWithItems(CategoryResponse):
    items: list[ItemResponse]


class ItemCategoryResponse(BaseModel):
    item: ItemResponse
    category: CategoryResponse

    class Config:
        orm_mode = True
