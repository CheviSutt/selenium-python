import unittest
from selenium import webdriver

porsche = "PORSCHE"


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        most_popular_items_elements = self.driver.find_elements_by_xpath(
            "//div[@id='tabTrending']/div[1]/div[2]//div//ul//li//a")
        for item in most_popular_items_elements:
            listing = item.text
            href = item.get_attribute("href")
            print(listing + ' - ' + href)


if __name__ == '__main__':
    unittest.main()
