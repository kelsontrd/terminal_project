from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

print("estou em db_base")
Base = declarative_base()
engine = create_engine("sqlite:///todo2.db")
Session = sessionmaker(bind=engine)
session = Session()