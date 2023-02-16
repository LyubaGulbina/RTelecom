import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests_RT.settings import *
from elements import WebElement
from pages.auth_page import AuthPage
from pages.reg_page import RegPage
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(r'C:\test\chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# test #1 - smoke test
def test_open_registration_page(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: Assert that the title is correct
    WebDriverWait(driver, 10).until(EC.title_is("Ростелеком ID"))

# test # 2 - check whether the first name field at the registration page is enabled

def test_name_field_reg_page_is_clickable(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: Assert that the name input field is present
    name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')))
    assert name_field.is_enabled()

# test # 3 - check whether the first name field at the registration page is enabled
def test_last_name_field_reg_page_is_clickable(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: Assert that the last name input field is present
    last_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')))
    assert last_name_field.is_enabled()

#test # 4 - check whether the phone or mail field is enabled:

def test_login_field_reg_page_is_clickable(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: Assert that the email or phone input field is present
    login_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[2]')))
    assert login_field.is_enabled()

# test # 5 - check whether the password and confirm password fields are enabled

def test_password_field_reg_page_is_clickable(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: Assert that the password input fields are clickable
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')))
    confirm_password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')))

    assert password_field.is_enabled()
    assert confirm_password_field.is_enabled()

#test # 6 - check whether the registration button is enabled

def test_reg_button_reg_page(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: Assert that the registration button is clickable and that it contains text "Продолжить"
    registration_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')))

    assert registration_button.is_enabled()
    assert registration_button.text == 'Продолжить'

# test # 7 - attempt to register with an invalid email

def test_invalid_mail_registration(driver):
    # Step 1: Open the login page
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the registration link
    registration_link = wait.until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    registration_link.click()

    # Step 3: locate elements by xpath
    name_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')))
    last_name_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')))
    # region_name_field = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')))
    email_or_phone_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/input')))
    password_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/input')))
    conf_password_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/input')))

    # Step 4: fill in the fields
    name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    # region_name_field.send_keys(region_name)
    email_or_phone_name_field.send_keys(invalid_email)
    password_field.send_keys(valid_password)
    conf_password_field.send_keys(valid_password)


    # Step 5: Click on the registration button and assert error message
    # registration_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//html/body/div[1]/main/section[2]/div/div/div/form/button')))
    # registration_button.click()
    form = driver.find_element(By.XPATH,'//html/body/div[1]/main/section[2]/div/div/div/form')
    #element = driver.find_element(By.XPATH, "//xpath_expression_here")

    form.submit()

    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span')))
    assert error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

