from behave import given, when
from actors.actor import Actor
from interactions.navigateToUrl import NavigateToUrl
from interactions.enterValue import EnterValue
from interactions.clickOn import ClickOn
from abilities.browseTheWeb import BrowseTheWeb # Para la habilidad de búsqueda de links
from tasks.accessProductsSection import AccessProductsSection
from selenium.webdriver.common.by import By # Para el localizador de DuckDuckGo

@given('El usuario navega al sitio principal')
def step_navigate_to_main_site(context):
    """
    Paso para que el Actor navegue al sitio principal a través de DuckDuckGo.
    """
    # Navegar a DuckDuckGo
    context.the_actor.attempts_to(
        NavigateToUrl.url("https://duckduckgo.com/")
    )
    # Realizar búsqueda en DuckDuckGo
    context.the_actor.attempts_to(
        EnterValue.into_the_field((By.NAME, "q"), "Automation Exercise"),
        ClickOn.the((By.XPATH, "//*[@id='searchbox_homepage']/div/div/div/button[2]")) # O (By.CSS_SELECTOR, ".search-button")
    )
    # Encontrar y hacer clic en el enlace de Automation Exercise en los resultados
    # Esta es una interacción más compleja que se puede poner directamente en la habilidad
    browse_ability = context.the_actor.uses_ability_to(BrowseTheWeb)
    browse_ability.find_links_containing_text_and_click("Automation Exercise", "automationexercise.com")


@when('Accede a la sección de productos')
def step_access_products_section(context):
    """
    Paso para que el Actor acceda a la sección de productos.
    """
    context.the_actor.attempts_to(
        AccessProductsSection.from_home_page()
    )

@when('Regresa a la sección de productos')
def step_return_to_products_section(context):
    """
    Paso para que el Actor regrese a la sección de productos.
    """
    context.the_actor.attempts_to(
        AccessProductsSection.again()
    )