from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage :

    def __init__ (self, driver) :
        self.driver = driver


    def goto_books (self) :
        """ Selects to the books option from dropdown. """
        
        self.driver.find_element_by_xpath('//option[contains(text(),"Books")]').click()
        

    def search_book (self, book):
        """ Searches for a particular book. 
            Returns whether the book is bestseller or not."""

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@type="text"]')
                )
            ).send_keys(book)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@type="submit"]')
                )
            ).click()