import unittest
from utilities.brewer_surveillant_les_appels import BrewerSpy
from utilities.carte_fake import CarteFake
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake
from utilities.machine_a_cafe_builder import MachineACaféBuilder
from utilities.brewer_spy import BrewerSpy
from utilities.cup_provider_spy import CupProviderSpy

class BrewerMatcher(unittest.TestCase):
    def __init__(self):
        self.__brewer = BrewerSpy()
        self.__lecteur_cb = LecteurCbFake()
        self.__machine_a_cafe = (MachineACaféBuilder()
                           .ayant_pour_brewer(self.__brewer)
                           .ayant_pour_lecteur_cb(self.__lecteur_cb)
                           .build())
        self.__carte = CarteFake.default()
