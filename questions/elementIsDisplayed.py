import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import QuestionError

class ElementIsDisplayed:
    """
    Una Pregunta que verifica si un elemento web está visible en la página.
    """
    def __init__(self, locator: tuple):
        """
        Inicializa la Pregunta ElementIsDisplayed.
        :param locator: El localizador del elemento a verificar.
        """
        self.locator = locator
        self.description = f"si el elemento con localizador {locator} está visible"

    @classmethod
    def with_locator(cls, locator: tuple):
        """
        Método de fábrica para crear una instancia de ElementIsDisplayed.
        Uso: ElementIsDisplayed.with_locator(HomePageElements.SOME_ELEMENT)
        """
        return cls(locator)

    def answered_by(self, actor: Actor) -> bool:
        """
        El Actor responde a la pregunta sobre la visibilidad del elemento.
        :param actor: La instancia del Actor que responde.
        :return: True si el elemento está visible, False en caso contrario.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            is_visible = browse_the_web_ability.is_element_displayed(self.locator)
            allure.attach(str(is_visible), name=f"Visibilidad de {self.locator}", attachment_type=allure.attachment_type.TEXT)
            return is_visible
        except Exception as e:
            raise QuestionError(f"Fallo al verificar la visibilidad de {self.locator}: {e}") from e
