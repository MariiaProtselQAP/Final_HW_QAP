from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import Valid_Data
from test_data import Invalid_Data

Base_URL = "https://b2c.passport.rt.ru"


#1 Регистрация c уже существующими данными
def test_registration_of_current_user(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Invalid_Data.current_user_name)
    driver.find_element(By.NAME, "lastName").send_keys(Invalid_Data.current_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Invalid_Data.current_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.current_user_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Invalid_Data.current_user_password)
    driver.find_element(By.NAME, "register").click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
        print("Регистрация успешна")
    except:
        print("Данная учетная запись уже существует")


#2 Регистрация нового пользователя
def registration_new_user(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.NAME, "register").click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.TAG_NAME, "h1"))
        print("Регистрация успешна")
    except:
        print("Данные указаны неверно")


#3 Регистрация с именем пользователя больше 30 символов
def registration_new_user_with_long_name(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Invalid_Data.first_name_41)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    if error_msg.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.':
        print("Проверка пройдена")

#4 Регистрация с именем пользователя в один символ
def registration_new_user_with_short_name(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Invalid_Data.first_name_1)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    if error_msg.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.':
        print("Проверка пройдена")

#5 Регистрация с именем пользователя с фамилией в один символ
def registration_new_user_with_short_last_name(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Invalid_Data.last_name_1)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    if error_msg.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.':
        print("Проверка пройдена")

#6 Регистрация с именем пользователя с фамилией в 41 символ
def registration_new_user_with_long_last_name(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Invalid_Data.last_name_41)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    if error_msg.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.':
        print("Проверка пройдена")


#7 Регистрация с паролем 25 символов
def registration_new_user_with_long_password(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.password_25)
    driver.find_element(By.ID, "password-confirm").send_keys(Invalid_Data.password_25)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    if error_msg.text == 'Длина пароля должна быть не более 20 символов':
        print("Проверка пройдена")

#8 Регистрация с паролем менее 8 символов
def registration_new_user_with_short_password(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.password_5)
    driver.find_element(By.ID, "password-confirm").send_keys(Invalid_Data.password_5)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    if error_msg.text == 'Длина пароля должна быть не менее 8 символов':
        print("Проверка пройдена")

#9 Регистрация с паролем без заглавных букв
def registration_new_user_with_password_no_lower(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Valid_Data.new_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.password_no_Lower)
    driver.find_element(By.ID, "password-confirm").send_keys(Invalid_Data.password_no_Lower)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    if error_msg.text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру':
        print("Проверка пройдена")

#10 Регистрация с неправильной почтой
def registration_new_user_with_wrong_email(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Invalid_Data.email_without_domain)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[3]/div/span')
    if error_msg.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru':
        print("Проверка пройдена")

#11 Регистрация с неправильным номером телефона
def registration_new_user_with_wrong_phoneNumber(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    driver.find_element(By.NAME, "firstName").send_keys(Valid_Data.new_user_first_name)
    driver.find_element(By.NAME, "lastName").send_keys(Valid_Data.new_user_last_name)
    driver.find_element(By.ID, "address").send_keys(Invalid_Data.invalid_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Valid_Data.new_user_valid_password)
    driver.find_element(By.ID, "password-confirm").send_keys(Valid_Data.new_user_valid_password)
    error_msg = driver.find_element(By.XPATH, '//[@id="page-right"]/div/div/div/form/div[3]/div/span')
    if error_msg.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru':
        print("Проверка пройдена")

#12 Авторизация с корректными данными по номеру телефона
def authorization_current_user(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    driver.find_element(By.ID, "username").send_keys(Invalid_Data.current_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.current_user_password)
    driver.find_element(By.ID, "kc-login").click

#13 Авторизация с некорректными данными по номеру телефона
def authorization_wrong_phoneNumber(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    driver.find_element(By.ID, "username").send_keys(Invalid_Data.invalid_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.current_user_password)
    driver.find_element(By.ID, "kc-login").click
    error_msg = driver.find_element(By.XPATH, '//[@id="form-error-message"]')
    if error_msg.text == 'Неверный логин или пароль':
        print("Проверка пройдена")

#14 Авторизация с неверным паролем
def authorization_wrong_password(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    driver.find_element(By.ID, "username").send_keys(Invalid_Data.current_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.password_5)
    driver.find_element(By.ID, "kc-login").click
    error_msg = driver.find_element(By.XPATH, '//[@id="form-error-message"]')
    if error_msg.text == 'Неверный логин или пароль':
        print("Проверка пройдена")


#15 Авторизация с неверной почтой
def authorization_wrong_email(selenium_driver):
    driver = selenium_driver

    driver.get(Base_URL)
    driver.find_element(By.ID, "t-btn-tab-mail").click()
    driver.find_element(By.ID, "username").send_keys(Invalid_Data.current_user_phoneNumber)
    driver.find_element(By.ID, "password").send_keys(Invalid_Data.password_5)
    driver.find_element(By.ID, "kc-login").click
    error_msg = driver.find_element(By.XPATH, '//[@id="form-error-message"]')
    if error_msg.text == 'Неверный логин или пароль':
        print("Проверка пройдена")


















