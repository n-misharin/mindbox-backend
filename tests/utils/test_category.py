import pytest
from sqlalchemy import select

from mindbox_backend.db.models import Category
from mindbox_backend.utils.category import insert_category


class TestItemCRUD:
    @pytest.mark.parametrize(
        "new_category",
        [
            {"title": "Категория 2"},
            {"title": "Категория 1"}
        ]
    )
    async def test_add_item(self, database, new_category):
        category = await insert_category(database, new_category["title"])
        db_categories = (await database.scalars(select(Category))).all()
        assert len(db_categories) == 1
        assert db_categories[0].id == category.id
        assert db_categories[0].title == new_category["title"]

    # TODO: add tests for select, update and insert
