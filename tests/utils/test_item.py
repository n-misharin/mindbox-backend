import pytest
from sqlalchemy import select

from mindbox_backend.db.models import Item, ItemCategory
from mindbox_backend.utils.category import insert_category
from mindbox_backend.utils.item import insert_item


class TestItemCRUD:
    @pytest.mark.parametrize(
        "new_item",
        [
            {
                "title": "Продукт",
                "cost": 199.99,
            },
            {
                "title": "Продукт 2",
                "cost": 200,
            }
        ]
    )
    async def test_add_item(self, database, new_item):
        item = await insert_item(database, new_item["title"], new_item["cost"])
        db_items = (await database.scalars(select(Item))).all()
        assert len(db_items) == 1
        assert db_items[0].id == item.id
        assert db_items[0].title == new_item["title"]
        assert db_items[0].cost == new_item["cost"]

    @pytest.mark.parametrize(
        "new_item",
        [
            {
                "title": "Ноутбук Lenevo",
                "cost": 100_999.99,
                "categories": [
                    {"title": "Оргтехника"}
                ]
            },
            {
                "title": "Ноутбук Lenevo 2",
                "cost": 200_999,
                "categories": [
                    {"title": "Оргтехника"},
                    {"title": "Компьютеры"}
                ]
            }
        ]
    )
    async def test_add_item_with_categories(self, database, new_item):
        categories_ids = []
        for category in new_item["categories"]:
            added_category = await insert_category(database, category["title"])
            categories_ids.append(added_category.id)
        item = await insert_item(database, new_item["title"], new_item["cost"], categories_ids)
        db_items = (await database.scalars(select(Item))).all()
        db_categories = (await database.scalars(select(ItemCategory))).all()
        assert len(db_items) == 1
        assert len(db_categories) == len(new_item["categories"])
        for db_category in db_categories:
            assert db_category.item_id == item.id
        assert db_items[0].title == new_item["title"] == item.title
        assert db_items[0].cost == new_item["cost"] == item.cost

    # TODO: add tests for select, update and insert
