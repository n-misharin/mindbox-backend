from fastapi import APIRouter, Depends, Path, Response, Body
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from mindbox_backend.db.connection.session import get_session
from mindbox_backend.schemas.category import CategoryResponse, CreateCategoryRequest
from mindbox_backend.utils.category import get_category_by_id, insert_category, update_category, delete_category_by_id

api_router = APIRouter(
    prefix="/category",
    tags=["Category"],
)


@api_router.get(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponse,
)
async def get_category(
        category_id: UUID4 = Path(...),
        session: AsyncSession = Depends(get_session),
):
    category = await get_category_by_id(session, category_id)
    return CategoryResponse.from_orm(category)


@api_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryResponse,
)
async def add_category(
        category_request: CreateCategoryRequest = Body(...),
        session: AsyncSession = Depends(get_session),
):
    category = await insert_category(session, category_request.title)
    return CategoryResponse.from_orm(category)


@api_router.put(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponse,
)
async def put_category(
        category_id: UUID4 = Path(...),
        category_values: CreateCategoryRequest = Body(...),
        session: AsyncSession = Depends(get_session),
):
    category = await update_category(session, category_id, category_values.dict())
    return CategoryResponse.from_orm(category)


@api_router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_class=Response,
)
async def delete_category(
        category_id: UUID4 = Path(...),
        session: AsyncSession = Depends(get_session)
):
    return await delete_category_by_id(session, category_id)
