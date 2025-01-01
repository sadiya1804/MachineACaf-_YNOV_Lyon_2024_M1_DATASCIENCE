from hardware.brewer import BrewerInterface

class BrewerSpy(BrewerInterface):
    def __init__(self):
        self.__make_a_coffee_appelé = False
        self.__has_water = True
        self.__has_coffee = True
        self.__add_chocolate_appelé = False
        self.__has_chocolate = True

    def make_a_coffee(self) -> bool:
        if not self.__has_water or not self.__has_coffee:
            return False
        self.__make_a_coffee_appelé = True
        return True

    def make_a_coffee_appelé(self):
        return self.__make_a_coffee_appelé
    
    def try_pull_water(self) -> bool:
        pass

    def pour_milk(self) -> bool:
        pass

    def pour_water(self) -> bool:
        pass

    def pour_sugar(self) -> bool:
        pass

    def pour_chocolate(self) -> bool:
        if not self.__has_chocolate:
            return False
        self.__add_chocolate_appelé = True
        return True

    def simulate_no_water(self):
        self.__has_water = False
        return self
    
    def simulate_no_coffee(self):
        self.__has_coffee = False
        return self
    
    def add_chocolate_appelé(self):
        return self.__add_chocolate_appelé