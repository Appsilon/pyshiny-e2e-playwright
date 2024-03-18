from shiny import App, ui

from e2e_testing_pyshiny.server import app_server
from e2e_testing_pyshiny.ui import app_ui

google_fonts_tag = ui.TagList(
    ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto"),
    ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Maven+Pro"),
)

ui_with_css = ui.TagList(ui.include_css("style.css"), google_fonts_tag, app_ui)

app = App(ui_with_css, app_server)
