from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class BasePageLocators:
    login_link_xpath = (By.XPATH, '//a[@id="login_link"]')
    login_link_css = (By.CSS_SELECTOR, '#loginn_link')
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")


@dataclass
class LoginFormPageLocators:
    _login_form_locator = '//form[@id="login_form"]'
    login_header = (By.XPATH, f'{_login_form_locator}/h2')
    title_email = (By.XPATH, f'{_login_form_locator}//label[@for="id_login-username"]')
    field_email = (By.XPATH, f'{_login_form_locator}//input[@type="email"]')
    title_password = (By.XPATH, f'{_login_form_locator}//label[@for="id_login-password"]')
    field_password = (By.XPATH, f'{_login_form_locator}//input[@type="password"]')
    forgot_password = (By.XPATH, f'{_login_form_locator}//a')
    btn_login = [By.XPATH, f'{_login_form_locator}//button[@name="login_submit"]']


@dataclass
class RegisterFormPageLocators:
    _register_form_locator = '//form[@id="register_form"]'
    register_header = (By.XPATH, f'{_register_form_locator}/h2')
    title_email = (By.XPATH, f'{_register_form_locator}//label[@for="id_registration-email"]')
    field_email = (By.XPATH, f'{_register_form_locator}//input[@id="id_registration-email"]')
    title_password = (By.XPATH, f'{_register_form_locator}//label[@for="id_registration-password1"]')
    field_password = (By.XPATH, f'{_register_form_locator}//input[@id="id_registration-password1"]')
    title_confirm_password = (By.XPATH, f'{_register_form_locator}//label[@for="id_registration-password2"]')
    field_confirm_password = (By.XPATH, f'{_register_form_locator}//input[@id="id_registration-password2"]')
    btn_register = (By.XPATH, f'{_register_form_locator}//button[@name="registration_submit"]')


@dataclass
class ProductPageLocators:
    title = (By.XPATH, '//h1')
    price = (By.XPATH, '//p[@class="price_color"]')
    btn_add_to_basket = (By.XPATH, '//form[@id="add_to_basket_form"]/button[@type="submit"]')
    added_product_alert = (By.XPATH, '//div[@id="messages"]/div[1]//strong')
    basket_total_price_alert = (By.XPATH, '//div[@id="messages"]/div[3]//strong')
