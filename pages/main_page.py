from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.login_link_xpath)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.login_link_xpath), 'Login link is not presented.'
