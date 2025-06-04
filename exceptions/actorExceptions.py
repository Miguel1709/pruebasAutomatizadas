class ActorError(Exception):
    """
    Clase base para excepciones relacionadas con el Actor en Screenplay.
    """
    pass

class NoAbilityError(ActorError):
    """
    Excepción lanzada cuando un Actor intenta usar una habilidad que no posee.
    """
    pass

class InteractionError(ActorError):
    """
    Excepción lanzada cuando una Interacción falla.
    """
    pass

class QuestionError(ActorError):
    """
    Excepción lanzada cuando una Pregunta falla.
    """
    pass