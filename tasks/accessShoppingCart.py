import allure
from actors.actor import Actor
from interactions.clickOn import ClickOn
from ui.homePageElements import HomePageElements # El link del carrito está en el header/home

class AccessShoppingCart:
    """
    Una Tarea que permite a un Actor acceder al carrito de compras.
    """
    def __init__(self):
        self.description = "acceder al carrito de compras"

    @classmethod
    def from_anywhere(cls):
        """
        Método de fábrica para acceder al carrito desde cualquier página
        donde el link del carrito sea visible (asumiendo que está en el header).
        """
        return cls()

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de acceder al carrito.
        """
        actor.attempts_to(
            ClickOn.the(HomePageElements.CART_LINK)
        )
