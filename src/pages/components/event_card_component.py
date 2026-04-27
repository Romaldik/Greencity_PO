from selenium.webdriver.common.by import By
from pages.components.base_component import BaseComponent

class EventCardComponent(BaseComponent):
    more_button_locator = (By.XPATH, "./app-events-list-item/div/div[3]/div[2]/button[1]")
    name_locator = (By.XPATH, ".//p[contains(@class, 'event-name')]")
    
    def click_more(self):
        self.find_element(*self.more_button_locator).click()
        
    def get_name(self):
        return self.find_element(*self.name_locator).text