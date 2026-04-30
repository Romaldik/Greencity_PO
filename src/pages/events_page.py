import allure
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from components.event_card_component import EventCardComponent

class EventsPage(BasePage):
    cards_locator = (By.XPATH, "//mat-card")
    filter_dropdown_locator = (By.XPATH, "//div[contains(@class, 'mat-mdc-select-arrow-wrapper')]")
    search_icon_locator = (By.XPATH, "//div[contains(@class, 'container-img')]")
    search_input_locator = (By.XPATH, "//input[@placeholder='Search']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Open filter dropdown")
    def open_filter_dropdown(self):
        self.driver.find_element(*self.filter_dropdown_locator).click()
    
    @allure.step("Select filter option: {option_id}")
    def select_filter_option(self, option_id):
        self.driver.find_element(By.ID, option_id).click()
            
    @allure.step("Get event cards")
    def get_cards(self) -> list[EventCardComponent]:
        elements = self.driver.find_elements(*self.cards_locator)
        return [EventCardComponent(el) for el in elements]
    
    def click_search_icon(self):
        self.driver.find_element(*self.search_icon_locator).click()
    
    @allure.step("Perform search for events with text: {text}")    
    def perform_search(self, text: str):
        search_input = self.driver.find_element(*self.search_input_locator)
        search_input.clear()
        search_input.send_keys(text + Keys.ENTER)
    
    def apply_filter(self, option_id):
        self.driver.find_element(*self.filter_dropdown_locator).click()
        self.driver.find_element(By.ID, option_id).click()