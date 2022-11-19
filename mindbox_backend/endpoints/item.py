from fastapi import APIRouter, Path, Depends, Response, Body
from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from mindbox_backend.db.connection.session import get_session
from mindbox_backend.db.models import Item
from mindbox_backend.schemas.item import ItemResponse, CreateItemRequest, PutItemRequest
from mindbox_backend.schemas.item_category import ItemWithCategories
from mindbox_backend.utils.item import get_item_by_id, insert_item, update_item, delete_item_by_id

api_router = APIRouter(
    prefix="/item",
    tags=["Item"],
)


@api_router.get(
    "/all",
    status_code=status.HTTP_200_OK,
    response_model=Page[ItemWithCategories],
)
async def get_items(
        session: AsyncSession = Depends(get_session)
):
    query = select(Item).order_by(Item.id)
    return await paginate(session, query)


@api_router.get(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=ItemResponse,
)
async def get_item(
        item_id: UUID4 = Path(...),
        session: AsyncSession = Depends(get_session)
):
    item = await get_item_by_id(session, item_id)
    return ItemResponse.from_orm(item)


@api_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ItemResponse,
)
async def add_item(
        item_request: CreateItemRequest = Body(...),
        session: AsyncSession = Depends(get_session)
):
    item = await insert_item(session, item_request.title, item_request.cost)
    return ItemResponse.from_orm(item)


@api_router.put(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=ItemResponse,
)
async def put_item(
        item_id: UUID4 = Path(...),
        item_values: PutItemRequest = Body(...),
        session: AsyncSession = Depends(get_session)
):
    item = await update_item(session, item_id, {key: val for key, val in item_values.dict().items() if val is not None})
    return ItemResponse.from_orm(item)


@api_router.delete(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_class=Response,
)
async def delete_item(
        item_id: UUID4 = Path(...),
        session: AsyncSession = Depends(get_session)
):
    return await delete_item_by_id(session, item_id)
