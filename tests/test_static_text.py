from playwright.sync_api import Page, expect


def test_footer(page: Page):
    # Given the app is open
    page.goto("http://localhost:8000")
    # Then the footer should contain the given text
    expect(page.get_by_test_id("footer")).to_contain_text("By Appsilon with 💙 ")
