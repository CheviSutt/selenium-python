import unittest
from selenium import webdriver


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
        search_input.send_keys('Porsche')
        search_btn = self.driver.find_element_by_css_selector('.btn-lightblue')
        search_btn.click()
        # exotics_page = self.driver.('#serverSideDataTable_wrapper')
        # self.assertEqual(exotics_page, self.driver.find_element_by_css_selector('#serverSideDataTable_wrapper'))




if __name__ == '__main__':
    unittest.main()
