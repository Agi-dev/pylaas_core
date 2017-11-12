class DummyAdapterAdapter:
    def __init__(self) -> None:
        self._identity = "I'm the adapter to DummyAdapter"

    def who_i_am(self):
        return self._identity
