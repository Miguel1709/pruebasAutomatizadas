import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class EnterValue:
    """
    Una interacción que permite a un Actor escribir texto en un campo de entrada.
    """
    def __init__(self, locator: tuple, text: str):
        """
        Inicializa la interacción EnterValue.
        :param locator: El localizador del campo de entrada.
        :param text: El texto a escribir.
        """
        self.locator = locator
        self.text = text
        self.description = f"escribir '{text}' en el campo con localizador {locator}"

    @classmethod
    def into_the_field(cls, locator: tuple, text: str):
        """
        Método de fábrica para crear una instancia de EnterValue.
        Uso: EnterValue.into_the_field(LoginPageElements.USERNAME_INPUT, "mi_usuario")
        """
        return cls(locator, text)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de escribir.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            browse_the_web_ability.find_and_type(self.locator, self.text)
        except Exception as e:
            raise InteractionError(f"Fallo al escribir '{self.text}' en {self.locator}: {e}") from e

