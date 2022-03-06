from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

sql_password = f":{settings.mysql_password}" if settings.mysql_password else ""
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{settings.mysql_username}{sql_password}@{settings.alembic_mysql_host}:{settings.mysql_port}/{settings.mysql_database}"

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # pylint: disable=no-member
