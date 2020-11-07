import time
import pytest
from selenium.webdriver.common.by import By
from TestData.config import TestData
from Locators.Locators import Locators
from Configuration.conftest import init_driver
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

@pytest.mark.run(order=1)
class Test_loginpage(BaseTest):

    def test_invalid_login(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(20)

        assert "Index" in self.driver.title
        print("Assertion Test Pass")
        try:
            assert "Index" in self.driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "Index" in self.driver.current_url

        self.driver.find_element(By.ID, Locators.SINGIN_BUTTON_ID).click()
        enter_username = self.driver.find_element(By.XPATH, Locators.USERNAME_XPATH)
        enter_username.send_keys(TestData.USER_NAME)
        time.sleep(2)

        enter_password = self.driver.find_element(By.XPATH, Locators.PASSWORD_XPATH)
        enter_password.send_keys(TestData.PASSWORD)
        time.sleep(2)

        enter_login_button = self.driver.find_element(By.ID, Locators.LOGIN_BUTTON_ID)
        enter_login_button.click()
        time.sleep(2)

        verifyWrongEmailErrorMessage = self.driver.find_element(By.XPATH, Locators.VERIFY_WRONG_EMAIL_XPATH)
        assert verifyWrongEmailErrorMessage.text == Locators.VERIFY_EMAIL_MESSAGE
        self.driver.back()

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        enter_valid_email = self.driver.find_element(By.ID, Locators.VALID_EMAIL_ID)
        enter_valid_email.send_keys(TestData.USER_NAME)
        time.sleep(2)
        self.driver.find_element(By.ID, Locators.INDEX_LOGIN_BUTTON_ID).click()









