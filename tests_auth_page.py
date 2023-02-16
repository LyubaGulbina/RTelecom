import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests_RT.settings import *
from elements import WebElement
from pages.auth_page import AuthPage
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(r'C:\test\chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# test #1 - smoke testing
def test_open_auth_page(driver):
    driver.get("https://b2c.passport.rt.ru/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))
    assert driver.title == "Ростелеком ID"


# test # 2 - check that the logo is displayed on the page
def test_company_logo_present():
    # initialize a web driver instance
    driver = webdriver.Chrome()

    # navigate to the website
    driver.get("https://b2c.passport.rt.ru/")

    # wait for the company logo element to be present
    company_logo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body:nth-child(2) div:nth-child(27) header:nth-child(1) div.main-header > div.main-header__logo-container")))

   # close the browser window
    driver.close()


# test # 3 - test that the logo is correctly located
def test_company_logo_present_on_the_right():
    # initialize a web driver instance
    driver = webdriver.Chrome()

    # navigate to the website
    driver.get("https://b2c.passport.rt.ru/")

    # wait for the company logo element to be present
    company_logo = driver.find_element(By.XPATH, '//*[@id="page-left"]/div/div[1]')

       # close the browser window
    driver.close()



# test # 4 - check that the authorization header is present

def test_authorization_header_present(driver):
    # navigate to the website
    driver.get("https://b2c.passport.rt.ru/")

    try:
        # find the header element using the XPath expression
        header_element = driver.find_element(By.XPATH, "//h1[contains(text(),'Авторизация')]")

        # verify that the header element is displayed on the page
        assert header_element.is_displayed()

    except AssertionError:
        # take a screenshot in case of test failure
        timestamp = str(time.time())
        filename = "screenshot_" + timestamp + ".png"
        driver.save_screenshot(filename)
        raise

# test # 5 - check that the header is correctly located
def test_auth_header_displayed_on_the_left(driver):
    # navigate to the website
    driver.get("https://b2c.passport.rt.ru/")

            # find the header element using the XPath expression

    title_element = driver.find_element(By.XPATH, '//*[@id="page-left"]//*[@id="page-left"]/div/div[2]/h2')

        # verify that the header element is displayed on the page correctly
    assert title_element.is_displayed()

#test # 6 - check that the phone tab is displayed

def test_phone_tab_is_displayed(driver):
    element = WebElement(web_driver=driver, id='t-btn-tab-phone')

        # navigate to the website
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    phone_tab = wait.until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone')))

    # Verify that the phone tab element is displayed
    assert phone_tab.is_displayed()


# test # 7 - check that the login tab is displayed

def test_login_tab_is_displayed(driver):
    # locate the element
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)
    login_tab = wait.until(EC.visibility_of_element_located((By.ID, 't-btn-tab-login')))
    # assert that it's clickable
    assert login_tab.is_displayed()

# test # 8 - check that the email tab is displayed

def test_mail_tab_is_displayed(driver):
    # locate the element

    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # locate the element
    mail_tab = wait.until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail')))

    # assert that it's clickable
    assert mail_tab.is_displayed()

# test # 9 - check that the 'Лицевой счет' tab is displayed

def test_pers_account_tab_is_displayed(driver):

    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)
    # locate the element
    pers_account_tab = wait.until(EC.visibility_of_element_located((By.ID, 't-btn-tab-ls')))

    # assert that it's displayed
    assert pers_account_tab.is_displayed()

# test # 10 - check that the user input field is enabled

def test_user_name_input_is_clickable():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    # locate the element
    user_name_input = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    wait = WebDriverWait(driver, 10)
    # locate the element
    user_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, user_name_input._locator[1])))
    user_name_input._web_driver = driver
    assert user_name_input.is_enabled()
    driver.quit()

# test # 11 - check that the password input field is enabled

def test_password_input_is_clickable():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    # locate the element
    password_input = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    wait = WebDriverWait(driver, 10)
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, password_input._locator[1])))
    password_input._web_driver = driver
    assert password_input.is_enabled()
    driver.quit()

# test # 12 - check that the forgotten password link is clickable

def test_forgotten_password_is_clickable():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    input_element = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    wait = WebDriverWait(driver, 10)
    input_element = wait.until(EC.visibility_of_element_located((By.XPATH, input_element._locator[1])))
    input_element._web_driver = driver
    assert input_element.is_enabled()
    driver.quit()

# test # 13 - check that the user agreement link is clickable

def test_user_agreement_link_is_clickable():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    # locate the element
    input_element = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/a')
    wait = WebDriverWait(driver, 10)
    # locate the element
    input_element = wait.until(EC.visibility_of_element_located((By.XPATH, input_element._locator[1])))
    input_element._web_driver = driver
    assert input_element.is_enabled()
    driver.quit()

# test # 14 - check that the login button is enabled

def test_login_button_is_clickable():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    # locate the element
    test_login_button = WebElement(xpath="//button[@id='kc-login']")
    test_login_button._web_driver = driver
    wait = WebDriverWait(driver, 10)
    # locate the element
    wait.until(EC.element_to_be_clickable((By.XPATH, test_login_button._locator[1])))

    assert test_login_button.is_clickable()
    driver.quit()

# test # 15 - check that the sign in link is clickable

def test_sign_in_link_is_clickable():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
        # locate the element
    sign_in_link = WebElement(xpath="//a[@id='kc-register']")
    sign_in_link._web_driver = driver
    wait = WebDriverWait(driver, 10)
        # wait for element to be clickable
    wait.until(EC.element_to_be_clickable((By.XPATH, sign_in_link._locator[1])))
        # check if element is clickable
    assert sign_in_link.is_clickable()
    driver.quit()

def test_successful_login(driver):
    # Initialize the webdriver
    driver = webdriver.Chrome()

    # Load the login page
    driver.get("https://b2c.passport.rt.ru/")
    auth_page = AuthPage(driver)

    auth_page.phone.send_keys(valid_phone)
    auth_page.password.send_keys(valid_password)

    login_button = auth_page.login_button
    login_button.click()

    # Assert that the last name and first name fields contain the correct information
    # last_name_element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "user-name__last-name")))
    last_name_element = driver.find_element(By.XPATH, "//h2[contains(text(),'Иванова')]")
    assert last_name_element.text == "Иванова"

    # first_name_element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "user-name__first-patronymic")))

    # assert first_name_element.text == "Ивана"


    # account_name_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="account_name"]')))
    # assert account_name_element.text == valid_account_name

    # Quit the webdriver
    driver.quit()

from Elements import WebElement

def test_successful_login(driver):
    # Load the login page
    driver.get("https://b2c.passport.rt.ru/")
    auth_page = AuthPage(driver)

    # Enter valid phone number and password
    auth_page.phone.send_keys(valid_phone)
    auth_page.password.send_keys(valid_password)

    # Submit the login form
    auth_page.form.submit_button.click()

    # Assert that the last name and first name fields contain the correct information
    last_name_element = WebElement(driver, By.CSS_SELECTOR, ".user-name__last-name")
    assert last_name_element.get_text() == "Иванова"

    first_name_element = WebElement(driver, By.CSS_SELECTOR, ".user-name__first-patronymic")
    assert first_name_element.get_text() == "Ивана"

    # Close the webdriver
    driver.close()

