import allure
from actors.actor import Actor
from interactions.scrollTo import ScrollTo
from interactions.clickOn import ClickOn
from ui.checkoutPageELements import CheckoutPageElements

class PlaceOrder:
    """
    Una Tarea que permite a un Actor hacer scroll y presionar el botón "Place Order".
    """
    def __init__(self):
        self.description = "hacer scroll y presionar el botón 'Place Order'"

    @classmethod
    def now(cls):
        """
        Método de fábrica para colocar la orden.
        """
        return cls()

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de colocar la orden.
        """
        actor.attempts_to(
            ScrollTo.the_end_of_page(), # Asumimos que el botón está al final
            ClickOn.the(CheckoutPageElements.PLACE_ORDER_BUTTON)
        )