from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from mindbox_backend.db.connection.session import get_session
from mindbox_backend.db.models import Category
from mindbox_backend.schemas.item_category import ItemCategoryResponse, ItemWithCategories, CategoryWithItems
from mindbox_backend.utils.item_category import get_query_for_items_with_categories, \
    get_query_for_pairs_of_item_and_category, get_query_for_categories_with_items

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
    return await paginate(session, get_query_for_pairs_of_item_and_category())


@api_router.get(
    "/items",
    status_code=status.HTTP_200_OK,
    response_model=Page[ItemWithCategories],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    print("-" * 10)
    print("\n".join([
        " ".join([str(i.id)] + [j.title for j in i.items])
        for i in (await session.scalars(select(Category).order_by(Category.id))).all()
    ]))
    print("-" * 10)
    return await paginate(session, get_query_for_items_with_categories())


@api_router.get(
    "/categories",
    status_code=status.HTTP_200_OK,
    response_model=Page[CategoryWithItems],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    return await paginate(session, get_query_for_categories_with_items())
