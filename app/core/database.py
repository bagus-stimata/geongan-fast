from sqlalchemy import create_engine, event, MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


DATABASE_URL = settings.DATABASE_URL  # Database utama aplikasi
IS_SQLITE = DATABASE_URL.startswith("sqlite")

# Untuk SQLite, perlu connect_args agar bisa diakses lintas thread
connect_args = {"check_same_thread": False} if IS_SQLITE else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,   # auto-drop dead connections (portable)
    pool_recycle=3600,    # keep < wait_timeout (MySQL); fine for Postgres too
    future=True,          # SQLAlchemy 2.0 style API
)

# Nama schema yang dipakai oleh seluruh model
PUBLIC_SCHEMA = "public"

# Mapping schema "public" ke default apabila pakai SQLite
if IS_SQLITE:
    engine = engine.execution_options(schema_translate_map={"public": None})

    db_path = engine.url.database

    @event.listens_for(engine, "connect")
    def _sqlite_on_connect(dbapi_connection, connection_record):
        # buat schema alias "public" yang menunjuk ke DB utama
        dbapi_connection.execute(f"ATTACH DATABASE '{db_path}' AS public")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class _BaseMetaData(MetaData):
    """MetaData with Postgres-friendly drop_all.

    The original :meth:`MetaData.drop_all` doesn't issue ``CASCADE`` which
    means dropping tables may fail when leftover tables outside of SQLAlchemy's
    metadata still depend on them.  Some of our tests create tables manually
    and rely on a hard reset between runs.  By overriding ``drop_all`` we
    ensure that, on PostgreSQL, the whole ``public`` schema is dropped and
    recreated so no stray foreign key constraints remain.
    """

    def drop_all(self, bind=None, tables=None, checkfirst=True):  # noqa: D401
        bind = bind or engine
        if bind.dialect.name == "postgresql":
            with bind.begin() as conn:
                conn.execute(text("DROP SCHEMA IF EXISTS public CASCADE"))
                conn.execute(text("CREATE SCHEMA public"))
        else:  # fall back to SQLAlchemy default
            super().drop_all(bind=bind, tables=tables, checkfirst=checkfirst)


Base = declarative_base(metadata=_BaseMetaData())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### Test the database connection: pada Terminal
# python - << 'PY'
# from app.core.database import engine
# print("dialect:", engine.dialect.name)
# PY