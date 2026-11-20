import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import RESULT_TITLES, SEARCH_CARD, SEARCH_INPUT, SEARCH_TERM, SKIP_BUTTON


@pytest.fixture
def driver():
    """A fresh Appium session per test, so each test is its own row in the report.

    The BrowserStack SDK injects credentials, hub URL, device and app
    from browserstack.yml, so only minimal capabilities live here.
    """
    options = UiAutomator2Options()
    options.set_capability("appium:allowInvisibleElements", True)
    drv = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield drv
    drv.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)


@pytest.fixture
def home_screen(driver, wait):
    """Skip onboarding and land on the main feed."""
    wait.until(EC.element_to_be_clickable(SKIP_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(SEARCH_CARD))


@pytest.fixture
def search_results(driver, wait, home_screen):
    """Search for SEARCH_TERM and wait for the results list."""
    wait.until(EC.element_to_be_clickable(SEARCH_CARD)).click()
    wait.until(EC.visibility_of_element_located(SEARCH_INPUT)).send_keys(SEARCH_TERM)
    wait.until(lambda d: len(d.find_elements(*RESULT_TITLES)) > 0)


@pytest.fixture
def open_article(driver, wait, search_results):
    """Open the first search result."""
    driver.find_elements(*RESULT_TITLES)[0].click()
