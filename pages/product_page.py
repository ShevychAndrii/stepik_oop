from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_the_basket(self) -> None:
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.btn_add_to_basket)
        btn_add_to_basket.click()

    def should_be_product_name_in_the_added_to_the_basket_alert(self) -> None:
        name = self.browser.find_element(*ProductPageLocators.title).text
        name_in_alert = self.browser.find_element(*ProductPageLocators.added_product_alert).text
        assert name == name_in_alert, f'Incorrect product name in the basket message. Actual: {name_in_alert}, Expected: {name}'

    def should_be_product_price_in_the_basket_total_price_alert(self) -> None:
        price = self.browser.find_element(*ProductPageLocators.price).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.basket_total_price_alert).text
        assert price == price_in_alert, f'Incorrect total basket price. Actual: {price_in_alert}, Expected: {price}'

    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.added_product_alert), \
            '"Product added to the basket" alert is shown, but should not be.'

    def should_success_message_disappear(self, timeout: int = 4) -> None:
        assert self.is_disappeared(*ProductPageLocators.added_product_alert, timeout=timeout), \
            f'"Product added to the basket" alert does not disappear after {timeout} seconds.'
