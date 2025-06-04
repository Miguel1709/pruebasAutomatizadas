import allure
from actors.actor import Actor
from abilities.browseTheWeb import BrowseTheWeb
from exceptions.actorExceptions import QuestionError

class CurrentUrl:
    """
    Una Pregunta que permite a un Actor obtener y verificar la URL actual del navegador.
    """
    def __init__(self, expected_value: str = None, comparison_type: str = "equal"):
        self.expected_value = expected_value
        self.comparison_type = comparison_type # "equal", "contains", "ends_with"

        if comparison_type == "equal":
            self.description = f"si la URL actual es igual a '{expected_value}'"
        elif comparison_type == "contains":
            self.description = f"si la URL actual contiene '{expected_value}'"
        elif comparison_type == "ends_with":
            self.description = f"si la URL actual termina con '{expected_value}'"
        else:
            self.description = "la URL actual" # Si no hay valor esperado o tipo de comparación

    @classmethod
    def is_equal_to(cls, expected_url: str):
        """
        Pregunta si la URL actual del navegador es exactamente igual a la URL esperada.
        Normaliza ambas URLs (elimina la barra final si existe) antes de comparar.
        """
        return cls(expected_url, "equal")

    @classmethod
    def contains_part(cls, url_part: str):
        """
        Pregunta si la URL actual del navegador contiene una parte específica.
        """
        return cls(url_part, "contains")

    @classmethod
    def ends_with_part(cls, url_suffix: str):
        """
        Pregunta si la URL actual del navegador termina con una parte específica.
        """
        return cls(url_suffix, "ends_with")

    def _normalize_url(self, url: str) -> str:
        """Elimina la barra diagonal final de una URL si existe."""
        if url.endswith('/'):
            return url[:-1]
        return url

    def answered_by(self, actor: Actor) -> bool:
        """
        El Actor responde a la pregunta de la URL actual.
        """
        try:
            browse_the_web_ability = actor.uses_ability_to(BrowseTheWeb)
            current_url = browse_the_web_ability.get_current_url()
            allure.attach(current_url, name="URL Actual (sin normalizar)", attachment_type=allure.attachment_type.TEXT)

            # Siempre imprimir los debugs si hay un valor esperado
            if self.expected_value is not None:
                # Normalizar solo para comparación 'equal' o 'contains' si es una URL completa
                normalized_expected_value = self.expected_value
                normalized_current_url = current_url

                if self.comparison_type in ["equal", "contains"]:
                    normalized_expected_value = self._normalize_url(self.expected_value)
                    normalized_current_url = self._normalize_url(current_url)

                # --- ¡ESTAS SON LAS LÍNEAS DE DEBUG QUE NECESITO VER EN TU CONSOLA! ---
                print(f"\n{'='*50}")
                print(f"DEBUG: Verificando URL:")
                print(f"DEBUG: Valor esperado: '{self.expected_value}'")
                print(f"DEBUG: URL actual (navegador): '{current_url}'")
                print(f"DEBUG: Tipo de comparación: '{self.comparison_type}'")
                if self.comparison_type in ["equal", "contains"]:
                    print(f"DEBUG: Valor esperado (normalizado): '{normalized_expected_value}'")
                    print(f"DEBUG: URL actual (normalizada): '{normalized_current_url}'")
                print(f"{'='*50}")
                # --- FIN LÍNEAS DE DEBUG ---

                result = False
                if self.comparison_type == "equal":
                    result = normalized_current_url == normalized_expected_value
                elif self.comparison_type == "contains":
                    result = normalized_expected_value in normalized_current_url
                elif self.comparison_type == "ends_with":
                    result = current_url.endswith(self.expected_value) # No normalizamos para ends_with

                allure.attach(f"Esperado: {self.expected_value} (tipo: {self.comparison_type}), Actual: {current_url}, Coincide: {result}", name="Verificación de URL", attachment_type=allure.attachment_type.TEXT)
                return result
            else:
                return current_url
        except Exception as e:
            raise QuestionError(f"Fallo al obtener la URL actual: {e}") from e

