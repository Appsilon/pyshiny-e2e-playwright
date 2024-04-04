from shiny import App, ui

from pyshiny_e2e_playwright.server import app_server
from pyshiny_e2e_playwright.ui import create_app_ui

app_ui = create_app_ui()

ui_with_css = ui.TagList(ui.include_css("style.css"), app_ui)

app = App(ui_with_css, app_server)
