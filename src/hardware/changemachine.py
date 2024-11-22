import abc

from hardware.coincode import CoinCode


class ChangeMachineInterface(abc.ABC):

    # Enregistre un callback, qui sera appelé lors de l'insertion d'une pièce reconnue valide
    # Attention : si le monnayeur est physiquement plein (plus de 5 pièces), cette méthode n'est
    # plus invoquée. Il est de la responsabilité du logiciel de surveiller cela.
    # @param callback prend un unique paramètre où sera injecté la valeur de la pièce détectée
    @abc.abstractmethod
    def register_money_inserted_callback(self, callback: CoinCode = None) -> None:
        pass

    # Vide le monnayeur et rend l'argent
    @abc.abstractmethod
    def flush_stored_money(self) -> None:
        pass

    # Vide le monnayeur et encaisse l'argent
    @abc.abstractmethod
    def collect_stored_money(self) -> None:
        pass

    # Fait tomber une pièce depuis le stock vers la trappe à monnaie
    # @param coin_code
    # @return True si la pièce était disponible
    # @return False si aucune pièce n'a pu être trouvée avec ce montant
    @abc.abstractmethod
    def drop_cashback(self, coin_code: CoinCode) -> bool:
        pass