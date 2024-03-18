import pytest
from playwright.sync_api import Page, expect

from e2e_testing_pyshiny.operation import Operation


@pytest.mark.parametrize(
    ("operation", "first_number", "second_number", "expected"),
    [
        (Operation("Addition"), 2, 3, 5),
        (Operation("Addition"), 5, 3, 8),
        (Operation("Addition"), 0, 0, 0),
        (Operation("Subtraction"), 5, 3, 2),
        (Operation("Subtraction"), 3, 5, -2),
        (Operation("Subtraction"), 0, 0, 0),
    ],
)
def test_operation(page: Page, operation: Operation, first_number: int, second_number: int, expected: int):
    page.goto("http://localhost:8000")

    operation_radio = page.get_by_test_id("operation").get_by_role("radio", name=operation.value)
    operation_radio.click()

    first_number_input = page.get_by_test_id("operation").get_by_label("First number")
    first_number_input.fill(str(first_number))

    second_number_input = page.get_by_test_id("operation").get_by_label("Second number")
    second_number_input.fill(str(second_number))

    expect(page.get_by_test_id("operation_result")).to_contain_text(str(expected))
