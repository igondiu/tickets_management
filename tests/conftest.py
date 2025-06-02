import os
import sys

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

# Absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Absolute path to the parent directory
parent_dir = os.path.dirname(current_dir)

# Add parent directory to sys.path so that no import errors occur when pytest is run from the terminal
sys.path.insert(0, os.path.join(parent_dir, "app"))

from app.main import application
from app.database import get_session


# Test database fixture available for all unit tests
@pytest.fixture(name="session", scope="session")
def session_fixture():
    # In memory SQLite Database for unit tests
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


# Override the get_session dependency
@pytest.fixture(name="client", scope="session")
def client_fixture(session: Session):
    def override_get_session():
        return session

    application.dependency_overrides[get_session] = override_get_session
    client = TestClient(application)
    yield client
    application.dependency_overrides.clear()
