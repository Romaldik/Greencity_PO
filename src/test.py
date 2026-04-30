import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.events_page import EventsPage

class TestGreenCity(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL) 

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_filtration_events(self):
        events_page = EventsPage(self.driver)
        
        events_page.open_filter_dropdown()
        
        events_page.select_filter_option('mat-option-4') 
        
        cards = events_page.get_cards()
        self.assertTrue(isinstance(cards, list), "Картки не відобразилися після фільтрації")

    def test_search_events(self):
        events_page = EventsPage(self.driver)
        
        events_page.click_search_icon()
        events_page.perform_search("Event") 
        
        cards = events_page.get_cards()
        self.assertGreater(len(cards), 0, "Немає івентів після пошуку!")

    def test_sign_up_error_handling(self):
        page = BasePage(self.driver)
        
        page.click_sign_up()
        modal = page.get_sign_up_modal()
        
        modal.fill_registration_form("Test12356@test.com", "Roman", "Test1234!", "Test1234!")
        modal.click_submit()
        
        wait = WebDriverWait(self.driver, 5)
        error_displayed = wait.until(lambda d: modal.is_error_displayed())
        self.assertTrue(error_displayed, "Помилки не виявлено")


if __name__ == "__main__":
    unittest.main()