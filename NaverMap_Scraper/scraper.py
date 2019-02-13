from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from base import BasePage
from locator import NaverMapLocator


class NaverMap(BasePage):
    """All methods for Naver Map page goes here"""

    def __init__(self, driver):
        super().__init__(webdriver.Chrome(driver))
        self.url = 'https://map.naver.com/'
        self.navigate()

    def type(self, value):
        self.find_element(*NaverMapLocator.SEARCH_BAR).clear()
        self.find_element(*NaverMapLocator.SEARCH_BAR).send_keys(value)

    def search(self, value=None):
        """Triggers the search"""
        if value is None:
            elem = self.find_element(*NaverMapLocator.SEARCH_BAR)
            elem.send_keys(Keys.ENTER)
        else:
            self.type(value)

    def no_search_result(self):
        try:
            self.search_result().find_element(*NaverMapLocator.NO_RESULT)
        except NoSuchElementException:
            return False
        return True

    def search_result(self):
        return self.wait_until_finding_element(*NaverMapLocator.SEARCH_RESULT)

    def search_summary(self):
        # Returns the summary for the search results
        if self.no_search_result():
            return "No search result"
        else:
            t = self.find_element(*NaverMapLocator.SEARCH_RESULT_TOP)
            return t.find_element(*NaverMapLocator.SUMMARY).text

    def go_next_page(self):
        # Go to the next list of the map
        if self.no_search_result():
            return "No search result"
        else:
            # Raises NoSuchElementException Error when there is not more tab to click
            next_tab = self.search_result().find_element(*NaverMapLocator.NEXT)
            self.click(next_tab)


if __name__ == '__main__':
    import os
    BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    driver = os.path.join(BASE, 'bin', 'chromedriver')
    n = NaverMap(driver)
    n.type('아이키')
    n.search()
    print(n.search_summary())
    n.go_next_page()
    n.go_next_page()
    n.go_next_page()
    n.go_next_page()
    n.go_next_page()
    n.go_next_page()
