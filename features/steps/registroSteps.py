from behave import when, then
from actors.actor import Actor
from tasks.authenticateUser import AuthenticateUser
from questions.elementIsDisplayed import  ElementIsDisplayed
from ui.homePageElements import HomePageElements # Para verificar el login en home

@when('Abre el formulario de registro')
def step_open_registration_form(context):
    """
    Paso para que el Actor abra el formulario de registro.
    (La tarea AuthenticateUser.register_new_user ya incluye este paso)
    """
    pass # La acción ya está en la tarea AuthenticateUser

@when('Ingresa los datos requeridos y crea la cuenta')
def step_fill_register_form(context):
    """
    Paso para que el Actor ingrese los datos y cree la cuenta.
    """
    # Crear la tarea de autenticación (registro)
    authenticate_task = AuthenticateUser.register_new_user(password="Test1234")
    # Pedirle al actor que realice la tarea
    context.the_actor.attempts_to(
        authenticate_task
    )
    # Guardar la información generada en el contexto para futuras aserciones si es necesario
    context.generated_user_name, context.generated_user_email = authenticate_task.get_generated_user_info()


@then('El nombre del usuario debe mostrarse en la página principal')
def step_check_user_logged_in(context):
    """
    Paso para que el Actor verifique que el nombre del usuario está visible.
    """
    assert context.the_actor.asks_for(ElementIsDisplayed.with_locator(HomePageElements.LOGGED_IN_AS_TEXT)), \
        "El texto 'Logged in as' no es visible, el usuario no está logueado."
    # Si quieres verificar el nombre específico:
    # assert context.the_actor.asks_for(TextOfElement.located_by(HomePageElements.LOGGED_IN_AS_TEXT)) == f"Logged in as {context.generated_user_name}", \
    #     "El nombre de usuario logueado no coincide."
