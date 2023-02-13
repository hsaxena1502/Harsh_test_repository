from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser =="Chrome":
        driver=webdriver.Chrome(executable_path="/Users/harshsaxena/Downloads/chromedriver_mac_arm64")
        print("launched chrome browser")
    elif browser=="firefox":
        driver=webdriver.firefox(executable_path1="/Users/harshsaxena/Drivers/firefoxdriver")
        print("launched firefox browser")
    return driver

def pytest_adoption(parser):            #this will get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request) :                  #thiw will return browser value to setup method
    return request.config.getoption("--browser")

################Pytest HTML report################
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerece'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

#####It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
