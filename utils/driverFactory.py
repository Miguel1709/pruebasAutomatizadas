from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """
    Clase de fábrica para crear y configurar instancias del WebDriver.
    """

    @staticmethod
    def get_chrome_driver():
        """
        Configura y retorna una instancia de Chrome WebDriver.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Inicia el navegador maximizado
        # Puedes añadir más opciones de Chrome aquí, por ejemplo, headless:
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--no-sandbox")

        # Instala el ChromeDriver si no está presente y crea el servicio
        service = Service(ChromeDriverManager().install())

        # Retorna la instancia del WebDriver
        return webdriver.Chrome(service=service, options=options)

