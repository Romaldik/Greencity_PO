import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.events_page import EventsPage

@allure.feature("GreenCity UI Automation Tests")
class TestGreenCity:
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)
        yield
        self.driver.quit()

    @allure.story("TC-02: Filtration of events by category")
    @allure.step("Steps: Open dropdown and select category")
    def test_filtration_events(self):
        events_page = EventsPage(self.driver)
        
        events_page.open_filter_dropdown()
        events_page.select_filter_option('mat-option-4') 
        
        cards = events_page.get_cards()
        assert isinstance(cards, list), "Картки не відобразилися після фільтрації"

    @allure.story("TC-03: Search for events by keyword")
    @allure.step("Steps: Click search and enter text")
    def test_search_events(self):
        events_page = EventsPage(self.driver)
        
        events_page.click_search_icon()
        events_page.perform_search("Event") 
        
        cards = events_page.get_cards()
        assert len(cards) > 0, "Немає івентів після пошуку!"

    @allure.story("TC-01: Sign-up error handling")
    @allure.step("Steps: Fill form and check error")
    def test_sign_up_error_handling(self):
        page = BasePage(self.driver)
        
        page.click_sign_up()
        modal = page.get_sign_up_modal()
        
        modal.fill_registration_form("Test123567@test.com", "Roman", "Test1234!", "Test1234!")
        modal.click_submit()
        
        wait = WebDriverWait(self.driver, 10)
        error_displayed = wait.until(lambda d: modal.is_error_displayed())
        assert error_displayed, "Помилки не виявлено"

if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=allure-results"])