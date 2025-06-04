from selenium.webdriver.common.by import By

class RegistrationPageElements:
    """
    Define los localizadores (Targets) para los elementos en las páginas
    de Registro y Creación de Cuenta.
    """
    # Primera parte del registro (Signup / Login)
    SIGNUP_NAME_INPUT = (By.NAME, "name")
    SIGNUP_EMAIL_INPUT = (By.XPATH, '//input[@data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.XPATH, '//button[@data-qa="signup-button"]')

    # Página "Enter Account Information"
    ENTER_ACCOUNT_INFO_HEADER = (By.XPATH, '//b[contains(text(),"Enter Account Information")]')
    GENDER_RADIO_MALE = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS_DROPDOWN = (By.ID, "days")
    MONTHS_DROPDOWN = (By.ID, "months")
    YEARS_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OPTIN_CHECKBOX = (By.ID, "optin")

    # Página "Address Information"
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@data-qa="create-account"]')
    ACCOUNT_CREATED_HEADER = (By.XPATH, '//b[contains(text(),"Account Created!")]')