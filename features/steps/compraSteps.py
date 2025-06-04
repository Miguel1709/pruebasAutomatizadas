from behave import when, then
from actors.actor import Actor
from tasks.accessShoppingCart import AccessShoppingCart
from tasks.procedToCheckout import ProceedToCheckout
from tasks.placeOrder import PlaceOrder
from tasks.completePayment import CompletePayment
from tasks.dowloadInvoiceAndContinue import DownloadInvoiceAndContinue
from questions.urlContains import UrlContains
from questions.elementIsDisplayed import ElementIsDisplayed
from ui.paymentPageElements import PaymentPageElements
from questions.currentUrl import CurrentUrl # Para verificar la URL completa

@when('El usuario accede al carrito de compras')
def step_access_shopping_cart(context):
    """
    Paso para que el Actor acceda al carrito de compras.
    """
    context.the_actor.attempts_to(
        AccessShoppingCart.from_anywhere()
    )

@when('Presiona el botón "Proceed To Checkout"')
def step_proceed_to_checkout(context):
    """
    Paso para que el Actor presione el botón "Proceed To Checkout".
    """
    context.the_actor.attempts_to(
        ProceedToCheckout.from_cart()
    )

@then('Es redirigido a la página de checkout')
def step_redirected_to_checkout_page(context):
    """
    Paso para que el Actor verifique la redirección a la página de checkout.
    """
    assert context.the_actor.asks_for(UrlContains.the_text("/checkout")), \
        "No se redirigió a la página de checkout."

@when('Hace scroll hasta el botón "Place Order"')
def step_scroll_to_place_order_button(context):
    """
    Paso para que el Actor haga scroll hasta el botón "Place Order".
    (La tarea PlaceOrder ya incluye el scroll, este paso puede ser redundante)
    """
    pass # La acción de scroll ya está en la tarea PlaceOrder

@when('Presiona el botón "Place Order"')
def step_place_order_button(context):
    """
    Paso para que el Actor presione el botón "Place Order".
    """
    context.the_actor.attempts_to(
        PlaceOrder.now()
    )

@then('Es redirigido a la página de pago')
def step_redirected_to_payment_page(context):
    """
    Paso para que el Actor verifique la redirección a la página de pago.
    """
    assert context.the_actor.asks_for(UrlContains.the_text("/payment")), \
        "No se redirigió a la página de pago."

@when('Ingresa los datos de la tarjeta y confirma el pago')
def step_enter_card_details_and_confirm_payment(context):
    """
    Paso para que el Actor ingrese los datos de la tarjeta y confirme el pago.
    """
    context.the_actor.attempts_to(
        CompletePayment.with_card_details(
            name_on_card="Miguel Test",
            card_number="4111111111111111",
            cvc="123",
            expiry_month="12",
            expiry_year="2026"
        )
    )

@then('El pedido se realiza correctamente')
def step_order_placed_successfully(context):
    """
    Paso para que el Actor verifique que el pedido se realizó correctamente.
    """
    assert context.the_actor.asks_for(ElementIsDisplayed.with_locator(PaymentPageElements.ORDER_PLACED_SUCCESS_HEADER)), \
        "El mensaje de 'Pedido realizado correctamente' no es visible."

@when('Descarga la factura de la compra')
def step_download_invoice(context):
    """
    Paso para que el Actor descargue la factura.
    """
    pass # La tarea DownloadInvoiceAndContinue ya incluye la descarga

@when('Presiona el botón "Continue"')
def step_press_continue_button(context):
    """
    Paso para que el Actor presione el botón "Continue".
    """
    context.the_actor.attempts_to(
        DownloadInvoiceAndContinue.and_return_to_home()
    )


@then('Es redirigido al inicio')
def step_redirected_to_home(context):
    """
    Paso para que el Actor verifique la redirección a la página de inicio.
    """
    # Añadimos un print aquí para confirmar que este paso se está ejecutando
    print("\nCONFIRMACIÓN: Ejecutando el paso 'Es redirigido al inicio'.")

    # La URL de inicio en automationexercise.com a menudo termina en '/'
    # Usaremos la lógica de 'ends_with_part' para ser flexibles.
    expected_suffix = "/"

    assert context.the_actor.asks_for(CurrentUrl.ends_with_part(expected_suffix)), \
        "No se redirigió al inicio. Revisa los logs de debug para las URLs comparadas."

    print("✅ Flujo terminado. Presiona ENTER para cerrar el navegador...")
    input()  # Mantener esta línea para pausar la ejecución del script

