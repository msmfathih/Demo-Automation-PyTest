from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from TestData.config import TestData
from Configuration.conftest import init_driver

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Homepage(BaseTest):


    def test_valid_login(self):
        self.driver.get("http://demo.automationtesting.in/Index.html")
        assert "Index" in self.driver.title
        print("Assertion Test Pass")

        clear_email_field = self.driver.find_element(By.ID, "email").clear()
        enter_valid_email = self.driver.find_element(By.ID, "email")
        enter_valid_email.send_keys(TestData.USER_NAME)
        time.sleep(2)

        press_login_button = self.driver.find_element(By.ID, "enterimg")
        press_login_button.click()


    def test_register_form(self):

        verifyRegisterPageTitle = self.driver.find_element(By.XPATH,
                                                                "//h1[contains(text(),'Automation Demo Site')]")
        assert verifyRegisterPageTitle.text == "Automation Demo Site"

        clear_first_name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        enter_first_name = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        enter_first_name.send_keys(TestData.FIRST_NAME)
        time.sleep(3)

        clear_first_name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        enter_first_name = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        enter_first_name.send_keys(TestData.LAST_NAME)
        time.sleep(2)

        clear_address_textfeild_area = self.driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[2]/div/textarea")
        enter_address = self.driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[2]/div/textarea")
        enter_address.send_keys(TestData.ADDRESS)
        time.sleep(2)

        enter_email = self.driver.find_element(By.XPATH,
                                               "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]")
        enter_email.send_keys("test@gmail.com")

        enter_phone_number = self.driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[4]/div/input")
        enter_phone_number.send_keys("65455545555")
        time.sleep(2)

    #
    # def test_select_gender(self):
    #     select_gender = self.driver.find_element(By.NAME, 'radiooptions')
    #     select_gender.click()
    #     time.sleep(2)

    def test_select_gender(self):
        radioBtnList = self.driver.find_elements(By.NAME, 'radiooptions')
        size = len(radioBtnList)
        print("Size of the radio button is " + str(radioBtnList))

        for radioButton in radioBtnList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(1)


    def test_select_hobby(self):
        select_hobby = self.driver.find_element(By.ID, 'checkbox1')
        select_hobby2 = self.driver.find_element(By.ID, 'checkbox2')
        select_hobby.click()
        select_hobby2.click()
        time.sleep(2)


    def test_select_language_dropdown(self):
        self.driver.find_element(By.ID, 'msdd').click()
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



    # def test_select_country(self):
    #     self.driver.find_element(By.XPATH, "//*[@class='select2-selection select2-selection--single']").click()
    #     time.sleep(2)
    #     drop_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.select2-selection__rendered')
    #
    #     for ele in drop_list:
    #         print(ele.text)
    #         if ele.text == "India":
    #             ele.click()
    #             break

    def test_select_skill(self):
        element1 = self.driver.find_element_by_id("Skills")
        sel = Select(element1)
        sel.select_by_index(3)
        time.sleep(2)


    def test_select_country(self):
        element1 = self.driver.find_element_by_id("countries")
        sel = Select(element1)
        sel.select_by_index(4)
        time.sleep(2)


    def test_select_dob(self):
        element1 = self.driver.find_element_by_id("yearbox")
        sel = Select(element1)
        sel.select_by_visible_text("1991")

        element1 = self.driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
        sel = Select(element1)
        sel.select_by_visible_text("November")

        element1 = self.driver.find_element(By.ID, 'daybox')
        sel = Select(element1)
        sel.select_by_index(14)

    def test_set_password(self):
        enter_password = self.driver.find_element(By.ID, 'firstpassword')
        enter_password.send_keys(TestData.ENTER_PASSWORD)

        confirm_password = self.driver.find_element(By.ID, 'secondpassword')
        confirm_password.send_keys(TestData.CONFIRM_PASSWORD)


    def test_upload_profile_picture(self):
        uploadFile = self.driver.find_element_by_id("imagesrc")
        uploadFile.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(2)





