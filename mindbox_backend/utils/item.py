from typing import Optional
from uuid import UUID

from sqlalchemy import select, update, delete, and_
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from mindbox_backend.db.models import Item, ItemCategory


async def get_item_by_id(session: AsyncSession, item_id: UUID) -> Item:
    query = select(Item).where(Item.id == item_id)
    item = await session.scalar(query)
    await session.commit()
    return item


async def insert_item(
        session: AsyncSession,
        title: str,
        cost: float,
        categories_ids: Optional[list[UUID]] = None,
) -> Item:
    item = Item(title=title, cost=cost)
    async with session.begin():
        session.add(item)
        await session.flush()
        await session.refresh(item)
        if categories_ids is not None and len(categories_ids) > 0:
            ins_values = []
            for _id in categories_ids:
                ins_values.append({
                    "category_id": str(_id),
                    "item_id": str(item.id)
                })
            query = insert(ItemCategory).values(ins_values)
            await session.execute(query)
    await session.refresh(item)
    return item


async def update_item(
        session: AsyncSession,
        item: Item,
        new_title: str,
        new_cost: float,
        new_categories: Optional[list[UUID]] = None
) -> Item:
    async with session.begin():
        old_item_query = select(ItemCategory.category_id).where(ItemCategory.item_id == item.id)
        old_item_categories = (await session.scalars(old_item_query)).all()
        await session.flush()

        if new_categories is None or len(new_categories) == 0:
            delete_query = delete(ItemCategory).where(ItemCategory.item_id == item.id)
            await session.execute(delete_query)
        else:
            sub_set = set(old_item_categories) - set(new_categories)
            delete_query = delete(ItemCategory).where(
                and_(
                    ItemCategory.category_id.in_(sub_set),
                    ItemCategory.item_id == item.id
                )
            )
            await session.execute(delete_query)
            new_add_category = set(new_categories) - set(old_item_categories)
            session.add_all([
                ItemCategory(
                    category_id=new_item_category,
                    item_id=item.id
                )
                for new_item_category in new_add_category
            ])
        query = update(Item).where(Item.id == item.id).values(
            title=new_title,
            cost=new_cost
        )
        await session.execute(query)
    await session.refresh(item)
    return item


async def delete_item_by_id(session: AsyncSession, item_id: UUID):
    query = delete(Item).where(Item.id == item_id)
    await session.execute(query)
    await session.commit()
