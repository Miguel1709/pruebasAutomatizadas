import allure
from actors.actor import Actor
from interactions.hoverOver import HoverOver
from interactions.clickOn import ClickOn
from interactions.closeModal import CloseModal
from ui.productListeningElements import ProductListingElements
from ui.commonElements import CommonElements
from abilities.browseTheWeb import BrowseTheWeb
from selenium.webdriver.support import expected_conditions as EC

class AddProductToCart:
    """
    Una Tarea que permite a un Actor agregar el primer producto visible al carrito.
    """
    def __init__(self):
        self.description = "agregar el primer producto de la lista al carrito"

    @classmethod
    def first_one_from_list(cls):
        """
        Método de fábrica para agregar el primer producto al carrito.
        """
        return cls()

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de agregar el producto al carrito.
        """
        browse_ability = actor.uses_ability_to(BrowseTheWeb)


            # Opcional: Asegurarse de que esté en el viewport si es necesario
            # browse_ability.scroll_to_element(ProductListingElements.FIRST_PRODUCT_CARD)

        actor.attempts_to(
            HoverOver.the(ProductListingElements.FIRST_PRODUCT_CARD),  # Hover sobre la tarjeta del producto
            ClickOn.the(ProductListingElements.FIRST_PRODUCT_CARD_ADD_TO_CART_BUTTON),  # Clic en el botón "Add to cart"
            CloseModal.by_clicking_button(CommonElements.MODAL_CLOSE_BUTTON)  # Cerrar el modal
        )

