from hardware.cupprovider import CupProviderInterface

class CupProviderSpy(CupProviderInterface):
    def __init__(self, cup_present: bool):
        self._cup_present = cup_present
        self._has_gobelet = True
        self._provide_cup_called = False

    def is_cup_present(self) -> bool:
        return self._cup_present

    def provide_cup(self):
        self._provide_cup_called = True

    def provide_cup_called(self) -> bool:
        if self._provide_cup_called and not self._has_gobelet:
            self._has_gobelet = False
        else:
            self._has_gobelet = True
        return self._has_gobelet

    def provide_stirrer(self):  
        pass

    def simulate_no_cup(self):
        self._has_tasse = False

