from typing import Any

from pony.orm import core as core
from pony.orm import dbapiprovider as dbapiprovider
from pony.orm import ormtypes as ormtypes
from pony.orm.core import log_orm as log_orm
from pony.orm.dbapiprovider import wrap_dbapi_exceptions as wrap_dbapi_exceptions
from pony.orm.dbproviders.postgres import PGArrayConverter as PGArrayConverter
from pony.orm.dbproviders.postgres import PGBlobConverter as PGBlobConverter
from pony.orm.dbproviders.postgres import PGColumn as PGColumn
from pony.orm.dbproviders.postgres import PGDatetimeConverter as PGDatetimeConverter
from pony.orm.dbproviders.postgres import PGIntConverter as PGIntConverter
from pony.orm.dbproviders.postgres import PGJsonConverter as PGJsonConverter
from pony.orm.dbproviders.postgres import PGProvider as PGProvider
from pony.orm.dbproviders.postgres import PGRealConverter as PGRealConverter
from pony.orm.dbproviders.postgres import PGSchema as PGSchema
from pony.orm.dbproviders.postgres import PGSQLBuilder as PGSQLBuilder
from pony.orm.dbproviders.postgres import PGTimedeltaConverter as PGTimedeltaConverter
from pony.orm.dbproviders.postgres import PGTranslator as PGTranslator
from pony.py23compat import buffer as buffer
from pony.py23compat import int_types as int_types

NoneType: Any

class CRColumn(PGColumn):
    auto_template: str

class CRSchema(PGSchema):
    column_class: Any

class CRTranslator(PGTranslator): ...
class CRSQLBuilder(PGSQLBuilder): ...

class CRIntConverter(PGIntConverter):
    signed_types: Any
    unsigned_types: Any

class CRBlobConverter(PGBlobConverter):
    def sql_type(converter) -> Any: ...

class CRTimedeltaConverter(PGTimedeltaConverter):
    sql_type_name: str

class PGUuidConverter(dbapiprovider.UuidConverter):
    def py2sql(converter, val: Any) -> Any: ...

class CRArrayConverter(PGArrayConverter):
    array_types: Any

class CRProvider(PGProvider):
    dbapi_module: Any
    dbschema_cls: Any
    translator_cls: Any
    sqlbuilder_cls: Any
    array_converter_cls: Any
    default_schema_name: str
    fk_types: Any
    def normalize_name(provider, name: Any) -> Any: ...
    def set_transaction_mode(provider, connection: Any, cache: Any) -> None: ...
    converter_classes: Any

provider_cls = CRProvider
