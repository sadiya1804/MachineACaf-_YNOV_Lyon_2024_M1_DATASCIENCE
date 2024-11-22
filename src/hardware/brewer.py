import abc


class BrewerInterface(abc.ABC):

    # Demande à la machine de faire couler un café.
    # Si aucune dose d'eau n'était préchargée dans le bouilleur, la machine tentera d'en charger une
    # @return True si aucun problème, False si défaillance
    @abc.abstractmethod
    def make_a_coffee(self) -> bool:
        pass

    # Tire une dose d'eau depuis le réservoir vers le bouilleur
    # @return True si une dose a été tirée avec succès
    # @return False si le bouilleur contenait déjà une dose d'eau
    # @return False si aucune dose complète n'a pu être tirée
    @abc.abstractmethod
    def try_pull_water(self) -> bool:
        pass

    # Ajoute une dose de lait au mélange.
    # Il est conseillé d'ajouter le lait en premier, sauf sur le capuccino.
    # @return True si aucun problème, False si défaillance
    @abc.abstractmethod
    def pour_milk(self) -> bool:
        pass

    # Ajoute une dose d'eau au mélange. Il est conseillé d'ajouter l'eau en dernier.
    # Si aucune dose d'eau n'était dans le bouilleur, la machine tentera d'en charger une
    # @return True si aucun problème, False si défaillance
    @abc.abstractmethod
    def pour_water(self) -> bool:
        pass

    # Ajoute une dose de sucre au mélange. Il est conseillé d'ajouter le sucre en premier.
    # @return True si aucun problème, False si défaillance
    @abc.abstractmethod
    def pour_sugar(self) -> bool:
        pass

    # Ajoute une dose de chocolat au mélange. Il est conseillé d'ajouter le chocolat
    # après le sucre mais avant les autre ingrédients.
    # @return True si aucun problème, False si défaillance
    @abc.abstractmethod
    def pour_chocolate(self) -> bool:
        pass