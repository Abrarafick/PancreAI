from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/pancreai_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


#hvg
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/pancreai_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Connection Test
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("✅ MySQL Connected Successfully!")
    except Exception as e:
        print("❌ Connection Failed")
        print(e)

#new add phase 2
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()