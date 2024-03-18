# ui.py
from shiny import ui

from e2e_testing_pyshiny.operation import Operation

app_ui = ui.page_bootstrap(
    ui.card(
        ui.panel_title("E2E Testing PyShiny Demo"),
        ui.p(
            "This app accompanies the blog post about end-to-end testing in PyShiny. ",
            ui.br(),
            "Check out the blog post and the source code on GitHub",
        ),
    ),
    ui.card(
        ui.layout_columns(
            ui.column(
                12,
                ui.div(
                    ui.input_radio_buttons("operation", "Operation", Operation.possible_operations()),
                    ui.input_numeric("first_number", "First number", value=1),
                    ui.input_numeric("second_number", "Second number", value=2),
                    data_testid="operation",
                ),
            ),
            ui.column(
                12,
                ui.output_ui("operation_result", data_testid="operation_result"),
            ),
        ),
    ),
    ui.card(
        ui.layout_columns(
            ui.column(
                12,
                ui.div(
                    ui.input_slider("slider", label="Slider", min=0, max=100, value=50),
                    data_testid="slider",
                ),
            ),
            ui.column(
                12,
                ui.output_ui("sum_value_box", data_testid="sum_of_numbers"),
            ),
        ),
    ),
    ui.card_footer(ui.input_dark_mode(), "By Appsilon with 💙 ", data_testid="footer"),
)
