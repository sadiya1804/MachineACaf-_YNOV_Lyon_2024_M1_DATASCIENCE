import abc


class CupProviderInterface(abc.ABC):
    # Relâche une touillette, sans possibilité de savoir si l'action a été efficace
    @abc.abstractmethod
    def provide_stirrer(self) -> None:
        pass

    # Renvoie l'état du capteur de présence d'une tasse
    # @return True si une tasse est présente
    # @return False si une tasse est absente
    @abc.abstractmethod
    def is_cup_present(self) -> bool:
        pass


    # Relâche un gobelet, s'il en reste. Il est conseillé de vérifier IsCupPresent ensuite.
    @abc.abstractmethod
    def provide_cup(self) -> None:
        pass