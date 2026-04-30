import allure
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent

class SignUpModal(BaseComponent):
    email_locator = (By.ID, "email")
    name_locator = (By.ID, "firstName")
    password_locator = (By.ID, "password")
    confrim_password_locator = (By.ID, "repeatPassword")   
    submit_button_locator = (By.XPATH, "//button[@type='submit' and contains(@class, 'greenStyle')]")
    error_message_locator = (By.XPATH, "//div[@class='alert-general-error']")
    
    @allure.step("Fill registration form with email: {email}, name: {name}")
    def fill_registration_form(self, email, name, password, confirm_password):
        self.find_element(*self.email_locator).send_keys(email)
        self.find_element(*self.name_locator).send_keys(name)
        self.find_element(*self.password_locator).send_keys(password)
        self.find_element(*self.confrim_password_locator).send_keys(password)
    
    @allure.step("Submit registration form") 
    def click_submit(self):
        self.find_element(*self.submit_button_locator).click()
        
    @allure.step("Check if error message is displayed")    
    def is_error_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, "//div[contains(@class, 'error-message error-message-show ng-star-inserted')]").is_displayed()
        except:
            return False
        