# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class TestAddGroup(unittest.TestCase):


    def setUp(self):
        service = Service(log_output="geckodriver.log")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("browser.cache.disk.enable", False)
        firefox_options.set_preference("browser.cache.memory.enable", False)
        firefox_options.set_preference("browser.cache.offline.enable", False)
        firefox_options.set_preference("network.http.use-cache", False)
        firefox_options.add_argument("-private")
        self.wd = webdriver.Firefox(service=service, options=firefox_options)
        #self.wd.execute_cdp_cmd("Network.clearBrowserCache", {})
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        time.sleep(3)
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME,"user").clear()
        wd.find_element(By.NAME,"user").send_keys("admin")
        wd.find_element(By.NAME,"pass").clear()
        wd.find_element(By.NAME,"pass").send_keys("secret")
        time.sleep(3)
        wd.find_element(By.ID, "LoginForm").submit()
        time.sleep(3)
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME,"new").click()
        time.sleep(3)
        wd.find_element(By.NAME,"group_name").click()
        wd.find_element(By.NAME,"group_name").clear()
        wd.find_element(By.NAME,"group_name").send_keys("name11111")
        wd.find_element(By.NAME,"group_header").click()
        wd.find_element(By.NAME,"group_header").clear()
        wd.find_element(By.NAME,"group_header").send_keys("logo11111")
        wd.find_element(By.NAME,"group_footer").click()
        wd.find_element(By.NAME,"group_footer").clear()
        wd.find_element(By.NAME,"group_footer").send_keys("Comment11111")
        wd.find_element(By.NAME,"submit").click()
        time.sleep(3)
        wd.find_element(By.LINK_TEXT, "group page").click()
        time.sleep(3)
        wd.find_element(By.LINK_TEXT, "Logout").click()

        wd.quit()
    '''
    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("name11111")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("logo11111")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Comment11111")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
      '''
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
