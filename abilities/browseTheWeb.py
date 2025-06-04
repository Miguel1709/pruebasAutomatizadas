
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import allure
import time
from selenium.webdriver.common.by import By  # Asegúrate de importar By aquí


class BrowseTheWeb:
    """
    Habilidad que permite a un Actor interactuar con una aplicación web
    a través de un Selenium WebDriver.
    """
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        Inicializa la habilidad con una instancia del WebDriver y un tiempo de espera.
        :param driver: Instancia del Selenium WebDriver.
        :param timeout: Tiempo máximo de espera para los elementos (en segundos).
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @classmethod
    def using(cls, driver: WebDriver):
        """
        Método de fábrica para crear una instancia de BrowseTheWeb.
        Uso: Actor.can(BrowseTheWeb.using(context.driver))
        """
        return cls(driver)

    @property
    def driver_browser(self) -> WebDriver:
        """
        Permite acceder directamente a la instancia del WebDriver si es necesario
        (usar con cautela, las interacciones deberían ser suficientes).
        """
        return self.driver

    # --- Métodos de interacción de bajo nivel (usados por Interactions) ---

    @allure.step("Navegar a la URL: {url}")
    def go_to_url(self, url: str):
        """Navega el navegador a la URL especificada."""
        self.driver.get(url)
        allure.attach(self.driver.current_url, name="URL Navegada", attachment_type=allure.attachment_type.TEXT)

    def _find_element(self, locator: tuple):
        """
        Espera hasta que un elemento esté presente en el DOM y lo retorna.
        Levanta AssertionError si el elemento no se encuentra en el tiempo esperado.
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Fallo al encontrar {locator}", attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"❌ Elemento no encontrado con localizador: {locator} después de {self.wait._timeout} segundos.")

    @allure.step("Hacer clic en el elemento con localizador: {locator}")
    def find_and_click(self, locator: tuple):
        """Espera hasta que un elemento sea clickeable y hace clic en él."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Click en {locator}", attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Fallo al hacer click en {locator}", attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"❌ Elemento no clickeable con localizador: {locator} después de {self.wait._timeout} segundos.")

    @allure.step("Escribir '{text}' en el campo con localizador: {locator}")
    def find_and_type(self, locator: tuple, text: str):
        """Espera, limpia y escribe texto en un elemento."""
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Escribir '{text}' en {locator}", attachment_type=allure.attachment_type.PNG)

    @allure.step("Seleccionar '{text}' del dropdown con localizador: {locator}")
    def find_and_select_by_text(self, locator: tuple, text: str):
        """Selecciona una opción de un dropdown por texto visible."""
        element = self._find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Seleccionar '{text}' en {locator}", attachment_type=allure.attachment_type.PNG)

    @allure.step("Hacer scroll hasta el elemento con localizador: {locator}")
    def scroll_to_element(self, locator: tuple):
        """Hace scroll hasta que un elemento sea visible."""
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5) # Pequeña pausa para asegurar el scroll
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Scroll a {locator}", attachment_type=allure.attachment_type.PNG)

    @allure.step("Hacer scroll al final de la página")
    def scroll_to_end_of_page(self):
        """Hace scroll al final de la página."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1) # Pequeña pausa para asegurar el scroll
        allure.attach(self.driver.get_screenshot_as_png(), name="Scroll al final de la página", attachment_type=allure.attachment_type.PNG)

    @allure.step("Hacer hover sobre el elemento con localizador: {locator}")
    def hover_element(self, locator: tuple):
        """Realiza un hover sobre un elemento."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Hover sobre {locator}", attachment_type=allure.attachment_type.PNG)

    @allure.step("Hacer clic en el elemento con localizador: {locator} (con reintento por StaleElementReferenceException)")
    def click_with_stale_retry(self, locator: tuple, attempts: int = 3):
        """
        Intenta hacer clic en un elemento con reintentos para manejar
        StaleElementReferenceException.
        """
        for _ in range(attempts):
            try:
                self.find_and_click(locator)
                return
            except StaleElementReferenceException:
                time.sleep(0.5)  # Espera breve antes de reintentar
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Fallo StaleElement {locator}", attachment_type=allure.attachment_type.PNG)
        raise AssertionError(f"❌ No se pudo hacer clic en el elemento {locator} después de {attempts} intentos debido a StaleElementReferenceException.")

    # --- Métodos para Preguntas (usados por Questions) ---

    def get_element_text(self, locator: tuple) -> str:
        """Obtiene el texto visible de un elemento."""
        return self._find_element(locator).text

    def is_element_displayed(self, locator: tuple) -> bool:
        """Verifica si un elemento es visible."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        """Obtiene la URL actual del navegador."""
        return self.driver.current_url

    def wait_for_url_contains(self, partial_url: str):
        """Espera hasta que la URL actual contenga un texto."""
        self.wait.until(EC.url_contains(partial_url))

    def wait_for_url_to_be(self, full_url: str):
        """Espera hasta que la URL actual sea exactamente una URL."""
        self.wait.until(EC.url_to_be(full_url))

    def find_links_containing_text_and_click(self, link_text_part: str, url_part: str):
        """
        Busca enlaces que contengan un texto y una parte de URL, y hace clic en el primero.
        Utilizado para la búsqueda en DuckDuckGo.
        """

        @allure.step(f"Buscando enlace con texto '{link_text_part}' y URL '{url_part}'")
        def _find_and_click_link(driver):
            links = driver.find_elements(By.TAG_NAME, "a")
            all_links_info = []  # Lista para almacenar información de todos los enlaces
            found_match = False

            for i, link in enumerate(links):
                try:
                    href = link.get_attribute("href")
                    text = link.text
                    link_info = f"Link {i}: Text='{text}', Href='{href}'"
                    all_links_info.append(link_info)

                    # Imprime en consola para depuración inmediata
                    print(f"DEBUG LINK: {link_info}")

                    if href and url_part in href and link_text_part in text:
                        print(f"DEBUG: ¡Enlace coincidente encontrado! Text='{text}', Href='{href}'")
                        allure.attach(driver.get_screenshot_as_png(), name=f"Link encontrado: {text}",
                                      attachment_type=allure.attachment_type.PNG)
                        link.click()
                        found_match = True
                        return True  # Retorna True si encuentra y hace clic
                except StaleElementReferenceException:
                    all_links_info.append(f"Link {i}: StaleElementReferenceException (reintentando)")
                    continue  # Continúa al siguiente enlace si el actual se vuelve stale
                except Exception as e:
                    all_links_info.append(f"Link {i}: Error al acceder a atributos: {e}")
                    continue

            # Si se llega aquí, no se encontró el enlace en esta iteración
            if not found_match:
                allure.attach("\n".join(all_links_info), name="Todos los enlaces encontrados en la página",
                              attachment_type=allure.attachment_type.TEXT)
                print("DEBUG: No se encontró un enlace coincidente en esta iteración.")
            return False  # Retorna False si no se encontró un enlace coincidente

        try:
            # Esperar hasta que la función interna retorne True (es decir, se encontró y se hizo clic)
            success = self.wait.until(_find_and_click_link)
            if not success:
                raise AssertionError(
                    f"No se encontró el enlace con texto '{link_text_part}' y URL '{url_part}' después de {self.wait._timeout} segundos.")
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Fallo de Timeout al buscar enlace",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Timeout al buscar el enlace con texto '{link_text_part}' y URL '{url_part}' después de {self.wait._timeout} segundos.")

