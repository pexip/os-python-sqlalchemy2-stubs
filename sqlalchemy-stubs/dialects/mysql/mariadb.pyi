from typing import Any

from .base import MySQLDialect as MySQLDialect

class MariaDBDialect(MySQLDialect):
    is_mariadb: bool = ...
    name: str = ...

def loader(driver: Any): ...