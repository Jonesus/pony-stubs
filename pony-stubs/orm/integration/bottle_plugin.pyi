from typing import Any

from pony.orm.core import db_session as db_session

def is_allowed_exception(e: Any) -> Any: ...

class PonyPlugin:
    name: str
    api: int
    def apply(self, callback: Any, route: Any) -> Any: ...
