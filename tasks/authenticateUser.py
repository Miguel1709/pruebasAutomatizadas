import allure
import random
from actors.actor import Actor
from interactions.navigateToUrl import NavigateToUrl
from interactions.clickOn import ClickOn
from interactions.enterValue import EnterValue
from interactions.selectFromDropdown import SelectFromDropdown
from interactions.submitForm import SubmitForm
from ui.homePageElements import HomePageElements
from ui.registrationPageElements import RegistrationPageElements
from ui.commonElements import CommonElements

class AuthenticateUser:
    """
    Una Tarea que permite a un Actor registrar un nuevo usuario o iniciar sesión.
    """
    def __init__(self, password: str = None, register: bool = True):
        self.password = password
        self.register = register
        self.generated_email = None
        self.generated_name = None
        self.description = "autenticarse en la aplicación"

    @classmethod
    def register_new_user(cls, password: str = "Test1234"):
        """
        Método de fábrica para registrar un nuevo usuario.
        """
        return cls(password=password, register=True)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de autenticación.
        """
        if self.register:
            self._perform_registration(actor)
        else:
            self._perform_login(actor) # No implementado en tu flujo original

    @allure.step("Realizar el proceso de registro de nuevo usuario")
    def _perform_registration(self, actor: Actor):
        """Pasos internos para el registro de un nuevo usuario."""
        self.generated_name = f"usuario{random.randint(1000, 9999)}"
        self.generated_email = f"{self.generated_name}@mail.com"

        actor.attempts_to(
            NavigateToUrl.url("http://www.automationexercise.com"),
            ClickOn.the(HomePageElements.SIGNUP_LOGIN_BUTTON),
            EnterValue.into_the_field(RegistrationPageElements.SIGNUP_NAME_INPUT, self.generated_name),
            EnterValue.into_the_field(RegistrationPageElements.SIGNUP_EMAIL_INPUT, self.generated_email),
            ClickOn.the(RegistrationPageElements.SIGNUP_BUTTON)
        )

        actor.attempts_to(
            ClickOn.the(RegistrationPageElements.GENDER_RADIO_MALE),
            EnterValue.into_the_field(RegistrationPageElements.PASSWORD_INPUT, self.password),
            SelectFromDropdown.the_option(text="10").from_(RegistrationPageElements.DAYS_DROPDOWN),
            SelectFromDropdown.the_option(text="May").from_(RegistrationPageElements.MONTHS_DROPDOWN),
            SelectFromDropdown.the_option(text="1995").from_(RegistrationPageElements.YEARS_DROPDOWN),
            ClickOn.the(RegistrationPageElements.NEWSLETTER_CHECKBOX),
            ClickOn.the(RegistrationPageElements.OPTIN_CHECKBOX)
        )

        actor.attempts_to(
            EnterValue.into_the_field(RegistrationPageElements.FIRST_NAME_INPUT, "Miguel"),
            EnterValue.into_the_field(RegistrationPageElements.LAST_NAME_INPUT, "Test"),
            EnterValue.into_the_field(RegistrationPageElements.COMPANY_INPUT, "Automation"),
            EnterValue.into_the_field(RegistrationPageElements.ADDRESS1_INPUT, "123 Calle Falsa"),
            EnterValue.into_the_field(RegistrationPageElements.ADDRESS2_INPUT, "Apto 456"),
            SelectFromDropdown.the_option(text="United States").from_(RegistrationPageElements.COUNTRY_DROPDOWN),
            EnterValue.into_the_field(RegistrationPageElements.STATE_INPUT, "Estado"),
            EnterValue.into_the_field(RegistrationPageElements.CITY_INPUT, "Ciudad"),
            EnterValue.into_the_field(RegistrationPageElements.ZIPCODE_INPUT, "12345"),
            EnterValue.into_the_field(RegistrationPageElements.MOBILE_NUMBER_INPUT, "3001234567")
        )

        actor.attempts_to(
            ClickOn.the(RegistrationPageElements.CREATE_ACCOUNT_BUTTON),
            ClickOn.the(CommonElements.CONTINUE_BUTTON_AFTER_ACTION) # Botón "Continue" después de crear cuenta
        )

    def _perform_login(self, actor: Actor):
        """Pasos internos para el inicio de sesión (no en el flujo actual)."""
        # Implementar lógica de login aquí
        pass

    def get_generated_user_info(self) -> tuple:
        """Retorna el nombre y email generados durante el registro."""
        return self.generated_name, self.generated_email

