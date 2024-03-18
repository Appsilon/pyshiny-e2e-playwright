from enum import Enum


class Operation(Enum):
    ADDITION = "Addition"
    SUBTRACTION = "Subtraction"

    @classmethod
    def possible_operations(cls) -> list[str]:
        return list(map(lambda c: c.value, cls))
