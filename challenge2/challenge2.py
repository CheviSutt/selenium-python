import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

porsche = "PORSCHE"


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        # search_input = self.driver.find_element_by_css_selector('#input-search')
        search_input = self.driver.find_element(By.ID, 'input-search')
        search_input.send_keys(porsche)
        print(" - Keys Sent:", porsche)
        search_btn = self.driver.find_element_by_css_selector('.btn-lightblue')
        search_btn.click()
        porsche_currently_listed = WebDriverWait(self.driver, 10).until(
            cond.visibility_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td[5]")))
        print(" - List Text:", porsche_currently_listed.text)
        self.assertTrue(porsche_currently_listed.text == porsche)


if __name__ == '__main__':
    unittest.main()
