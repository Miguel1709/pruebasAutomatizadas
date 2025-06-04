import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class ScrollTo:
    """
    Una interacción que permite a un Actor hacer scroll hasta un elemento o al final de la página.
    """
    def __init__(self, locator: tuple = None, end_of_page: bool = False):
        """
        Inicializa la interacción ScrollTo.
        :param locator: El localizador del elemento al que se hará scroll (opcional).
        :param end_of_page: Si es True, hace scroll al final de la página.
        """
        self.locator = locator
        self.end_of_page = end_of_page
        if self.end_of_page:
            self.description = "hacer scroll al final de la página"
        elif self.locator:
            self.description = f"hacer scroll hasta el elemento con localizador {locator}"
        else:
            raise ValueError("Debe especificar un localizador o establecer end_of_page en True.")

    @classmethod
    def the_element(cls, locator: tuple):
        """
        Método de fábrica para hacer scroll hasta un elemento.
        Uso: ScrollTo.the_element(SomePageElements.SOME_ELEMENT)
        """
        return cls(locator=locator)

    @classmethod
    def the_end_of_page(cls):
        """
        Método de fábrica para hacer scroll al final de la página.
        Uso: ScrollTo.the_end_of_page()
        """
        return cls(end_of_page=True)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de scroll.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            if self.end_of_page:
                browse_the_web_ability.scroll_to_end_of_page()
            elif self.locator:
                browse_the_web_ability.scroll_to_element(self.locator)
        except Exception as e:
            raise InteractionError(f"Fallo al hacer scroll: {e}") from e
