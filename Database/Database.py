from sqlalchemy import create_engine,text

from sqlalchemy.orm import sessionmaker

from .Base import Base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/sala"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    database = get_db()
    database
    with engine.connect() as connection:
        result = connection.execute(text("select nombre from hospital"))
        for row in result:
            print("username:", row['nombre'])
    print(next(database))