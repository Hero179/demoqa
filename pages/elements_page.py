from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')

    def exist_text(self):
        try:
           self.text.find_element()
        except NoSuchElementException:
            return False
        return True