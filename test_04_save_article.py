from selenium.webdriver.support import expected_conditions as EC

from locators import NAVIGATE_UP, SAVE_ACTION, SAVED_LIST_STATS, SAVED_TAB


def test_save_article_appears_in_saved_list(driver, wait):
    wait.until(EC.element_to_be_clickable(SAVE_ACTION)).click()

    # back to the search screen, then up to the main feed
    driver.back()
    wait.until(EC.element_to_be_clickable(NAVIGATE_UP)).click()

    wait.until(EC.element_to_be_clickable(SAVED_TAB)).click()
    stats = wait.until(EC.visibility_of_element_located(SAVED_LIST_STATS))
    assert stats.text.startswith("1 article")
