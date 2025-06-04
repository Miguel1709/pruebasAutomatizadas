import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class ClickOn:
    """
    Una interacción que permite a un Actor hacer clic en un elemento web.
    """
    def __init__(self, locator: tuple):
        """
        Inicializa la interacción ClickOn.
        :param locator: El localizador del elemento en el que se hará clic.
        """
        self.locator = locator
        self.description = f"hacer clic en el elemento con localizador {locator}"

    @classmethod
    def the(cls, locator: tuple):
        """
        Método de fábrica para crear una instancia de ClickOn.
        Uso: ClickOn.the(HomePageElements.SOME_BUTTON)
        """
        return cls(locator)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de hacer clic.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            browse_the_web_ability.find_and_click(self.locator)
        except Exception as e:
            raise InteractionError(f"Fallo al hacer clic en {self.locator}: {e}") from e

