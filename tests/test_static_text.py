from playwright.sync_api import Page, expect


def test_footer(page: Page):
    page.goto("http://localhost:8000")

    expect(page.get_by_test_id("footer")).to_contain_text("By Appsilon with 💙 ")
