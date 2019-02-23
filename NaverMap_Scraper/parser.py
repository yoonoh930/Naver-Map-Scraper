##
## Parser classes inherits naver map class
## and it implements all functionality
## in order to parse data
from collections import deque

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

from locator import ParserLocator
from map import NaverMap


class NaverMapParser(NaverMap):
    """All methods for Parser goes here"""


    def __init__(self, driver=None, query=None, start_from=1, end_at=8):
        self.dq = deque()
        self.start_from = start_from
        self.end_at = end_at
        if driver is None:
            super().__init__()
        else:
            super().__init__(driver)

        if query is not None:
            self.search(query)

        #self.parse_list()

    def parse_webelem(self, webelem):
        # !Having a trouble collecting ADMINRDNAME data.
        # ! Need to fix it later.
        # ! What I can think of it is when we parse it later
        # !  using detail link, we can add them
        d = dict()
        try:
            d['name'] = webelem.find_element(*ParserLocator.NAME).text
        except StaleElementReferenceException:
            d['name'] = ''

        try:
            d['roadname'] = webelem.find_element(*ParserLocator.RDNAME).text.rstrip(' 지번')
        except StaleElementReferenceException:
            d['roadname'] = ''

        try:
            elem = webelem.find_element(*ParserLocator.ADMIN)
            hover = ActionChains(self.driver).move_to_element(elem)
            hover.perform()
            d['adminrdname'] = self.driver.find_element(*ParserLocator.ADMINRDNAME).text
        except StaleElementReferenceException:
            d['adminrdname'] = ''

        try:
            d['tel'] = webelem.find_element(*ParserLocator.TEL).text
        except StaleElementReferenceException:
            d['tel'] = ''
        except NoSuchElementException:
            d['te;'] = ''

        try:
            d['cat'] = webelem.find_element(*ParserLocator.CAT).text
        except StaleElementReferenceException:
            d['cat'] = ''
        except NoSuchElementException:
            d['cat'] = ''

        try:
            d['details'] = webelem.find_element(*ParserLocator.DETAIL).get_attribute('href')
        except StaleElementReferenceException:
            d['details'] = ''
        except NoSuchElementException:
            d['details'] = ''

        return d

    def parse_cur_itm_list(self):
        # ! Because the next page has same structure, it is not waiting enough to parse the new item...
        i = self.search_item_list()
        ii = [self.parse_webelem(elem) for elem in i]
        return ii

    def parse_list(self, start_from=None, end_at=None):

        if start_from is None:
            start_from = self.start_from
        if end_at is None:
            end_at = self.end_at
        if end_at == 0:
            end_at = float('inf')
        
        while self.current_page() < start_from:
            self.go_next_page()

        while True:
            li = self.parse_cur_itm_list()
            self.dq.extend(li)
            try:
                self.go_next_page()
            except NoSuchElementException:
                break

            if self.current_page() == end_at:
                break
        
        return self.dq


if __name__ == '__main__':
    n = NaverMapParser(query='치킨', start_from=3)
    print(n.search_summary())
    print(n.parse_webelem(n.search_item_list()[0]))
    print(n.parse_webelem(n.search_item_list()[1]))
    print(n.parse_webelem(n.search_item_list()[2]))