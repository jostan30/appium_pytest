from selenium.webdriver.support import expected_conditions as EC

from locators import FORWARD_BUTTON, PAGE_INDICATOR, SEARCH_CARD, SKIP_BUTTON


def test_onboarding_navigation_and_skip(driver, wait):
    indicator = wait.until(EC.visibility_of_element_located(PAGE_INDICATOR))
    assert indicator.get_attribute("content-desc") == "Page 1 of 4"

    wait.until(EC.element_to_be_clickable(FORWARD_BUTTON)).click()
    wait.until(
        lambda d: d.find_element(*PAGE_INDICATOR).get_attribute("content-desc")
        == "Page 2 of 4"
    )

    wait.until(EC.element_to_be_clickable(SKIP_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(SEARCH_CARD)).is_displayed()
