from pages.base_page import BasePage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = BasePage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, url=browser.current_url)
    login_page.should_be_login_page()
