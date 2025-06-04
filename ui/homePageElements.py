from selenium.webdriver.common.by import By

class HomePageElements:
    """
    Define los localizadores (Targets) para los elementos de la Página de Inicio.
    """
    SIGNUP_LOGIN_BUTTON = (By.XPATH, '//a[contains(text(), "Signup / Login")]')
    PRODUCTS_LINK = (By.PARTIAL_LINK_TEXT, "Products")
    LOGGED_IN_AS_TEXT = (By.XPATH, '//a[contains(text(), "Logged in as")]')
    CART_LINK = (By.LINK_TEXT, 'Cart')
    # Añadir localizadores para el campo de búsqueda y botón de búsqueda si están en el home
    SEARCH_PRODUCT_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")