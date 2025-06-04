import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class NavigateToUrl:
    """
    Una interacción que permite a un Actor navegar a una URL específica.
    """
    def __init__(self, url: str):
        """
        Inicializa la interacción NavigateToUrl.
        :param url: La URL a la que navegar.
        """
        self.url = url
        self.description = f"navegar a la URL: {url}"

    @classmethod
    def url(cls, url: str):
        """
        Método de fábrica para crear una instancia de NavigateToUrl.
        Uso: NavigateToUrl.url("http://www.automationexercise.com")
        """
        return cls(url)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de navegar.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            browse_the_web_ability.go_to_url(self.url)
        except Exception as e:
            raise InteractionError(f"Fallo al navegar a {self.url}: {e}") from e
