import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="session")
def driver():
    """One Appium session shared by every test file in the run.

    The BrowserStack SDK injects credentials, hub URL, device and app
    from browserstack.yml, so only minimal capabilities live here.
    """
    options = UiAutomator2Options()
    options.set_capability("appium:allowInvisibleElements", True)
    drv = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def wait(driver):
    return WebDriverWait(driver, 20)
