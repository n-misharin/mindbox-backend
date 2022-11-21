from uuid import UUID

import pytest
from sqlalchemy import select
from starlette import status

from mindbox_backend.config.utils import get_settings
from mindbox_backend.db.models import Item, Category, ItemCategory
from tests.utils import gen_items, gen_categories, gen_category_for_items


class TestItemCategoryEndpoints:
    @staticmethod
    def get_url():
        return f"{get_settings().PATH_PREFIX}"

    @pytest.mark.parametrize(
        "new_items",
        [
            gen_items(1),
            gen_items(5),
            gen_items(50)
        ]
    )
    async def test_get_items(self, client, database, new_items):
        database.add_all(new_items)

        db_items = (await database.scalars(select(Item).order_by(Item.id))).all()
        await database.commit()

        response = await client.get(f"{TestItemCategoryEndpoints.get_url()}/all/items",)

        assert response.status_code == status.HTTP_200_OK
        items = response.json()["items"]

        assert len(items) == len(new_items)
        for i in range(len(items)):
            db_item = db_items[i]
            item = items[i]
            assert item["title"] == db_item.title
            assert item["cost"] == db_item.cost
            assert UUID(item["id"]) == db_item.id

    @pytest.mark.parametrize(
        "new_items",
        [
            gen_items(2),
            gen_items(1),
            gen_items(5),
            gen_items(100)
        ]
    )
    async def test_get_items_pagination(self, client, database, new_items):
        database.add_all(new_items)
        await database.commit()

        response = await client.get(f"{TestItemCategoryEndpoints.get_url()}/all/items",)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["page"] == 1
        assert response.json()["size"] == get_settings().PAGINATION_PAGE_SIZE
        assert response.json()["total"] == len(new_items)

    async def test_get_categories(self, client, database):
        categories = gen_categories(10)
        database.add_all(categories)
        await database.commit()
        db_categories = (await database.scalars(select(Category).order_by(Category.id))).all()

        items = gen_items(10)
        database.add_all(items)
        await database.commit()
        db_items = (await database.scalars(select(Item).order_by(Item.id))).all()

        item_category = gen_category_for_items(db_items, db_categories)
        database.add_all(item_category)
        await database.commit()

        item_category_dict = dict()
        for elem in item_category:
            if str(elem.category_id) not in item_category_dict.keys():
                item_category_dict[str(elem.category_id)] = []
            item_category_dict[str(elem.category_id)].append(str(elem.item_id))

        response = await client.get(f"{TestItemCategoryEndpoints.get_url()}/all/categories")
        categories = response.json()["items"]

        for i in range(len(categories)):
            cur = categories[i]
            assert len(set(e["id"] for e in cur["items"])) == len(set(item_category_dict[cur["id"]]))
            for j in range(len(cur["items"])):
                assert cur["items"][j]["id"] in item_category_dict[cur["id"]]

    async def test_get_pairs(self, client, database):
        categories = gen_categories(10)
        database.add_all(categories)
        await database.commit()
        db_categories = (await database.scalars(select(Category).order_by(Category.id))).all()

        items = gen_items(10)
        database.add_all(items)
        await database.commit()
        db_items = (await database.scalars(select(Item).order_by(Item.id))).all()

        item_category = gen_category_for_items(db_items, db_categories)
        database.add_all(item_category)
        await database.commit()

        assert len(item_category) == len((await database.scalars(select(ItemCategory))).all())

        item_category_dict = dict()
        for elem in item_category:
            if str(elem.category_id) not in item_category_dict.keys():
                item_category_dict[str(elem.category_id)] = []
            item_category_dict[str(elem.category_id)].append(str(elem.item_id))

        response = await client.get(f"{TestItemCategoryEndpoints.get_url()}/all/pairs")
        pairs = response.json()["items"]

        assert response.json()["total"] == len(item_category)
        assert len(pairs) == min(50, len(item_category))
        for pair in pairs:
            assert pair["item"]["id"] in item_category_dict[pair["category"]["id"]]

    # To be continued ...
