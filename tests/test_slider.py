import pytest
from playwright.sync_api import Page, expect


def set_slider_value_directly(page: Page, test_id: str, value: int):
    js_code = f"""
    var slider = $("[data-testid='{test_id}']").find(".js-range-slider");
    slider.data("ionRangeSlider").update({{ from: {value} }});
    """
    page.evaluate(js_code)


def test_slider_boundaries(page: Page):
    # Given the app is open
    page.goto("http://localhost:8000")

    # When I set the slider value to 0
    set_slider_value_directly(page, "slider", 0)

    # Then the output should be 0
    expect(page.get_by_test_id("sum_of_numbers")).to_contain_text("0")

    # When I set the slider value to 100
    set_slider_value_directly(page, "slider", 100)

    # Then the output should be 5050
    expect(page.get_by_test_id("sum_of_numbers")).to_contain_text("5050")


@pytest.mark.parametrize("slider_value", [25, 26, 50, 75])
def test_slider_directly(page: Page, slider_value: int):
    # Given the app is open
    page.goto("http://localhost:8000")

    # When I set the slider value to slider_value
    set_slider_value_directly(page, "slider", slider_value)

    # Then the output should be the sum of numbers from 0 to slider_value
    expected = sum(range(slider_value + 1))
    expect(page.get_by_test_id("sum_of_numbers")).to_contain_text(str(expected))
