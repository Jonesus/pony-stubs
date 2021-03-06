from collections.abc import Generator
from typing import Any

from pony import options as options
from pony import utils as utils
from pony.orm import core as core
from pony.orm.asttranslation import ASTTranslator as ASTTranslator
from pony.orm.asttranslation import TranslationError as TranslationError
from pony.orm.asttranslation import ast2src as ast2src
from pony.orm.asttranslation import create_extractors as create_extractors
from pony.orm.asttranslation import get_child_nodes as get_child_nodes
from pony.orm.core import JOIN as JOIN
from pony.orm.core import Attribute as Attribute
from pony.orm.core import DescWrapper as DescWrapper
from pony.orm.core import EntityMeta as EntityMeta
from pony.orm.core import OptimizationFailed as OptimizationFailed
from pony.orm.core import Query as Query
from pony.orm.core import Set as Set
from pony.orm.core import UseAnotherTranslator as UseAnotherTranslator
from pony.orm.core import const_functions as const_functions
from pony.orm.core import extract_vars as extract_vars
from pony.orm.core import special_functions as special_functions
from pony.orm.decompiling import DecompileError as DecompileError
from pony.orm.decompiling import decompile as decompile
from pony.orm.decompiling import operator_mapping as operator_mapping
from pony.orm.ormtypes import Array as Array
from pony.orm.ormtypes import FuncType as FuncType
from pony.orm.ormtypes import Json as Json
from pony.orm.ormtypes import MethodType as MethodType
from pony.orm.ormtypes import QueryType as QueryType
from pony.orm.ormtypes import RawSQLType as RawSQLType
from pony.orm.ormtypes import SetType as SetType
from pony.orm.ormtypes import are_comparable_types as are_comparable_types
from pony.orm.ormtypes import array_types as array_types
from pony.orm.ormtypes import coerce_types as coerce_types
from pony.orm.ormtypes import comparable_types as comparable_types
from pony.orm.ormtypes import normalize as normalize
from pony.orm.ormtypes import normalize_type as normalize_type
from pony.orm.ormtypes import numeric_types as numeric_types
from pony.orm.ormtypes import raw_sql as raw_sql
from pony.py23compat import PY310 as PY310
from pony.py23compat import buffer as buffer
from pony.py23compat import int_types as int_types
from pony.utils import between as between
from pony.utils import coalesce as coalesce
from pony.utils import concat as concat
from pony.utils import copy_ast as copy_ast
from pony.utils import is_ident as is_ident
from pony.utils import localbase as localbase
from pony.utils import reraise as reraise
from pony.utils import throw as throw

NoneType: Any

def check_comparable(left_monad: Any, right_monad: Any, op: str = ...) -> None: ...

class IncomparableTypesError(TypeError):
    def __init__(exc, type1: Any, type2: Any) -> None: ...

def sqland(items: Any) -> Any: ...
def sqlor(items: Any) -> Any: ...
def join_tables(alias1: Any, alias2: Any, columns1: Any, columns2: Any) -> Any: ...
def type2str(t: Any) -> Any: ...

class Local(localbase):
    def __init__(local) -> None: ...
    @property
    def translator(self) -> Any: ...

translator_counter: Any
local: Any

class SQLTranslator(ASTTranslator):
    dialect: Any
    row_value_syntax: bool
    json_path_wildcard_syntax: bool
    json_values_are_comparable: bool
    rowid_support: bool
    def __enter__(translator) -> None: ...
    def __exit__(translator, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def default_post(translator, node: Any) -> None: ...
    def dispatch(translator, node: Any) -> Any: ...
    def dispatch_external(translator, node: Any) -> None: ...
    def call(translator, method: Any, node: Any) -> Any: ...
    def deepcopy(translator) -> Any: ...
    def __init__(
        translator,
        tree: Any,
        parent_translator: Any,
        code_key: Any | None = ...,
        filter_num: Any | None = ...,
        extractors: Any | None = ...,
        vars: Any | None = ...,
        vartypes: Any | None = ...,
        left_join: bool = ...,
        optimize: Any | None = ...,
    ) -> None: ...
    def init(
        translator,
        tree: Any,
        parent_translator: Any,
        code_key: Any | None = ...,
        filter_num: Any | None = ...,
        extractors: Any | None = ...,
        vars: Any | None = ...,
        vartypes: Any | None = ...,
        left_join: bool = ...,
        optimize: Any | None = ...,
    ) -> Any: ...
    @property
    def namespace(translator) -> Any: ...
    def can_be_optimized(translator) -> Any: ...
    def process_query_qual(
        translator,
        prev_translator: Any,
        prev_limit: Any,
        prev_offset: Any,
        names: Any,
        try_extend_prev_query: bool = ...,
    ) -> None: ...
    def construct_subquery_ast(
        translator,
        limit: Any | None = ...,
        offset: Any | None = ...,
        aliases: Any | None = ...,
        star: Any | None = ...,
        distinct: Any | None = ...,
        is_not_null_checks: bool = ...,
    ) -> Any: ...
    def construct_sql_ast(
        translator,
        limit: Any | None = ...,
        offset: Any | None = ...,
        distinct: Any | None = ...,
        aggr_func_name: Any | None = ...,
        aggr_func_distinct: Any | None = ...,
        sep: Any | None = ...,
        for_update: bool = ...,
        nowait: bool = ...,
        skip_locked: bool = ...,
        is_not_null_checks: bool = ...,
    ) -> Any: ...
    def construct_delete_sql_ast(translator) -> Any: ...
    def get_used_attrs(translator) -> Any: ...
    def without_order(translator) -> Any: ...
    def order_by_numbers(translator, numbers: Any) -> Any: ...
    def order_by_attributes(translator, attrs: Any) -> Any: ...
    def apply_kwfilters(
        translator, filterattrs: Any, original_names: bool = ...
    ) -> Any: ...
    def apply_lambda(
        translator,
        func_id: Any,
        filter_num: Any,
        order_by: Any,
        func_ast: Any,
        argnames: Any,
        original_names: Any,
        extractors: Any,
        vars: Any,
        vartypes: Any,
    ) -> Any: ...
    def preGeneratorExp(translator, node: Any) -> Any: ...
    def postExpr(translator, node: Any) -> Any: ...
    def preCompare(translator, node: Any) -> Any: ...
    def postConstant(translator, node: Any) -> Any: ...
    def postNameConstant(translator, node: Any) -> Any: ...
    def postNum(translator, node: Any) -> Any: ...
    def postStr(translator, node: Any) -> Any: ...
    def postBytes(translator, node: Any) -> Any: ...
    def postList(translator, node: Any) -> Any: ...
    def postTuple(translator, node: Any) -> Any: ...
    def postName(translator, node: Any) -> Any: ...
    def resolve_name(translator, name: Any) -> Any: ...
    def postAdd(translator, node: Any) -> Any: ...
    def postSub(translator, node: Any) -> Any: ...
    def postMult(translator, node: Any) -> Any: ...
    def postMatMult(translator, node: Any) -> None: ...
    def postDiv(translator, node: Any) -> Any: ...
    def postFloorDiv(translator, node: Any) -> Any: ...
    def postMod(translator, node: Any) -> Any: ...
    def postLShift(translator, node: Any) -> None: ...
    def postRShift(translator, node: Any) -> None: ...
    def postPow(translator, node: Any) -> Any: ...
    def postUSub(translator, node: Any) -> Any: ...
    def postAttribute(translator, node: Any) -> Any: ...
    def postAnd(translator, node: Any) -> Any: ...
    def postOr(translator, node: Any) -> Any: ...
    def postBitOr(translator, node: Any) -> Any: ...
    def postBitAnd(translator, node: Any) -> Any: ...
    def postBitXor(translator, node: Any) -> Any: ...
    def postNot(translator, node: Any) -> Any: ...
    def preCall(translator, node: Any) -> Any: ...
    def postCall(translator, node: Any) -> Any: ...
    def postkeyword(translator, node: Any) -> None: ...
    def postSubscript(translator, node: Any) -> Any: ...
    def postSlice(translator, node: Any) -> None: ...
    def postIndex(translator, node: Any) -> Any: ...
    def postIfExp(translator, node: Any) -> Any: ...
    def postJoinedStr(translator, node: Any) -> Any: ...
    def postFormattedValue(translator, node: Any) -> Any: ...

def combine_limit_and_offset(
    limit: Any, offset: Any, limit2: Any, offset2: Any
) -> Any: ...
def coerce_monads(m1: Any, m2: Any, for_comparison: bool = ...) -> Any: ...

max_alias_length: int

class SqlQuery:
    def __init__(
        sqlquery,
        translator: Any,
        parent_sqlquery: Any | None = ...,
        left_join: bool = ...,
    ) -> None: ...
    def get_tableref(sqlquery, name_path: Any) -> Any: ...
    def add_tableref(
        sqlquery, name_path: Any, parent_tableref: Any, attr: Any
    ) -> Any: ...
    def make_alias(sqlquery, name: Any) -> Any: ...
    def join_table(
        sqlquery, parent_alias: Any, alias: Any, table_name: Any, join_cond: Any
    ) -> None: ...

class TableRef:
    def __init__(tableref, sqlquery: Any, name: Any, entity: Any) -> None: ...
    def make_join(tableref, pk_only: bool = ...) -> Any: ...

class ExprTableRef(TableRef):
    def __init__(
        tableref,
        sqlquery: Any,
        name: Any,
        subquery_ast: Any,
        expr_names: Any,
        expr_aliases: Any,
    ) -> None: ...
    def make_join(tableref, pk_only: bool = ...) -> Any: ...

class StarTableRef(TableRef):
    def __init__(
        tableref, sqlquery: Any, name: Any, entity: Any, subquery_ast: Any
    ) -> None: ...
    def make_join(tableref, pk_only: bool = ...) -> Any: ...

class ExprJoinedTableRef:
    def __init__(
        tableref,
        sqlquery: Any,
        parent_tableref: Any,
        parent_columns: Any,
        name: Any,
        entity: Any,
    ) -> None: ...
    def make_join(tableref, pk_only: bool = ...) -> Any: ...

class JoinedTableRef:
    def __init__(
        tableref, sqlquery: Any, name_path: Any, parent_tableref: Any, attr: Any
    ) -> None: ...
    def make_join(tableref, pk_only: bool = ...) -> Any: ...

def wrap_monad_method(cls_name: Any, func: Any) -> Any: ...

class MonadMeta(type):
    def __new__(meta, cls_name: Any, bases: Any, cls_dict: Any) -> Any: ...

class MonadMixin(metaclass=MonadMeta): ...

class Monad(metaclass=MonadMeta):
    disable_distinct: bool
    disable_ordering: bool
    def __init__(monad, type: Any, nullable: bool = ...) -> None: ...
    def mixin_init(monad) -> None: ...
    def to_single_cell_value(monad) -> Any: ...
    def cmp(monad, op: Any, monad2: Any) -> Any: ...
    def contains(monad, item: Any, not_in: bool = ...) -> None: ...
    def nonzero(monad) -> Any: ...
    def negate(monad) -> Any: ...
    def getattr(monad, attrname: Any) -> Any: ...
    def len(monad) -> None: ...
    def count(monad, distinct: Any | None = ...) -> Any: ...
    def aggregate(
        monad, func_name: Any, distinct: Any | None = ..., sep: Any | None = ...
    ) -> Any: ...
    def __call__(monad, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(monad, key: Any) -> None: ...
    def __add__(monad, monad2: Any) -> None: ...
    def __sub__(monad, monad2: Any) -> None: ...
    def __mul__(monad, monad2: Any) -> None: ...
    def __truediv__(monad, monad2: Any) -> None: ...
    def __floordiv__(monad, monad2: Any) -> None: ...
    def __pow__(monad, monad2: Any) -> None: ...
    def __neg__(monad) -> None: ...
    def __or__(monad, monad2: Any) -> None: ...
    def __and__(monad, monad2: Any) -> None: ...
    def __xor__(monad, monad2: Any) -> None: ...
    def abs(monad) -> None: ...
    def cast_from_json(monad, type: Any) -> None: ...
    def to_int(monad) -> Any: ...
    def to_str(monad) -> Any: ...
    def to_real(monad) -> Any: ...

def distinct_from_monad(distinct: Any, default: Any | None = ...) -> Any: ...

class RawSQLMonad(Monad):
    def __init__(monad, rawtype: Any, varkey: Any, nullable: bool = ...) -> None: ...
    def contains(monad, item: Any, not_in: bool = ...) -> Any: ...
    def nonzero(monad) -> Any: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

typeerror_re_1: Any
typeerror_re_2: Any

def reraise_improved_typeerror(
    exc: Any, func_name: Any, orig_func_name: Any
) -> None: ...
def raise_forgot_parentheses(monad: Any) -> None: ...

class MethodMonad(Monad):
    def __init__(monad, parent: Any, attrname: Any) -> None: ...
    def getattr(monad, attrname: Any) -> None: ...
    def __call__(monad, *args: Any, **kwargs: Any) -> Any: ...
    def contains(monad, item: Any, not_in: bool = ...) -> None: ...
    def nonzero(monad) -> None: ...
    def negate(monad) -> None: ...
    def aggregate(
        monad, func_name: Any, distinct: Any | None = ..., sep: Any | None = ...
    ) -> None: ...
    def __getitem__(monad, key: Any) -> None: ...
    def __add__(monad, monad2: Any) -> None: ...
    def __sub__(monad, monad2: Any) -> None: ...
    def __mul__(monad, monad2: Any) -> None: ...
    def __truediv__(monad, monad2: Any) -> None: ...
    def __floordiv__(monad, monad2: Any) -> None: ...
    def __pow__(monad, monad2: Any) -> None: ...
    def __neg__(monad) -> None: ...
    def abs(monad) -> None: ...

class EntityMonad(Monad):
    def __init__(monad, entity: Any) -> None: ...
    def __getitem__(monad, *args: Any) -> None: ...

class ListMonad(Monad):
    def __init__(monad, items: Any) -> None: ...
    def contains(monad, x: Any, not_in: bool = ...) -> Any: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class BufferMixin(MonadMixin): ...
class UuidMixin(MonadMixin): ...

def make_numeric_binop(op: Any, sqlop: Any) -> Any: ...

class NumericMixin(MonadMixin):
    def mixin_init(monad) -> None: ...
    __add__: Any
    __sub__: Any
    __mul__: Any
    __truediv__: Any
    __floordiv__: Any
    __mod__: Any
    __and__: Any
    __or__: Any
    __xor__: Any
    def __pow__(monad, monad2: Any) -> Any: ...
    def __neg__(monad) -> Any: ...
    def abs(monad) -> Any: ...
    def nonzero(monad) -> Any: ...
    def negate(monad) -> Any: ...

def numeric_attr_factory(name: Any) -> Any: ...
def make_datetime_binop(op: Any, sqlop: Any) -> Any: ...

class DateMixin(MonadMixin):
    def mixin_init(monad) -> None: ...
    attr_year: Any
    attr_month: Any
    attr_day: Any
    def __add__(monad, other: Any) -> Any: ...
    def __sub__(monad, other: Any) -> Any: ...

class TimeMixin(MonadMixin):
    def mixin_init(monad) -> None: ...
    attr_hour: Any
    attr_minute: Any
    attr_second: Any

class TimedeltaMixin(MonadMixin):
    def mixin_init(monad) -> None: ...

class DatetimeMixin(DateMixin):
    def mixin_init(monad) -> None: ...
    def call_date(monad) -> Any: ...
    attr_hour: Any
    attr_minute: Any
    attr_second: Any
    def __add__(monad, other: Any) -> Any: ...
    def __sub__(monad, other: Any) -> Any: ...

def make_string_binop(op: Any, sqlop: Any) -> Any: ...
def make_string_func(sqlop: Any) -> Any: ...

class StringMixin(MonadMixin):
    def mixin_init(monad) -> None: ...
    __add__: Any
    def __getitem__(monad, index: Any) -> Any: ...
    def negate(monad) -> Any: ...
    def nonzero(monad) -> Any: ...
    def len(monad) -> Any: ...
    def contains(monad, item: Any, not_in: bool = ...) -> Any: ...
    call_upper: Any
    call_lower: Any
    def call_startswith(monad, arg: Any) -> Any: ...
    def call_endswith(monad, arg: Any) -> Any: ...
    def strip(monad, chars: Any, strip_type: Any) -> Any: ...
    def call_strip(monad, chars: Any | None = ...) -> Any: ...
    def call_lstrip(monad, chars: Any | None = ...) -> Any: ...
    def call_rstrip(monad, chars: Any | None = ...) -> Any: ...

class JsonMixin:
    disable_distinct: bool
    disable_ordering: bool
    def mixin_init(monad) -> None: ...
    def get_path(monad) -> Any: ...
    def __getitem__(monad, key: Any) -> Any: ...
    def contains(monad, key: Any, not_in: bool = ...) -> Any: ...
    def __or__(monad, other: Any) -> Any: ...
    def len(monad) -> Any: ...
    def cast_from_json(monad, type: Any) -> Any: ...
    def nonzero(monad) -> Any: ...

class ArrayMixin(MonadMixin):
    def contains(monad, key: Any, not_in: bool = ...) -> Any: ...
    def len(monad) -> Any: ...
    def nonzero(monad) -> Any: ...
    def __getitem__(monad, index: Any) -> Any: ...

class ObjectMixin(MonadMixin):
    def mixin_init(monad) -> None: ...
    def negate(monad) -> Any: ...
    def nonzero(monad) -> Any: ...
    def getattr(monad, attrname: Any) -> Any: ...
    def requires_distinct(monad, joined: bool = ...) -> Any: ...

class ObjectIterMonad(ObjectMixin, Monad):
    def __init__(monad, tableref: Any, entity: Any) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...
    def requires_distinct(monad, joined: bool = ...) -> Any: ...

class AttrMonad(Monad):
    @staticmethod
    def new(parent: Any, attr: Any, *args: Any, **kwargs: Any) -> Any: ...
    def __new__(cls, *args: Any) -> Any: ...
    def __init__(monad, parent: Any, attr: Any) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class ObjectAttrMonad(ObjectMixin, AttrMonad):
    def __init__(monad, parent: Any, attr: Any) -> None: ...

class StringAttrMonad(StringMixin, AttrMonad): ...
class NumericAttrMonad(NumericMixin, AttrMonad): ...
class DateAttrMonad(DateMixin, AttrMonad): ...
class TimeAttrMonad(TimeMixin, AttrMonad): ...
class TimedeltaAttrMonad(TimedeltaMixin, AttrMonad): ...
class DatetimeAttrMonad(DatetimeMixin, AttrMonad): ...
class BufferAttrMonad(BufferMixin, AttrMonad): ...
class UuidAttrMonad(UuidMixin, AttrMonad): ...
class JsonAttrMonad(JsonMixin, AttrMonad): ...
class ArrayAttrMonad(ArrayMixin, AttrMonad): ...

class ParamMonad(Monad):
    @staticmethod
    def new(t: Any, paramkey: Any) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(monad, t: Any, paramkey: Any) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class ObjectParamMonad(ObjectMixin, ParamMonad):
    def __init__(monad, entity: Any, paramkey: Any) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...
    def requires_distinct(monad, joined: bool = ...) -> None: ...

class StringParamMonad(StringMixin, ParamMonad): ...
class NumericParamMonad(NumericMixin, ParamMonad): ...
class DateParamMonad(DateMixin, ParamMonad): ...
class TimeParamMonad(TimeMixin, ParamMonad): ...
class TimedeltaParamMonad(TimedeltaMixin, ParamMonad): ...
class DatetimeParamMonad(DatetimeMixin, ParamMonad): ...
class BufferParamMonad(BufferMixin, ParamMonad): ...
class UuidParamMonad(UuidMixin, ParamMonad): ...

class ArrayParamMonad(ArrayMixin, ParamMonad):
    def __init__(
        monad, t: Any, paramkey: Any, list_monad: Any | None = ...
    ) -> None: ...
    def contains(monad, key: Any, not_in: bool = ...) -> Any: ...

class JsonParamMonad(JsonMixin, ParamMonad):
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class ExprMonad(Monad):
    @staticmethod
    def new(t: Any, sql: Any, nullable: bool = ...) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(monad, type: Any, sql: Any, nullable: bool = ...) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class ObjectExprMonad(ObjectMixin, ExprMonad):
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class StringExprMonad(StringMixin, ExprMonad): ...
class NumericExprMonad(NumericMixin, ExprMonad): ...
class DateExprMonad(DateMixin, ExprMonad): ...
class TimeExprMonad(TimeMixin, ExprMonad): ...
class TimedeltaExprMonad(TimedeltaMixin, ExprMonad): ...
class DatetimeExprMonad(DatetimeMixin, ExprMonad): ...
class JsonExprMonad(JsonMixin, ExprMonad): ...
class ArrayExprMonad(ArrayMixin, ExprMonad): ...

class JsonItemMonad(JsonMixin, Monad):
    def __init__(monad, parent: Any, key: Any) -> None: ...
    def get_path(monad) -> Any: ...
    def to_int(monad) -> Any: ...
    def to_str(monad) -> Any: ...
    def to_real(monad) -> Any: ...
    def cast_from_json(monad, type: Any) -> Any: ...
    def getsql(monad) -> Any: ...

class ConstMonad(Monad):
    @staticmethod
    def new(value: Any) -> Any: ...
    def __new__(cls, *args: Any) -> Any: ...
    def __init__(monad, value: Any) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class NoneMonad(ConstMonad):
    type: Any
    def __init__(monad, value: Any | None = ...) -> None: ...
    def cmp(monad, op: Any, monad2: Any) -> Any: ...
    def contains(monad, item: Any, not_in: bool = ...) -> Any: ...
    def nonzero(monad) -> Any: ...
    def negate(monad) -> Any: ...
    def getattr(monad, attrname: Any) -> Any: ...
    def len(monad) -> Any: ...
    def count(monad, distinct: Any | None = ...) -> Any: ...
    def aggregate(
        monad, func_name: Any, distinct: Any | None = ..., sep: Any | None = ...
    ) -> Any: ...
    def __call__(monad, *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(monad, key: Any) -> Any: ...
    def __add__(monad, monad2: Any) -> Any: ...
    def __sub__(monad, monad2: Any) -> Any: ...
    def __mul__(monad, monad2: Any) -> Any: ...
    def __truediv__(monad, monad2: Any) -> Any: ...
    def __floordiv__(monad, monad2: Any) -> Any: ...
    def __pow__(monad, monad2: Any) -> Any: ...
    def __neg__(monad) -> Any: ...
    def __or__(monad, monad2: Any) -> Any: ...
    def __and__(monad, monad2: Any) -> Any: ...
    def __xor__(monad, monad2: Any) -> Any: ...
    def abs(monad) -> Any: ...
    def to_int(monad) -> Any: ...
    def to_str(monad) -> Any: ...
    def to_real(monad) -> Any: ...

class EllipsisMonad(ConstMonad): ...

class StringConstMonad(StringMixin, ConstMonad):
    def len(monad) -> Any: ...

class JsonConstMonad(JsonMixin, ConstMonad): ...
class BufferConstMonad(BufferMixin, ConstMonad): ...
class NumericConstMonad(NumericMixin, ConstMonad): ...
class DateConstMonad(DateMixin, ConstMonad): ...
class TimeConstMonad(TimeMixin, ConstMonad): ...
class TimedeltaConstMonad(TimedeltaMixin, ConstMonad): ...
class DatetimeConstMonad(DatetimeMixin, ConstMonad): ...

class BoolMonad(Monad):
    def __init__(monad, nullable: bool = ...) -> None: ...
    def nonzero(monad) -> Any: ...

sql_negation: Any

class BoolExprMonad(BoolMonad):
    def __init__(monad, sql: Any, nullable: bool = ...) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...
    def negate(monad) -> Any: ...

cmp_ops: Any
cmp_negate: Any

class CmpMonad(BoolMonad):
    EQ: str
    NE: str
    def __init__(monad, op: Any, left: Any, right: Any) -> None: ...
    def negate(monad) -> Any: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class LogicalBinOpMonad(BoolMonad):
    def __init__(monad, operands: Any) -> None: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class AndMonad(LogicalBinOpMonad):
    binop: str

class OrMonad(LogicalBinOpMonad):
    binop: str

class NotMonad(BoolMonad):
    def __init__(monad, operand: Any) -> None: ...
    def negate(monad) -> Any: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...

class HybridFuncMonad(Monad):
    def __init__(monad, func_type: Any, func_name: Any, *params: Any) -> None: ...
    def __call__(monad, *args: Any, **kwargs: Any) -> Any: ...

class HybridMethodMonad(HybridFuncMonad):
    def __init__(monad, parent: Any, attrname: Any, func: Any) -> None: ...

registered_functions: Any

class FuncMonadMeta(MonadMeta):
    def __new__(meta, cls_name: Any, bases: Any, cls_dict: Any) -> Any: ...

class FuncMonad(Monad, metaclass=FuncMonadMeta):
    def __call__(monad, *args: Any, **kwargs: Any) -> Any: ...

def get_classes(classinfo: Any) -> Generator[Any, None, None]: ...

class FuncIsinstanceMonad(FuncMonad):
    func: Any
    def call(monad, obj: Any, classinfo: Any) -> Any: ...

class FuncBufferMonad(FuncMonad):
    func: Any
    def call(
        monad, source: Any, encoding: Any | None = ..., errors: Any | None = ...
    ) -> Any: ...

class FuncBoolMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncIntMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncStrMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncFloatMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncDecimalMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncDateMonad(FuncMonad):
    func: Any
    def call(monad, year: Any, month: Any, day: Any) -> Any: ...
    def call_today(monad) -> Any: ...

class FuncTimeMonad(FuncMonad):
    func: Any
    def call(monad, *args: Any) -> Any: ...

class FuncTimedeltaMonad(FuncMonad):
    func: Any
    def call(
        monad,
        days: Any | None = ...,
        seconds: Any | None = ...,
        microseconds: Any | None = ...,
        milliseconds: Any | None = ...,
        minutes: Any | None = ...,
        hours: Any | None = ...,
        weeks: Any | None = ...,
    ) -> Any: ...

class FuncDatetimeMonad(FuncDateMonad):
    func: Any
    def call(
        monad,
        year: Any,
        month: Any,
        day: Any,
        hour: Any | None = ...,
        minute: Any | None = ...,
        second: Any | None = ...,
        microsecond: Any | None = ...,
    ) -> Any: ...
    def call_now(monad) -> Any: ...

class FuncBetweenMonad(FuncMonad):
    func: Any
    def call(monad, x: Any, a: Any, b: Any) -> Any: ...

class FuncConcatMonad(FuncMonad):
    func: Any
    def call(monad, *args: Any) -> Any: ...

class FuncLenMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncGetattrMonad(FuncMonad):
    func: Any
    def call(monad, obj_monad: Any, name_monad: Any) -> Any: ...

class FuncRawSQLMonad(FuncMonad):
    func: Any
    def call(monad, *args: Any) -> None: ...

class FuncCountMonad(FuncMonad):
    func: Any
    def call(monad, x: Any | None = ..., distinct: Any | None = ...) -> Any: ...

class FuncAbsMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncSumMonad(FuncMonad):
    func: Any
    def call(monad, x: Any, distinct: Any | None = ...) -> Any: ...

class FuncAvgMonad(FuncMonad):
    func: Any
    def call(monad, x: Any, distinct: Any | None = ...) -> Any: ...

class FuncGroupConcatMonad(FuncMonad):
    func: Any
    def call(
        monad, x: Any, sep: Any | None = ..., distinct: Any | None = ...
    ) -> Any: ...

class FuncCoalesceMonad(FuncMonad):
    func: Any
    def call(monad, *args: Any) -> Any: ...

class FuncDistinctMonad(FuncMonad):
    func: Any
    def call(monad, x: Any) -> Any: ...

class FuncMinMonad(FuncMonad):
    func: Any
    def call(monad, *args: Any) -> Any: ...

class FuncMaxMonad(FuncMonad):
    func: Any
    def call(monad, *args: Any) -> Any: ...

def minmax(monad: Any, sqlop: Any, *args: Any) -> Any: ...

class FuncSelectMonad(FuncMonad):
    func: Any
    def call(monad, queryset: Any) -> Any: ...

class FuncExistsMonad(FuncMonad):
    func: Any
    def call(monad, arg: Any) -> Any: ...

class FuncDescMonad(FuncMonad):
    func: Any
    def call(monad, expr: Any) -> Any: ...

class DescMonad(Monad):
    def __init__(monad, expr: Any) -> None: ...
    def getsql(monad) -> Any: ...

class JoinMonad(Monad):
    def __init__(monad, type: Any) -> None: ...
    def __call__(monad, x: Any) -> Any: ...  # type: ignore

class FuncRandomMonad(FuncMonad):
    func: Any
    def __init__(monad, type: Any) -> None: ...
    def __call__(monad) -> Any: ...  # type: ignore

class SetMixin(MonadMixin):
    forced_distinct: bool
    def call_distinct(monad) -> Any: ...

def make_attrset_binop(op: Any, sqlop: Any) -> Any: ...

class AttrSetMonad(SetMixin, Monad):
    def __init__(monad, parent: Any, attr: Any) -> None: ...
    def cmp(monad, op: Any, monad2: Any) -> None: ...
    def contains(monad, item: Any, not_in: bool = ...) -> Any: ...
    def getattr(monad, name: Any) -> Any: ...
    def call_select(monad) -> Any: ...
    call_filter: Any
    def call_exists(monad) -> Any: ...
    def requires_distinct(monad, joined: bool = ..., for_count: bool = ...) -> Any: ...
    def count(monad, distinct: Any | None = ...) -> Any: ...
    len: Any
    def aggregate(
        monad, func_name: Any, distinct: Any | None = ..., sep: Any | None = ...
    ) -> Any: ...
    def nonzero(monad) -> Any: ...
    def negate(monad) -> Any: ...
    call_is_empty: Any
    def make_tableref(monad, sqlquery: Any) -> Any: ...
    def make_expr_list(monad) -> Any: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...
    __add__: Any
    __sub__: Any
    __mul__: Any
    __truediv__: Any
    __floordiv__: Any

def make_numericset_binop(op: Any, sqlop: Any) -> Any: ...

class NumericSetExprMonad(SetMixin, Monad):
    def __init__(monad, op: Any, sqlop: Any, left: Any, right: Any) -> None: ...
    def aggregate(
        monad, func_name: Any, distinct: Any | None = ..., sep: Any | None = ...
    ) -> Any: ...
    def getsql(monad, sqlquery: Any | None = ...) -> Any: ...
    __add__: Any
    __sub__: Any
    __mul__: Any
    __truediv__: Any
    __floordiv__: Any

class QuerySetMonad(SetMixin, Monad):
    nogroup: bool
    def __init__(monad, subtranslator: Any) -> None: ...
    def to_single_cell_value(monad) -> Any: ...
    def requires_distinct(monad, joined: bool = ...) -> None: ...
    def call_limit(monad, limit: Any | None = ..., offset: Any | None = ...) -> Any: ...
    def contains(monad, item: Any, not_in: bool = ...) -> Any: ...
    def nonzero(monad) -> Any: ...
    def negate(monad) -> Any: ...
    def count(monad, distinct: Any | None = ...) -> Any: ...
    len: Any
    def aggregate(
        monad, func_name: Any, distinct: Any | None = ..., sep: Any | None = ...
    ) -> Any: ...
    def call_count(monad, distinct: Any | None = ...) -> Any: ...
    def call_sum(monad, distinct: Any | None = ...) -> Any: ...
    def call_min(monad) -> Any: ...
    def call_max(monad) -> Any: ...
    def call_avg(monad, distinct: Any | None = ...) -> Any: ...
    def call_group_concat(
        monad, sep: Any | None = ..., distinct: Any | None = ...
    ) -> Any: ...
    def getsql(monad) -> Any: ...

def find_or_create_having_ast(sections: Any) -> Any: ...
