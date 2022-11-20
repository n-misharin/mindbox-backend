from sqlalchemy import select

from mindbox_backend.db.models import Item, Category, ItemCategory


def get_query_for_items_with_categories() -> select:
    return select(Item).order_by(Item.id)


def get_query_for_categories_with_items() -> select:
    return select(Category).order_by(Category.id)


def get_query_for_pairs_of_item_and_category() -> select:
    return select(ItemCategory).order_by(ItemCategory.item_id)
