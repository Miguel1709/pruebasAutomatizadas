import allure
from actors.actor import Actor
from interactions.clickOn import ClickOn
from interactions.navigateToUrl import NavigateToUrl
from ui.homePageElements import HomePageElements

class AccessProductsSection:
    """
    Una Tarea que permite a un Actor navegar a la sección de productos.
    """
    def __init__(self, from_home: bool = True):
        self.from_home = from_home
        self.description = "acceder a la sección de productos"

    @classmethod
    def from_home_page(cls):
        """Método de fábrica para acceder desde la página de inicio."""
        return cls(from_home=True)

    @classmethod
    def again(cls):
        """Método de fábrica para regresar a la sección de productos."""
        return cls(from_home=False)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de acceder a la sección de productos.
        """
        if self.from_home:
            actor.attempts_to(
                ClickOn.the(HomePageElements.PRODUCTS_LINK)
            )
        else:
            # Asumiendo que "Regresa a la sección de productos" implica volver a hacer clic en el link de productos
            # desde cualquier página donde el header sea visible.
            actor.attempts_to(
                ClickOn.the(HomePageElements.PRODUCTS_LINK)
            )

