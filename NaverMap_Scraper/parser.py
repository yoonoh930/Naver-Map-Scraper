##
## Parser classes inherits naver map class
## and it implements all functionality
## in order to parse data
from collections import deque
from map import NaverMap


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
        #d['name'] = webelem.


if __name__ == '__main__':
    n = NaverMapParser(query='치킨')
    print(n.search_summary())