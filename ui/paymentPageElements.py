from selenium.webdriver.common.by import By

class PaymentPageElements:
    """
    Define los localizadores (Targets) para los elementos en la Página de Pago.
    """
    NAME_ON_CARD_INPUT = (By.NAME, 'name_on_card')
    CARD_NUMBER_INPUT = (By.NAME, 'card_number')
    CVC_INPUT = (By.NAME, 'cvc')
    EXPIRY_MONTH_INPUT = (By.NAME, 'expiry_month')
    EXPIRY_YEAR_INPUT = (By.NAME, 'expiry_year')
    SUBMIT_PAYMENT_BUTTON = (By.ID, 'submit')
    ORDER_PLACED_SUCCESS_HEADER = (By.CSS_SELECTOR, 'h2[data-qa="order-placed"]')
    DOWNLOAD_INVOICE_LINK = (By.LINK_TEXT, 'Download Invoice')
    CONTINUE_BUTTON = (By.XPATH, '//a[@data-qa="continue-button"]')
