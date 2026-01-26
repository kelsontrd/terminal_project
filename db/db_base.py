from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager

Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)


@contextmanager
def get_session():
    """Gerenciador de contexto para sessões do banco de dados"""
    session = Session()
    try:
        yield session
        session.commit()  # Commit automático se tudo correr bem
    except Exception:
        session.rollback()  # Rollback em caso de erro
        raise  # Re-lança a exceção
    finally:
        session.close()  # Sempre fecha a sessão