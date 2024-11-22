import abc

class CardHandleInterface(abc.ABC):
    # Tente de prélever le montant passé en paramètre sur la carte
    # @param amountInCents le montant en centimes à prélever
    # @return True si la somme a été prélevée
    # @return False si la somme ne peut pas être prélevée
    @abc.abstractmethod
    def try_charge_amount(self, amount_in_cents: int) -> bool:
        pass

    # Rembourse une somme sur la carte
    # @param amountInCents le montant en centimes à rembourser
    @abc.abstractmethod
    def refund(self, amount_in_cents: int) -> None:
        pass

class CreditCardInterface(abc.ABC):
    # Enregistre un callback appelé lors de l'appui sur un bouton de la façade avant
    # @param callback prend un unique paramètre qui contiendra l'ID du bouton pressé
    @abc.abstractmethod
    def register_card_detected_callback(self, card_detected_callback: CardHandleInterface = None) -> None:
        pass