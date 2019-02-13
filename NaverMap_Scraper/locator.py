from selenium.webdriver.common.by import By

class NaverMapLocator(object):
    """A class for naver map locator"""

    SEARCH_BAR = (By.ID, 'search-input')
    CURRENT_TAB = (By.TAG_NAME, 'strong')
    next_tab_path = '//ul[@class="lst_site"]/following-sibling::div[@class="paginate_wrap"]//strong/following-sibling::a'
    current_tab_path = '//ul[@class="lst_site"]/following-sibling::div[@class="paginate_wrap"]//strong'
    NEXT = (By.XPATH, next_tab_path)
    CURRENT = (By.XPATH, current_tab_path)
    SUMMARY = (By.CLASS_NAME, 'srt_tit')
    NO_RESULT = (By.CLASS_NAME, 'no_result')
    SEARCH_RESULT = (By.CLASS_NAME, 'search_result')
    SEARCH_RESULT_TOP = (By.CLASS_NAME, 'search_result_top')
