import allure
from selenium.webdriver.common.by import By
from pages.components.sign_up_modal import SignUpModal

class BasePage:
    sign_up_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-up-link")
    
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Click 'Sign Up' button in header")    
    def click_sign_up(self):
        self.driver.find_element(*self.sign_up_button_locator).click() 
    
    def get_sign_up_modal(self):
        modal_element = self.driver.find_element(By.XPATH, "//app-auth-modal")
        return SignUpModal(modal_element)
    
    