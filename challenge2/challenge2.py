import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

porsche = "Porsche"


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        title = self.driver.title
        print(" - Title:", title)
        self.assertEqual(title, self.driver.title)
        # self.assertTrue(title == self.driver.title)
        search_input = self.driver.find_element_by_css_selector('#input-search')
        search_input.send_keys(porsche)
        print(" - Keys Sent:", porsche)
        search_btn = self.driver.find_element_by_css_selector('.btn-lightblue')
        WebDriverWait(search_btn, 10)
        search_btn.click()
        element = self.driver.find_element_by_css_selector(".search-resultstable")
        WebDriverWait(element, 10)
        # exotics_page = self.driver.find_element_by_class_name('search-resultstable')
        # WebDriverWait(self.driver, 10).until(exotics_page)
    # self.assertEqual(exotics_page, self.driver.find_element_by_css_selector('#serverSideDataTable_wrapper'))


if __name__ == '__main__':
    unittest.main()
