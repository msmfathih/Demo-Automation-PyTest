from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from TestData.config import TestData
from Locators.Locators import Locators
from Configuration.conftest import init_driver

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Homepage(BaseTest):


    def test_valid_login(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(20)

        assert "Index" in self.driver.title
        print("Assertion Test Pass")

        enter_valid_email = self.driver.find_element(By.ID, Locators.VALID_EMAIL_ID)
        enter_valid_email.send_keys(TestData.USER_NAME)
        time.sleep(2)
        self.driver.find_element(By.ID, Locators.INDEX_LOGIN_BUTTON_ID).click()


    def test_register_form(self):

        verifyRegisterPageTitle = self.driver.find_element(By.XPATH, Locators.VERIFY_REGISTER_PAGE_TITLE)
        assert verifyRegisterPageTitle.text == Locators.REGISTER_PAGE_TITLE_MESSAGE

        enter_first_name = self.driver.find_element(By.XPATH, Locators.FIRST_NAME_XPATH)
        enter_first_name.send_keys(TestData.FIRST_NAME)
        time.sleep(2)

        enter_last_name = self.driver.find_element(By.XPATH, Locators.LAST_NAME_XPATH)
        enter_last_name.send_keys(TestData.LAST_NAME)
        time.sleep(2)

        enter_address = self.driver.find_element(By.XPATH, Locators.ADDRESS_XPATH)
        enter_address.send_keys(TestData.ADDRESS)
        time.sleep(2)

        enter_email = self.driver.find_element(By.XPATH,Locators.EMAIL_ADDRESS_XPATH)
        enter_email.send_keys(TestData.ENTER_EMAIL)

        enter_phone_number = self.driver.find_element(By.XPATH, Locators.PHONE_NUMBER_XPATH)
        enter_phone_number.send_keys(TestData.ENTER_PHONE_NUMBER)
        time.sleep(2)


    def test_select_gender(self):
        radioBtnList = self.driver.find_elements(By.NAME, Locators.GENDER_NAME)
        size = len(radioBtnList)
        print("Size of the radio button is " + str(radioBtnList))

        for radioButton in radioBtnList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(1)


    def test_select_hobby(self):
        select_hobby = self.driver.find_element(By.ID, Locators.HOBBY1_ID)
        select_hobby2 = self.driver.find_element(By.ID, Locators.HOBBY2_ID)
        select_hobby.click()
        select_hobby2.click()
        time.sleep(2)


    def test_select_language_dropdown(self):
        self.driver.find_element(By.ID, Locators.LANGUAGE_DROPDOWN_ID).click()
        drop_list = self.driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')
        for ele in drop_list:
            print(ele.text)
            if ele.text == TestData.DROPDOWN_LANGUAGE:
                ele.click()
                break
            for ele in drop_list:
                print(ele.text)
                if ele.text == TestData.DROPDOWN_LANGUAGE2:
                    ele.click()
                    break

    def test_select_skill(self):
        element1 = self.driver.find_element_by_id(Locators.SKILL_ID)
        sel = Select(element1)
        sel.select_by_index(3)
        time.sleep(2)


    def test_select_country(self):
        element1 = self.driver.find_element_by_id(Locators.COUNTRY_ID)
        sel = Select(element1)
        sel.select_by_index(4)
        time.sleep(2)


    def test_select_dob(self):
        element1 = self.driver.find_element_by_id(Locators.DOB_YEAR_ID)
        sel = Select(element1)
        sel.select_by_visible_text("1991")

        element1 = self.driver.find_element(By.XPATH, Locators.DOB_MONTH_XPATH)
        sel = Select(element1)
        sel.select_by_visible_text("November")

        element1 = self.driver.find_element(By.ID, Locators.DOB_DATE_ID)
        sel = Select(element1)
        sel.select_by_index(14)

    def test_set_password(self):
        enter_password = self.driver.find_element(By.ID, Locators.SET_PASSWORD_ID)
        enter_password.send_keys(TestData.ENTER_PASSWORD)

        confirm_password = self.driver.find_element(By.ID, Locators.CONFIRM_PASSWORD_ID)
        confirm_password.send_keys(TestData.CONFIRM_PASSWORD)


    def test_upload_profile_picture(self):
        uploadFile = self.driver.find_element_by_id(Locators.UPLOAD_PROFILE_PICTURE_ID)
        uploadFile.send_keys(Locators.PROFILE_IMAGE_PATH)
        time.sleep(2)





