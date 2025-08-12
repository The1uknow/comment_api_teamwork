from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

SQL_DATABASE = 'sqlite:///les43.db'


engine = create_engine(SQL_DATABASE)


SessionLocal = sessionmaker(bind = engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()