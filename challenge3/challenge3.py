import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_for_loop(self):
        self.driver.get("https://www.copart.com")
        most_popular_items_elements = self.driver.find_elements_by_xpath(
            "//div[@id='tabTrending']//a")
        for item in most_popular_items_elements:
            listing = item.text
            href = item.get_attribute("href")
            print("For Loop: " + listing + ' - ' + href)

    def test_challenge3_while_loop(self):
        self.driver.get("https://www.copart.com")
        list_of_elements_2 = self.driver.find_elements(By.XPATH, "//div[@id='tabTrending']//a")
        count = 0
        while count < len(list_of_elements_2):
            text = list_of_elements_2[count].text
            href = list_of_elements_2[count].get_attribute("href")
            print("While Loop: " + text + ' - ' + href)
            count += 1


if __name__ == '__main__':
    unittest.main()
