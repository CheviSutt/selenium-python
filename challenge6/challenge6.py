import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

search_criteria: str = 'Skyline'


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):

        count: int = 0
        path_to_input: str = ''
        path_to_filter_entered: str = ''
        try:
            search_field = self.driver.find_element(By.ID, "input-search")
            search_field.send_keys("nissan")
            search_btn = self.driver.find_element_by_css_selector('.btn-lightblue')
            search_btn.click()
            search_results_table = WebDriverWait(self.driver, 10).until(
                cond.visibility_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']//tbody//td")))
            filter_options_title = self.driver.find_elements(By.XPATH, "//*[@class='list-group']/li/h4/a[1]")
            for option in filter_options_title:
                if option.text == "Model":
                    option.click()
                    input_for_el = count
                    path_to_input = "//*[@class='list-group']/li[" + str(input_for_el) + "]/div/form/div/input"
                    path_to_filter_entered = "//*[@class='list-group']/li[" + str(
                        input_for_el) + "]/div/ul/li/div/label/abbr"
                    print("Pth", path_to_input)
                count += 1
            input_selected = WebDriverWait(self.driver, 10).until(
                cond.visibility_of_element_located((By.XPATH, path_to_input)))
            input_selected.send_keys(search_criteria)
            input_selected.send_keys(Keys.RETURN)
            filtered_item = WebDriverWait(self.driver, 10).until(
                cond.visibility_of_element_located((By.XPATH, path_to_filter_entered)))
            print(filtered_item.text)
            self.assertTrue(filtered_item.text == search_criteria)

        except Exception as ex:
            print("You should get a screen pic")
            self.driver.save_screenshot("./screenshots/screen_shot.png")
            print("Screen shot taken and can be found in challenge6/screenshots")
            tb = sys.exc_info()[2]
            print(ex + tb)


if __name__ == '__main__':
    unittest.main()

# DONE - wait for table xpath to exist "//*[@id='serverSideDataTable']//tbody//td"  - search_field.
# DONE - get list of elements - //*[@class="list-group"]/li/h4/a[1] loop and click the one we want.
# DONE - le = list of elements find elements by (xpath)//*[@class="list-group"]/li/h4/a[1]
# DONE - for e le:
#     if e.text == "Model":
#         e.click()
# DONE - loop through elements to click the one you want.
# "//*[@id='serverSideDataTable + count + ]//tbody//td"
# DONE create a screen shot folder
