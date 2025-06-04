import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class HoverOver:
    """
    Una interacción que permite a un Actor pasar el ratón sobre un elemento.
    """
    def __init__(self, locator: tuple):
        """
        Inicializa la interacción HoverOver.
        :param locator: El localizador del elemento sobre el que se hará hover.
        """
        self.locator = locator
        self.description = f"pasar el ratón sobre el elemento con localizador {locator}"

    @classmethod
    def the(cls, locator: tuple):
        """
        Método de fábrica para crear una instancia de HoverOver.
        Uso: HoverOver.the(ProductListingElements.FIRST_PRODUCT_CARD)
        """
        return cls(locator)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de hover.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            browse_the_web_ability.hover_element(self.locator)
        except Exception as e:
            raise InteractionError(f"Fallo al hacer hover sobre {self.locator}: {e}") from e
