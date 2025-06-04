import allure
from actors.actor import Actor
from interactions.enterValue import EnterValue
from interactions.submitForm import SubmitForm
from ui.paymentPageElements import PaymentPageElements

class CompletePayment:
    """
    Una Tarea que permite a un Actor ingresar los datos de la tarjeta y confirmar el pago.
    """
    def __init__(self, name_on_card: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str):
        self.name_on_card = name_on_card
        self.card_number = card_number
        self.cvc = cvc
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.description = "ingresar los datos de la tarjeta y confirmar el pago"

    @classmethod
    def with_card_details(cls, name_on_card: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str):
        """
        Método de fábrica para completar el pago con detalles específicos.
        """
        return cls(name_on_card, card_number, cvc, expiry_month, expiry_year)

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de completar el pago.
        """
        actor.attempts_to(
            EnterValue.into_the_field(PaymentPageElements.NAME_ON_CARD_INPUT, self.name_on_card),
            EnterValue.into_the_field(PaymentPageElements.CARD_NUMBER_INPUT, self.card_number),
            EnterValue.into_the_field(PaymentPageElements.CVC_INPUT, self.cvc),
            EnterValue.into_the_field(PaymentPageElements.EXPIRY_MONTH_INPUT, self.expiry_month),
            EnterValue.into_the_field(PaymentPageElements.EXPIRY_YEAR_INPUT, self.expiry_year),
            SubmitForm.by_clicking(PaymentPageElements.SUBMIT_PAYMENT_BUTTON)
        )
