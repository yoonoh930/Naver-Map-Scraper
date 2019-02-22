##
## Parser classes inherits naver map class
## and it implements all functionality
## in order to parse data
from collections import deque
from map import NaverMap
from locator import ParserLocator
from selenium.webdriver.common.action_chains import ActionChains


class NaverMapParser(NaverMap):
    """All methods for Parser goes here"""

    def __init__(self, driver=None, query=None):
        if driver is None:
            super().__init__()
        else:
            super().__init__(driver)

        if query is not None:
            self.search(query)

    def parse_webelem(self, webelem):
        # Gotta implement this. 
        # Return a dict of information extracted
        d = dict()
        d['name'] = webelem.find_element(*ParserLocator.NAME).text
        d['roadname'] = webelem.find_element(*ParserLocator.RDNAME).text.rstrip(' 지번')
        elem = webelem.find_element(*ParserLocator.ADMIN)
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        d['adminrdname'] = self.driver.find_element(*ParserLocator.ADMINRDNAME).text
        d['tel'] = webelem.find_element(*ParserLocator.TEL).text
        d['cat'] = webelem.find_element(*ParserLocator.CAT).text

        return d


if __name__ == '__main__':
    n = NaverMapParser(query='치킨')
    print(n.search_summary())
    print(n.parse_webelem(n.search_item_list()[0]))
    print(n.parse_webelem(n.search_item_list()[1]))
    print(n.parse_webelem(n.search_item_list()[2]))