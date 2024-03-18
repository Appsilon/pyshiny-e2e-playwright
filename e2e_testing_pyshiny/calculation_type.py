from enum import Enum


class CalculationType(Enum):
    ADDITION = "Addition"
    SUBTRACTION = "Subtraction"

    @classmethod
    def possible_calculation_types(cls) -> list[str]:
        return list(map(lambda c: c.value, cls))
