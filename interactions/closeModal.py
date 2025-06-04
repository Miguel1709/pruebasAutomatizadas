import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError
from ui.commonElements import CommonElements # Importa el localizador del modal

class CloseModal:
    """
    Una interacción que permite a un Actor cerrar un modal genérico.
    """
    def __init__(self, locator: tuple = CommonElements.MODAL_CLOSE_BUTTON):
        """
        Inicializa la interacción CloseModal.
        :param locator: El localizador del botón para cerrar el modal.
        """
        self.locator = locator
        self.description = "cerrar el modal actual"

    @classmethod
    def by_clicking_button(cls, locator: tuple = CommonElements.MODAL_CLOSE_BUTTON):
        """
        Método de fábrica para cerrar el modal.
        Uso: CloseModal.by_clicking_button()
        """
        return cls(locator)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de cerrar el modal.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            browse_the_web_ability.find_and_click(self.locator)
        except Exception as e:
            raise InteractionError(f"Fallo al cerrar el modal con localizador {self.locator}: {e}") from e
