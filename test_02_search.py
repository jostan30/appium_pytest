from selenium.webdriver.support import expected_conditions as EC

from locators import RESULT_TITLES, SEARCH_CARD, SEARCH_INPUT, SEARCH_TERM


def test_search_returns_expected_first_result(driver, wait, home_screen):
    wait.until(EC.element_to_be_clickable(SEARCH_CARD)).click()
    search_input = wait.until(EC.visibility_of_element_located(SEARCH_INPUT))
    search_input.send_keys(SEARCH_TERM)

    wait.until(lambda d: len(d.find_elements(*RESULT_TITLES)) > 0)
    first_title = driver.find_elements(*RESULT_TITLES)[0]
    assert first_title.text == SEARCH_TERM
