import pytest
from playwright.sync_api import Page, expect


def set_slider_value_directly(page: Page, test_id: str, value: int):
    js_code = f"""
    var slider = $("[data-testid='{test_id}']").find(".js-range-slider");
    slider.data("ionRangeSlider").update({{ from: {value} }});
    """
    page.evaluate(js_code)


@pytest.mark.parametrize("slider_value", [25, 26, 50, 75])
def test_slider_directly(page: Page, slider_value: int):
    # Given the app is open
    page.goto("http://localhost:8000")

    # When I set the slider value to slider_value
    set_slider_value_directly(page, "range_sum_slider", slider_value)

    # Then the output should be the sum of numbers from 0 to slider_value
    n = slider_value
    expected = n * (n + 1) // 2
    expect(page.get_by_test_id("range_sum_result")).to_contain_text(str(expected))


@pytest.mark.parametrize(("slider_value", "expected"), [(0, 0), (100, 5050)])
def test_slider_boundaries(page: Page, slider_value: int, expected: int):
    # Given the app is open
    page.goto("http://localhost:8000")

    # When I set the slider value to slider_value
    set_slider_value_directly(page, "range_sum_slider", slider_value)

    # Then the output should be expected
    expect(page.get_by_test_id("range_sum_result")).to_contain_text(str(expected))
