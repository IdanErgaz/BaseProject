from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


# @pytest.fixture()
# def setup():
#     service = Service("C://Drivers/chromedriver.exe")
#     global driver
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     return driver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        service = Service("C://Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        print('Lunching Chrome browser..........')
    elif browser=='firefox':
        service = Service("C://Drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        print("Lunching Firefox Browser...")
    return driver

        #currently we still have issue with opening the IE browser
    # else:
    #     driver=webdriver.Ie(executable_path="C:\\Projects\\Automation\\Drivers\\IEDriverServer.exe")
    #     # driver=webdriver.Ie()

def pytest_addoption(parser):#this will get a value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Idan\'s Project'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Idan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)