from pylaas_core.interface.core.service_interface import ServiceInterface
import time


class Dummy(ServiceInterface):
    def __init__(self) -> None:
        super().__init__()
        self._microtime = int(round(time.time() * 1000))
