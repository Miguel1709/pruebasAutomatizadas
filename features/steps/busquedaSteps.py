from behave import when, then
from actors.actor import Actor
from tasks.searchForProduct import SearchForProduct
from tasks.addProductToCart import AddProductToCart
from questions.elementIsDisplayed import ElementIsDisplayed
from ui.productListeningElements import ProductListingElements

@when('Ingresa "{product_name}" en el campo de búsqueda')
def step_enter_search_term(context, product_name):
    """
    Paso para que el Actor busque un producto específico.
    """
    context.the_actor.attempts_to(
        SearchForProduct.named(product_name)
    )

@when('Presiona el botón de búsqueda')
def step_click_search_button(context):
    """
    Este paso es redundante si la tarea SearchForProduct ya incluye el clic.
    Se mantiene para mapear el Gherkin, pero la acción ya está en la tarea.
    """
    pass # La acción ya está en la tarea SearchForProduct

@then('Se muestran resultados relacionados con "{product_name}"')
def step_check_search_results(context, product_name):
    """
    Paso para que el Actor verifique si se muestran los resultados de búsqueda.
    """
    assert context.the_actor.asks_for(ElementIsDisplayed.with_locator(ProductListingElements.SEARCHED_PRODUCTS_TITLE)), \
        f"El título 'Searched Products' no está visible para '{product_name}'"

@then('Agrega el primer producto de búsqueda al carrito')
def step_add_first_search_product(context):
    """
    Paso para que el Actor agregue el primer producto de búsqueda al carrito.
    """
    context.the_actor.attempts_to(
        AddProductToCart.first_one_from_list()
    )
