
import os

import pytest
from pydantic import ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models import Base, Calculation
from app.schemas import CalculationCreate
from app.calculation_factory import CalculationFactory


@pytest.fixture
def postgres_session():
    """Connect to PostgreSQL for testing."""

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        pytest.fail("DATABASE_URL is not configured")

    engine = create_engine(database_url)

    Base.metadata.create_all(engine)

    try:
        with engine.connect() as connection:
            transaction = connection.begin()

            try:
                with Session(bind=connection) as session:
                    yield session
            finally:
                transaction.rollback()
    finally:
        engine.dispose()


def test_postgres_save_calculation(postgres_session):
    """Test saving and reading a calculation."""

    data = CalculationCreate(
        a=20,
        b=5,
        type="Divide"
    )

    result = CalculationFactory.calculate(data)

    calculation = Calculation(
        a=data.a,
        b=data.b,
        type=data.type,
        result=result
    )

    postgres_session.add(calculation)
    postgres_session.flush()

    calculation_id = calculation.id

    postgres_session.expunge_all()

    saved = postgres_session.get(
        Calculation, calculation_id
    )

    assert saved is not None
    assert saved.a == 20
    assert saved.b == 5
    assert saved.type == "Divide"
    assert saved.result == 4


@pytest.mark.parametrize(
    "invalid_data",
    [
        {"a": 10, "b": 0, "type": "Divide"},
        {"a": 10, "b": 5, "type": "Power"},
        {"a": "hello", "b": 5, "type": "Add"},
        {"a": float("nan"), "b": 5, "type": "Add"},
    ]
)
def test_invalid_calculation_data(invalid_data):
    """Test that invalid inputs are rejected."""

    with pytest.raises(ValidationError):
        CalculationCreate(**invalid_data)
