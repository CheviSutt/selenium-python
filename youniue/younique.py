import time
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
        self.driver.get("https://www.youniqueproducts.com/products/view/US-51081-01")
        # time.sleep(10)
        add_to_cart_button = self.driver.find_element_by_css_selector('.addToCartWithQty button').click()
        cond.visibility_of_element_located((By.XPATH, "/html//button[@id='viewCart']"))
        # cart_contents = cond.visibility_of_element_located((By.XPATH, "/html//table[@id='cartview']//td[@class='clr-fix ctr']/span[.='$12.00']"))
        cart_contents = self.driver.find_elements_by_css_selector(".totals groupRow")
        print(cart_contents)


if __name__ == '__main__':
    unittest.main()
