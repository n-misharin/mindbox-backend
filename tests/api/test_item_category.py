from uuid import UUID

import pytest
from starlette import status

from mindbox_backend.config.utils import get_settings
from mindbox_backend.utils.item import insert_item
from tests.utils import gen_items


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
        db_items = []
        for item in new_items:
            db_item = await insert_item(database, item.title, item.cost)
            db_items.append(db_item)
        db_items.sort(key=lambda x: x.id)

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
        for item in new_items:
            await insert_item(database, item.title, item.cost)
        response = await client.get(
            f"{TestItemCategoryEndpoints.get_url()}/all/items",
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["page"] == 1
        assert response.json()["size"] == get_settings().PAGINATION_PAGE_SIZE
        assert response.json()["total"] == len(new_items)

    async def test_get_categories(self):
        pass

