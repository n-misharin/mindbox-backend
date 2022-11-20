import os
import random
from pathlib import Path

from alembic.config import Config
from faker import Faker

from mindbox_backend.db.models import Item

PROJECT_PATH = Path(__file__).parent.parent.resolve()


def make_alembic_config(cmd_opts, base_path: Path = PROJECT_PATH) -> Config:
    """
    Создает объект конфигурации alembic на основе аргументов командной строки,
    подменяет относительные пути на абсолютные.
    """
    path_to_folder = cmd_opts.config

    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(base_path, cmd_opts.config + "alembic.ini")

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name, cmd_opts=cmd_opts)

    alembic_location = config.get_main_option("script_location")
    if not os.path.isabs(alembic_location):
        config.set_main_option("script_location", os.path.join(base_path, path_to_folder + alembic_location))
    if cmd_opts.pg_url:
        config.set_main_option("sqlalchemy.url", cmd_opts.pg_url)

    return config


def gen_items(count: int = 1) -> list[Item]:
    faker = Faker()
    items = []
    for i in range(count):
        title = faker.sentence(nb_words=4)
        cost = random.randint(100, 100_000_000) / 100
        items.append(Item(title=title, cost=cost))
    return items

a = {1, 2, 4, 7}
b = {1, 3, 4, 9}
print(a - b)
