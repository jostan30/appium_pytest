from selenium.webdriver.support import expected_conditions as EC

from locators import RESULT_TITLES, SAVE_ACTION


def test_open_article_from_results(driver, wait):
    driver.find_elements(*RESULT_TITLES)[0].click()

    save_action = wait.until(EC.visibility_of_element_located(SAVE_ACTION))
    assert save_action.get_attribute("content-desc") == "Save"
    # the search results list is gone once the article is open
    assert len(driver.find_elements(*RESULT_TITLES)) == 0
