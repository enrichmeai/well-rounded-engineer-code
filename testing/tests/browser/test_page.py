"""Browser tests: Playwright drives a real Chromium through the page, the way a person would.
They are the slowest and the most realistic, so there are only a few of them.

If Playwright's own Chromium is not installed, point CHROMIUM_EXECUTABLE at another Chromium build.
"""

import os

import pytest
from playwright.sync_api import expect, sync_playwright

pytestmark = pytest.mark.browser


@pytest.fixture(scope="module")
def browser():
    executable = os.environ.get("CHROMIUM_EXECUTABLE") or None
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=executable)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, base_url):
    page = browser.new_page()
    page.goto(base_url)
    yield page
    page.close()


def test_the_page_has_a_title_and_a_heading(page):
    expect(page).to_have_title("Tip splitter")
    expect(page.get_by_role("heading", name="Tip splitter")).to_be_visible()


def test_a_person_can_split_a_bill(page):
    page.get_by_label("Bill total").fill("60")
    page.get_by_label("Number of people").fill("3")
    page.get_by_label("Tip (%)").fill("10")
    page.get_by_role("button", name="Split the bill").click()
    expect(page.get_by_role("status")).to_have_text("Each person pays 22.00 (total 66.00, tip 6.00)")


def test_bad_input_shows_the_error_from_the_api(page):
    page.get_by_label("Bill total").fill("lots")
    page.get_by_role("button", name="Split the bill").click()
    expect(page.get_by_role("status")).to_have_text("total and tip must be numbers")
