from pylaas_core.abstract.abstract_service import AbstractService
import time

from pylaas_core.interface.technical.container_configurable_aware_interface import ContainerConfigurableAwareInterface


class DummyConfigurable(AbstractService, ContainerConfigurableAwareInterface):
    _microtime = 0
    _configs = None

    def __init__(self) -> None:
        super().__init__()
        self._microtime = int(round(time.time() * 1000))

    def set_configs(self, configurations):
        self._configs = configurations
        return self
