# BasePage
#  \- NaverMap

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):
    """Base page class that is initialized on every page object class"""

    def __set__(self, obj, value):
        """Set the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, self.ID)))
        driver.find_element_by_id(self.ID).clear()
        driver.find_element_by_id(self.ID).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, self.ID)))
        element = driver.find_element_by_id(self.ID)
        return element.get_attribute("ID")


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for the search box where search string is entered
    ID = "search-input"


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def wait_until_finding_class(self, class_name):
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )


class NaverMap(BasePage):
    """All methods for Naver Map page goes here"""

    search_text_element = SearchTextElement()

    def __init__(self, driver):
        self.url = 'https://map.naver.com/'
        self.driver = webdriver.Chrome(driver)
        self.navigate()

    def type(self, value):
        self.search_text_element = value

    def search(self):
        """Triggers the search"""

        elem = self.driver.find_element_by_id('search-input')
        elem.send_keys(Keys.ENTER)

    def search_summary(self):
        # Returns the summary for the search results
        self.wait_until_finding_class('srt_tit')
        s = self.driver.find_element_by_class_name('srt_tit').text
        return s

    def go_next_page(self):
        # Go to the next list of the map
        self.wait_until_finding_class('pre')
        path = '//ul[@class="lst_site"]/following-sibling::div[@class="paginate_wrap"]//strong//following-sibling::a'
        next = self.driver.find_element_by_xpath(path)
        ActionChains(self.driver).move_to_element(next).click().perform()


if __name__ == '__main__':
    import os
    BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    driver = os.path.join(BASE, 'bin', 'chromedriver')
    n = NaverMap(driver)
    n.type('치킨')
    n.search()
    print(n.search_summary())
    n.go_next_page()
    n.go_next_page()