import faicons
from shiny import Inputs, Outputs, Session, reactive, render, ui

from pyshiny_e2e_playwright.calculation_type import CalculationType


def app_server(inputs: Inputs, outputs: Outputs, session: Session):
    @reactive.Calc
    def calculate_result_based_on_operation() -> float | int:
        calculation_type = CalculationType(inputs.calculation_type())
        if calculation_type == CalculationType.ADDITION:
            return inputs.first_operand() + inputs.second_operand()
        elif calculation_type == CalculationType.SUBTRACTION:
            return inputs.first_operand() - inputs.second_operand()
        else:
            raise ValueError(f"Unsupported operation: {calculation_type}")

    @render.ui
    def calculation_result_display():
        return ui.value_box(
            "Calculation Result",
            calculate_result_based_on_operation(),
            "Adjust operands or operation to see changes.",
            showcase=faicons.icon_svg("calculator"),
        )

    @reactive.Calc
    def calculate_sum_of_range() -> int:
        return sum(range(inputs.range_sum_slider() + 1))

    @render.ui
    def range_sum_result_display():
        return ui.value_box(
            "Range Sum Result",
            calculate_sum_of_range(),
            "Slide to adjust the range.",
            showcase=faicons.icon_svg("sliders"),
        )
