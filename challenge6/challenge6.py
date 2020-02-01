import unittest
from selenium import webdriver


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        self.driver.get("https://www.copart.com")


if __name__ == '__main__':
    unittest.main()
