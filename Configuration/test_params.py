import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestRentVehicle(BaseTest):

    @pytest.mark.parametrize(
                                 "username, password",
                                [
                                    ("ashikamrf71@gmail.com", "ashika@91"),
                                    ("admin@gmail.com", "admin@123"),
                                ]
                            )
    def test_login(self, username, password):
        """
        This param method used to login Rent Vehicle Application
        :param username:
        :param password:
        :return:
        """
        self.driver.get("http://rentvehicles.multicompetition.com/login")

        try:
            assert "Rent Vehicles" in self.driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "rentvehicles" in self.driver.current_url

        self.driver.find_element(By.ID, 'email').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//p[contains(text(),'Need to logout ?')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//p[contains(text(),'Logout')]").click()
        time.sleep(3)

