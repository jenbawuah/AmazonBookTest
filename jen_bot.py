import time
import sys
import os
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pages import home_page
from pages import results_page
from pages import product_page
from pages import checkout_page


class JenBot:

    def __init__(self):

        dir_driver = os.path.join("resources", "drivers")
        # Select the directory based on current Operating System
        if sys.platform == "win32":
            dir_driver = os.path.join(dir_driver, "windows")
        elif sys.platform == "linux":
            dir_driver = os.path.join(dir_driver, "linux")
        elif sys.platform == "darwin":
            dir_driver = os.path.join(dir_driver, "macos")

        chrome_driver = os.path.join(dir_driver, "chromedriver")
        # Add .exe in file for Windows
        if sys.platform == "win32":
            chrome_driver = os.path.abspath(chrome_driver) + ".exe"

        self.url = "https://www.amazon.co.uk"
        opts = ChromeOptions()
        opts.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(executable_path=chrome_driver, options=opts)
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Accept Cookies
        time.sleep(5)

        for i in range(0, 5):
            try:
                self.driver.find_element_by_xpath('//input[@name="accept"]').click()
                time.sleep(1)
            except:
                pass

    def get_driver(self):
        """ Simply returns the webdriver object. """
        return self.driver


class JenTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bot = JenBot()
        cls.driver = cls.bot.get_driver()

        # Pages

        cls.homepage = home_page.HomePage(cls.driver)
        cls.res_page = results_page.ResultsPage(cls.driver)
        cls.product_page = product_page.ProductPage(cls.driver)
        cls.checkout_page = checkout_page.CheckOutPage(cls.driver)

        cls.homepage.goto_books()
        book = "Harry Potter and the Philosopher's Stone"
        cls.homepage.search_book(book)
        cls.bestseller = cls.res_page.is_bestseller(book)

        cls.is_kindle = cls.product_page.is_kindle_available()
        cls.product_page.goto_check_out()
        cls.checked_out = cls.checkout_page.check_out()
        cls.bot.driver.quit()

    def test_book_search(self):
        self.assertEqual(self.bestseller, True)

    def test_check_kindle(self):
        self.assertEqual(self.is_kindle, True)

    def test_check_out(self):
        self.assertEqual(self.checked_out, True)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
    #bot.driver.quit()
