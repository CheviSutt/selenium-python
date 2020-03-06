import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

porsche = "Porsche"


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        model_count = 0
        all_makes = []
        make = ''
        self.driver.get("https://www.copart.com")
        search_input = self.driver.find_element(By.ID, 'input-search')
        search_input.send_keys(porsche)
        search_btn = self.driver.find_element_by_css_selector('.btn-lightblue')
        search_btn.click()
        porsche_currently_listed = WebDriverWait(self.driver, 10).until(
            cond.visibility_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td[5]")))
        show_entries = self.driver.find_elements(By.XPATH, "//select[@name='serverSideDataTable_length'][1]/option")
        for select_entry in show_entries:
            if select_entry.text == 100:
                select_entry.click()
        # print("Ethan", select_entry.get_attribute('value'))

        vehicle_row_by_make = WebDriverWait(self.driver, 5).until(
            cond.visibility_of_all_elements_located((By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr/td[6]/span")))
        for vehicle_make in vehicle_row_by_make:
            make = vehicle_make.text
            all_makes.append(make)
        # print(all_makes)
        make_dict = {i: all_makes.count(i) for i in all_makes}
        print(make_dict)

        # if make == make:
        #     model_count += 1
        #     print(make + ': x' + str(model_count))
        #     if model_count >= 1:
        #         all_makes.append([make])
        # for make in all_makes:
        #     print("Hello", make)
        # print(" - List Text:", porsche_currently_listed.text)
        # self.assertTrue(porsche_currently_listed.text == porsche)


if __name__ == '__main__':
    unittest.main()
