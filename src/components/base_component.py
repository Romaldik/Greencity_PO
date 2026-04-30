import allure 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseComponent:
    def __init__(self, root: WebElement):
        self.node = root
        self.driver = root.parent
        
    def find_element(self, by=By.XPATH, value=None):
        return self.node.find_element(by, value)
    
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    