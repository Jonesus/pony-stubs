from typing import Any

from pony.orm import core as core
from pony.orm import dbapiprovider as dbapiprovider
from pony.orm import sqltranslation as sqltranslation
from pony.orm.core import DatabaseError as DatabaseError
from pony.orm.core import TranslationError as TranslationError
from pony.orm.core import log_orm as log_orm
from pony.orm.core import log_sql as log_sql
from pony.orm.dbapiprovider import DBAPIProvider as DBAPIProvider
from pony.orm.dbapiprovider import get_version_tuple as get_version_tuple
from pony.orm.dbapiprovider import wrap_dbapi_exceptions as wrap_dbapi_exceptions
from pony.orm.dbschema import Column as Column
from pony.orm.dbschema import DBObject as DBObject
from pony.orm.dbschema import DBSchema as DBSchema
from pony.orm.dbschema import Table as Table
from pony.orm.ormtypes import Json as Json
from pony.orm.sqlbuilding import SQLBuilder as SQLBuilder
from pony.py23compat import buffer as buffer
from pony.py23compat import int_types as int_types
from pony.utils import is_ident as is_ident
from pony.utils import throw as throw

NoneType: Any

class OraTable(Table):
    def get_objects_to_create(table, created_tables: Any | None = ...) -> Any: ...

class OraSequence(DBObject):
    typename: str
    def __init__(sequence, table: Any, name: Any | None = ...) -> None: ...
    def exists(
        sequence, provider: Any, connection: Any, case_sensitive: bool = ...
    ) -> Any: ...
    def get_create_command(sequence) -> Any: ...

trigger_template: Any

class OraTrigger(DBObject):
    typename: str
    def __init__(trigger, table: Any, column: Any, sequence: Any) -> None: ...
    def exists(
        trigger, provider: Any, connection: Any, case_sensitive: bool = ...
    ) -> Any: ...
    def get_create_command(trigger) -> Any: ...

class OraColumn(Column):
    auto_template: Any

class OraSchema(DBSchema):
    dialect: str
    table_class: Any
    column_class: Any

class OraNoneMonad(sqltranslation.NoneMonad):
    def __init__(monad, value: Any | None = ...) -> None: ...

class OraConstMonad(sqltranslation.ConstMonad):
    @staticmethod
    def new(value: Any) -> Any: ...

class OraTranslator(sqltranslation.SQLTranslator):
    dialect: str
    rowid_support: bool
    json_path_wildcard_syntax: bool
    json_values_are_comparable: bool
    NoneMonad: Any
    ConstMonad: Any

class OraBuilder(SQLBuilder):
    dialect: str
    def INSERT(
        builder, table_name: Any, columns: Any, values: Any, returning: Any | None = ...
    ) -> Any: ...
    def SELECT_FOR_UPDATE(
        builder, nowait: Any, skip_locked: Any, *sections: Any
    ) -> Any: ...
    def SELECT(builder, *sections: Any) -> Any: ...
    def ROWID(builder, *expr_list: Any) -> Any: ...
    def LIMIT(builder, limit: Any, offset: Any | None = ...) -> None: ...
    def TO_REAL(builder, expr: Any) -> Any: ...
    def TO_STR(builder, expr: Any) -> Any: ...
    def DATE(builder, expr: Any) -> Any: ...
    def RANDOM(builder) -> Any: ...
    def MOD(builder, a: Any, b: Any) -> Any: ...
    def DATE_ADD(builder, expr: Any, delta: Any) -> Any: ...
    def DATE_SUB(builder, expr: Any, delta: Any) -> Any: ...
    def DATE_DIFF(builder, expr1: Any, expr2: Any) -> Any: ...
    def DATETIME_ADD(builder, expr: Any, delta: Any) -> Any: ...
    def DATETIME_SUB(builder, expr: Any, delta: Any) -> Any: ...
    def DATETIME_DIFF(builder, expr1: Any, expr2: Any) -> Any: ...
    def build_json_path(builder, path: Any) -> Any: ...
    def JSON_QUERY(builder, expr: Any, path: Any) -> Any: ...
    json_value_type_mapping: Any
    def JSON_VALUE(builder, expr: Any, path: Any, type: Any) -> Any: ...
    def JSON_NONZERO(builder, expr: Any) -> Any: ...
    def JSON_CONTAINS(builder, expr: Any, path: Any, key: Any) -> Any: ...
    def JSON_ARRAY_LENGTH(builder, value: Any) -> None: ...
    def GROUP_CONCAT(
        builder, distinct: Any, expr: Any, sep: Any | None = ...
    ) -> Any: ...

json_item_re: Any

class OraBoolConverter(dbapiprovider.BoolConverter):
    def py2sql(converter, val: Any) -> Any: ...
    def sql2py(converter, val: Any) -> Any: ...
    def sql_type(converter) -> Any: ...

class OraStrConverter(dbapiprovider.StrConverter):
    def validate(converter, val: Any, obj: Any | None = ...) -> Any: ...
    def sql2py(converter, val: Any) -> Any: ...
    def sql_type(converter) -> Any: ...

class OraIntConverter(dbapiprovider.IntConverter):
    signed_types: Any
    unsigned_types: Any
    def init(self, kwargs: Any) -> None: ...

class OraRealConverter(dbapiprovider.RealConverter):
    def sql_type(converter) -> Any: ...

class OraDecimalConverter(dbapiprovider.DecimalConverter):
    def sql_type(converter) -> Any: ...

class OraBlobConverter(dbapiprovider.BlobConverter):
    def sql2py(converter, val: Any) -> Any: ...

class OraDateConverter(dbapiprovider.DateConverter):
    def sql2py(converter, val: Any) -> Any: ...

class OraTimeConverter(dbapiprovider.TimeConverter):
    sql_type_name: str
    def __init__(
        converter, provider: Any, py_type: Any, attr: Any | None = ...
    ) -> None: ...
    def sql2py(converter, val: Any) -> Any: ...
    def py2sql(converter, val: Any) -> Any: ...

class OraTimedeltaConverter(dbapiprovider.TimedeltaConverter):
    sql_type_name: str
    def __init__(
        converter, provider: Any, py_type: Any, attr: Any | None = ...
    ) -> None: ...

class OraDatetimeConverter(dbapiprovider.DatetimeConverter):
    sql_type_name: str

class OraUuidConverter(dbapiprovider.UuidConverter):
    def sql_type(converter) -> Any: ...

class OraJsonConverter(dbapiprovider.JsonConverter):
    json_kwargs: Any
    optimistic: bool
    def sql2py(converter, dbval: Any) -> Any: ...
    def sql_type(converter) -> Any: ...

class OraProvider(DBAPIProvider):
    dialect: str
    paramstyle: str
    max_name_len: int
    table_if_not_exists_syntax: bool
    index_if_not_exists_syntax: bool
    varchar_default_max_len: int
    uint64_support: bool
    dbapi_module: Any
    dbschema_cls: Any
    translator_cls: Any
    sqlbuilder_cls: Any
    name_before_table: str
    converter_classes: Any
    def inspect_connection(provider, connection: Any) -> None: ...
    def should_reconnect(provider, exc: Any) -> Any: ...
    def normalize_name(provider, name: Any) -> Any: ...
    def normalize_vars(provider, vars: Any, vartypes: Any) -> None: ...
    def set_transaction_mode(provider, connection: Any, cache: Any) -> None: ...
    def execute(
        provider,
        cursor: Any,
        sql: Any,
        arguments: Any | None = ...,
        returning_id: bool = ...,
    ) -> Any: ...
    def get_pool(provider, *args: Any, **kwargs: Any) -> Any: ...
    def table_exists(
        provider, connection: Any, table_name: Any, case_sensitive: bool = ...
    ) -> Any: ...
    def index_exists(
        provider,
        connection: Any,
        table_name: Any,
        index_name: Any,
        case_sensitive: bool = ...,
    ) -> Any: ...
    def fk_exists(
        provider,
        connection: Any,
        table_name: Any,
        fk_name: Any,
        case_sensitive: bool = ...,
    ) -> Any: ...
    def table_has_data(provider, connection: Any, table_name: Any) -> Any: ...
    def drop_table(provider, connection: Any, table_name: Any) -> None: ...

provider_cls = OraProvider

def to_int_or_decimal(val: Any) -> Any: ...
def to_decimal(val: Any) -> Any: ...
def output_type_handler(
    cursor: Any, name: Any, defaultType: Any, size: Any, precision: Any, scale: Any
) -> Any: ...

class OraPool:
    forked_pools: Any
    def __init__(pool, **kwargs: Any) -> None: ...
    def connect(pool) -> Any: ...
    def release(pool, con: Any) -> None: ...
    def drop(pool, con: Any) -> None: ...
    def disconnect(pool) -> None: ...

def get_inputsize(arg: Any) -> Any: ...
def set_input_sizes(cursor: Any, arguments: Any) -> None: ...
