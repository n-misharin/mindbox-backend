from fastapi import APIRouter, Path, Depends, Response, Body, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from mindbox_backend.db.connection.session import get_session
from mindbox_backend.schemas.item import ItemResponse, CreateItemRequest, PutItemRequest
from mindbox_backend.utils.item import get_item_by_id, insert_item, update_item, delete_item_by_id

api_router = APIRouter(
    prefix="/item",
    tags=["Item"],
)


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
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item id=`{item_id}` not found."
        )
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
    item = await insert_item(session, item_request.title, item_request.cost, item_request.categories)
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
    item = await get_item_by_id(session, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item id=`{item_id}` not found."
        )
    try:
        item = await update_item(
            session,
            item,
            item_values.title,
            item_values.cost,
            item_values.categories
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid request data."
        )
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
    item = await get_item_by_id(session, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item id=`{item_id}` not found."
        )
    return await delete_item_by_id(session, item_id)
