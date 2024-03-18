import pytest
from playwright.sync_api import Page, expect

from pyshiny_e2e_playwright.calculation_type import CalculationType


@pytest.mark.parametrize(
    ("calculation_type", "first_operand", "second_operand", "expected"),
    [
        (CalculationType("Addition"), 2, 3, 5),
        (CalculationType("Addition"), 5, 3, 8),
        (CalculationType("Addition"), 0, 0, 0),
        (CalculationType("Subtraction"), 5, 3, 2),
        (CalculationType("Subtraction"), 3, 5, -2),
        (CalculationType("Subtraction"), 0, 0, 0),
    ],
)
def test_calculation(
    page: Page, calculation_type: CalculationType, first_operand: int, second_operand: int, expected: int
):
    # Given the app is open
    page.goto("http://localhost:8000")

    # When I select the calculation type
    calculation_radio = page.get_by_test_id("calculation_inputs").get_by_role("radio", name=calculation_type.value)
    calculation_radio.click()

    # And I fill the first and second operands
    first_number_input = page.get_by_test_id("calculation_inputs").get_by_label("Operand 1")
    first_number_input.fill(str(first_operand))

    second_number_input = page.get_by_test_id("calculation_inputs").get_by_label("Operand 2")
    second_number_input.fill(str(second_operand))

    # Then the result should be the expected value
    expect(page.get_by_test_id("calculation_result")).to_contain_text(str(expected))
