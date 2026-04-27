import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.components.event_card_component import EventCardComponent

class EventsPage(BasePage):
    main_header_locator = (By.XPATH, "//h1[contains(@class, 'main-header')]")
    items_found_locator = (By.XPATH, "//div[@class='active-filter-container']/p")
    cards_locator = (By.XPATH, "//mat-card")
    
    filter_dropdown_locator = (By.XPATH, "//div[contains(@class, 'mat-mdc-select-arrow')]")
    search_icon_locator = (By.XPATH, "//div[contains(@class, 'container-img')]")
    search_input_locator = (By.XPATH, "//input[@placeholder='Search']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_items_count(self):
        try:
            text = self.driver.find_element(*self.items_found_locator).text
            count = re.search(r'\d+', text)
            return int(count.group()) if count else 0
        except:
            return 0
        
    def get_cards(self) -> list[EventCardComponent]:
        elements = self.driver.find_elements(*self.cards_locator)
        return [EventCardComponent(el) for el in elements]
    
    def click_search_icon(self):
        self.driver.find_element(*self.search_icon_locator).click()
        
    def perform_search(self, text: str):
        search_input = self.driver.find_element(*self.search_input_locator)
        search_input.clear()
        search_input.send_keys(text + Keys.ENTER)
        
    def open_filter_dropdown(self):
        self.driver.find_element(*self.filter_dropdown_locator).click()
    
    def select_filter_option(self, option_id: str):
        self.driver.find_element(By.ID, option_id).click()
        