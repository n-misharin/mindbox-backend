from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from mindbox_backend.db.connection.session import get_session
from mindbox_backend.db.models import ItemCategory
from mindbox_backend.schemas.item_category import ItemCategoryResponse

api_router = APIRouter(
    prefix="/all",
    tags=["All"],
)


@api_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Page[ItemCategoryResponse],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    query = select(ItemCategory).order_by(ItemCategory.item_id)
    return await paginate(session, query)
