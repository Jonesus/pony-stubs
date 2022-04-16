from typing import Any

from . import flask, orm, thirdparty, utils  # type: ignore

def detect_mode() -> Any: ...

MODE: Any
MAIN_FILE: Any
MAIN_DIR: Any
PONY_DIR: Any
