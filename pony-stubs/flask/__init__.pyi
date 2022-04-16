from typing import Any

from pony.orm import db_session as db_session

class Pony:
    app: Any
    def __init__(self, app: Any | None = ...) -> None: ...
    def init_app(self, app: Any) -> None: ...
