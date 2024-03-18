from playwright.sync_api import Page, expect


def test_footer(page: Page):
    # Given the app is open
    page.goto("http://localhost:8000")
    # Then the footer should contain the given text
    expect(page.get_by_test_id("footer")).to_contain_text("By Appsilon with 💙 ")


def test_github_link(page: Page):
    # Given the app is open
    page.goto("http://localhost:8000")

    # When the user clicks on the source code on GitHub link
    locator = page.get_by_test_id("intro").get_by_text("source code on GitHub")
    with page.expect_popup() as page1_info:
        locator.click()
    page1 = page1_info.value

    # Then the user should be redirected to the correct page in a new tab
    expect(page1).to_have_url("https://github.com/Appsilon/pyshiny-e2e-playwright")
