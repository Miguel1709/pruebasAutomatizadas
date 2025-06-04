import allure
from actors.actor import Actor
from interactions.clickOn import ClickOn
from ui.paymentPageElements import PaymentPageElements
from ui.commonElements import CommonElements # Para el botón de continuar genérico

class DownloadInvoiceAndContinue:
    """
    Una Tarea que permite a un Actor descargar la factura y luego presionar "Continue".
    """
    def __init__(self):
        self.description = "descargar la factura de la compra y continuar"

    @classmethod
    def and_return_to_home(cls):
        """
        Método de fábrica para descargar la factura y continuar.
        """
        return cls()

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de descargar la factura y continuar.
        """
        actor.attempts_to(
            ClickOn.the(PaymentPageElements.DOWNLOAD_INVOICE_LINK),
            ClickOn.the(CommonElements.CONTINUE_BUTTON_AFTER_ACTION) # Botón "Continue"
        )
