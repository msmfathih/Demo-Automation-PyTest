from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from TestData.config import TestData
from Configuration.conftest import init_driver

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Staticpage(BaseTest):

    def test_navigate_static_page(self):
        self.driver.get(TestData.REGISTER_PAGE)
        self.driver.implicitly_wait(20)

        assert "Register" in self.driver.title
        print("Assertion Test Pass")

    def test_mouse_over_pages(self):
        ack = ActionChains(self.driver)
        ack.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Interactions')]")).perform()
        ack.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Drag and Drop')]")).perform()
        ack.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Static')]")).click().perform()
        time.sleep(10)

    # def test_drag_and_drop(self):
    #     source_element = self.driver.find_element_by_xpath("//img[@id='mongo']")
    #     target_element = self.driver.find_element_by_xpath("//div[@id='droparea']")
    #     ack_chains = ActionChains(self.driver)
    #
    #     ack_chains.click_and_hold(source_element)\
    #         .move_to_element(target_element)\
    #         .release()\
    #         .perform()










