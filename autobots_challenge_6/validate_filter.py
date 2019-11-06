import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

silveraldo = "Silveraldo"


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_validate_filter(self):
        self.driver.get("https://www.copart.com")
        search_input = self.driver.find_element_by_css_selector('#input-search')
        search_input.send_keys(silveraldo)
        print(" - Keys Sent:", silveraldo)
        search_btn = self.driver.find_element_by_css_selector('.btn-lightblue')
        search_btn.click()
        # engine_type_checkbox = self.driver.find_element_by_xpath("//ul[@class='list-group']//a[@href='#collapseinside16']/i[@class='fa fa-minus-square']")
        # engine_type_checkbox.click()

        # engine_type_checkbox = WebDriverWait(self.driver, 10).until(
        #     cond.visibility_of_element_located((By.XPATH, "//div[@id='filters-collapse-1']//ul[@class='list-group']/li[16]//a[@href='#collapseinside16']")))
        # engine_type_checkbox.click()


if __name__ == '__main__':
    unittest.main()
