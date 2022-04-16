from typing import Any

class getfullargspec:
    kwonlyargs: Any
    kwonlydefaults: Any
    def __init__(self, f: Any) -> None: ...
    def __iter__(self: Any) -> Any: ...

class FunctionMaker:
    shortsignature: Any
    name: Any
    doc: Any
    module: Any
    annotations: Any
    signature: Any
    dict: Any
    defaults: Any
    def __init__(
        self,
        func: Any | None = ...,
        name: Any | None = ...,
        signature: Any | None = ...,
        defaults: Any | None = ...,
        doc: Any | None = ...,
        module: Any | None = ...,
        funcdict: Any | None = ...,
    ) -> None: ...
    def update(self, func: Any, **kw: Any) -> None: ...
    def make(
        self,
        src_templ: Any,
        evaldict: Any | None = ...,
        addsource: bool = ...,
        **attrs: Any
    ) -> Any: ...
    @classmethod
    def create(
        cls,
        obj: Any,
        body: Any,
        evaldict: Any,
        defaults: Any | None = ...,
        doc: Any | None = ...,
        module: Any | None = ...,
        addsource: bool = ...,
        **attrs: Any
    ) -> Any: ...

def decorator(caller: Any, func: Any | None = ...) -> Any: ...

contextmanager: Any
