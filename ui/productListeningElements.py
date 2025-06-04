from selenium.webdriver.common.by import By

class ProductListingElements:
    """
    Define los localizadores (Targets) para los elementos en las páginas
    de listado de productos (ej. después de una búsqueda o filtro).
    """
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, '//*[contains(text(), "Searched Products")]')
    WOMEN_CATEGORY_LINK = (By.XPATH, '//a[normalize-space()="Women"]')
    TOPS_SUBCATEGORY_LINK = (By.XPATH, '//a[contains(text(), "Tops")]')
    WOMEN_TOPS_PRODUCTS_TITLE = (By.XPATH, '//h2[contains(text(), "Women - Tops Products")]')
    # Localizador genérico para el primer botón "Add to cart" en una tarjeta de producto
    # Asumiendo que el botón es visible al hacer hover sobre la tarjeta del producto.
    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, 'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products')

    # El localizador de la tarjeta del producto para el hover
    FIRST_PRODUCT_CARD_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.product-overlay > div > a')

