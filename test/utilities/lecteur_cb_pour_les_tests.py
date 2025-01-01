import unittest

from hardware.creditcard import CreditCardInterface, CardHandleInterface


class LecteurCbFake(CreditCardInterface):
    def __init__(self):
        self.__callback = None

    def register_card_detected_callback(self, card_detected_callback: CardHandleInterface = None) -> None:
        self.__callback = card_detected_callback

    def simuler_carte_détectée(self, carte: CardHandleInterface) -> None:
        self.__callback(carte)