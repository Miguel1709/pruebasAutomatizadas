from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.driverFactory import DriverFactory # Importa tu fábrica de drivers
from actors.actor import Actor
from abilities.browseTheWeb import  BrowseTheWeb

def before_scenario(context, scenario):
    """
    Hook de Behave que se ejecuta antes de cada escenario.
    Inicializa el WebDriver y el Actor con sus habilidades.
    """
    context.driver = DriverFactory.get_chrome_driver()
    context.the_actor = Actor("Marta").can(BrowseTheWeb.using(context.driver))
    context.base_url = "http://www.automationexercise.com" # URL base del sitio

def after_scenario(context, scenario):
    """
    Hook de Behave que se ejecuta después de cada escenario.
    Cierra el navegador.
    """
    print(f"\nEscenario finalizado: {scenario.name}")
    if hasattr(context, "driver"):
        context.driver.quit()
