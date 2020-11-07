import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if  request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if  request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()



#Parallal execution
#py.test -v -n 2
#pip install pytest-xdist


#reporting
#py.test -v -s --html=test_param_result.html
#py.test -v -s --html=.\Reports\reports.html  --self-contained-html test_home_page.py

#Run Test Suite Collections
#py.test -v -s C:\Users\fathih\PycharmProjects\Rent Vehicles\admin_test_suite

