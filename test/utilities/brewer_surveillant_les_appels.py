try:
    from hardware.brewer import BrewerInterface
except ImportError:
    class BrewerInterface:
        def try_pull_water(self) -> bool:
            pass

        def pour_milk(self) -> bool:
            pass

        def pour_water(self) -> bool:
            pass

        def pour_sugar(self) -> bool:
            pass

        def pour_chocolate(self) -> bool:
            pass


class BrewerSpy(BrewerInterface):
    def try_pull_water(self) -> bool:
        pass

    def pour_milk(self) -> bool:
        pass

    def pour_water(self) -> bool:
        pass

    def pour_sugar(self) -> bool:
        pass

    def pour_chocolate(self) -> bool:
        pass

    def __init__(self):
        self.__make_a_coffee_appelé = False

    def make_a_coffee(self) -> bool:
        self.__make_a_coffee_appelé = True
        return True

    def make_a_coffee_appelé(self):
        return self.__make_a_coffee_appelé