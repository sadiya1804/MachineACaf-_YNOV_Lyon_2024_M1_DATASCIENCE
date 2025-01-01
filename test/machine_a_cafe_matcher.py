import unittest
from utilities.brewer_surveillant_les_appels import BrewerSpy
from utilities.carte_fake import CarteFake
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake
from utilities.machine_a_cafe_builder import MachineACaféBuilder
from utilities.brewer_spy import BrewerSpy
from utilities.cup_provider_spy import CupProviderSpy

class BrewerMatcher(unittest.TestCase):

    def assertCoffeeOrdered(self, brewer):
        self.assertTrue(brewer.make_a_coffee_appelé())

    def assertNoCoffeeOrdered(self, brewer):
        self.assertFalse(brewer.make_a_coffee_appelé())

    def assertAmountCharged(self, card, expected_amount):
        self.assertEqual(expected_amount, card.somme_operations_en_centimes())

    def assertCupProvided(self, cup_provider):
        self.assertTrue(cup_provider.provide_cup_called())
    
    def assertChocolateOrdered(self, brewer):
        self.assertTrue(brewer.add_chocolate_appelé())
    
    def assertLatteOrdered(self, brewer):
        self.assertTrue(brewer.add_latte_appelé())
    
    def assertCappuccinoOrdered(self, brewer):
        self.assertTrue(brewer.add_capuccino_appelé())
    
    def assertNoChocolateOrdered(self, brewer):
        self.assertFalse(brewer.add_chocolate_appelé())
    
    def assertNoLatteOrdered(self, brewer):
        self.assertFalse(brewer.add_latte_appelé())