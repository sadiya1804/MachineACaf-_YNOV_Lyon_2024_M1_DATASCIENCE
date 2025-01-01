from hardware.brewer import BrewerInterface
from extended_brewer_interface import ExtendedBrewerInterface
from hardware.creditcard import CreditCardInterface, CardHandleInterface
from hardware.cupprovider import CupProviderInterface

class MachineACafé:
    def __init__(self, brewer: ExtendedBrewerInterface, lecteur_cb: CreditCardInterface, cup_provider: CupProviderInterface = None,):
        lecteur_cb.register_card_detected_callback(self._credit_card_callback)
        self._brewer = brewer
        self._cup_provider = cup_provider

    def _credit_card_callback(self, card_handle: CardHandleInterface) -> None:
        if self._cup_provider and not self._cup_provider.is_cup_present():
            self._cup_provider.provide_cup()

        debit_success = card_handle.try_charge_amount(50)
        if not debit_success:
            return
        
        brewing_success = self._brewer.make_a_coffee()
        if not brewing_success:
            card_handle.refund(50)
    
    def _chocolate_callback(self, card_handle: CardHandleInterface) -> None:
        if self._cup_provider and not self._cup_provider.is_cup_present():
            self._cup_provider.provide_cup()

        debit_success = card_handle.try_charge_amount(60) # faudrait demander le prix d'un supp de chocolat et des autres
        if not debit_success:
            return
        
        brewing_success = self._brewer.pour_chocolate()
        if not brewing_success:
            card_handle.refund(60)
    
    def _latte_callback(self, card_handle: CardHandleInterface) -> None:
        if self._cup_provider and not self._cup_provider.is_cup_present():
            self._cup_provider.provide_cup()

        debit_success = card_handle.try_charge_amount(70)
        if not debit_success:
            return
        
        brewing_success = self._brewer.pour_latte()
        if not brewing_success:
            card_handle.refund(70)