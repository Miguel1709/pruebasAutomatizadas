import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import QuestionError

class TextOfElement:
    """
    Una Pregunta que retorna el texto visible de un elemento web.
    """
    def __init__(self, locator: tuple):
        """
        Inicializa la Pregunta TextOfElement.
        :param locator: El localizador del elemento cuyo texto se desea obtener.
        """
        self.locator = locator
        self.description = f"el texto del elemento con localizador {locator}"

    @classmethod
    def located_by(cls, locator: tuple):
        """
        Método de fábrica para crear una instancia de TextOfElement.
        Uso: TextOfElement.located_by(HomePageElements.WELCOME_MESSAGE)
        """
        return cls(locator)

    def answered_by(self, actor: Actor) -> str:
        """
        El Actor responde a la pregunta sobre el texto del elemento.
        :param actor: La instancia del Actor que responde.
        :return: El texto visible del elemento.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            element_text = browse_the_web_ability.get_element_text(self.locator)
            allure.attach(element_text, name=f"Texto de {self.locator}", attachment_type=allure.attachment_type.TEXT)
            return element_text
        except Exception as e:
            raise QuestionError(f"Fallo al obtener el texto de {self.locator}: {e}") from e
