from pages.base_page import WebPage, PageLoadMixin
from elements import WebElement
from selenium.webdriver.common.by import By


class AuthPage(PageLoadMixin, WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    email = WebElement(id='email')

    password = WebElement(id='password')

    phone = WebElement (id='username')

    login_button = WebElement (id='kc-login')

    registration_link = WebElement(id='kc-register')

    submit_button = WebElement(By.CSS_SELECTOR, "button[type=submit]")

    form = WebElement(By.CSS_SELECTOR, "form[action='/login']")

class AuthForm(WebPage):
    def __init__(self, web_driver):
        print("AuthForm constructor called with web_driver:", web_driver)
        super().__init__(web_driver)

    @property
    def submit_button(self):
        print("Finding submit button")
        return self.driver.find_element_by_xpath('//button[@type="submit"]')

    # rest of the class


