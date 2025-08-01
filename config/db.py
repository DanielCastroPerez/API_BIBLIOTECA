from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "mysql+pymysql://root:@localhost:3306/storedb"
engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
