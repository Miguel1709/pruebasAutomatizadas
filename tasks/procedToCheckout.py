import allure
from actors.actor import Actor
from interactions.clickOn import ClickOn
from ui.cartPageELements import CartPageElements

class ProceedToCheckout:
    """
    Una Tarea que permite a un Actor proceder al checkout desde el carrito.
    """
    def __init__(self):
        self.description = "proceder al checkout"

    @classmethod
    def from_cart(cls):
        """
        Método de fábrica para proceder al checkout.
        """
        return cls()

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de proceder al checkout.
        """
        actor.attempts_to(
            ClickOn.the(CartPageElements.PROCEED_TO_CHECKOUT_BUTTON)
        )