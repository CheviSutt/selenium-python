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
        self.assertTrue(title == self.driver.title)


if __name__ == '__main__':
    unittest.main()
