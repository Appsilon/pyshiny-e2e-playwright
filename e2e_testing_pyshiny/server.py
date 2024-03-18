# server.py
import faicons
from shiny import Inputs, Outputs, Session, reactive, render, ui

from e2e_testing_pyshiny.operation import Operation


def app_server(inputs: Inputs, outputs: Outputs, session: Session):
    @reactive.Calc
    def operation_result_num() -> float | int:
        if Operation(inputs.operation()) == Operation.ADDITION:
            return inputs.first_number() + inputs.second_number()
        elif Operation(inputs.operation()) == Operation.SUBTRACTION:
            return inputs.first_number() - inputs.second_number()
        else:
            raise ValueError(f"Unknown operation: {inputs.operation()}")

    @render.ui
    def operation_result():
        return ui.value_box(
            "Operation result",
            operation_result_num(),
            "change the operation or numbers to see the result",
            showcase=faicons.icon_svg("calculator"),
        )

    @reactive.Calc
    def slider_sum() -> int:
        return sum(range(inputs.slider() + 1))

    @render.ui
    def sum_value_box():
        return ui.value_box(
            "Sum of numbers from 0 to slider value",
            slider_sum(),
            "move the slider to change the value",
            showcase=faicons.icon_svg("sliders"),
        )
