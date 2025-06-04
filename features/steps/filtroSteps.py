from behave import when, then
from actors.actor import Actor
from tasks.filterProductsByCategory import FilterProductsByCategory
from tasks.addProductToCart import AddProductToCart
from questions.elementIsDisplayed import ElementIsDisplayed
from ui.productListeningElements import ProductListingElements

@when('Selecciona la categoría "Women"')
def step_select_women_category(context):
    """
    Paso para que el Actor seleccione la categoría "Women".
    (La tarea FilterProductsByCategory ya incluye la selección de categoría)
    """
    pass # La acción ya está en la tarea FilterProductsByCategory

@when('Selecciona la subcategoría "Tops"')
def step_select_tops_subcategory(context):
    """
    Paso para que el Actor seleccione la subcategoría "Tops".
    (La tarea FilterProductsByCategory ya incluye la selección de subcategoría)
    """
    context.the_actor.attempts_to(
        FilterProductsByCategory.by_women_and_tops()
    )

@then('Se muestran productos de la categoría Tops')
def step_check_tops_products_displayed(context):
    """
    Paso para que el Actor verifique que se muestran productos de la categoría Tops.
    """
    assert context.the_actor.asks_for(ElementIsDisplayed.with_locator(ProductListingElements.WOMEN_TOPS_PRODUCTS_TITLE)), \
        "El título 'Women - Tops Products' no es visible."

@then('Agrega el primer producto al carrito')
def step_add_first_filtered_product(context):
    """
    Paso para que el Actor agregue el primer producto filtrado al carrito.
    """
    context.the_actor.attempts_to(
        AddProductToCart.first_one_from_list()
    )
