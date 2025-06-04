import allure
from exceptions.actorExceptions import   NoAbilityError

class Actor:
    """
    Representa a un Actor en el Screenplay Pattern.
    Un Actor tiene habilidades y puede realizar Tareas y Preguntar.
    """
    def __init__(self, name: str = "Web User"):
        """
        Inicializa un Actor con un nombre y un diccionario de habilidades.
        :param name: El nombre del Actor.
        """
        self.name = name
        self.abilities = {}

    def can(self, ability_instance):
        """
        Asigna una habilidad a este Actor.
        :param ability_instance: Una instancia de una clase de Habilidad (ej., BrowseTheWeb.using(driver)).
        :return: El propio Actor para encadenamiento.
        """
        self.abilities[ability_instance.__class__.__name__] = ability_instance
        return self

    def uses_ability_to(self, ability_type):
        """
        Obtiene una habilidad específica que el Actor posee.
        :param ability_type: El tipo de habilidad a obtener (ej., BrowseTheWeb).
        :return: La instancia de la habilidad.
        :raises NoAbilityError: Si el Actor no tiene la habilidad solicitada.
        """
        ability = self.abilities.get(ability_type.__name__)
        if not ability:
            raise NoAbilityError(f"{self.name} no tiene la habilidad {ability_type.__name__}")
        return ability

    def attempts_to(self, *tasks):
        """
        El Actor intenta realizar una o más Tareas.
        :param tasks: Una o más instancias de Tarea.
        """
        with allure.step(f"{self.name} intenta realizar:"):
            for task in tasks:
                task.perform_as(self)

    def asks_for(self, question):
        """
        El Actor hace una Pregunta y obtiene una respuesta.
        :param question: Una instancia de una clase de Pregunta.
        :return: La respuesta a la pregunta.
        """
        with allure.step(f"{self.name} pregunta: {question.description}"):
            return question.answered_by(self)
