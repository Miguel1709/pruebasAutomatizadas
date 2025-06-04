from selenium.webdriver.common.by import By

class CommonElements:
    """
    Define localizadores (Targets) para elementos comunes que pueden aparecer
    en múltiples páginas, como modales, headers, etc.
    """
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".close-modal")
    # Si hay un elemento de cabecera que siempre está presente en el sitio
    HEADER_CART_LINK = (By.LINK_TEXT, 'Cart') # Ya definido en HomePageElements, pero podría ser común
    HEADER_PRODUCTS_LINK = (By.PARTIAL_LINK_TEXT, "Products") # Ya definido en HomePageElements
    HEADER_SIGNUP_LOGIN_LINK = (By.XPATH, '//a[contains(text(), "Signup / Login")]') # Ya definido en HomePageElements
    CONTINUE_BUTTON_AFTER_ACTION = (By.XPATH, '//a[@data-qa="continue-button"]') # Botón genérico de continuar

