import allure
from actors.actor import Actor
from interactions.enterValue import EnterValue
from interactions.clickOn import ClickOn
from ui.homePageElements import HomePageElements # Asumiendo que la búsqueda está en el home

class SearchForProduct:
    """
    Una Tarea que permite a un Actor buscar un producto.
    """
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.description = f"buscar el producto '{product_name}'"

    @classmethod
    def named(cls, product_name: str):
        """
        Método de fábrica para buscar un producto por su nombre.
        """
        return cls(product_name)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de buscar un producto.
        """
        actor.attempts_to(
            EnterValue.into_the_field(HomePageElements.SEARCH_PRODUCT_INPUT, self.product_name),
            ClickOn.the(HomePageElements.SEARCH_BUTTON)
        )
