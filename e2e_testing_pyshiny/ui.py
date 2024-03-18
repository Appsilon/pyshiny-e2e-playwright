from shiny import ui

from e2e_testing_pyshiny.calculation_type import CalculationType


def create_app_ui():
    return ui.page_bootstrap(
        ui.card(
            ui.panel_title("E2E Testing with PyShiny and Playwright"),
            ui.p(
                "This app demonstrates end-to-end testing in PyShiny. ",
                ui.br(),
                "Explore the blog post and source code on GitHub.",
            ),
        ),
        ui.card(
            ui.layout_columns(
                ui.column(
                    12,
                    ui.div(
                        ui.input_radio_buttons(
                            "calculation_type", "Choose Operation", CalculationType.possible_calculation_types()
                        ),
                        ui.input_numeric("first_operand", "Operand 1", value=1),
                        ui.input_numeric("second_operand", "Operand 2", value=2),
                        data_testid="calculation_inputs",
                    ),
                ),
                ui.column(
                    12,
                    ui.output_ui("calculation_result_display", data_testid="calculation_result"),
                ),
            ),
        ),
        ui.card(
            ui.layout_columns(
                ui.column(
                    12,
                    ui.div(
                        ui.input_slider("range_sum_slider", label="Range Sum Slider", min=0, max=100, value=50),
                        data_testid="range_sum_slider",
                    ),
                ),
                ui.column(
                    12,
                    ui.output_ui("range_sum_result_display", data_testid="range_sum_result"),
                ),
            ),
        ),
        ui.card_footer(ui.input_dark_mode(), "By Appsilon with 💙", data_testid="footer"),
    )
