from hardware.brewer import BrewerInterface
from machine_a_cafe import MachineACafé
from utilities.brewer_defaillant_fake import BrewerDefaillantFake
from utilities.brewer_surveillant_les_appels import BrewerSpy
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake
from hardware.cupprovider import CupProviderInterface

class MachineACaféBuilder:
    def __init__(self):
        self.__brewer = BrewerSpy()
        self.__lecteur_cb = LecteurCbFake()
        self.__cup_provider = None
        #self.__age_du_capitaine = None

    def build(self) -> MachineACafé:
        return MachineACafé(self.__brewer, self.__lecteur_cb, cup_provider=self.__cup_provider)

    def ayant_pour_brewer(self, brewer: BrewerInterface):
        self.__brewer = brewer
        return self

    def ayant_pour_lecteur_cb(self, lecteur_cb: BrewerInterface):
        self.__lecteur_cb = lecteur_cb
        return self

    def brewer_defaillant(self):
        return self.ayant_pour_brewer(BrewerDefaillantFake())

    def ayant_pour_cup_provider(self, cup_provider: CupProviderInterface):
        self.__cup_provider = cup_provider
        return self

    # def avec_age_du_capitaine(self, age: int):
    #     self.__age_du_capitaine = age
    #     return self