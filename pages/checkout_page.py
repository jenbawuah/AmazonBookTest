from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
    
    
    def check_out(self, email=None, password=None):
        """ Selects the books and moves to checkout. """
        
        # Goto Create account if credentials are not provided
        # Else login
        if not email or not password:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@id="createAccountSubmit"]')
                    )
                ).click()
            #self.driver.find_element_by_xpath('//a[@id="createAccountSubmit"]').click()
            _name = "Jennifer"
            _email = "nothing@gmail.com"
            _password = "mypassword"

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@name="customerName"]')
                    )
                ).send_keys(_name)

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@name="email"]')
                    )
                ).send_keys(_email)

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@name="password"]')
                    )
                ).send_keys(_password)

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@name="passwordCheck"]')
                    )
                ).send_keys(_password)

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@type="submit"]')
                    )
                ).click()

        else:

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@type="email"]')
                    )
                ).send_keys(email)

            #email_box = self.driver.find_element_by_xpath('//input[@type="email"]')
            #email_box.send_keys(email)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@id="continue"]')
                    )
                ).click()
            #self.driver.find_element_by_xpath('//input[@id="continue"]').click()

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@type="password"]')
                    )
                ).send_keys(password)

            #password_box = self.driver.find_element_by_xpath('//input[@type="password"]')
            #password_box.send_keys(password)
            self.driver.find_element_by_xpath('//input[@id="signInSubmit"]').click()
        return True
