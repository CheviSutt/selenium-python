import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        listings = []
        self.driver.get("https://www.copart.com")
        most_popular_items_elements = self.driver.find_elements_by_xpath(
            "//div[@id='tabTrending']/div[1]/div[2]/div/ul/li/a")
        for item in most_popular_items_elements:
            listing_title = item.text
            href = item.get_attribute("href")
            listings.append([listing_title, href])

        for make in listings:
            model_make = make[0]
            make_url = make[1]
            self.driver.get(make_url)
            try:
                search_table = WebDriverWait(self.driver, 5).until(
                    cond.visibility_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td")))
                make_column = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td[5]")
                model_column = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td[6]")
                if make_column.text or model_column.text == model_make:
                    print(f'{model_make}: Passed')
            except Exception as ex:
                print(f'{model_make}: Did Not Pass')
                print(ex)

        if __name__ == '__main__':
            unittest.main()
