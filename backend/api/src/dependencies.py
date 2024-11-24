from contextlib import contextmanager

from sqlalchemy.exc import IntegrityError
from src.database import SessionLocal


@contextmanager
def get_db_session(autocommit: bool = True, suppress_integrity_error: bool = False):
    session = SessionLocal()
    try:
        yield session
        if autocommit:
            session.commit()
    finally:
        session.close()
