from pylaas_core.abstract.abstract_service import AbstractService
import time


class Dummy(AbstractService):
    _microtime = int(round(time.time() * 1000))

    def test_magic_service_injection(self):
        return self.dummy_configurable_service()
