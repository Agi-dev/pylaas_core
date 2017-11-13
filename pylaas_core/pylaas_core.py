"""
This module implements the alfred core system.

"""
from pylaas_core.interface.technical.container_interface import ContainerInterface
from pylaas_core.technical.container import Container


class PylaasCore():
    _container = None
    _instance = None

    def __new__(cls):
        """
        ensure PylaasCore is always a singleton

        Returns:
            PylassCore (PylaasCore)
        """
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def _init(self, definitions):
        """Init PylaasCore

        init default Container with definitions

        Args:
            definitions (dict|string): container definitions
        """
        self._container = Container()
        self._container.add_definitions(definitions)

    def get_container(self) -> ContainerInterface:
        """Get current container

        Returns:
            container (ContainerInterface): current container

        """
        return self._container

    def get_service(self, service_id):
        """Get service

        Args:
            service_id (string): service id to instantiate from container

        Returns:
            service (ServiceInterface): service instance (singletons)

        """
        return self.get_container().get(service_id)
