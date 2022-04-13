
from appium.webdriver.webdriver import WebDriver
class Basepage:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver
    def find(self,locator,value:str=None):
        if isinstance(locator,tuple):
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator,value)
