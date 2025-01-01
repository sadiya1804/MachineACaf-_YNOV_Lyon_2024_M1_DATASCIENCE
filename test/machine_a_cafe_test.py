import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utilities.carte_fake import CarteFake
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake
from utilities.machine_a_cafe_builder import MachineACaféBuilder
from utilities.brewer_spy import BrewerSpy
from utilities.cup_provider_spy import CupProviderSpy
from machine_a_cafe_matcher import BrewerMatcher


class MyTestCase(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)
        
        matcher = BrewerMatcher()
        # ALORS un café est commandé au hardware
        matcher.assertCoffeeOrdered(brewer)

        # ET le prix d'un café est débité
        matcher.assertAmountCharged(carte, -50)

    def test_sans_provision(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # ET une carte n'ayant de pas de provision
        carte = CarteFake(False)

        # QUAND cette carte est détectée
        lecteur_cb.simuler_carte_détectée(carte)

        matcher = BrewerMatcher()

        # ALORS aucun café n'est commandé au hardware
        matcher.assertNoCoffeeOrdered(brewer)

    def test_defaillance(self):
        # ETANT DONNE une machine a café au brewer défaillant
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .brewer_defaillant()
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        matcher = BrewerMatcher()

        # ALORS l'argent n'est pas débité
        matcher.assertAmountCharged(carte, 0)

    def test_sans_detection_cb(self):
        # ETANT DONNE une machine a café
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .build())

        # QUAND aucune carte n'est détectée

        matcher = BrewerMatcher()
        # ALORS aucun café n'est commandé au hardware
        matcher.assertNoCoffeeOrdered(brewer)

    def test_manque_d_eau(self):
        # ETANT DONNE une machine à café sans eau
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        brewer.simulate_no_water()  # Simuler le manque d'eau

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        matcher = BrewerMatcher()
        # ALORS aucun café n'est commandé au hardware
        matcher.assertNoCoffeeOrdered(brewer)

    def test_manque_de_cafe(self):
        # ETANT DONNE une machine à café sans café
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        brewer.simulate_no_coffee()  # Simuler le manque de café

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        matcher = BrewerMatcher()
        # ALORS aucun café n'est commandé au hardware
        matcher.assertNoCoffeeOrdered(brewer)

    def test_fourniture_gobelet(self):
        # ETANT DONNE une machine à café sans tasse détectée
        cup_provider = CupProviderSpy(cup_present=False)
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .ayant_pour_cup_provider(cup_provider)
                          .build())
        
        # QUAND un utilisateur commande un produit
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)

        matcher = BrewerMatcher()

        # ALORS la machine fournit un gobelet
        matcher.assertCupProvided(cup_provider)
        # ET le café est commandé
        matcher.assertCoffeeOrdered(brewer)
    
    def test_add_chocolate(self):
        # ETANT DONNE une machine à café
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND un utilisateur commande un chocolat
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)
        machine_a_cafe._chocolate_callback(carte)

        matcher = BrewerMatcher()
        # ALORS le chocolat est commandé
        matcher.assertChocolateOrdered(brewer)
        # Et le montant total est 50 + 60 = 110
        matcher.assertAmountCharged(carte, -110)
    
    def test_add_latte(self):
        # ETANT DONNE une machine à café
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND un utilisateur commande un latte
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)
        machine_a_cafe._latte_callback(carte)

        # ALORS le latte est commandé
        self.assertTrue(brewer.add_latte_appelé())
        # Et le montant total est 50 + 70 = 120
        self.assertEqual(-120, carte.somme_operations_en_centimes())

    def test_add_capuccino(self):
        # ETANT DONNE une machine à café
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND un utilisateur commande un capuccino
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)
        machine_a_cafe._capuccino_callback(carte)

        # ALORS le capuccino est commandé
        self.assertTrue(brewer.add_capuccino_appelé())

        # Et le montant total est 50 + 80 = 130
        self.assertEqual(-130, carte.somme_operations_en_centimes())    

    def test_no_chocolate(self):
        # ETANT DONNE une machine à café
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())
        brewer.simulate_no_chocolate()

        # QUAND un utilisateur commande un chocolat
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)

        # ALORS le chocolat n'est pas commandé
        self.assertFalse(brewer.add_chocolate_appelé())

        # Et le montant total est 50
        self.assertEqual(-50, carte.somme_operations_en_centimes())
    
    def test_no_latte(self):
        # ETANT DONNE une machine à café
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())
        brewer.simulate_no_latte()

        # QUAND un utilisateur commande un latte
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)

        # ALORS le latte n'est pas commandé
        self.assertFalse(brewer.add_latte_appelé())

        # Et le montant total est 50
        self.assertEqual(-50, carte.somme_operations_en_centimes())

    def test_no_capuccino(self):
        # ETANT DONNE une machine à café
        brewer = BrewerSpy()
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())
        brewer.simulate_no_capuccino()

        # QUAND un utilisateur commande un capuccino
        carte = CarteFake.default()
        machine_a_cafe._credit_card_callback(carte)

        # ALORS le capuccino n'est pas commandé
        self.assertFalse(brewer.add_capuccino_appelé())

        # Et le montant total est 50
        self.assertEqual(-50, carte.somme_operations_en_centimes())

if __name__ == '__main__':
    unittest.main()
