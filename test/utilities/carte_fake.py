
from hardware.creditcard import CardHandleInterface, CreditCardInterface

class CarteFake(CardHandleInterface):
    def try_charge_amount(self, amount_in_cents: int) -> bool:
        if self.__approvisionnee:
            self.__somme_operations -= amount_in_cents
            return True
        return False

    def refund(self, amount_in_cents: int) -> None:
        self.__somme_operations += amount_in_cents

    def __init__(self, approvisionnee):
        self.__approvisionnee = approvisionnee
        self.__somme_operations = 0

    def somme_operations_en_centimes(self):
        return self.__somme_operations

    @classmethod
    def default(cls) -> 'CarteFake':
        return cls(approvisionnee = True)

class Creditfake(CreditCardInterface):
    def register_card_detected_callback(self, card_detected_callback: CardHandleInterface = None) -> None:
        raise NotImplementedError()
    