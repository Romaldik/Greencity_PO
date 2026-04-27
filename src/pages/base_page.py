from selenium.webdriver.common.by import By
from pages.components.sign_up_modal import SignUpModal

class BasePage:
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    sign_up_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-up-link")
    language_switcher = (By.XPATH, "//ul[@aria-label='language switcher']")
    language_en_option = (By.XPATH, ".//span[contains(text(), 'En')]")
    language_ua_option = (By.XPATH, ".//span[contains(text(), 'Uk')]")
    
    eco_news_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and (contains(., 'Еко новини') or contains(., 'Eco news'))]")
    events_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and (contains(., 'Події') or contains(., 'Events'))]")
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button_locator).click()
        
    def click_sign_up(self):
        self.driver.find_element(*self.sign_up_button_locator).click() 
    
    def get_sign_up_modal(self):
        modal_element = self.driver.find_element(By.XPATH, "//app-auth-modal")
        return SignUpModal(modal_element)
    
    def switch_language(self, language):
        switcher = self.driver.find_element(*self.language_switcher)
        switcher.click()
        
        if language.lower() == 'en':
            option = self.driver.find_element(*self.language_en_option)
            
        elif language.lower() == 'ua':
            option = self.driver.find_element(*self.language_ua_option)
            
        else:
            raise ValueError("Unsupported language: {}".format(language))
        option.click()
    
    def navigate_to_eco_news(self):
        self.driver.find_element(*self.eco_news_link_locator).click()
        
    def get_events_link(self):
        return self.driver.find_element(*self.events_link_locator)
    
    def navigate_to_events(self):
        self.get_events_link().click()