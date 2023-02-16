from pages.base_page import WebPage
from elements import WebElement


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)



registration_link = WebElement(id='kc-register')


