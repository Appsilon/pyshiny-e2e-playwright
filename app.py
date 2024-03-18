from shiny import App, ui

from pyshiny_e2e_playwright.server import app_server
from pyshiny_e2e_playwright.ui import create_app_ui

app_ui = create_app_ui()
google_fonts_tag = ui.TagList(
    ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto"),
    ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Maven+Pro"),
)

ui_with_css = ui.TagList(ui.include_css("style.css"), google_fonts_tag, app_ui)

app = App(ui_with_css, app_server)
