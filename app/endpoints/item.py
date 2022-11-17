from fastapi import APIRouter, Path, Depends
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.connection.session import get_session
from app.db.models.item import Item
from app.schemas.item import ItemSchema

api_router = APIRouter(
    prefix="/item",
    tags=["Item"],
)


@api_router.get(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=ItemSchema,
)
async def get_item(
        item_id: UUID4 = Path(...),
        session: AsyncSession = Depends(get_session)
):
    res = await session.scalar(select(Item))
    # item = await get_item_by_id(session, item_id)
    # if item:
    #     return ItemSchema.from_orm(item)
