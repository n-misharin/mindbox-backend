from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from mindbox_backend.db.connection.session import get_session
from mindbox_backend.db.models import ItemCategory, Item, Category
from mindbox_backend.schemas.item_category import ItemCategoryResponse, ItemWithCategories, CategoryWithItems

api_router = APIRouter(
    prefix="/all",
    tags=["All"],
)


@api_router.get(
    "/pairs",
    status_code=status.HTTP_200_OK,
    response_model=Page[ItemCategoryResponse],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    query = select(ItemCategory).order_by(ItemCategory.item_id)
    print("------------>", [i.__dict__ for i in (await session.scalars(query))])
    return await paginate(session, query)


@api_router.get(
    "/items",
    status_code=status.HTTP_200_OK,
    response_model=Page[ItemWithCategories],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    query = select(Item).order_by(Item.id)
    return await paginate(session, query)


@api_router.get(
    "/categories",
    status_code=status.HTTP_200_OK,
    response_model=Page[CategoryWithItems],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    query = select(Category).order_by(Category.id)
    return await paginate(session, query)
