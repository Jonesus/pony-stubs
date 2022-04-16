from typing import Any

from pony.orm import core as core
from pony.orm.core import DBSchemaError as DBSchemaError
from pony.orm.core import MappingError as MappingError
from pony.orm.core import log_sql as log_sql
from pony.py23compat import int_types as int_types
from pony.utils import throw as throw

class DBSchema:
    dialect: Any
    inline_fk_syntax: bool
    named_foreign_keys: bool
    def __init__(schema, provider: Any, uppercase: bool = ...) -> None: ...
    def column_list(schema, columns: Any) -> Any: ...
    def case(schema, s: Any) -> Any: ...
    def add_table(schema, table_name: Any, entity: Any | None = ...) -> Any: ...
    def order_tables_to_create(schema) -> Any: ...
    def generate_create_script(schema) -> Any: ...
    def create_tables(schema, provider: Any, connection: Any) -> None: ...
    def check_tables(schema, provider: Any, connection: Any) -> Any: ...

class DBObject:
    def create(table, provider: Any, connection: Any) -> None: ...

class Table(DBObject):
    typename: str
    def __init__(table, name: Any, schema: Any, entity: Any | None = ...) -> None: ...
    def add_entity(table, entity: Any) -> None: ...
    def exists(
        table, provider: Any, connection: Any, case_sensitive: bool = ...
    ) -> Any: ...
    def get_create_command(table) -> Any: ...
    def format_option(table, name: Any, value: Any) -> Any: ...
    def get_objects_to_create(table, created_tables: Any | None = ...) -> Any: ...
    def add_column(
        table,
        column_name: Any,
        sql_type: Any,
        converter: Any,
        is_not_null: Any | None = ...,
        sql_default: Any | None = ...,
    ) -> Any: ...
    def add_index(
        table,
        index_name: Any,
        columns: Any,
        is_pk: bool = ...,
        is_unique: Any | None = ...,
        m2m: bool = ...,
    ) -> Any: ...
    def add_foreign_key(
        table,
        fk_name: Any,
        child_columns: Any,
        parent_table: Any,
        parent_columns: Any,
        index_name: Any | None = ...,
        on_delete: bool = ...,
        interleave: bool = ...,
    ) -> Any: ...

class Column:
    auto_template: str
    def __init__(
        column,
        name: Any,
        table: Any,
        sql_type: Any,
        converter: Any,
        is_not_null: Any | None = ...,
        sql_default: Any | None = ...,
    ) -> None: ...
    def get_sql(column) -> Any: ...

class Constraint(DBObject):
    def __init__(constraint, name: Any, schema: Any) -> None: ...

class DBIndex(Constraint):
    typename: str
    def __init__(
        index,
        name: Any,
        table: Any,
        columns: Any,
        is_pk: bool = ...,
        is_unique: Any | None = ...,
    ) -> None: ...
    def exists(
        index, provider: Any, connection: Any, case_sensitive: bool = ...
    ) -> Any: ...
    def get_sql(index) -> Any: ...
    def get_create_command(index) -> Any: ...

class ForeignKey(Constraint):
    typename: str
    def __init__(
        foreign_key,
        name: Any,
        child_table: Any,
        child_columns: Any,
        parent_table: Any,
        parent_columns: Any,
        index_name: Any,
        on_delete: Any,
        interleave: bool = ...,
    ) -> None: ...
    def exists(
        foreign_key, provider: Any, connection: Any, case_sensitive: bool = ...
    ) -> Any: ...
    def get_sql(foreign_key) -> Any: ...
    def get_create_command(foreign_key) -> Any: ...
