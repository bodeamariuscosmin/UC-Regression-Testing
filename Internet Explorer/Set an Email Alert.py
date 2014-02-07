from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Alert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(60)
        self.base_url = "https://staging.urbancompass.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_alert(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qa+renter@urbancompass.com")
        driver.find_element_by_xpath(".//*[@id='sign-in']/div[2]/form/fieldset[2]/input").send_keys("parola")
        driver.find_element_by_css_selector("#sign-in > div.modal_content > form > input[type=\"submit\"]").click()
        time.sleep(10)
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Brooklyn")
        driver.find_element_by_id("search_button").click()
        driver.find_element_by_xpath("//li[@id='save_search']/a/img").click()
        time.sleep(5)
        driver.find_element_by_css_selector("div.save_button").click()
        driver.find_element_by_link_text("Rentals").click()
        driver.find_element_by_id("address_search").click()
        driver.find_element_by_id("address_search").send_keys("Manhattan")
        driver.find_element_by_id("search_button").click()
        driver.find_element_by_xpath("//li[@id='save_search']/a/img").click()
        time.sleep(5)
        driver.find_element_by_css_selector("div.save_button").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#manage_alerts").click()
        driver.find_element_by_id("notify-immediately").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Search alerts").click()
        driver.find_element_by_css_selector("div.search-alert-run").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Search alerts").click()
        driver.find_element_by_css_selector("div.search-alert-delete.remove-button").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Search alerts").click()
        driver.find_element_by_css_selector("div.search-alert-delete.remove-button").click()
        driver.find_element_by_link_text("Me").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()