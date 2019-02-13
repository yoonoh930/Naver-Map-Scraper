from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.drive.current_url

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    def hover(self, *locator):
        elem = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()

    def wait_until_finding_element(self, *locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element(*locator)
            # I am not sure what's the difference between using
            #   EC and just find_element_by...
            # EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return self.find_element(*locator)