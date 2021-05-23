from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def is_bestseller(self, book) -> bool:
        """ Returns if the book is bestseller or not. """

        product = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@data-cel-widget="search_result_1"]')
            )
        )
        ans = WebDriverWait(product, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, ".//a")
            )
        )[0].text
        # ans = product.find_elements_by_xpath(".//a")[0].text
        if ans == "Best Seller" or "Amazon Charts" in ans:
            is_bestseller = True
        else:
            is_bestseller = False

        book_link = None
        for p in product.find_elements_by_xpath(".//a"):
            if book in p.text:
                book_link = p
                break
        if book_link: book_link.click()

        return is_bestseller
