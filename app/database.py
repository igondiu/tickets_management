from sqlmodel import Session, create_engine, SQLModel
import settings as app_settings

# echo=True prints all the SQL statements
engine = create_engine(app_settings.SQLALCHEMY_DATABASE_URL, echo=True if app_settings.LOGS_LEVEL == "DEBUG" else False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session
