from hardware.brewer import BrewerInterface


class BrewerDefaillantFake(BrewerInterface):
    def make_a_coffee(self) -> bool:
        return False

    def try_pull_water(self) -> bool:
        raise NotImplementedError()

    def pour_milk(self) -> bool:
        raise NotImplementedError()

    def pour_water(self) -> bool:
        raise NotImplementedError()

    def pour_sugar(self) -> bool:
        raise NotImplementedError()

    def pour_chocolate(self) -> bool:
        raise NotImplementedError()