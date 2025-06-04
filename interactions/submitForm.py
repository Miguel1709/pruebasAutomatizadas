import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class SubmitForm:
    """
    Una interacción que permite a un Actor enviar un formulario haciendo clic en un botón de envío.
    """
    def __init__(self, submit_button_locator: tuple):
        """
        Inicializa la interacción SubmitForm.
        :param submit_button_locator: El localizador del botón de envío del formulario.
        """
        self.submit_button_locator = submit_button_locator
        self.description = f"enviar el formulario haciendo clic en {submit_button_locator}"

    @classmethod
    def by_clicking(cls, submit_button_locator: tuple):
        """
        Método de fábrica para enviar un formulario.
        Uso: SubmitForm.by_clicking(LoginPageElements.LOGIN_BUTTON)
        """
        return cls(submit_button_locator)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de enviar el formulario.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            browse_the_web_ability.find_and_click(self.submit_button_locator)
        except Exception as e:
            raise InteractionError(f"Fallo al enviar el formulario haciendo clic en {self.submit_button_locator}: {e}") from e
