import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import QuestionError

class UrlContains:
    """
    Una Pregunta que verifica si la URL actual del navegador contiene una subcadena específica.
    """
    def __init__(self, partial_url: str):
        """
        Inicializa la Pregunta UrlContains.
        :param partial_url: La subcadena que se espera que contenga la URL.
        """
        self.partial_url = partial_url
        self.description = f"si la URL actual contiene '{partial_url}'"

    @classmethod
    def the_text(cls, partial_url: str):
        """
        Método de fábrica para crear una instancia de UrlContains.
        Uso: UrlContains.the_text("/checkout")
        """
        return cls(partial_url)

    def answered_by(self, actor: Actor) -> bool:
        """
        El Actor responde a la pregunta sobre si la URL actual contiene la subcadena.
        :param actor: La instancia del Actor que responde.
        :return: True si la URL contiene la subcadena, False en caso contrario.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            current_url = browse_the_web_ability.get_current_url()
            result = self.partial_url in current_url
            allure.attach(f"URL actual: {current_url}, Contiene '{self.partial_url}': {result}", name="Verificación de URL", attachment_type=allure.attachment_type.TEXT)
            return result
        except Exception as e:
            raise QuestionError(f"Fallo al verificar si la URL contiene '{self.partial_url}': {e}") from e
