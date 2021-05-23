from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def show_more_formats(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//span[@id="showMoreFormatsPrompt"]')
                )
            ).click()
        except:
            pass

    def is_kindle_available(self) -> bool:
        """ Checks if the book is available in Kindle format. """

        elems = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//span")
            )
        )
        for elem in elems:
            if elem.text == "Kindle Edition": return True
        return False

    def goto_check_out(self):
        """ Selects the books and moves to checkout. """
        self.driver.find_element_by_xpath('//input[@id="buy-now-button"]').click()
