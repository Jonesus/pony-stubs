from typing import Any

from pony import options as options

localbase = object

class PonyDeprecationWarning(DeprecationWarning): ...

def deprecated(stacklevel: Any, message: Any) -> None: ...
def decorator(caller: Any, func: Any | None = ...) -> Any: ...
def decorator_with_params(dec: Any) -> Any: ...
def cut_traceback(func: Any, *args: Any, **kwargs: Any) -> Any: ...

cut_traceback_depth: int

def reraise(exc_type: Any, exc: Any, tb: Any) -> None: ...
def throw(exc_type: Any, *args: Any, **kwargs: Any) -> None: ...
def truncate_repr(s: Any, max_len: int = ...) -> Any: ...

codeobjects: Any

def get_codeobject_id(codeobject: Any) -> Any: ...

lambda_args_cache: Any

def get_lambda_args(func: Any) -> Any: ...
def error_method(*args: Any, **kwargs: Any) -> None: ...
def is_ident(string: Any) -> Any: ...
def split_name(name: Any) -> Any: ...
def uppercase_name(name: Any) -> Any: ...
def lowercase_name(name: Any) -> Any: ...
def camelcase_name(name: Any) -> Any: ...
def mixedcase_name(name: Any) -> Any: ...
def import_module(name: Any) -> Any: ...
def is_absolute_path(filename: Any) -> Any: ...
def absolutize_path(filename: Any, frame_depth: Any) -> Any: ...
def current_timestamp() -> Any: ...
def datetime2timestamp(d: Any) -> Any: ...
def timestamp2datetime(t: Any) -> Any: ...

expr1_re: Any
expr2_re: Any
expr3_re: Any

def parse_expr(s: Any, pos: int = ...) -> Any: ...
def tostring(x: Any) -> Any: ...
def strjoin(
    sep: Any, strings: Any, source_encoding: str = ..., dest_encoding: Any | None = ...
) -> Any: ...
def count(*args: Any, **kwargs: Any) -> Any: ...
def avg(iter: Any) -> Any: ...
def group_concat(items: Any, sep: str = ...) -> Any: ...
def coalesce(*args: Any) -> Any: ...
def distinct(iter: Any) -> Any: ...
def concat(*args: Any) -> Any: ...
def between(x: Any, a: Any, b: Any) -> Any: ...
def is_utf8(encoding: Any) -> Any: ...
def pickle_ast(val: Any) -> Any: ...
def unpickle_ast(pickled: Any) -> Any: ...
def copy_ast(tree: Any) -> Any: ...

class HashableDict(dict[Any, Any]):
    def __hash__(self): ...  # type: ignore
    def __deepcopy__(self, memo: Any) -> Any: ...
    __setitem__: Any
    __delitem__: Any
    clear: Any
    pop: Any
    popitem: Any
    setdefault: Any
    update: Any

def deref_proxy(value: Any) -> Any: ...
def deduplicate(value: Any, deduplication_cache: Any) -> Any: ...
