from mindbox_backend.endpoints.item import api_router as item_router
from mindbox_backend.endpoints.category import api_router as category_router
from mindbox_backend.endpoints.item_category import api_router as item_category_router


list_of_routes = [
    item_router,
    category_router,
    item_category_router,
]
