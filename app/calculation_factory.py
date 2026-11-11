
from operator import add, sub, mul, truediv

from app.schemas import CalculationCreate


class CalculationFactory:
    """Handles the four calculator operations."""

    OPERATIONS = {
        "Add": add,
        "Sub": sub,
        "Multiply": mul,
        "Divide": truediv,
    }

    @classmethod
    def calculate(cls, calculation: CalculationCreate) -> float:
        operation = cls.OPERATIONS[calculation.type]

        return float(
            operation(calculation.a, calculation.b)
        )
