"""
This module implements the alfred core system.

PylaasCore.init(<definitions: file|{}>)
"""
from pylaas_core.technical.container import Container


class PylaasCore:
    """
    Attributes:
        _container (Container) : unique instance
    """
    _container = None

    def __new__(cls):
        """Prevent instantiation
        """
        raise TypeError("PylaasCore class may not be instantiated")

    @classmethod
    def init(cls, definitions):
        """Init AlfredCore

        init default Container with definitions

        Args:
            definitions (dict): container definitions
        """
        cls._container = Container()
        cls._container.add_definition(definitions)

    @classmethod
    def get_container(cls):
        """Get current container

        Returns:
            container (ContainerInterface): current container

        """
        return cls._container

    @classmethod
    def get_service(cls, service_id):
        """Get service

        Args:
            service_id (string): service id to instantiate from container

        Returns:
            service (ServiceInterface): service instance (singletons)

        """
        return cls.get_container().get(service_id)
