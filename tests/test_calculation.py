
import pytest
from pydantic import ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models import Base, Calculation
from app.schemas import CalculationCreate, CalculationRead
from app.calculation_factory import CalculationFactory


# Test all four operations
@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("Add", 10, 5, 15),
        ("Sub", 10, 5, 5),
        ("Multiply", 10, 5, 50),
        ("Divide", 10, 5, 2),
    ],
)
def test_calculation_operations(operation, a, b, expected):
    calculation = CalculationCreate(
        a=a,
        b=b,
        type=operation
    )

    result = CalculationFactory.calculate(calculation)

    assert result == pytest.approx(expected)


# Test division by zero
def test_division_by_zero():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type="Divide")


# Test invalid operation
def test_invalid_operation():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=5, type="Invalid")


# Test missing required fields
def test_missing_fields():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, type="Add")


# Test output schema
def test_calculation_read():
    calculation = CalculationRead(
        id=1,
        a=10,
        b=5,
        type="Add",
        result=15
    )

    assert calculation.id == 1
    assert calculation.result == 15


# Test saving a calculation to a database
def test_save_calculation():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    data = CalculationCreate(
        a=10,
        b=5,
        type="Add"
    )

    result = CalculationFactory.calculate(data)

    with Session(engine) as session:
        calculation = Calculation(
            a=data.a,
            b=data.b,
            type=data.type,
            result=result
        )

        session.add(calculation)
        session.commit()
        session.refresh(calculation)

        assert calculation.id is not None
        assert calculation.a == 10
        assert calculation.b == 5
        assert calculation.type == "Add"
        assert calculation.result == pytest.approx(15)

    engine.dispose()
