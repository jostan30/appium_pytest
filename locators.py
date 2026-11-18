"""Shared locators and test data for the Wikipedia Android E2E tests."""
from appium.webdriver.common.appiumby import AppiumBy

PKG = "org.wikipedia.alpha:id/"
SEARCH_TERM = "Appium"

SKIP_BUTTON = (AppiumBy.ID, PKG + "fragment_onboarding_skip_button")
FORWARD_BUTTON = (AppiumBy.ID, PKG + "fragment_onboarding_forward_button")
PAGE_INDICATOR = (AppiumBy.ID, PKG + "view_onboarding_page_indicator")
SEARCH_CARD = (AppiumBy.ID, PKG + "search_container")
SEARCH_INPUT = (AppiumBy.ID, PKG + "search_src_text")
RESULT_TITLES = (AppiumBy.ID, PKG + "page_list_item_title")
SAVE_ACTION = (AppiumBy.ACCESSIBILITY_ID, "Save")
NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
SAVED_TAB = (AppiumBy.ACCESSIBILITY_ID, "Saved")
SAVED_LIST_STATS = (AppiumBy.ID, PKG + "item_reading_list_statistical_description")
