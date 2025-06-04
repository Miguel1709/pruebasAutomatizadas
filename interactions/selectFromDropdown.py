import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import InteractionError

class SelectFromDropdown:
    """
    Una interacción que permite a un Actor seleccionar una opción de un dropdown.
    """
    def __init__(self, text: str, locator: tuple = None): # locator ahora es opcional en el init
        """
        Inicializa la interacción SelectFromDropdown.
        :param text: El texto visible de la opción a seleccionar.
        :param locator: El localizador del elemento dropdown (opcional, se puede establecer después).
        """
        self.text = text
        self.locator = locator # Se inicializa como None y se establece con .from_()
        self.description = f"seleccionar '{text}' del dropdown con localizador {locator}"

    @classmethod
    def the_option(cls, text: str):
        """
        Método de fábrica para crear una instancia de SelectFromDropdown (parte 1).
        Retorna una instancia de la clase que luego espera el localizador con .from_().
        """
        return cls(text=text)

    def from_(self, locator: tuple):
        """
        Método para especificar el localizador del dropdown.
        Este método se llama después de the_option().
        """
        self.locator = locator
        self.description = f"seleccionar '{self.text}' del dropdown con localizador {self.locator}"
        return self # Retorna la instancia para que sea el objeto que perform_as recibe

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la interacción de seleccionar.
        :param actor: La instancia del Actor que realiza la interacción.
        """
        if not self.locator:
            raise ValueError("El localizador del dropdown no ha sido especificado. Usa .from_(locator).")

        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            with allure.step(f"Seleccionando '{self.text}' del dropdown {self.locator}"): # Step interno para detalle
                browse_the_web_ability.find_and_select_by_text(self.locator, self.text)
        except Exception as e:
            raise InteractionError(f"Fallo al seleccionar '{self.text}' del dropdown {self.locator}: {e}") from e
